# -*- coding: utf-8 -*-
"""Montaje del corte v7 (pitch de 90 s). Corre en el sandbox de Higgsfield."""
import subprocess, os, json
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
MP3 = ["hf_20260825_224804_1e659e28-37af-4e15-9d87-8da5bf55ae9e",
       "hf_20260825_231417_3ac45e41-dc99-4b73-903b-c5f9a005228b",
       "hf_20260825_231053_2e3eb2c0-7153-4ced-b44a-f9476c6998b4",
       "hf_20260825_231417_a9f43579-ae7c-48c0-bdcf-d48c91e1955e",
       "hf_20260825_231804_63750fd9-327a-4cca-afc9-252bd62c324d",
       "hf_20260825_224804_35b7137c-decb-4aa0-8992-2ffc1e807ff8",
       "hf_20260825_224812_2e194e7f-c8b3-4e80-9d03-550699fcbcb5",
       "hf_20260825_224803_ed5339b2-0a47-4bbf-adcc-ec592e8b4217",
       "hf_20260825_224812_883a734f-cb56-4b07-8434-3f587e584efd"]
WIN = [w for _, w in json.load(open("ui/plan-v7.json"))]
# la escena 2 vino con 6 s de audio alucinado despues de "equipo": se corta ahi
TRIM = {2: 12.5, 5: 23.0}
FPS = 25
os.makedirs("src7", exist_ok=True); os.makedirs("seg7", exist_ok=True)
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])

for i, f in enumerate(MP3, 1):
    if not os.path.exists(f"src7/a{i}.mp3"): sh(f"curl -sfo src7/a{i}.mp3 '{B}{f}.mp3'")

# ---- video: corte duro entre escenas; la fluidez la da la envolvente de cada plano
segs = []
for i, w in enumerate(WIN, 1):
    src, out = f"ui/clips/v7-{i:02d}.mp4", f"seg7/s{i}.mp4"
    sh(f"ffmpeg -y -v error -i '{src}' -vf 'scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}' "
       f"-t {w:.3f} -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p '{out}'")
    d = dur(out)
    if abs(d - w) > 0.15: print("CORTO", i, w, round(d, 2))
    segs.append(out)
with open("seg7/list.txt", "w") as fh:
    for s in segs: fh.write(f"file '{os.path.abspath(s)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg7/list.txt -c copy seg7/video.mp4")

# ---- audio: cada escena es su locucion mas el aire que la separa de la siguiente
parts = []
for i, w in enumerate(WIN, 1):
    t = TRIM.get(i)
    cut = f"-t {t} -af afade=t=out:st={t-0.2}:d=0.2" if t else ""
    sh(f"ffmpeg -y -v error -i src7/a{i}.mp3 {cut} -ar 48000 -ac 2 seg7/a{i}.wav")
    parts.append(f"seg7/a{i}.wav")
    g = round(w - dur(f"seg7/a{i}.wav"), 3)
    if g < 0: print("VENTANA CORTA en escena", i, g); g = 0.05
    sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {g} seg7/g{i}.wav")
    parts.append(f"seg7/g{i}.wav")
with open("seg7/alist.txt", "w") as fh:
    for p in parts: fh.write(f"file '{os.path.abspath(p)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg7/alist.txt -c copy seg7/voz.wav")
sh("ffmpeg -y -v error -i seg7/video.mp4 -i seg7/voz.wav -c:v copy -c:a aac -b:a 192k corte-v7.mp4")
print("VIDEO", dur("seg7/video.mp4"), "VOZ", dur("seg7/voz.wav"), "FINAL", dur("corte-v7.mp4"))
