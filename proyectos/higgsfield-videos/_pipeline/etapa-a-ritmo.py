# -*- coding: utf-8 -*-
"""Etapa A: mide la voz y re-deriva el ritmo, los cortes, el plan y los cues.

El error del intento anterior fue medir cada toma contra su PROPIA mediana: una
toma entera rapida se quedaba rapida. El espectador escucha el video como una
sola pieza, asi que el objetivo tiene que ser global.

No toca archivos del proyecto: imprime el resultado en JSON para aplicarlo en el
repo. El sandbox es efimero y no sobrevive entre llamadas.
"""
import json, os, subprocess, unicodedata

CFG = json.load(open("cfg.json"))
LET = CFG["letras"]
BANDA = 0.08          # +-8% alrededor de la mediana es prosodia, no defecto
CLAMP = (0.80, 1.25)  # techo de correccion por tramo; mas suena procesado
PAUSA = (0.20, 0.40)  # las pausas entre frases se acotan a esta ventana


def sh(c):
    subprocess.run(c, shell=True, check=True, capture_output=True)


def dur(p):
    r = subprocess.run(f"ffprobe -v error -show_entries format=duration -of json '{p}'",
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])


def silabas(t):
    """Grupos vocalicos: mide el tempo percibido mucho mejor que los caracteres."""
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    n = p = 0
    for c in t:
        v = c in "aeiou"
        n += v and not p
        p = v
    return n


os.makedirs("src", exist_ok=True)
for i, f in enumerate(CFG["tomas"], 1):
    if not os.path.exists(f"src/t{i}.mp3"):
        sh(f"curl -sfo src/t{i}.mp3 '{CFG['base']}{f}.mp3'")
    sh(f"ffmpeg -y -v error -i src/t{i}.mp3 -af 'atempo={CFG['speed']}' "
       f"-ar 48000 -ac 2 src/s{i}.wav")

from faster_whisper import WhisperModel
M = WhisperModel("small", device="cpu", compute_type="int8")
tramos, texto = {}, {}
for i, le in enumerate(LET, 1):
    segs, _ = M.transcribe(f"src/s{i}.wav", language="es", word_timestamps=True,
                           vad_filter=False, beam_size=5)
    pal = [(w.start, w.end, w.word.strip()) for s in segs for w in (s.words or [])]
    # la particion sale de las palabras, no de silencedetect: sus tramos cortan
    # frases por la mitad y el ritmo de medio enunciado no significa nada
    fr, cur = [], []
    for k, (a, b, w) in enumerate(pal):
        cur.append((a, b, w))
        if (w.endswith((".", "?", "!", "…")) or k == len(pal) - 1
                or pal[k + 1][0] - b > 0.45):
            fr.append(cur); cur = []
    fs = []
    for f in fr:
        a, b = f[0][0], f[-1][1]
        t = " ".join(w for _, _, w in f)
        s = silabas(t)
        if b - a >= 0.25 and s >= 2:
            fs.append((a, b, t, s, s / (b - a)))
    tramos[le] = fs
    texto[le] = [[round(a, 2), round(b, 2), t] for a, b, t, _, _ in fs]
    print(f"  {le}: {len(fs)} frases, {dur(f'src/s{i}.wav'):.2f}s", flush=True)

