# -*- coding: utf-8 -*-
"""Montaje del corte v4. Corre en el sandbox de Higgsfield."""
import subprocess, os, json, math
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
GEN = {"faena": "hf_20260822_143353_ea2b7d28-9cab-40fb-af41-527b4e45fff0.mp4",
       "grid":  "hf_20260822_143439_526d90d7-fad3-42e6-9372-08239aeb2026.mp4"}
AUD = ["hf_20260822_164917_b99d0c46-f5f8-4f8e-97d8-82377d895465.mp3",
       "hf_20260822_164917_66535b86-a460-46a9-8377-1e09af9b63ec.mp3",
       "hf_20260822_164917_de7c20aa-0ff4-493e-8dd3-cc54756e8014.mp3",
       "hf_20260822_164917_e8c7cc7c-4fbf-4baa-9b73-781dc05c7032.mp3",
       "hf_20260822_164917_84a5d5ef-2f1a-4be3-8fd7-52e0d9a23ebf.mp3",
       "hf_20260822_164917_b51a94a7-d542-474b-bca3-94734d35a52e.mp3",
       "hf_20260822_164917_1d9804c8-ff61-4179-8040-869aed3ca198.mp3"]
# aire despues de cada escena. Las escenas 3 y 5 son tablas: el silencio no es pausa,
# es el tiempo que necesita el espectador para leerlas.
GAPS = [1.0, 1.0, 11.0, 1.5, 8.0, 1.5, 3.0]
PRE  = 4.0

PLAN = [
 ("plate", "ui/clips/plate.mp4",           0.00,  4.00, None),
 ("1a",  "src/faena.mp4",                  0.00,  5.00, None),
 ("1b",  "ui/clips/v4-01-stack.mp4",       0.00,  7.77, None),
 ("2a",  "src/grid.mp4",                   0.00,  5.00, None),
 ("2b",  "ui/clips/v4-02-equipo.mp4",      0.00,  7.90, None),
 ("3a",  "ui/clips/v4-03-hoy.mp4",         0.00, 14.00, None),
 ("3b",  "ui/clips/v4-03-hoy.mp4",        14.00,  9.16, (1.28, 0.60, 0.86)),
 ("4",   "ui/clips/v4-04-costo.mp4",       0.00,  7.93, None),
 ("5a",  "ui/clips/v4-05-velaria.mp4",     0.00, 12.50, None),
 ("5b",  "ui/clips/v4-05-velaria.mp4",    12.50,  8.17, (1.28, 0.60, 0.86)),
 ("6a",  "ui/clips/v4-06-decision.mp4",    0.00,  9.50, None),
 ("6b",  "ui/clips/v4-06-decision.mp4",    9.50,  5.82, (1.25, 0.50, 0.88)),
 ("7",   "ui/clips/v4-07-cierre.mp4",      0.00, 10.21, None),
]
FPS = 25
os.makedirs("src", exist_ok=True); os.makedirs("seg4", exist_ok=True)
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])

for k, v in GEN.items():
    if not os.path.exists(f"src/{k}.mp4"): sh(f"curl -sfo src/{k}.mp4 '{B}{v}'")
for i, v in enumerate(AUD, 1):
    if not os.path.exists(f"src/v4a{i}.mp3"): sh(f"curl -sfo src/v4a{i}.mp3 '{B}{v}'")

loops = {}
def loop_base(srcf):
    if srcf in loops: return loops[srcf]
    key = os.path.basename(srcf).replace(".mp4", "")
    out = f"seg4/loop_{key}.mp4"
    sh(f"ffmpeg -y -v error -i '{srcf}' -vf 'scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}' "
       f"-an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p seg4/_f.mp4")
    sh(f"ffmpeg -y -v error -i seg4/_f.mp4 -vf reverse -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p seg4/_r.mp4")
    with open("seg4/_l.txt", "w") as fh:
        for _ in range(4):
            fh.write(f"file '{os.path.abspath('seg4/_f.mp4')}'\nfile '{os.path.abspath('seg4/_r.mp4')}'\n")
    sh(f"ffmpeg -y -v error -f concat -safe 0 -i seg4/_l.txt -c copy '{out}'")
    loops[srcf] = out
    return out

segs = []
for name, srcf, ss, tgt, zoom in PLAN:
    base = loop_base(srcf) if srcf.startswith("src/") else srcf
    vf = [f"scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}"]
    if zoom:
        z, cx, cy = zoom
        vf.insert(0, f"crop=iw/{z}:ih/{z}:(iw-iw/{z})*{cx}:(ih-ih/{z})*{cy}")
    out = f"seg4/{name}.mp4"
    sh(f"ffmpeg -y -v error -ss {ss:.3f} -i '{base}' -vf '{','.join(vf)}' -t {tgt:.3f} "
       f"-an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p '{out}'")
    d = dur(out)
    if abs(d - tgt) > 0.15: print("CORTO", name, tgt, round(d, 2))
    segs.append(out)

with open("seg4/list.txt", "w") as fh:
    for s in segs: fh.write(f"file '{os.path.abspath(s)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg4/list.txt -c copy seg4/video.mp4")

sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {PRE} seg4/pre.wav")
parts = ["seg4/pre.wav"]
for i in range(1, 8):
    sh(f"ffmpeg -y -v error -i src/v4a{i}.mp3 -ar 48000 -ac 2 seg4/a{i}.wav")
    parts.append(f"seg4/a{i}.wav")
    g = GAPS[i - 1]
    sh(f"ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t {g} seg4/g{i}.wav")
    parts.append(f"seg4/g{i}.wav")
with open("seg4/alist.txt", "w") as fh:
    for p in parts: fh.write(f"file '{os.path.abspath(p)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg4/alist.txt -c copy seg4/audio.wav")
sh("ffmpeg -y -v error -i seg4/video.mp4 -i seg4/audio.wav -c:v copy -c:a aac -b:a 192k corte-v4.mp4")
print("VIDEO", dur("seg4/video.mp4"), "AUDIO", dur("seg4/audio.wav"), "FINAL", dur("corte-v4.mp4"))
