# -*- coding: utf-8 -*-
"""Montaje de Velaria General. Corre en el sandbox de Higgsfield."""
import subprocess, os, json
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
# La narracion va en CINCO TOMAS CONTINUAS y se corta en escenas: dentro de una
# toma el modelo no cambia de tempo ni de acento. La E se separo de la D porque
# la toma larga traia una alucinacion de 40 s: menos texto por toma, menos riesgo.
TOMAS = ["hf_20260901_085159_4bca9323-3906-443d-800e-8b54a03ba989",  # A escenas 1-2
         "hf_20260901_085159_3a9106d6-a91b-4b8d-8c2a-9ad45659c07c",  # B escenas 3-5
         "hf_20260901_085159_ec2d957c-1494-4913-a24f-ef2f363f1489",  # C escenas 6-7
         "hf_20260901_085343_65586801-8ac0-43dc-8d40-eaf08ac169b0",  # D escenas 8-9
         "hf_20260901_085343_defa80a2-5bfa-45e6-9175-bf7724ec7929"]  # E escenas 10-11
# la voz se acelera un 8% antes de cortar: da cadencia sin subir el tono. Los
# tiempos de cortes-voz.json ya estan escritos en este reloj.
SPEED = 1.08
CUTS = json.load(open("cortes-voz.json"))
PLAN = [n for n, _ in json.load(open("ui/plan-mec.json"))]
WIN = [w for _, w in json.load(open("ui/plan-mec.json"))]
FPS = 25
os.makedirs("src", exist_ok=True); os.makedirs("seg", exist_ok=True)
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])

for i, f in enumerate(TOMAS, 1):
    if not os.path.exists(f"src/t{i}.mp3"): sh(f"curl -sfo src/t{i}.mp3 '{B}{f}.mp3'")
    if not os.path.exists(f"src/t{i}.wav"):
        sh(f"ffmpeg -y -v error -i src/t{i}.mp3 -af 'atempo={SPEED}' -ar 48000 -ac 2 src/t{i}.wav")
# atrim + asetpts reinicia el reloj ANTES del fade. Con -ss/-to de salida el filtro
# sigue viendo los timestamps del original y el fade de cierre se dispara antes de
# tiempo: asi es como se apagaba la voz a media escena.
for i, (tk, tramos) in enumerate(CUTS, 1):
    trozos = []
    for k, (ini, fin) in enumerate(tramos):
        out = f"src/a{i}_{k}.wav"
        sh(f"ffmpeg -y -v error -i src/t{tk}.wav -af "
           f"'atrim=start={ini}:end={fin},asetpts=N/SR/TB' -ar 48000 -ac 2 '{out}'")
        trozos.append(out)
    with open(f"src/l{i}.txt", "w") as fh:
        for t in trozos: fh.write(f"file '{os.path.abspath(t)}'\n")
    sh(f"ffmpeg -y -v error -f concat -safe 0 -i src/l{i}.txt -c copy src/c{i}.wav")
    d = dur(f"src/c{i}.wav")
    sh(f"ffmpeg -y -v error -i src/c{i}.wav -af "
       f"'afade=t=in:d=0.05,afade=t=out:st={d-0.08:.3f}:d=0.08' src/a{i}.wav")
    esperado = round(sum(e - s2 for s2, e in tramos), 3)
    if abs(d - esperado) > 0.05: print("CORTE MAL en escena", i, esperado, round(d, 2))

segs = []
for i, w in enumerate(WIN, 1):
    name = PLAN[i - 1]
    src, out = f"ui/clips/{name}.mp4", f"seg/s{i}.mp4"
    sh(f"ffmpeg -y -v error -i '{src}' -vf 'scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}' "
       f"-t {w:.3f} -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p '{out}'")
    d = dur(out)
    if abs(d - w) > 0.15: print("CORTO", i, w, round(d, 2))
    segs.append(out)
with open("seg/list.txt", "w") as fh:
    for s2 in segs: fh.write(f"file '{os.path.abspath(s2)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg/list.txt -c copy seg/video.mp4")

