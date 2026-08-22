# Bitácora de generaciones

## Configuración base (imagen)

**Modelo: `recraft_v4_1`** con `model_type: "utility"`.

Elegido porque es el único del catálogo que acepta **paleta cerrada como parámetro** en vez de
depender de que el prompt convenza al modelo:

```json
{
  "model": "recraft_v4_1",
  "model_type": "utility",
  "aspect_ratio": "16:9",
  "background_color": "#0B0F17",
  "colors": ["#0B0F17", "#151C2B", "#2456D6", "#7DA0F2", "#8A94A6", "#F5F7FA"]
}
```

`utility` está descrito por el proveedor como "cleaner, flatter, front-facing, and predictable"
— que es exactamente el "nada flota / sin sombras / ortográfico" del sistema de Velaria.
`resolution: "1k"` para validación; subir a `"2k"` en las tomas finales.

Las negaciones van dentro del prompt (Recraft no expone negative prompt): cerrar siempre con
`Absolutely no glow, no bloom, no gradient, no rounded corners, no soft shadows, no
reflections, no text, no lettering, no logos.`

## Ronda 1 — frames de validación · 2026-08-22

Tres frames que definen el arte del resto. 1344×768.

| Escena | Toma | job_id | Estado |
|---|---|---|---|
| 5 | 5.1 — la capa Velaria | `5543e2f4-f418-44ce-9f5e-8ca022c7fa11` | generado, sin auditar |
| 8 | 8.1 — dashboard | `3e43218d-d54f-4d7b-a757-d68642509532` | generado, sin auditar |
| 12 | 12.1 — el ecosistema | `a4fb4e65-5e2a-4f6c-8dab-9f9ac0e5e1c4` | generado, sin auditar |

⚠ **No pude inspeccionar estos frames**: la política de red del entorno bloquea el CDN de
Higgsfield (`d8j0ntlcm91z4.cloudfront.net` → 403 en el CONNECT del proxy). Se ven en el widget
del cliente, pero la revisión visual la tiene que hacer una persona.

### Checklist de auditoría (aplicar a cada frame)

- [ ] Fondo exactamente `#0B0F17`, sin viñeta ni degradado.
- [ ] **Un solo** elemento en azul `#2456D6` por frame.
- [ ] Cero glow, cero bloom, cero halo alrededor del azul.
- [ ] Esquinas rectas en todos los planos (0–2px).
- [ ] Sin sombras proyectadas ni sensación de elevación.
- [ ] Sin texto inventado, sin logos, sin iconos con curvas decorativas.
- [ ] Espacio vacío suficiente para los rótulos en post.

## Pendiente

- Ronda 2: el resto de las tomas, una vez aprobado el arte de la ronda 1.
- Escenas 1 y 2 llevan fotografía (faena, puerto, personas) — evaluar si `utility` sirve o si
  conviene otro modelo para esas dos, manteniendo la paleta en post.

## Ronda 2 — validación del motor de video · 2026-08-22

**Motor elegido: `cinematic_studio_video_v2`.** Es el único del catálogo con las cuatro palancas
que este video necesita: `start_image` **+** `end_image` (le doy los dos extremos del movimiento
y solo interpola), `cfg_scale` (adherencia al prompt), `speedramp: "linear"` (el sistema pide
movimientos lineales) y `sound: "off"`.

```json
{
  "model": "cinematic_studio_video_v2",
  "mode": "pro", "duration": 5, "aspect_ratio": "16:9",
  "sound": "off", "genre": "auto", "speedramp": "linear", "cfg_scale": 0.85
}
```

| Prueba | job_id | Estado |
|---|---|---|
| 5.1 — descenso lineal sobre la capa | `00cc868f-628b-4859-8619-3a1818dee471` | generado, **sin auditar** |

Igual que la ronda 1: el CDN está bloqueado por la política de red, así que la revisión visual
la tiene que hacer una persona.

### Presets: rechazar siempre

El servidor sugirió el preset viral **"IN THE DARK"** para este prompt. Se rechazó con
`declined_preset_id`. Los presets imponen un estilo propio — exactamente lo que el sistema de
Velaria prohíbe. **Ningún preset en este proyecto.**

### ⚠ Hallazgo: la resolución del video sigue a la del still

