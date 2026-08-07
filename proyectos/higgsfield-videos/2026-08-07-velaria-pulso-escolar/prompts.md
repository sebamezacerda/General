# Prompts usados

## Fórmula de estilo (va literal en TODOS los prompts de imagen y video)

```
Hand-drawn whiteboard marker illustration on a clean plain off-white dry-erase surface:
uniform thin black marker strokes with a slightly wobbly hand-drawn quality, simple rounded
figures and diagrammatic objects, flat fills, no shading, no gradients, no texture, with ONE
signature accent — cobalt blue — used sparingly on a single highlighted element per frame
while everything else stays black on white. The background is always the plain empty
off-white board with no grid, no vignette and no painted color; drawings sit directly on it,
and motion is simple limited animation on twos with elements drawn on and wiped off cleanly.
```

Ancla de estilo: preset **Whiteboard Doodle** `b347d852-98fc-4013-92b7-6b0219fb21be`
→ `media_id b5b79be0-98bb-478a-b449-f989756555d2` como `image_references`.
Modelo imagen: `seedream_v5_pro`. Modelo video: `gemini_omni`. Voz: `seed_audio`.

## Assets (job_ids reusables como `image_references`)

| Asset | job_id |
|---|---|
| Ancla de estilo | `636dd192-6c68-4d71-88d1-7c47b54e91be` |
| Especialista de operaciones | `64ac185f-37de-460d-80b8-5bb9649740af` |
| Ingeniero de software | `27c99de1-4ab9-473f-8fe7-9b82bfb0ecaf` |
| Persona nueva | `f8a0b09e-01fd-457d-abd2-4a8f2cf6575c` |
| Oficina de operaciones | `a0e5545e-e099-4c57-9b11-ae89f9a7eb7c` |
| Oficina, cenital | `3d2c4bab-850d-41b2-8f86-d8215bf84ae9` |
| Sala de pizarra | `f64498ba-3761-442c-b718-f3ae53cc8000` |
| Archivo de biblioratos | `8bb0548c-33f2-449e-b933-796e2ac8e7da` |
| Sala de métricas | `eff3b485-e6b7-4c18-8095-25d0e50d906e` |
| Libreta azul (hilo conductor) | `f1bc38f2-5b00-4ce8-adc0-20d8b82a3adc` |
| Pila de papeles | `9f5bdea0-30f8-43cb-9f70-77980bf9d650` |
| Emblema Velaria | `2b7f6a7b-b6e2-47d5-bbbd-d6dad7214de2` |
| Monitor saturado | `91c057bc-4cd1-44a0-b93e-abe6e95e242d` |

## Estructura del prompt de cada bloque de video

```
Style: {FÓRMULA}; simple limited animation on twos — the visual style is EXACTLY as in the reference images.
PALETTE LOCK: use ONLY the colors and the background treatment of the reference images
(plain off-white dry-erase board, thin black marker lines, one cobalt blue accent). ...
A single 10-second scene of FIVE hard-cut shots. ... Characters only emote and gesture,
they do NOT talk. Motion starts on frame 1 (no opening freeze).
REFERENCES (look, identity, palette): @Image1 = LOCATION (...). @Image2 = ... 
SHOT 1 — 0.0s to 2.0s — {TAMAÑO+ÁNGULO}: {acción}; {UN movimiento de cámara}.
HARD CUT.   ... (5 planos, corte a 2/4/6/8 s)
AUDIO: {SFX diegéticos, 2-4 señales} — no voice, no narration, no music.
NEGATIVE: opening on a reference image, leading freeze, dissolves or fades, NEW or foreign
colors, style drift, extra people, characters talking, lip-sync, on-screen text, captions,
photorealism, 3D render, watermark.
```

**Ojo:** el backend responde con recomendación de preset "3D RENDER" en vez de encolar.
Hay que reenviar con `declined_preset_id: 5a77643c-b6cc-4efd-bdc6-ab8ff48dfa82`.

## Narración (`seed_audio`, voice_type `element`)

Frase de dirección, idéntica en las seis líneas (es lo que mantiene el timbre estable):

```
[ narrador comercial chileno, tono claro y seguro, timbre cálido y directo, ritmo ágil,
starts speaking immediately] [00:00-00:09] {línea}
```

## Música (`sonilo_music`, 60 s)

```
Instrumental electronic underscore for a sixty-second corporate explainer, no vocals.
Opens dry and unresolved: a sparse ticking pulse and a single held low tone for the first
eighteen seconds. At eighteen seconds it cuts to silence for a beat, then a clean
four-on-the-floor kick and a bright arpeggiated synth enter together and lift the track.
Through the middle it drives forward, warm and confident, minimal. In the last eight seconds
the drums drop away and it resolves onto one calm sustained chord that fades.
```
