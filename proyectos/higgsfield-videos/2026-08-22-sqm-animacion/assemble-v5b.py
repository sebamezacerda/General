# -*- coding: utf-8 -*-
"""Montaje del corte v5. Corre en el sandbox de Higgsfield."""
import subprocess, os, json
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/hf_20260823_020532_"
JOBS = ["418867af-5a06-4543-b22b-ceef73795345","06909148-9740-4d33-9350-69dc11d50afa",
        "e19a0409-f01a-41c2-9adf-1d7e5ddbaaab","28593d23-85b0-4c04-a6d3-ebfac2dcd3d5",
        "ca770c3f-918f-40b8-a314-a1663f1c831a","a5122b55-5320-4529-8e70-2c9fa36f6b64",
        "3c1db039-80d2-4a0f-bf70-1868fbe4cbc6","8feeb4a6-1491-4025-bd5c-519b6326a7eb",
        "2315ebc6-d027-4c6d-928c-dc2e07f66593","cac111d0-4acd-40ce-9b93-f69f510056fa"]
WIN = [16.8, 20.2, 18.9, 21.0, 21.6, 19.1, 19.5, 18.7, 18.8, 14.6]
PRE = 4.0
FPS = 25
os.makedirs("src5", exist_ok=True); os.makedirs("seg5b", exist_ok=True)
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])

for i, j in enumerate(JOBS, 1):
    if not os.path.exists(f"src5/a{i}.mp3"): sh(f"curl -sfo src5/a{i}.mp3 '{B}{j}.mp3'")

# ---- video: una toma por escena. Las pantallas llevan subtitulo fijo abajo, asi que
# un corte con zoom lo recortaria: la fluidez la da la envolvente de fundido de cada escena.
segs = ["ui/clips/plate.mp4"]
for i, w in enumerate(WIN, 1):
    src = f"ui/clips/v5-{i:02d}.mp4"
    out = f"seg5b/s{i}.mp4"
    sh(f"ffmpeg -y -v error -i '{src}' -vf 'scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}' "
       f"-t {w:.3f} -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p '{out}'")
    d = dur(out)
    if abs(d - w) > 0.15: print("CORTO", i, w, round(d, 2))
    segs.append(out)

with open("seg5b/list.txt", "w") as fh:
    for s in segs: fh.write(f"file '{os.path.abspath(s)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg5b/list.txt -c copy seg5b/video.mp4")

# ---- audio: el aire de cada escena es su ventana menos lo que dura la voz
sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {PRE} seg5b/pre.wav")
parts = ["seg5b/pre.wav"]
for i, w in enumerate(WIN, 1):
    sh(f"ffmpeg -y -v error -i src5/a{i}.mp3 -ar 48000 -ac 2 seg5b/a{i}.wav")
    parts.append(f"seg5b/a{i}.wav")
    g = round(w - dur(f"seg5b/a{i}.wav"), 3)
    if g < 0: print("VENTANA CORTA en escena", i, g); g = 0.05
    sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {g} seg5b/g{i}.wav")
    parts.append(f"seg5b/g{i}.wav")
with open("seg5b/alist.txt", "w") as fh:
    for p in parts: fh.write(f"file '{os.path.abspath(p)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg5b/alist.txt -c copy seg5b/audio.wav")
sh("ffmpeg -y -v error -i seg5b/video.mp4 -i seg5b/audio.wav -c:v copy -c:a aac -b:a 192k corte-v5b.mp4")
print("VIDEO", dur("seg5b/video.mp4"), "AUDIO", dur("seg5b/audio.wav"), "FINAL", dur("corte-v5b.mp4"))
