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

---

# v2 — Isometric Flat Vector (versión en inglés)

## Fórmula de estilo (literal en todos los prompts)

```
Isometric flat vector illustration on a plain solid pale-grey background: clean geometric
forms in true isometric projection with no outlines, broad flat fields of colour with one
slightly darker tone per face for depth, crisp straight edges and softly rounded corners, a
restrained palette of cool greys and desaturated slate with ONE signature accent — cobalt
blue — carrying the key element of every frame. No texture, no grain, no gradients, no
realistic lighting and no cast shadow beyond a simple soft contact shadow; motion is smooth
and mechanical, with elements sliding and snapping along the isometric axes.
```

Preset **Isometric Flat Vector** `c109eddb-1a79-478a-afd5-273bd0b205e5`
→ `media_id 090c5e7b-d9f3-4351-8329-143a0e77eeb7`.

## Assets v2 (job_ids reusables)

| Asset | job_id |
|---|---|
| Ancla de estilo | `68f11314-3290-4fbc-94cb-43f20c4c736a` |
| Especialista de operaciones | `1012e04b-9d1c-449f-9dd9-cae9b31c84dc` |
| Ingeniero de software | `379b9220-bb9f-42d9-9678-3a8b48e685f5` |
| Persona nueva | `0353ccf5-3d97-472c-960c-b773c16c461f` |
| Oficina isométrica | `dfc4b531-284c-4915-873c-62430b2cd10a` |
| Oficina, esquina opuesta | `2ff12b10-8dd9-4d80-bbd4-f18b5e1f89d7` |
| Losa con hueco circular | `96323044-87fe-422a-b388-9bf1efa6472b` |
| Sala de racks | `018509c0-70fc-4a17-a8d8-98e3ed824925` |
| Sala de tablero | `f09cf6f7-0832-49cc-aa55-979a90a8b9c5` |
| Carpeta azul (hilo conductor) | `0c6273e6-4311-44e9-b55a-b3a46fa48af0` |
| Pila de ventanas de app | `88c633c1-0596-4f48-b40a-5eafc43b8587` |
| Emblema Velaria isométrico | `4af1641d-46ce-4ae1-a6fa-f951850f90e0` |
| Iconos de escritorio (carpeta manila, ventana, cursor) | `ddaf2628-3ae0-4a35-b81a-a511f306aa8b` |

## Cómo pedir las herramientas sin nombrar marcas

En vez de "Excel" / "PowerPoint" / "icono de carpeta de Mac", describir la forma:

```
a green-barred window showing an empty grid of spreadsheet cells
an orange-barred window showing a simple bar chart on a slide
a blue-barred window showing blank ruled document lines
a folder icon with the classic small raised tab on the top-left edge
a grey application window with three small round dots in a row along its title bar
```

Y siempre cerrar el NEGATIVE con: `on-screen text, captions, lettering, brand logos`.

## Dirección de voz (inglés, Bram)

```
[ crisp corporate explainer narrator, confident and dry, warm direct timbre, brisk pace,
starts speaking immediately] [00:00-00:09] {línea}
```
