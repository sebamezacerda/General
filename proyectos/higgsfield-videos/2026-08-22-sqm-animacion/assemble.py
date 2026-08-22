# -*- coding: utf-8 -*-
"""Montaje del corte. Corre en el sandbox de Higgsfield (ffmpeg + salida a internet)."""
import subprocess, os, json, math
B = "https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/"
GEN = {"g1a": "hf_20260822_143353_ea2b7d28-9cab-40fb-af41-527b4e45fff0.mp4",
       "g1b": "hf_20260822_143353_0efafda1-7473-4074-8a48-fab24279810b.mp4",
       "g2":  "hf_20260822_143439_526d90d7-fad3-42e6-9372-08239aeb2026.mp4",
       "g3":  "hf_20260822_143353_ae78329e-7ae7-48d6-8e0c-4f4f4a2f43fc.mp4",
       "g5":  "hf_20260822_135008_00cc868f-628b-4859-8619-3a1818dee471.mp4",
       "g12": "hf_20260822_143353_a0a60789-3982-4ccb-b1ad-00e13b33cd32.mp4"}
AUD = ["hf_20260822_140149_e3a54302-dec5-4659-a42c-75a999aad78c.mp3",
       "hf_20260822_140417_93e7d5cb-fa6c-41fd-bfd5-8fb3d7f8575c.mp3",
       "hf_20260822_140913_a8b3cb6d-5fc6-4417-bdc5-4116e41ddfa4.mp3",
       "hf_20260822_140913_d5008900-1e02-4bb1-b80a-2acd629756ca.mp3",
       "hf_20260822_140913_83f695a8-7051-4464-a8ae-38c20bfd2164.mp3",
       "hf_20260822_140913_b2334537-37c0-4703-b21d-fe31d0c495e6.mp3",
       "hf_20260822_140913_3fca2d25-9df3-4930-ad9a-9653230cdaec.mp3",
       "hf_20260822_140913_a74812f6-cf5e-477a-a3fc-a9e0969eff8e.mp3",
       "hf_20260822_140913_c84c06ec-a51a-41cb-9141-2cc46e4f3633.mp3",
       "hf_20260822_140913_c8e4d02e-134a-40d3-96d1-401230195c70.mp3",
       "hf_20260822_140913_499815c9-8802-465f-8297-4f6ca0981600.mp3",
       "hf_20260822_140913_363e2a5e-7dfd-41a2-a896-6737affc79c6.mp3"]

# (nombre, fuente, desde, duracion, zoom|None, capa|None)
# zoom = (factor, centro x 0-1, centro y 0-1) — recorte sobre el mismo plano, para cortar
# a un detalle sin renderizar una pantalla nueva
PLAN = [
 ("plate",  "ui/clips/plate.mp4",            0.00,  4.00, None,               None),
 ("1a",  "src/g1a.mp4",                      0.00,  7.75, None,               None),
 ("1b",  "src/g1b.mp4",                      0.00,  8.75, None,               "ui/clips/ov-01-sistemas"),
 ("2a",  "src/g2.mp4",                       0.00,  8.00, None,               "ui/clips/ov-02-areas"),
 ("2b",  "src/g2.mp4",                       8.00,  7.00, (1.55, 0.24, 0.52), None),
 ("2c",  "src/g2.mp4",                      15.00,  7.96, None,               "ui/clips/ov-02-areas"),
 ("3a",  "src/g3.mp4",                       0.00,  7.60, None,               "ui/clips/ov-03-brasil"),
 ("3b",  "src/g3.mp4",                       7.60,  6.00, (1.70, 0.60, 0.52), None),
 ("4a",  "ui/clips/04-dependencias.mp4",     0.00,  8.00, None,               None),
 ("4b",  "ui/clips/04-dependencias.mp4",     8.00,  5.30, (1.35, 0.50, 0.66), None),
 ("4c",  "ui/clips/04-pregunta.mp4",         0.00, 14.23, None,               None),
 ("5a",  "src/g5.mp4",                       0.00,  6.60, None,               "ui/clips/ov-05-capa"),
 ("5b",  "src/g5.mp4",                       6.60,  6.50, (1.45, 0.50, 0.46), None),
 ("6a",  "ui/clips/06-criterios.mp4",        0.00,  7.85, None,               None),
 ("6b",  "ui/clips/06-permisos.mp4",         0.00,  8.85, None,               None),
 ("7a",  "ui/clips/07-registro.mp4",         0.00,  5.90, None,               None),
 ("7b",  "ui/clips/07-patron.mp4",           0.00,  6.95, None,               None),
 ("8a",  "ui/clips/08-insight.mp4",          0.00,  7.50, None,               None),
 ("8b",  "ui/clips/08-insight.mp4",          7.50,  6.20, (1.32, 0.50, 0.40), None),
 ("9a",  "ui/clips/09-mcp.mp4",              0.00,  9.28, None,               None),
 ("9b",  "ui/clips/09-skill.mp4",            0.00,  5.00, None,               None),
 ("9c",  "ui/clips/09-skill.mp4",            5.00,  5.28, (1.38, 0.74, 0.52), None),
 ("10a", "ui/clips/10-bandeja.mp4",          0.00,  7.00, None,               None),
 ("10b", "ui/clips/10-caso.mp4",             0.00,  7.94, None,               None),
 ("11a", "ui/clips/11-valor.mp4",            0.00,  8.00, None,               None),
 ("11b", "ui/clips/11-valor.mp4",            8.00,  8.06, (1.42, 0.26, 0.26), None),
 ("12a", "src/g12.mp4",                      0.00,  7.00, None,               "ui/clips/ov-12-cierre"),
 ("12b", "ui/clips/12-plataforma.mp4",       0.00,  5.00, None,               None),
 ("12c", "ui/clips/12-plataforma.mp4",       5.00,  5.75, (1.30, 0.42, 0.44), None),
]
FPS = 25
os.makedirs("src", exist_ok=True); os.makedirs("seg", exist_ok=True)
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])