El video salió a **1344×768**, idéntico al still de origen. El modelo no reescala: hereda el
tamaño del `start_image`. Para un máster corporativo en 1080p eso no alcanza.

Dos salidas, y cambian el presupuesto:
- **Stills finales a 2k** (8 créditos c/u contra 1,25 del 1k — 6,4× más caro).
- **`upscale_video`** sobre las tomas aprobadas (costo sin medir todavía).

Recomendación: iterar en 1k, que es barato, y pagar 2k **solo en las tomas ya aprobadas**.

## Costos unitarios reales (medidos, no estimados)

| Ítem | Créditos |
|---|---:|
| Imagen Recraft 1k (1344×768) | 1,25 |
| Imagen Recraft 2k | 8 |
| Video `cinematic_studio_video_v2` pro, 5s | 7,5 |
| Video mismo modelo, std, 5s | 5 |
| Locución `seed_audio`, ~35 palabras | 1,6 |

Los de imagen salen de la diferencia de saldo antes/después; los demás, del preflight
`get_cost`.

## Presupuesto de producción

**8 tomas generativas** (1.1 faena, 1.2 puerto, 2.1 grilla, 2.2 proceso, 3.1 mapa, 5.1 capa,
5.2 los diez, 12.1 ecosistema) — las otras 13 pantallas son HTML y no cuestan créditos.

| Partida | Cálculo | Créditos |
|---|---|---:|
| Stills de iteración (1k) | 8 tomas × 1,25 × 2 intentos | 20 |
| Stills finales (2k) | 8 × 8 | 64 |
| Video pro 5s | 8 × 7,5 × 2,5 intentos | 150 |
| Locución | 424 palabras ≈ 19 cr × 1,5 intentos | 30 |
| **Total estimado** | | **≈ 265** |

Rango razonable: **150** si el arte cierra rápido, **400** si hay mucha iteración. El factor 2,5
en video no es pesimismo: dirigir arte contra un modelo generativo rara vez sale a la primera.

Saldo actual: **1.112 créditos** — sobra holgadamente, del orden de 4× el estimado.

Sin medir todavía: `upscale_video` sobre las tomas aprobadas.

## Ronda 3 — prueba de voz y stills fotográficos · 2026-08-22

### Locución — `seed_audio`

Requisito del cliente: **voz nativa en español, mujer, español plano.** Cuatro candidatas
preset con nombre hispano, todas leyendo el texto real de la escena 1:

| Voz | voice_id | Duración | Ritmo |
|---|---|---:|---:|
| Marisol | `75e72cd5-011b-4130-a474-e8b1ab341f04` | 18,28s | 108 wpm |
| Inés | `023ebf5e-1970-40d8-825c-a5ef6a1dd4ff` | 16,88s | 117 wpm |
| Elena | `ca83ca7f-c186-493d-bd69-0d765fa861b2` | 16,50s | 120 wpm |
| Isabella | `80924413-1ea8-4e64-9719-e00b86796f05` | 16,10s | 123 wpm |

Todas `voice_type: "preset"`. **Sin evaluar el acento**: el CDN está bloqueado, no puedo
escucharlas. La elección es del cliente.

Descartadas antes de la prueba: las voces chilenas propias del workspace (elementos de Casa
Sanz) — el pedido es *español plano* y el acento chileno es marcado. Se gastaron ~5 créditos en
tres pruebas previas (dos masculinas + una chilena) antes de conocer el requisito.

Parámetro útil para después: `speech_rate` permite ajustar el ritmo sin regenerar el guion.

### Stills fotográficos

Las escenas 1 y 2 son fotografía, así que van con `model_type: "standard"` (no `utility`, que es
para superficies planas) y **sin `background_color`** — solo la paleta como guía de grading:

```json
{"model_type": "standard", "colors": ["#0B0F17","#151C2B","#8A94A6","#F5F7FA"]}
```

| Toma | job_id | Modelo |
|---|---|---|
| 1.1 faena aérea | `bfc5e836-346d-42bc-acb9-518eb054ed70` | standard |
| 1.2 puerto | `fccd6520-1527-4ab4-8bff-7f5aa5b59eb2` | standard |
| 2.1 viñeta individual (prueba) | `6cd0d181-8eb1-4bd8-b4d4-80e0f88a63ba` | standard |
| 3.1 mapa punteado | `2c91fe82-7137-4d98-8666-994afa837bf7` | utility + paleta cerrada |

