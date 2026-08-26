# -*- coding: utf-8 -*-
"""Montaje del video del mecanismo (guion Tito). Corre en el sandbox de Higgsfield."""
import subprocess, os, json
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
MP3 = ["hf_20260826_115500_c1c23fd9-a8c4-4ac6-b79e-7849c52c625b",  # 1 que hace Velaria
       "hf_20260826_115501_4e6aebe3-edf2-4b23-8e73-f55ea1962470",  # 2 en cinco pasos
       "hf_20260826_115647_b61dd10c-30d1-4e3d-b493-5bd61ad672a4",  # 3 paso 1a
       "hf_20260826_115647_c6c9a233-5b3b-4641-ab95-1555ed1558f1",  # 4 paso 1b
       "hf_20260826_115501_6d8a4e8c-7c16-493b-92a8-7732706b75ac",  # 5 paso 2 piezas
       "hf_20260826_115501_66e104a1-9570-4dd8-b3d1-edd56f29a396",  # 6 paso 3 conocimiento
       "hf_20260826_115514_8ee04e40-a06f-4081-b2c0-b72e657b4c8e",  # 7 paso 4 la base
       "hf_20260826_115515_ae046f26-bfa5-490a-9e4b-f591f4e30223",  # 8 paso 5 reparto
       "hf_20260826_115514_b3547178-2fb5-476c-980a-e19c3ef4c4c4"]  # 9 cierre
WIN = [w for _, w in json.load(open("ui/plan-mec.json"))]
# la 7 trae cola alucinada ("Argen. Eso.") despues de "se entera": se corta ahi
TRIM = {7: 14.4}
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
    src, out = f"ui/clips/m-{i:02d}.mp4", f"seg/s{i}.mp4"
    sh(f"ffmpeg -y -v error -i '{src}' -vf 'scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}' "
       f"-t {w:.3f} -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p '{out}'")
    d = dur(out)
    if abs(d - w) > 0.15: print("CORTO", i, w, round(d, 2))
    segs.append(out)
with open("seg/list.txt", "w") as fh:
    for s in segs: fh.write(f"file '{os.path.abspath(s)}'\n")
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
    for p in parts: fh.write(f"file '{os.path.abspath(p)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg/alist.txt -c copy seg/voz.wav")
sh("ffmpeg -y -v error -i seg/video.mp4 -i seg/voz.wav -c:v copy -c:a aac -b:a 192k corte-v1.mp4")
print("VIDEO", dur("seg/video.mp4"), "VOZ", dur("seg/voz.wav"), "FINAL", dur("corte-v1.mp4"))