for k, v in GEN.items():
    if not os.path.exists(f"src/{k}.mp4"): sh(f"curl -sfo src/{k}.mp4 '{B}{v}'")
for i, v in enumerate(AUD, 1):
    if not os.path.exists(f"src/a{i}.mp3"): sh(f"curl -sfo src/a{i}.mp3 '{B}{v}'")

segs = []
loops = {}
def loop_base(srcf):
    """Los planos generados duran 5s. Se hace un bucle ida y vuelta largo, una sola vez
    por fuente, y despues cada plano corta el tramo que necesita."""
    if srcf in loops: return loops[srcf]
    key = os.path.basename(srcf).replace(".mp4", "")
    out = f"seg/loop_{key}.mp4"
    sh(f"ffmpeg -y -v error -i '{srcf}' -vf 'scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}' "
       f"-an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p seg/_f.mp4")
    sh(f"ffmpeg -y -v error -i seg/_f.mp4 -vf reverse -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p seg/_r.mp4")
    with open("seg/_l.txt", "w") as fh:
        for _ in range(6):
            fh.write(f"file '{os.path.abspath('seg/_f.mp4')}'\nfile '{os.path.abspath('seg/_r.mp4')}'\n")
    sh(f"ffmpeg -y -v error -f concat -safe 0 -i seg/_l.txt -c copy '{out}'")
    loops[srcf] = out
    return out

for name, srcf, ss, tgt, zoom, ov in PLAN:
    base = loop_base(srcf) if srcf.startswith("src/") else srcf
    vf = [f"scale=1920:1080:flags=lanczos,setsar=1,fps={FPS}"]
    if zoom:
        z, cx, cy = zoom
        vf.insert(0, f"crop=iw/{z}:ih/{z}:(iw-iw/{z})*{cx}:(ih-ih/{z})*{cy}")
    cut = f"seg/c_{name}.mp4"
    sh(f"ffmpeg -y -v error -ss {ss:.3f} -i '{base}' -vf '{','.join(vf)}' -t {tgt:.3f} "
       f"-an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p '{cut}'")
    if ov:
        out = f"seg/{name}.mp4"
        sh(f"ffmpeg -y -v error -i '{cut}' -framerate {FPS} -i '{ov}/%05d.png' "
           f"-filter_complex '[0:v][1:v]overlay=0:0:eof_action=repeat' -t {tgt:.3f} "
           f"-an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p '{out}'")
        segs.append(out)
    else:
        segs.append(cut)

with open("seg/list.txt", "w") as fh:
    for s in segs: fh.write(f"file '{os.path.abspath(s)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg/list.txt -c copy seg/video.mp4")

sh("ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t 4 seg/sil4.wav")
sh("ffmpeg -y -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t 1 seg/sil1.wav")
parts = ["seg/sil4.wav"]
for i in range(1, 13):
    sh(f"ffmpeg -y -v error -i src/a{i}.mp3 -ar 48000 -ac 2 seg/a{i}.wav")
    parts.append(f"seg/a{i}.wav")
    if i < 12: parts.append("seg/sil1.wav")
with open("seg/alist.txt", "w") as fh:
    for p in parts: fh.write(f"file '{os.path.abspath(p)}'\n")
sh("ffmpeg -y -v error -f concat -safe 0 -i seg/alist.txt -c copy seg/audio.wav")
sh("ffmpeg -y -v error -i seg/video.mp4 -i seg/audio.wav -c:v copy -c:a aac -b:a 192k corte-v3.mp4")
print("VIDEO", dur("seg/video.mp4"), "AUDIO", dur("seg/audio.wav"), "FINAL", dur("corte-v3.mp4"))