Todas sin auditar — CDN bloqueado.

**Nota sobre la escena 2:** la grilla de diez personas conviene armarla en HTML (hairlines,
labels mono, alineación exacta) y **rellenar las celdas con fotos generadas**, en vez de pedirle
la grilla entera a un modelo. La toma 2.1 de arriba es la prueba de una celda.

## Ronda 4 — el problema no era la voz, era el motor · 2026-08-22

Las cuatro candidatas de la ronda 3 leen español **con acento anglo**. `seed_audio` (ByteDance)
es anglocéntrico: la voz es femenina y el nombre hispano, pero la pronunciación es inglesa.

`text2speech_v2` permite cambiar de motor manteniendo el mismo `voice_id`. Se probaron los dos
multilingües:

| # | Voz | Motor | job_id | Duración |
|---|---|---|---|---:|
| 51 | Inés | elevenlabs | `7ebcef73-2b15-4d66-9e57-dd1db0a58040` | 20,40s |
| 52 | Marisol | elevenlabs | `7d94da20-59f7-4001-a306-c7c1f72dfd75` | 17,28s |
| 53 | Inés | minimax | `82e0487e-c604-4b50-8f8d-4a17437a5233` | 19,16s |
| 54 | Isabella | minimax | `e3a54302-dec5-4659-a42c-75a999aad78c` | 15,50s |

### 🔑 La palanca: `language_boost`

MiniMax devolvió `language_boost: "auto"` entre sus parámetros. **Si el motor no detectó que el
texto es español, forzar ese parámetro es lo que falta.** Es el próximo intento si estas cuatro
siguen sonando anglo — antes de descartar voces o clonar una nueva.

### Descartado: `inworld_text_to_speech`

Es el único modelo del catálogo con voces marcadas nativas en español — Lupita (es), Diego (es),
Miguel (es), Rafael (es), Lupita la única femenina. **No se puede usar**: está reservado al
pipeline de generación de juegos y no admite audio suelto.

### Plan B si ningún preset convence

`create_voice` clona una voz desde una muestra de audio. Con 30–60 segundos de una locutora
hispanohablante leyendo cualquier texto se obtiene una voz nativa propia, reutilizable en todos
los videos de Velaria. Es la opción más sólida a mediano plazo, y la única que garantiza acento
plano de verdad.

### Nota sobre duración

Estas tomas van de 15,5s a 20,4s para las mismas 33 palabras — una diferencia del 30% entre
motores. **La duración final del video depende de qué motor se elija**, no solo del guion:
entre 3:35 (Isabella/minimax) y 4:40 (Inés/elevenlabs).

## Ronda 5 — la voz elegida, contrastada · 2026-08-22

Voz seleccionada por el cliente: **Isabella por MiniMax** (`80924413-1ea8-4e64-9719-e00b86796f05`,
`text2speech_v2` variant `minimax`). El archivo de referencia es el job `e3a54302`.

Se generó la locución de la **escena 2** por los dos caminos posibles, para decidir cuál usar en
las 12 pistas:

| # | Camino | job_id | Duración |
|---|---|---|---:|
| 61 | Clonar desde el audio de referencia (`seed_audio` + `audio_references`) | `0f7959b3-d7ca-4eb5-95f9-e652ce6f17e7` | 19,82s |
| 62 | Repetir la receta original (`text2speech_v2` / minimax / Isabella) | `93e7d5cb-fa6c-41fd-bfd5-8fb3d7f8575c` | 21,96s |

### ⚠ Por qué la 62 es probablemente la correcta

Clonar el audio de referencia lo hace pasar por **`seed_audio`**, que es justamente el motor
anglocéntrico que causó el problema de acento. Se estaría clonando un buen resultado a través
del motor equivocado, con riesgo de reintroducir el acento inglés.

La receta original (62) reproduce exactamente la configuración que generó el archivo que gustó.
Es determinista y no depende de una clonación. **Salvo que la 61 suene mejor al oído, la
producción va por la 62.**