todas = sorted((t for le in LET for t in tramos[le]), key=lambda t: t[4])
peso, acc = sum(t[1] - t[0] for t in todas), 0.0
OBJ = todas[len(todas) // 2][4]
for t in todas:                       # mediana ponderada por duracion
    acc += t[1] - t[0]
    if acc >= peso / 2:
        OBJ = t[4]; break


def f_habla(r):
    o = min(max(r, OBJ * (1 - BANDA)), OBJ * (1 + BANDA))
    return min(max(o / r, CLAMP[0]), CLAMP[1])


def f_pausa(g):
    return min(max(g / min(max(g, PAUSA[0]), PAUSA[1]), 0.5), 4.0)


ritmo = {}
for i, le in enumerate(LET, 1):
    D, pz, t = dur(f"src/s{i}.wav"), [], 0.0
    for (a, b, _, _, r) in tramos[le]:
        if a > t + 0.02:
            pz.append([t, a, f_pausa(a - t)])
        pz.append([max(a, t), b, f_habla(r)]); t = b
    if D > t + 0.02:
        pz.append([t, D, f_pausa(D - t)])
    ritmo[le] = [[round(a, 3), round(b, 3), round(f, 4)] for a, b, f in pz if b - a > 0.005]


def mapa(viejo, nuevo):
    """t del reloj viejo -> t del reloj nuevo, pasando por la fuente."""
    def tabla(pl):
        o, t = [], 0.0
        for a, b, f in pl:
            d = (b - a) / f; o.append((a, b, t, t + d, f)); t += d
        return o
    V, N = tabla(viejo), tabla(nuevo)

    def m(x):
        s = V[-1][1]
        for a, b, ta, tb, f in V:
            if x <= tb:
                s = a + (x - ta) * f; break
        s = min(max(s, N[0][0]), N[-1][1])
        for a, b, ta, tb, f in N:
            if s <= b:
                return round(ta + (s - a) / f, 3)
        return round(N[-1][3], 3)
    return m


VIEJO = json.load(open("ritmo-viejo.json"))
MAP = {le: mapa(VIEJO[le], ritmo[le]) for le in LET}


# ---------------------------------------------------------------- tomas nuevas
for i, le in enumerate(LET, 1):
    tr = []
    for k, (a, b, f) in enumerate(ritmo[le]):
        o = f"src/r{k:03d}.wav"
        sh(f"ffmpeg -y -v error -i src/s{i}.wav -af "
           f"'atrim={a}:{b},asetpts=N/SR/TB,atempo={f}' -ar 48000 -ac 2 {o}")
        tr.append(o)
    open("src/l.txt", "w").write("".join(f"file '{os.path.abspath(t)}'\n" for t in tr))
    sh(f"ffmpeg -y -v error -f concat -safe 0 -i src/l.txt -c copy src/t{i}.wav")


# ---------------------------------------------------------------- fronteras
import numpy as np

ENV = {}


def envolvente(w):
    """Envolvente RMS en ventanas de 20 ms. Se lee la pista entera una vez: mil
    llamadas a ffmpeg para sondear niveles tardan mas que decodificar el wav."""
    r = subprocess.run(f"ffmpeg -v error -i {w} -ac 1 -ar 16000 -f s16le -",
                       shell=True, capture_output=True)
    x = np.frombuffer(r.stdout, "<i2").astype(np.float32) / 32768.0
    n = 320
    x = x[:len(x) // n * n].reshape(-1, n)
    rms = np.sqrt((x ** 2).mean(1) + 1e-12)
    return 20 * np.log10(rms), n / 16000.0


def al_silencio(w, t, D):
    """Un corte sobre la cola de una palabra se oye como un chasquido; en
    silencio es invisible. Se busca el punto mas callado del entorno."""
    if w not in ENV:
        ENV[w] = envolvente(w)
    db, paso = ENV[w]
    if t <= 0.06 or t >= D - 0.06 or not len(db):
        return round(min(max(t, 0.0), D), 3)
    c = int(t / paso); r = int(0.30 / paso)
    a, b = max(1, c - r), min(len(db) - 1, c + r + 1)
    j = a + int(np.argmin(db[a:b]))
    return round(min(max(j * paso, 0.06), D - 0.06), 3) if db[j] < db[c] - 0.5 else round(t, 3)


VC = json.load(open("cortes-viejos.json"))
DT = {le: dur(f"src/t{i}.wav") for i, le in enumerate(LET, 1)}
NC = []
for tk, tr in VC:
    if not tr:
        NC.append([tk, []]); continue
    le = LET[tk - 1]; m = MAP[le]
    NC.append([tk, [[al_silencio(f"src/t{tk}.wav", m(a), DT[le]),
                     al_silencio(f"src/t{tk}.wav", m(b), DT[le])] for a, b in tr]])
for j in range(1, len(NC)):
    a, b = NC[j - 1], NC[j]      # dos escenas seguidas comparten frontera
    if a[0] == b[0] and a[1] and b[1] and abs(a[1][-1][1] - b[1][0][0]) < 0.35:
        p = round((a[1][-1][1] + b[1][0][0]) / 2, 3)
        a[1][-1][1] = p; b[1][0][0] = p


# ---------------------------------------------------------------- plan y cues
PLAN = json.load(open("plan-viejo.json"))
CUES = json.load(open("cues-viejos.json"))     # {lamina: [fracciones]}
plan_n, cues_n = [], {}
for k, (nom, ven) in enumerate(PLAN):
    tk, tv = VC[k]
    if not tv:
        plan_n.append([nom, ven]); continue
    tn = NC[k][1]
    vo_v = round(sum(b - a for a, b in tv), 3)
    vo_n = round(sum(b - a for a, b in tn), 3)
    plan_n.append([nom, round(vo_n + (ven - vo_v), 3)])
    m = MAP[LET[tk - 1]]

    def nueva(phi):
        """fraccion vieja -> absoluto en la toma -> fraccion nueva. Camina los
        tramos: una escena puede estar hecha de dos trozos no contiguos."""
        off, acc, x = phi * vo_v, 0.0, tv[-1][1]
        for a, b in tv:
            if off <= acc + (b - a) + 1e-9:
                x = a + (off - acc); break
            acc += b - a
        y, acc = m(x), 0.0
        for a, b in tn:
            if y <= b + 1e-9:
                return round(min(max((acc + max(y - a, 0.0)) / vo_n, 0.0), 1.0), 4)
            acc += b - a
        return 1.0
    cues_n[nom] = {"vo": vo_n, "vo_viejo": vo_v,
                   "f": {str(p): nueva(p) for p in CUES.get(nom, [])}}

antes = sorted(t[4] for t in todas)
desp = sorted(t[3] / ((t[1] - t[0]) / f_habla(t[4])) for t in todas)


def d(x):
    n = len(x); return round(x[n // 10], 2), round(x[n // 2], 2), round(x[(9 * n) // 10], 2)


print("\n===JSON===")
print(json.dumps({"objetivo": round(OBJ, 3), "frases": len(todas),
                  "antes": d(antes), "despues": d(desp),
                  "ritmo": ritmo, "cortes": NC, "plan": plan_n,
                  "cues": cues_n, "texto": texto,
                  "tomas": {le: round(DT[le], 3) for le in LET}},
                 ensure_ascii=False))
