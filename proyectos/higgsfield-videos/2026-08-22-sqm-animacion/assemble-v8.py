# -*- coding: utf-8 -*-
"""Montaje del corte v8 de SQM, con cama musical. Corre en el sandbox de Higgsfield."""
import subprocess, os, json
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
# La narracion se graba en CUATRO TOMAS CONTINUAS, no en trece pistas sueltas.
# Dentro de una toma el modelo mantiene el mismo tempo y el mismo acento; entre
# generaciones independientes no, y eso era lo que se oia como cambios de voz.
TOMAS = ["hf_20260901_090034_04469c3e-7222-4155-b95a-9084226b4cca",  # A escenas 2-4
         "hf_20260831_215317_e76e7745-45ef-4cd3-89b0-25516a6e009e",  # B escenas 5-7
         "hf_20260901_083623_303bf1cd-1acd-4733-b33b-b670e4dae910",  # C escenas 8-10
         "hf_20260901_090033_f9165e69-649f-45aa-831d-be0680c68b1e"]  # D escenas 11-15
# la voz se acelera un 7% antes de cortar: da cadencia sin subir el tono ni
# obligar a regenerar. Los tiempos de cortes-voz.json ya estan en este reloj.
SPEED = 1.07
CUTS = json.load(open("cortes-voz.json"))
RITMO = json.load(open("ritmo.json"))
PLAN = [n for n, _ in json.load(open("ui/plan-v8.json"))]
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
    if not os.path.exists(f"src8/t{i}.wav"):
        sh(f"ffmpeg -y -v error -i src8/t{i}.mp3 -af 'atempo={SPEED}' -ar 48000 -ac 2 src8/s{i}.wav")
        # ritmo: las pausas de la toma van de 0,2 a 0,8 s y eso es lo que se oye
        # como "hay partes mas rapidas que otras". El plan las acota a 0,2-0,4 s y
        # deja el habla intacta (normalizar tambien la velocidad de cada frase se
        # probo y AUMENTABA la dispersion: la prosodia real ya varia a proposito).
        letra = "ABCD"[i - 1]; trozos = []
        for k, (a, b, f2) in enumerate(RITMO[letra]):
            o = f"src8/r{i}_{k:03d}.wav"
            sh(f"ffmpeg -y -v error -i src8/s{i}.wav -af "
               f"'atrim={a}:{b},asetpts=N/SR/TB,atempo={f2}' -ar 48000 -ac 2 {o}")
            trozos.append(o)
        with open(f"src8/r{i}.txt", "w") as fh:
            for t in trozos: fh.write(f"file '{os.path.abspath(t)}'\n")
        sh(f"ffmpeg -y -v error -f concat -safe 0 -i src8/r{i}.txt -c copy src8/t{i}.wav")
# cada escena es uno o varios trozos de su toma; los cortes caen en el silencio
# entre frases. El formato es [toma, [[ini,fin], ...]]: el segundo tramo sirve para
# saltarse una alucinacion del modelo sin regenerar la toma entera.
# BUG corregido: antes el recorte usaba -ss/-to DESPUES de -i y el afade se
# calculaba sobre el reloj relativo. Con seek de salida el filtro sigue viendo los
# timestamps del archivo original, asi que el fade de cierre se disparaba a los
# pocos segundos y la voz se apagaba a media escena. atrim + asetpts reinicia el
# reloj antes del fade, que es lo unico que garantiza que ambos hablen del mismo 0.
for i, (tk, tramos) in enumerate(CUTS, 1):
    if not tramos:                       # escena sin voz (la intro de marca)
        sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t 0.02 src8/a{i}.wav")
        continue
    trozos = []
    for k, (ini, fin) in enumerate(tramos):
        out = f"src8/a{i}_{k}.wav"
        sh(f"ffmpeg -y -v error -i src8/t{tk}.wav -af "
           f"'atrim=start={ini}:end={fin},asetpts=N/SR/TB' -ar 48000 -ac 2 '{out}'")
        trozos.append(out)
    with open(f"src8/l{i}.txt", "w") as fh:
        for t in trozos: fh.write(f"file '{os.path.abspath(t)}'\n")
    sh(f"ffmpeg -y -v error -f concat -safe 0 -i src8/l{i}.txt -c copy src8/c{i}.wav")
    d = dur(f"src8/c{i}.wav")
    sh(f"ffmpeg -y -v error -i src8/c{i}.wav -af "
       f"'afade=t=in:d=0.05,afade=t=out:st={d-0.08:.3f}:d=0.08' src8/a{i}.wav")
    esperado = round(sum(b - a for a, b in tramos), 3)
    if abs(d - esperado) > 0.05: print("CORTE MAL en escena", i, esperado, round(d, 2))