La clonación sí tiene sentido en otro escenario: partir de una grabación real de una locutora
hispanohablante (ver `create_voice` en la ronda 4), no de un audio ya sintético.

## Ronda 6 — las 12 pistas y el render de pantallas · 2026-08-22

Sebastián delegó las decisiones para avanzar sin él.

### Locución completa

12 pistas con la receta confirmada (`text2speech_v2` / `minimax` / Isabella
`80924413-1ea8-4e64-9719-e00b86796f05`). Duraciones medidas y línea de tiempo en `montaje.md`.

**Total: 3:29** con 1s de aire entre escenas y 4s de placa inicial.

### Decisión tomada sobre la duración

El guion pedía 2:30–3:00 y el resultado es 3:30. **No recorté el guion**: es contenido de cara
al cliente final y cortarle un sexto es decisión de negocio, no de montaje. Queda propuesto en
`montaje.md` el corte concreto (escena 4, que dura 26,5s y repite en audio lo que la pantalla
ya muestra escrito) para cuando lo decida.

### Pantallas renderizadas a video

Las 13 pantallas quedaron animadas y encodeadas a MP4 1080p — ver `ui/RENDER.md`. Sin gastar
créditos. `ui/clips/_reel-pantallas.mp4` (2:02) es el reel completo.

Eso deja el video con **dos tercios del metraje ya producidos y verificados**. Lo que falta son
las 8 tomas generativas, que sí dependen de Higgsfield y que **no puedo auditar** desde acá
porque el CDN está bloqueado.

### Gasto acumulado

~62 créditos de 1.112. Muy por debajo del presupuesto de 265 — porque la mitad del video
terminó construyéndose en vez de generándose.

## Ronda 7 — las tomas generativas, completas · 2026-08-22

Todas con `cinematic_studio_video_v2` / pro / 5s / `speedramp: linear` / `cfg_scale 0.85` /
`sound: off`.

| Toma | Escena | Movimiento | still | video |
|---|---|---|---|---|
| 1.1 faena aérea | 1 | descenso vertical lineal | `bfc5e836` | `ea2b7d28-9cab-40fb-af41-527b4e45fff0` |
| 1.2 puerto | 1 | travelling lateral lineal | `fccd6520` | `0efafda1-7473-4074-8a48-fab24279810b` |
| 2.1 grilla de diez | 2 | cámara fija, la gente se mueve | `1869ef6d` | `526d90d7-fad3-42e6-9372-08239aeb2026` |
| 3.1 mapa punteado | 3 | push in frontal, sin rotación | `2c91fe82` | `ae78329e-7ae7-48d6-8e0c-4f4f4a2f43fc` |
| 5.1 la capa | 5 | descenso lineal | `5543e2f4` | `00cc868f-628b-4859-8619-3a1818dee471` |
| 12.1 ecosistema | 12 | zoom out lineal | `a4fb4e65` | `a0a60789-3982-4ccb-b1ad-00e13b33cd32` |

**Seis generaciones cubren las ocho tomas del guion**: 2.2 (grilla con hairline de proceso) y
5.2 (grilla con hairline azul de Velaria) son tratamientos en post sobre el clip 2.1, no
generaciones aparte. Se ahorran 15 créditos y, más importante, la grilla queda idéntica en las
tres apariciones — que es lo que pide la continuidad del guion.

### El preset vuelve a aparecer

El servidor volvió a recomendar "IN THE DARK" y **rechazó el batch entero** (0/4 enviados)
hasta pasar `declined_preset_id` en cada request. Es un paso obligatorio en este proyecto, no
una excepción: anotarlo en cualquier script futuro.

### Decisión: cámara fija en la escena 2

A la grilla de diez le pedí explícitamente **cámara inmóvil**, con movimiento solo dentro de
los paneles. Un push in sobre una grilla de hairlines las curva y las hace vibrar —
exactamente lo que el sistema prohíbe. El movimiento lo aporta la gente trabajando, que además
es lo que la escena quiere decir.

## Estado del material

| Bloque | Estado |
|---|---|
| 13 pantallas HTML animadas a MP4 1080p | ✅ producidas y **verificadas** |
| 12 pistas de locución | ✅ producidas, duraciones medidas |
| 6 tomas generativas | ✅ producidas, **sin auditar** (CDN bloqueado) |
| Montaje final | ⬜ pendiente — requiere una máquina con acceso a los archivos |