parts = []
for i, w in enumerate(WIN, 1):
    parts.append(f"src/a{i}.wav")
    g = round(w - dur(f"src/a{i}.wav"), 3)
    if g < 0: print("VENTANA CORTA en escena", i, g); g = 0.05
    sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {g} seg/g{i}.wav")
    parts.append(f"seg/g{i}.wav")
with open("seg/alist.txt", "w") as fh:
    for p2 in parts: fh.write(f"file '{os.path.abspath(p2)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg/alist.txt -c copy seg/voz.wav")
T = dur("seg/voz.wav")

# ---- cama: las mismas cuatro piezas electronicas del corte de SQM, una por bloque
# cuatro pistas intercaladas, para que la musica acompane el avance de los pasos
BEDS = ["hf_20260826_135133_65a8fa4f-44ea-4719-bf00-e27b3abfb27f.m4a",  # sobria
        "hf_20260826_135133_81e3d4d0-918f-4243-9879-3f8dd234ddeb.m4a",  # tensa
        "hf_20260826_135133_9872ad48-9432-4f31-9b71-f866857932f4.m4a",  # brillante
        "hf_20260826_135133_974ce7e4-9d0a-4c3a-8840-cb8471714b68.m4a"]  # resuelta
BLOQUES = [(1, 2), (3, 5), (6, 7), (8, 11)]
for i, f in enumerate(BEDS, 1):
    if not os.path.exists(f"src/b{i}.m4a"): sh(f"curl -sfo src/b{i}.m4a '{B}{f}'")

corte = []
for k, (ini, fin) in enumerate(BLOQUES, 1):
    L = round(sum(WIN[ini - 1:fin]), 3)
    if k < len(BLOQUES): L += 2.0     # el sobrante lo consume el acrossfade siguiente
    n = max(1, -(-int(L) // 55))
    ins = " ".join(f"-i src/b{k}.m4a" for _ in range(n))
    if n == 1:
        fc = "[0:a]anull[c]"
    else:
        fc = "[0][1]acrossfade=d=2[x1];" + "".join(
            f"[x{j}][{j + 1}]acrossfade=d=2[x{j + 1}];" for j in range(1, n - 1)) + f"[x{n - 1}]anull[c]"
    sh(f"ffmpeg -y -v error {ins} -filter_complex '{fc}' -map '[c]' -ar 48000 -ac 2 seg/bl{k}_raw.wav")
    sh(f"ffmpeg -y -v error -i seg/bl{k}_raw.wav -af 'atrim=0:{L},asetpts=N/SR/TB,volume=-17dB' seg/bl{k}.wav")
    corte.append(f"seg/bl{k}.wav")

# bloque a bloque encadenado: la musica nunca desaparece en el corte
ins = " ".join(f"-i {p2}" for p2 in corte)
fc = "[0][1]acrossfade=d=2[y1];" + "".join(
    f"[y{j}][{j + 1}]acrossfade=d=2[y{j + 1}];" for j in range(1, len(corte) - 1)) + f"[y{len(corte) - 1}]anull[z]"
sh(f"ffmpeg -y -v error {ins} -filter_complex '{fc}' -map '[z]' -ar 48000 -ac 2 seg/bed_raw.wav")
sh(f"ffmpeg -y -v error -i seg/bed_raw.wav -af "
   f"'atrim=0:{T:.3f},asetpts=N/SR/TB,afade=t=in:d=1.5,afade=t=out:st={T - 2.5:.3f}:d=2.5' seg/bed.wav")

# ---- mezcla: nivel fijo, sin ducking
sh(f"ffmpeg -y -v error -i seg/voz.wav -i seg/bed.wav -filter_complex "
   f"\"[0:a][1:a]amix=inputs=2:duration=first:normalize=0[mix]\" -map '[mix]' -ar 48000 -ac 2 seg/mezcla.wav")

sh("ffmpeg -y -v error -i seg/video.mp4 -i seg/mezcla.wav -c:v copy -c:a aac -b:a 192k corte-v3.mp4")
print("VIDEO", dur("seg/video.mp4"), "VOZ", T, "CAMA", dur("seg/bed.wav"), "FINAL", dur("corte-v3.mp4"))
