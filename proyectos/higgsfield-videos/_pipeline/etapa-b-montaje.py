# -*- coding: utf-8 -*-
"""Etapa B: arma la voz con el ritmo nuevo, le pone la cama musical, la pega al
video mudo que se rindio aparte y verifica el resultado."""
import json, os, re, subprocess

C = json.load(open("cfg.json"))
CUTS = json.load(open("cortes-voz.json"))
RIT = json.load(open("ritmo.json"))
PLAN = json.load(open("plan.json"))
NOM = [n for n, _ in PLAN]; WIN = [w for _, w in PLAN]
LET = C["letras"]
os.makedirs("src", exist_ok=True); os.makedirs("seg", exist_ok=True)


def sh(c):
    subprocess.run(c, shell=True, check=True, capture_output=True)


def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])


def db(cmd):
    # OJO: nada de -v error en estas mediciones. volumedetect imprime su
    # resultado en nivel info y con -v error el filtro corre pero no dice nada:
    # el regex no encuentra nada, devuelve 0.0 y la verificacion queda vacia.
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    m = re.search(r"mean_volume: (-?[\d.]+)", r.stdout + r.stderr)
    return float(m.group(1)) if m else 0.0


avisos = []
for i, f in enumerate(C["tomas"], 1):
    sh(f"curl -sfo src/t{i}.mp3 '{C['base']}{f}.mp3'")
    # la voz se acelera antes de cortar: da cadencia sin subir el tono
    sh(f"ffmpeg -y -v error -i src/t{i}.mp3 -af 'atempo={C['speed']}' -ar 48000 -ac 2 src/s{i}.wav")
    tr = []
    for k, (a, b, fa) in enumerate(RIT[LET[i - 1]]):
        o = f"src/r{k:03d}.wav"
        sh(f"ffmpeg -y -v error -i src/s{i}.wav -af "
           f"'atrim={a}:{b},asetpts=N/SR/TB,atempo={fa}' -ar 48000 -ac 2 {o}")
        tr.append(o)
    open("src/l.txt", "w").write("".join(f"file '{os.path.abspath(t)}'\n" for t in tr))
    sh(f"ffmpeg -y -v error -f concat -safe 0 -i src/l.txt -c copy src/t{i}.wav")
    print(f"  toma {LET[i-1]}: {dur(f'src/t{i}.wav'):.2f}s", flush=True)

# atrim + asetpts reinicia el reloj ANTES del fade. Con -ss/-to de salida el filtro
# sigue viendo los timestamps del original y el cierre se dispara antes de tiempo:
# asi es como se apagaba la voz a media escena en el corte v12.
for i, (tk, tramos) in enumerate(CUTS, 1):
    if not tramos:                       # la intro de marca no lleva voz
        sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t 0.02 src/a{i}.wav")
        continue
    tr = []
    for k, (a, b) in enumerate(tramos):
        o = f"src/a{i}_{k}.wav"
        sh(f"ffmpeg -y -v error -i src/t{tk}.wav -af "
           f"'atrim=start={a}:end={b},asetpts=N/SR/TB' -ar 48000 -ac 2 '{o}'")
        tr.append(o)
    open(f"src/c{i}.txt", "w").write("".join(f"file '{os.path.abspath(t)}'\n" for t in tr))
    sh(f"ffmpeg -y -v error -f concat -safe 0 -i src/c{i}.txt -c copy src/c{i}.wav")
    d = dur(f"src/c{i}.wav")
    sh(f"ffmpeg -y -v error -i src/c{i}.wav -af "
       f"'afade=t=in:d=0.05,afade=t=out:st={d-0.08:.3f}:d=0.08' src/a{i}.wav")
    esp = round(sum(b - a for a, b in tramos), 3)
    if abs(d - esp) > 0.05:
        avisos.append(f"CORTE MAL escena {i}: esperado {esp} real {round(d,2)}")

parts = []
for i, w in enumerate(WIN, 1):
    parts.append(f"src/a{i}.wav")
    g = round(w - dur(f"src/a{i}.wav"), 3)
    if g < 0:
        avisos.append(f"VENTANA CORTA escena {i}: {g}"); g = 0.05
    sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {g} seg/g{i}.wav")
    parts.append(f"seg/g{i}.wav")