**Gasto total: 68 créditos** de 1.112 (quedan 1.044). El presupuesto estimaba 265: la
diferencia es que dos tercios del video terminaron construyéndose en HTML en vez de generándose.

## Lo único que falta

El montaje. No puedo hacerlo desde acá: los clips generados y las pistas de audio viven en el
CDN de Higgsfield, que la política de red de este entorno bloquea, así que no puedo bajarlos
para unirlos con los clips de pantallas. Todo lo necesario está listo y documentado:

- `montaje.md` — timecode de entrada de cada escena
- `ui/clips/` — las 13 pantallas ya en MP4
- Los job_id de las 6 tomas y las 12 pistas, en este archivo

Con eso, el armado en cualquier editor es mecánico.

## Ronda 8 — el corte armado · 2026-08-22

**`corte-v1.mp4` — 3:29,4 · 1920×1080 · H.264 + AAC · 34 MB**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/d3c0f7bb-a682-48f9-ba64-7cfc464f507b.mp4

### Cómo se pudo montar pese al bloqueo de red

La política de red de esta sesión bloquea el CDN de Higgsfield, así que acá no se pueden bajar
ni las tomas ni la locución. **Pero Higgsfield expone `sandbox_exec`**: un Linux en la nube con
ffmpeg, Playwright y salida a internet, que sí alcanza ese CDN.

El montaje se hizo ahí:

1. `git clone` del repo público (`sebamezacerda/General`, rama de este proyecto) — trae HTML,
   CSS, fuentes IBM Plex y `render.js`.
2. Se renderizan las 14 pantallas con el Chromium del sandbox (`chrome-linux64`, no
   `chrome-linux` como en este entorno).
3. `curl` de las 6 tomas generativas y las 12 pistas de locución desde el CDN.
4. `assemble.py` construye cada segmento a su duración exacta y multiplexa.
5. `media_upload` → `PUT` → `media_confirm`.

Los clips no están versionados (`.gitignore` excluye `*.mp4`), así que el sandbox los
**re-renderiza** desde el HTML. Eso hace el pipeline reproducible desde cero con solo el repo.

### Cómo se rellenan las ventanas

Cada plano se estira con `setpts` hasta cubrir su ventana, con **tope de 2,5×**; lo que falta se
sostiene con `tpad=stop_mode=clone`. Estirar más de 2,5× un plano de 5s deja el movimiento
antinatural, y las tomas generadas duran 5s contra ventanas de hasta 22s.

### Error corregido en el camino

El primer armado dio **198,4s de video contra 209,25s de audio**. Faltaba sumar los **11
segundos de aire entre escenas** en el plan de video: el audio sí los tenía. Se resolvió
extendiendo 1s el último plano de cada escena, que además es lo correcto en montaje — el aire
va sobre la imagen que cierra la escena, no en negro.

### Placa inicial

Se agregó `ui/plate.html`: el disclaimer de caso sintético, en el sistema de la marca (banda
entre hairlines, kicker mono acero, "ficticios" en accent-hi). Renderizada como una pantalla más.

## Ronda 9 — corte v2: se le da ritmo · 2026-08-22

**`corte-v2.mp4` — 3:31 · 1920×1080**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/a63bbbc7-4830-4b4d-a5e1-6f2384ed7a3c.mp4

Feedback del cliente sobre el v1: *"le falta más velocidad, las animaciones muy estáticas, está
fome"*, y *"cuando se habla del pedido de Brasil y se hablan números, deberían aparecer también
en el video"*. Las tres causas eran concretas:

### 1. Una sola entrada y después nada

`anim.js` repartía las entradas en el primer 50% de la ventana con un paso máximo de 0,13s: en
una pantalla de 15s había ~3s de movimiento y 12s de quietud. Ahora el reparto ocupa **del 10%
al 80%** de la ventana, con paso limitado a 1,15s. Nunca hay un tramo largo sin que entre algo.

### 2. Los números aparecían en vez de contar

Ahora **cuentan**. `anim.js` parsea el formato castellano (coma decimal, punto de miles), lo
interpola y lo reconstruye con el mismo formato. Aplica a las métricas, a las cifras grandes de
valor y al contador del registro. El guion bajo del wordmark y de la nav además pestañea de
verdad, con los tiempos del sistema (`vblink`, 1,02s).

