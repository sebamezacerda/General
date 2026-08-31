# -*- coding: utf-8 -*-
"""Montaje del corte v8 de SQM, con cama musical. Corre en el sandbox de Higgsfield."""
import subprocess, os, json
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
# La narracion se graba en CUATRO TOMAS CONTINUAS, no en trece pistas sueltas.
# Dentro de una toma el modelo mantiene el mismo tempo y el mismo acento; entre
# generaciones independientes no, y eso era lo que se oia como cambios de voz.
TOMAS = ["hf_20260831_215317_bebf5409-07ec-48eb-a951-42132a992c47",  # A escenas 1-3
         "hf_20260831_215317_e76e7745-45ef-4cd3-89b0-25516a6e009e",  # B escenas 4-6
         "hf_20260831_215317_24b37c23-b599-4d94-b231-9fffec92c104",  # C escenas 7-9
         "hf_20260831_215317_65c4a6d9-15ba-4706-a78b-026f49aabd56"]  # D escenas 10-13
CUTS = json.load(open("cortes-voz.json"))
MUS = "hf_20260826_125423_e30abb49-79a0-4b66-a08a-e3a2e0bbb6fa.m4a"
WIN = [w for _, w in json.load(open("ui/plan-v8.json"))]
FPS = 25
os.makedirs("src8", exist_ok=True); os.makedirs("seg8", exist_ok=True)
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])

for i, f in enumerate(TOMAS, 1):
    if not os.path.exists(f"src8/t{i}.mp3"): sh(f"curl -sfo src8/t{i}.mp3 '{B}{f}.mp3'")
# cada escena es un trozo de su toma; los cortes caen en el silencio entre frases
# BUG corregido: antes el recorte usaba -ss/-to DESPUES de -i y el afade se
# calculaba sobre el reloj relativo. Con seek de salida el filtro sigue viendo los
# timestamps del archivo original, asi que el fade de cierre se disparaba a los
# pocos segundos y la voz se apagaba a media escena. atrim + asetpts reinicia el
# reloj antes del fade, que es lo unico que garantiza que ambos hablen del mismo 0.
for i, (tk, ini, fin) in enumerate(CUTS, 1):
    d = round(fin - ini, 3)
    sh(f"ffmpeg -y -v error -i src8/t{tk}.mp3 -af "
       f"'atrim=start={ini}:end={fin},asetpts=N/SR/TB,"
       f"afade=t=in:d=0.05,afade=t=out:st={d-0.08:.3f}:d=0.08' "
       f"-ar 48000 -ac 2 src8/a{i}.wav")
    got = dur(f"src8/a{i}.wav")
    if abs(got - d) > 0.05: print("CORTE MAL en escena", i, "esperado", d, "obtenido", round(got,2))
if not os.path.exists("src8/mus.m4a"): sh(f"curl -sfo src8/mus.m4a '{B}{MUS}'")

# ---- video
segs = []
for i, w in enumerate(WIN, 1):
    src, out = f"ui/clips/v8-{i:02d}.mp4", f"seg8/s{i}.mp4"
    sh(f"ffmpeg -y -v error -i '{src}' -vf 'scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}' "
       f"-t {w:.3f} -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p '{out}'")
    d = dur(out)
    if abs(d - w) > 0.15: print("CORTO", i, w, round(d, 2))
    segs.append(out)
with open("seg8/list.txt", "w") as fh:
    for s in segs: fh.write(f"file '{os.path.abspath(s)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg8/list.txt -c copy seg8/video.mp4")

# ---- voz: cada escena mas el aire que la separa de la siguiente
parts = []
for i, w in enumerate(WIN, 1):
    parts.append(f"src8/a{i}.wav")
    g = round(w - dur(f"src8/a{i}.wav"), 3)
    if g < 0: print("VENTANA CORTA en escena", i, g); g = 0.05
    sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {g} seg8/g{i}.wav")
    parts.append(f"seg8/g{i}.wav")
with open("seg8/alist.txt", "w") as fh:
    for p in parts: fh.write(f"file '{os.path.abspath(p)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg8/alist.txt -c copy seg8/voz.wav")
T = dur("seg8/voz.wav")