# ---- video
segs = []
for i, w in enumerate(WIN, 1):
    src, out = f"ui/clips/{PLAN[i - 1]}.mp4", f"seg8/s{i}.mp4"
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

# ---- cama: cuatro pistas de libreria que trajo el cliente, una por bloque
# narrativo, para que la musica acompane el relato en vez de ser un loop plano.
# Medidas antes de asignarlas: m3 es plana (pulso 0,8 dB) y va al planteo; m1 sube
# la tension; m2 tiene el pulso mas marcado (16 dB) y entra justo cuando entra
# Velaria; m4 es la mas abierta arriba y cierra.
BEDS = ["1c784bd1-fd35-4643-9f0c-16425a5e7c2e.mp3",   # m1  100 bpm  tensa
        "5755ffc4-aae2-4e1b-9259-f8e66e34c567.mp3",   # m2  121 bpm  pulso fuerte
        "b0849c43-de85-48b2-b8ac-33d02b8b90e7.mp3",   # m3   90 bpm  plana
        "d5e674e2-8aac-4c8a-8d74-1b42650fde48.mp3"]   # m4  102 bpm  abierta
BLOQUES = [(1, 4), (5, 7), (8, 10), (11, 15)]
ASIGNA  = [3, 1, 2, 4]              # bloque -> pista (1..4), en ese orden narrativo
BASE_MEDIA = "https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
for i, f in enumerate(BEDS, 1):
    if not os.path.exists(f"src8/b{i}.mp3"): sh(f"curl -sfo src8/b{i}.mp3 '{BASE_MEDIA}{f}'")

corte = []
for k, (ini, fin) in enumerate(BLOQUES, 1):
    L = round(sum(WIN[ini - 1:fin]), 3)
    if k < len(BLOQUES): L += 2.0     # el sobrante lo consume el acrossfade siguiente
    pista = f"src8/b{ASIGNA[k - 1]}.mp3"
    dp = dur(pista)
    # se encadena la pista consigo misma las veces que haga falta para cubrir el
    # bloque; el numero sale de su duracion real, que va de 30 a 154 s segun la pieza
    n = max(1, -(-int(L + 2) // int(dp - 2)))
    ins = " ".join(f"-i {pista}" for _ in range(n))
    if n == 1:
        fc = "[0:a]anull[c]"
    else:
        fc = "[0][1]acrossfade=d=2[x1];" + "".join(
            f"[x{j}][{j + 1}]acrossfade=d=2[x{j + 1}];" for j in range(1, n - 1)) + f"[x{n - 1}]anull[c]"
    sh(f"ffmpeg -y -v error {ins} -filter_complex '{fc}' -map '[c]' -ar 48000 -ac 2 seg8/bl{k}_raw.wav")
    # el despeje de 300-3500 Hz le abre el carril a la voz; volumen fijo, no loudnorm:
    # en una pieza larga el loudnorm de una pasada bombea
    sh(f"ffmpeg -y -v error -i seg8/bl{k}_raw.wav -af "
       f"'atrim=0:{L},asetpts=N/SR/TB,highpass=f=38:poles=2,"
       f"equalizer=f=900:width_type=q:w=0.9:g=-2.0,"
       f"equalizer=f=2200:width_type=q:w=0.8:g=-3.0,"
       f"volume=-17dB' seg8/bl{k}.wav")
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

sh("ffmpeg -y -v error -i seg8/video.mp4 -i seg8/mezcla.wav -c:v copy -c:a aac -b:a 192k corte-v13.mp4")
print("VIDEO", dur("seg8/video.mp4"), "VOZ", T, "CAMA", dur("seg8/bed.wav"), "FINAL", dur("corte-v13.mp4"))
