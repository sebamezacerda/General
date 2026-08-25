# -*- coding: utf-8 -*-
"""Montaje del video Cordillera. Corre en el sandbox de Higgsfield."""
import subprocess, os, json
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
AUD = ["hf_20260825_122313_1f6daec8-8cf9-4068-9d52-ea2e4e0c7bff","hf_20260825_122313_fab9f2bd-2495-4d7e-8e54-27ce30138683",
       "hf_20260825_122313_374b18a1-4e91-4cde-8aa7-7fe7f12dcef7","hf_20260825_122326_28886723-dbe7-4f36-a3b2-6f8190fe4b83",
       "hf_20260825_122313_65c63f72-908f-4600-b6a4-bb0aa4a51faa","hf_20260825_122313_d379c487-6ac6-4034-95e7-8629f814440c",
       "hf_20260825_122313_e89bf14d-9466-4d05-80fc-3a81d86a5b96","hf_20260825_122313_45dc3722-62a7-4142-bd1c-82c8b19bd032",
       "hf_20260825_122313_b6f9470d-5151-4d60-b43d-5902ac3caa07","hf_20260825_122313_3404f086-ecf0-4060-9bb3-74c1c22eb73b",
       "hf_20260825_122313_d0713794-0eda-4db6-a0f9-bce286e76a5f","hf_20260825_122313_1ccb37da-af86-42e9-a077-a2ccf89888ac"]
WIN = [16.5, 16.6, 16.6, 17.1, 17.3, 17.1, 20.6, 20.6, 16.7, 23.0, 18.8, 16.0]
PRE, FPS = 4.0, 25
os.makedirs("src", exist_ok=True); os.makedirs("seg", exist_ok=True)
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])
for i, f in enumerate(AUD, 1):
    if not os.path.exists(f"src/a{i}.mp3"): sh(f"curl -sfo src/a{i}.mp3 '{B}{f}.mp3'")

segs = ["ui/clips/plate.mp4"]
for i, w in enumerate(WIN, 1):
    out = f"seg/s{i}.mp4"
    sh(f"ffmpeg -y -v error -i 'ui/clips/c-{i:02d}.mp4' -vf 'scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}' "
       f"-t {w:.3f} -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p '{out}'")
    d = dur(out)
    if abs(d - w) > 0.15: print("CORTO", i, w, round(d, 2))
    segs.append(out)
with open("seg/list.txt", "w") as fh:
    for s in segs: fh.write(f"file '{os.path.abspath(s)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg/list.txt -c copy seg/video.mp4")

sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {PRE} seg/pre.wav")
parts = ["seg/pre.wav"]
for i, w in enumerate(WIN, 1):
    sh(f"ffmpeg -y -v error -i src/a{i}.mp3 -ar 48000 -ac 2 seg/a{i}.wav")
    parts.append(f"seg/a{i}.wav")
    g = round(w - dur(f"seg/a{i}.wav"), 3)
    if g < 0: print("VENTANA CORTA", i, g); g = 0.05
    sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {g} seg/g{i}.wav")
    parts.append(f"seg/g{i}.wav")
with open("seg/alist.txt", "w") as fh:
    for p in parts: fh.write(f"file '{os.path.abspath(p)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg/alist.txt -c copy seg/audio.wav")
sh("ffmpeg -y -v error -i seg/video.mp4 -i seg/audio.wav -c:v copy -c:a aac -b:a 192k cordillera-v1.mp4")
print("VIDEO", dur("seg/video.mp4"), "AUDIO", dur("seg/audio.wav"), "FINAL", dur("cordillera-v1.mp4"))
