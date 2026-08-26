# -*- coding: utf-8 -*-
"""Montaje de Velaria General. Corre en el sandbox de Higgsfield."""
import subprocess, os, json
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
MP3 = ["hf_20260826_115500_c1c23fd9-a8c4-4ac6-b79e-7849c52c625b",  # 01 que hace Velaria
       "hf_20260826_115501_4e6aebe3-edf2-4b23-8e73-f55ea1962470",  # 02 en cinco pasos
       "hf_20260826_115647_b61dd10c-30d1-4e3d-b493-5bd61ad672a4",  # 03 paso 1a
       "hf_20260826_165229_800bab79-229a-4fa3-9b11-334bb90c6ea5",  # 04 paso 1b
       "hf_20260826_165928_7049a46d-230c-4749-b6d4-492143bd81a4",  # 05 el ejemplo: cotizaciones
       "hf_20260826_165229_384eaaaa-f0a3-47dd-ac71-642b55010607",  # 06 paso 2 piezas
       "hf_20260826_165928_70c0d51c-87c2-456e-ae20-852c70420d31",  # 07 paso 3 conocimiento
       "hf_20260826_115514_8ee04e40-a06f-4081-b2c0-b72e657b4c8e",  # 08 paso 4 la base
       "hf_20260826_115515_ae046f26-bfa5-490a-9e4b-f591f4e30223",  # 09 paso 5 reparto
       "hf_20260826_165228_203f242f-3e47-4214-b17d-6b97d361bfa0"]  # 10 cierre
PLAN = [n for n, _ in json.load(open("ui/plan-mec.json"))]
WIN = [w for _, w in json.load(open("ui/plan-mec.json"))]
# la 8 trae cola alucinada tras "se entera"; la 10, seis segundos de balbuceo
# despues de "vision" -- ahi se corta antes de la palabra "Velaria" suelta,
# que es la que sonaba con acento raro
TRIM = {8: 14.4, 10: 4.95}
FPS = 25
os.makedirs("src", exist_ok=True); os.makedirs("seg", exist_ok=True)
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])

for i, f in enumerate(MP3, 1):
    if not os.path.exists(f"src/a{i}.mp3"): sh(f"curl -sfo src/a{i}.mp3 '{B}{f}.mp3'")

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
    t = TRIM.get(i)
    cut = f"-t {t} -af afade=t=out:st={t-0.2}:d=0.2" if t else ""
    sh(f"ffmpeg -y -v error -i src/a{i}.mp3 {cut} -ar 48000 -ac 2 seg/a{i}.wav")
    parts.append(f"seg/a{i}.wav")
    g = round(w - dur(f"seg/a{i}.wav"), 3)
    if g < 0: print("VENTANA CORTA en escena", i, g); g = 0.05
    sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {g} seg/g{i}.wav")
    parts.append(f"seg/g{i}.wav")
with open("seg/alist.txt", "w") as fh:
    for p2 in parts: fh.write(f"file '{os.path.abspath(p2)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg/alist.txt -c copy seg/voz.wav")
T = dur("seg/voz.wav")

# ---- cama: las mismas cuatro piezas electronicas del corte de SQM, una por bloque
BEDS = ["hf_20260826_135133_65a8fa4f-44ea-4719-bf00-e27b3abfb27f.m4a",  # A que hace Velaria
        "hf_20260826_135133_81e3d4d0-918f-4243-9879-3f8dd234ddeb.m4a",  # B el paso 1 y el ejemplo
        "hf_20260826_135133_9872ad48-9432-4f31-9b71-f866857932f4.m4a",  # C piezas y conocimiento
        "hf_20260826_135133_974ce7e4-9d0a-4c3a-8840-cb8471714b68.m4a"]  # D reparto y cierre
BLOQUES = [(1, 3), (4, 5), (6, 8), (9, 10)]
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

sh("ffmpeg -y -v error -i seg/video.mp4 -i seg/mezcla.wav -c:v copy -c:a aac -b:a 192k corte-v2.mp4")
print("VIDEO", dur("seg/video.mp4"), "VOZ", T, "CAMA", dur("seg/bed.wav"), "FINAL", dur("corte-v2.mp4"))