open("seg/al.txt", "w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
sh("ffmpeg -y -v error -f concat -safe 0 -i seg/al.txt -c copy seg/voz.wav")
T = dur("seg/voz.wav")

# ---- cama: cuatro pistas de libreria que trajo el cliente, una por bloque
# narrativo. Medidas antes de asignarlas: m3 es la mas plana (pulso 0,8 dB) y va
# al planteo; m1 sube la tension; m2 tiene el pulso mas marcado (16 dB) y entra
# cuando entra Velaria; m4 es la mas abierta arriba y cierra.
BEDS = ["1c784bd1-fd35-4643-9f0c-16425a5e7c2e.mp3",   # m1  100 bpm  tensa
        "5755ffc4-aae2-4e1b-9259-f8e66e34c567.mp3",   # m2  121 bpm  pulso fuerte
        "b0849c43-de85-48b2-b8ac-33d02b8b90e7.mp3",   # m3   90 bpm  plana
        "d5e674e2-8aac-4c8a-8d74-1b42650fde48.mp3"]   # m4  102 bpm  abierta
BM = "https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
for i, f in enumerate(BEDS, 1):
    sh(f"curl -sfo src/b{i}.mp3 '{BM}{f}'")
corte = []
for k, (ini, fin) in enumerate(C["bloques"], 1):
    L = round(sum(WIN[ini - 1:fin]), 3)
    if k < len(C["bloques"]):
        L += 2.0                      # el sobrante lo consume el acrossfade siguiente
    pista = f"src/b{C['asigna'][k-1]}.mp3"
    dp = dur(pista)
    n = max(1, -(-int(L + 2) // int(dp - 2)))
    ins = " ".join(f"-i {pista}" for _ in range(n))
    fc = ("[0:a]anull[c]" if n == 1 else
          "[0][1]acrossfade=d=2[x1];" + "".join(
              f"[x{j}][{j+1}]acrossfade=d=2[x{j+1}];" for j in range(1, n - 1)) + f"[x{n-1}]anull[c]")
    sh(f"ffmpeg -y -v error {ins} -filter_complex '{fc}' -map '[c]' -ar 48000 -ac 2 seg/br{k}.wav")
    # el despeje de 900 y 2200 Hz le abre el carril a la voz; volumen fijo, no
    # loudnorm: en una pieza larga el loudnorm de una pasada bombea
    sh(f"ffmpeg -y -v error -i seg/br{k}.wav -af 'atrim=0:{L},asetpts=N/SR/TB,"
       f"highpass=f=38:poles=2,equalizer=f=900:width_type=q:w=0.9:g=-2.0,"
       f"equalizer=f=2200:width_type=q:w=0.8:g=-3.0,volume=-17dB' seg/bl{k}.wav")
    corte.append(f"seg/bl{k}.wav")
ins = " ".join(f"-i {p}" for p in corte)
fc = "[0][1]acrossfade=d=2[y1];" + "".join(
    f"[y{j}][{j+1}]acrossfade=d=2[y{j+1}];" for j in range(1, len(corte) - 1)) + f"[y{len(corte)-1}]anull[z]"
sh(f"ffmpeg -y -v error {ins} -filter_complex '{fc}' -map '[z]' -ar 48000 -ac 2 seg/br.wav")
sh(f"ffmpeg -y -v error -i seg/br.wav -af 'atrim=0:{T:.3f},asetpts=N/SR/TB,"
   f"afade=t=in:d=1.5,afade=t=out:st={T-2.5:.3f}:d=2.5' seg/bed.wav")
sh("ffmpeg -y -v error -i seg/voz.wav -i seg/bed.wav -filter_complex "
   "\"[0:a][1:a]amix=inputs=2:duration=first:normalize=0[mix]\" -map '[mix]' "
   "-ar 48000 -ac 2 seg/mezcla.wav")

sh(f"curl -sfo seg/video.mp4 '{C['video']}'")
V = dur("seg/video.mp4")
if abs(V - sum(WIN)) > 0.3:
    avisos.append(f"VIDEO DESCUADRADO: {round(V,2)} vs plan {round(sum(WIN),2)}")
sh(f"ffmpeg -y -v error -i seg/video.mp4 -i seg/mezcla.wav -c:v copy -c:a aac -b:a 192k {C['salida']}")

# ---------------------------------------------------------------- verificacion
print("\n== escenas mudas ==")
mal = 0
for i, (tk, tr) in enumerate(CUTS, 1):
    if not tr:
        continue
    D = dur(f"src/a{i}.wav")
    q = [db(f"ffmpeg -hide_banner -nostats -i src/a{i}.wav -af 'atrim={k*D/4:.3f}:{(k+1)*D/4:.3f},"
            f"asetpts=N/SR/TB,volumedetect' -f null - 2>&1") for k in range(4)]
    if min(q) < -45:
        mal += 1; print(f"  MUDA {NOM[i-1]}: {[round(x,1) for x in q]}")
print("  ninguna" if not mal else f"  {mal} con problema")

print("\n== fronteras de escena en silencio ==")
peor, ruid = None, 0
for i, (tk, tr) in enumerate(CUTS, 1):
    for a, b in tr:
        for t in (a, b):
            v = db(f"ffmpeg -hide_banner -nostats -i src/t{tk}.wav -af 'atrim={max(0,t-0.06):.3f}:{t+0.06:.3f},"
                   f"asetpts=N/SR/TB,volumedetect' -f null - 2>&1")
            if peor is None or v > peor[0]:
                peor = (v, NOM[i - 1], round(t, 2))
            if v > -35:
                ruid += 1; print(f"  RUIDOSA {NOM[i-1]} en {t:.2f}s: {v:.1f} dB")
print(f"  {ruid} audibles · la peor {peor[0]:.1f} dB ({peor[1]}, {peor[2]}s)")

print(f"\nVIDEO {V:.2f}  VOZ {T:.2f}  FINAL {dur(C['salida']):.2f}")
for a in avisos:
    print("AVISO:", a)
if not avisos:
    print("sin avisos de corte")
sh(f"curl -f -X PUT -H 'Content-Type: video/mp4' --upload-file {C['salida']} '{C['put']}'")
print("SUBIDO", C["url"])