# ---- cama: cuatro piezas electronicas, una por bloque narrativo, para que la
# musica cambie con el relato en vez de ser un loop plano de tres minutos.
# tres pistas, intercaladas: la primera vuelve en el ultimo bloque y cierra el arco
BEDS = ["hf_20260826_135133_65a8fa4f-44ea-4719-bf00-e27b3abfb27f.m4a",  # 1 sobria
        "hf_20260826_135133_81e3d4d0-918f-4243-9879-3f8dd234ddeb.m4a",  # 2 tensa
        "hf_20260826_135133_9872ad48-9432-4f31-9b71-f866857932f4.m4a",  # 3 brillante
        "hf_20260826_135133_65a8fa4f-44ea-4719-bf00-e27b3abfb27f.m4a"]  # 1 otra vez
BLOQUES = [(1, 3), (4, 6), (7, 9), (10, 13)]   # escenas de cada bloque, inclusivo
for i, f in enumerate(BEDS, 1):
    if not os.path.exists(f"src8/b{i}.m4a"): sh(f"curl -sfo src8/b{i}.m4a '{B}{f}'")

corte = []
for k, (ini, fin) in enumerate(BLOQUES, 1):
    L = round(sum(WIN[ini - 1:fin]), 3)
    # cada bloque se rinde 2 s mas largo salvo el ultimo: ese sobrante lo consume el
    # acrossfade con el bloque siguiente, y asi la suma vuelve a dar la duracion exacta
    if k < len(BLOQUES): L += 2.0
    n = max(1, -(-int(L) // 55))
    ins = " ".join(f"-i src8/b{k}.m4a" for _ in range(n))
    if n == 1:
        fc = "[0:a]anull[c]"
    else:
        fc = "[0][1]acrossfade=d=2[x1];" + "".join(
            f"[x{j}][{j + 1}]acrossfade=d=2[x{j + 1}];" for j in range(1, n - 1)) + f"[x{n - 1}]anull[c]"
    sh(f"ffmpeg -y -v error {ins} -filter_complex '{fc}' -map '[c]' -ar 48000 -ac 2 seg8/bl{k}_raw.wav")
    # volumen fijo, no loudnorm: en una pieza larga el loudnorm de una pasada bombea
    sh(f"ffmpeg -y -v error -i seg8/bl{k}_raw.wav -af 'atrim=0:{L},asetpts=N/SR/TB,volume=-17dB' "
       f"seg8/bl{k}.wav")
    corte.append(f"seg8/bl{k}.wav")

# encadenado de bloque a bloque: sin hueco de silencio en el corte
ins = " ".join(f"-i {p}" for p in corte)
fc = "[0][1]acrossfade=d=2[y1];" + "".join(
    f"[y{j}][{j + 1}]acrossfade=d=2[y{j + 1}];" for j in range(1, len(corte) - 1)) + f"[y{len(corte) - 1}]anull[z]"
sh(f"ffmpeg -y -v error {ins} -filter_complex '{fc}' -map '[z]' -ar 48000 -ac 2 seg8/bed_raw.wav")
sh(f"ffmpeg -y -v error -i seg8/bed_raw.wav -af "
   f"'atrim=0:{T:.3f},asetpts=N/SR/TB,afade=t=in:d=1.5,afade=t=out:st={T - 2.5:.3f}:d=2.5' seg8/bed.wav")

# ---- mezcla: nivel fijo, sin ducking. Agacharla en cada frase sonaba a bombeo.
sh(f"ffmpeg -y -v error -i seg8/voz.wav -i seg8/bed.wav -filter_complex "
   f"\"[0:a][1:a]amix=inputs=2:duration=first:normalize=0[mix]\" "
   f"-map '[mix]' -ar 48000 -ac 2 seg8/mezcla.wav")

sh("ffmpeg -y -v error -i seg8/video.mp4 -i seg8/mezcla.wav -c:v copy -c:a aac -b:a 192k corte-v8.mp4")
print("VIDEO", dur("seg8/video.mp4"), "VOZ", T, "CAMA", dur("seg8/bed.wav"), "FINAL", dur("corte-v8.mp4"))