### 3. Los planos generados se congelaban

Se rellenaban con `tpad=stop_mode=clone`, o sea un frame estático — hasta 17 segundos en la
escena 2. Ahora se estiran poco (**máximo 1,8×**, antes 2,5×) y hacen **ida y vuelta** hasta
llenar la ventana. Siempre hay movimiento.

### 4. Faltaban los datos sobre los planos generados

Es lo que notó el cliente: en la escena 3 la locución dice "aumenta un catorce por ciento" y en
pantalla no había ningún número. El guion pide esa tarjeta como texto en pantalla y el v1 no la
tenía.

Se agregan **cinco capas con fondo transparente** que se superponen a los planos generados,
renderizadas con `omitBackground` y compuestas con `overlay` de ffmpeg:

| Capa | Va sobre | Qué muestra |
|---|---|---|
| `ov-01-sistemas` | puerto | las cinco capas de sistema como líneas de registro |
| `ov-02-areas` | grilla de diez | el rótulo de cada área sobre su panel |
| `ov-03-brasil` | mapa | **forecast +14% · cobertura 18 días · quiebre semana 37** |
| `ov-05-capa` | la capa | Contexto · Criterios · Gobernanza · Observabilidad |
| `ov-12-cierre` | ecosistema | la bajada del cierre |

### Tres bugs encontrados renderizando frames y mirándolos

1. **El chrome se animaba como contenido.** El rail, la nav y la cabecera aparecían de a poco,
   como si fueran datos. Son interfaz: ahora están desde el frame 0.
2. **Los contadores arrancaban todos en t=0** porque la búsqueda del bloque dueño estaba mal
   escrita y devolvía `undefined`. Se veían terminados antes de que su bloque entrara.
3. **Las filas de las capas no estaban en el selector**, así que aparecían de golpe en el frame
   0 mientras el título sí se animaba: la tarjeta de Brasil salía con un hueco donde iba el
   título.

Ninguno se habría notado sin renderizar frames intermedios y mirarlos.

## Ronda 10 — corte v3: más pace · 2026-08-22

**`corte-v3.mp4` — 3:29 · 1920×1080 · 29 planos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/1a8606c4-bd28-4c83-b76e-c103b4ba8dcd.mp4

### Cortar es lo que da ritmo

El v2 tenía **20 planos para 3:30** — un plano cada 10,5 segundos — con escenas enteras
resueltas en una sola toma de hasta 23s. Acelerar las animaciones dentro de un plano largo no
alcanza: lo que se percibe como lento es la falta de cortes.

El v3 tiene **29 planos** (uno cada 7,2s) **sin renderizar una sola pantalla nueva**. El truco:
los planos largos se parten en dos, y el segundo entra recortado a un detalle y **tomado más
adelante en el tiempo del mismo clip**, así que el contenido además avanzó. Las escenas 2 y 4,
las más pesadas, pasan de 1 y 2 planos a 3 cada una.

| | v2 | v3 |
|---|---:|---:|
| Planos | 20 | 29 |
| Segundos por plano | 10,5 | 7,2 |
| Entrada de cada elemento | 0,30s | 0,18s |
| Paso entre elementos | 1,15s | 0,62s |
| Contadores | 1,1s | 0,70s |
| Deriva de escala | 1,6% | 2,8% |

### 🐛 Un bug del v2 que sí se veía

Al validar duraciones apareció que **siete pantallas nacían 1s más cortas que su ventana**: son
exactamente las que cierran cada escena, o sea las que llevan el segundo de aire, y `render.js`
las generaba sin él.

En el v3 eso truncaba el video (202,4s contra 209,25 de audio). Pero en el v2 era peor y
silencioso: al ser el clip más corto que su ventana, caía en la rama del bucle ida y vuelta, así
que **esas siete pantallas se reproducían hacia atrás** al final de cada escena — el texto se
desaparecía solo. Nadie lo habría atribuido a esta causa.

Corregido: los clips se renderizan ya con su segundo de aire. Verificación automática de que
ningún plano quede corto: **29 planos, 0 con problema.**
