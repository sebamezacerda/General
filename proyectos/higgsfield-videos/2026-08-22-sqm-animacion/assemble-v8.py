# -*- coding: utf-8 -*-
"""Montaje del corte v8 de SQM, con cama musical. Corre en el sandbox de Higgsfield."""
import subprocess, os, json
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
MP3 = ["hf_20260823_020532_418867af-5a06-4543-b22b-ceef73795345",  # 01 tu equipo ya usa IA
       "hf_20260826_125404_89c97e27-b40a-4938-b25e-903920b7e0b9",  # 02 villano
       "hf_20260825_231053_2e3eb2c0-7153-4ced-b44a-f9476c6998b4",  # 03 los tres ejes
       "hf_20260826_125404_dfb911b1-117e-494e-ad24-be18efec108b",  # 04 veamos un ejemplo
       "hf_20260826_125404_9a02bcab-3ed0-40ca-8465-1d3ab6663298",  # 05 el caso
       "hf_20260826_125404_cad7cbff-7de4-484a-8333-f61a18fb4215",  # 06 hoy sin Velaria
       "hf_20260826_125404_3835cbb4-3e3f-4ef0-8072-920dfa14215b",  # 07 con Velaria
       "hf_20260826_125404_239047de-57f0-41d8-9a46-1538b2b884d8",  # 08 Velaria aprende
       "hf_20260826_125404_dd85dfa3-22bf-4b00-8d72-c4ad57c83144",  # 09 la Skill repartida
       "hf_20260825_224812_2e194e7f-c8b3-4e80-9d03-550699fcbcb5",  # 10 gobernanza
       "hf_20260826_125404_c080551e-171e-4975-a622-b0a04a9462f4",  # 11 impacto
       "hf_20260825_224812_883a734f-cb56-4b07-8434-3f587e584efd"]  # 12 cierre
MUS = "hf_20260826_125423_e30abb49-79a0-4b66-a08a-e3a2e0bbb6fa.m4a"
WIN = [w for _, w in json.load(open("ui/plan-v8.json"))]
FPS = 25
os.makedirs("src8", exist_ok=True); os.makedirs("seg8", exist_ok=True)
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])

for i, f in enumerate(MP3, 1):
    if not os.path.exists(f"src8/a{i}.mp3"): sh(f"curl -sfo src8/a{i}.mp3 '{B}{f}.mp3'")
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
    sh(f"ffmpeg -y -v error -i src8/a{i}.mp3 -ar 48000 -ac 2 seg8/a{i}.wav")
    parts.append(f"seg8/a{i}.wav")
    g = round(w - dur(f"seg8/a{i}.wav"), 3)
    if g < 0: print("VENTANA CORTA en escena", i, g); g = 0.05
    sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {g} seg8/g{i}.wav")
    parts.append(f"seg8/g{i}.wav")
with open("seg8/alist.txt", "w") as fh:
    for p in parts: fh.write(f"file '{os.path.abspath(p)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg8/alist.txt -c copy seg8/voz.wav")
T = dur("seg8/voz.wav")

# ---- cama: la pieza generada dura 60 s, asi que se encadena consigo misma con
# crossfades de 2 s. Es un pad sostenido sin melodia, asi que la costura no se oye.
sh("ffmpeg -y -v error -i src8/mus.m4a -i src8/mus.m4a -i src8/mus.m4a -i src8/mus.m4a "
   "-filter_complex '[0][1]acrossfade=d=2[a];[a][2]acrossfade=d=2[b];[b][3]acrossfade=d=2[c]' "
   "-map '[c]' -ar 48000 -ac 2 seg8/bed.wav")

# ---- mezcla: la cama a -30 LUFS y ademas agachandose 6 dB cuando ella habla.
# Se tiene que sentir, no oir.
sh(f"ffmpeg -y -v error -i seg8/voz.wav -i seg8/bed.wav -filter_complex "
   f"\"[1:a]atrim=0:{T:.3f},asetpts=N/SR/TB,loudnorm=I=-30:TP=-6:LRA=7,"
   f"afade=t=in:d=2.5,afade=t=out:st={T-3.5:.3f}:d=3.5[m];"
   f"[m][0:a]sidechaincompress=threshold=0.025:ratio=6:attack=25:release=450:makeup=1[duck];"
   f"[duck][0:a]amix=inputs=2:duration=first:normalize=0[mix]\" "
   f"-map '[mix]' -ar 48000 -ac 2 seg8/mezcla.wav")

sh("ffmpeg -y -v error -i seg8/video.mp4 -i seg8/mezcla.wav -c:v copy -c:a aac -b:a 192k corte-v8.mp4")
print("VIDEO", dur("seg8/video.mp4"), "VOZ", T, "CAMA", dur("seg8/bed.wav"), "FINAL", dur("corte-v8.mp4"))
