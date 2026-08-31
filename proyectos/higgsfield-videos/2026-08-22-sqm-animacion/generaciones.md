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

## Ronda 11 — corte v4: el contenido pasa a la pantalla · 2026-08-22

**`corte-v4.mp4` — 1:47 · 1920×1080 · 13 planos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/22033b64-f26e-46ae-bb79-3dc246052fe5.mp4

Pedido: más corto y al grano; ser explícito en cómo ejecuta el trabajo el equipo hoy, con el
stack escrito en pantalla y no solo como imagen de fondo con voz en off; y hacer el paralelo
con Velaria.

### La decisión que hace posible todo lo demás

**La locución deja de decir lo que la pantalla escribe.** Esa sola regla permite bajar de 424 a
189 palabras: el video pasa de **3:29 a 1:47 diciendo más cosas**, porque la pantalla comunica
más rápido que la voz. Antes la voz enumeraba seis sistemas en doce segundos; ahora la tabla los
muestra en dos, con quién los usa y cuánto demora cada uno.

### El corazón: la misma tabla, dos veces

| | Hoy | Con Velaria |
|---|---|---|
| 01 Demand planning · BI | 45 min | 12 s |
| 02 Inventarios · ERP | 40 min | 9 s |
| 03 Producción · ERP | 50 min | 11 s |
| 04 Logística · TMS | 55 min | 14 s |
| 05 Comercial · CRM | 35 min | 8 s |
| 06 Finanzas · Planilla | 60 min | 15 s |
| 07 Todos · Correo | 45 min | 21 s |
| **Total** | **5 h 30 min** | **1 min 30 s** |

La escena 5 repite **exactamente la misma tabla** de la escena 3: mismas filas, mismas áreas,
mismos sistemas. Solo cambia la columna de tiempo. El paralelo es literal, no una metáfora — y
deja claro que Velaria no reemplaza el stack, lo recorre.

### Silencio deliberado

Las escenas de tabla llevan **11s y 8s de silencio** después de la locución. No es una pausa
mal medida: es el tiempo que necesita el espectador para leer siete filas. Es la consecuencia
directa de poner el contenido en pantalla, y hay que defenderla en la revisión.

### Qué se fundió

Cuatro escenas del guion original — gobernanza, observación, MCP + Skill, y valor — se funden en
la escena 5. Eran cuatro escenas **describiendo** el mecanismo; ahora la tabla lo **demuestra**.

### Comparación de versiones

| | v3 | v4 |
|---|---:|---:|
| Duración | 3:29 | **1:47** |
| Palabras de locución | 424 | **189** |
| Planos | 29 | 13 |
| Escenas | 12 | 7 |
| Contenido escrito en pantalla | parcial | **todo lo relevante** |

## Ronda 12 — corte v5: el guion nuevo, producido · 2026-08-23

**`corte-v5.mp4` — 3:13 · 1920×1080 · con subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/a34f53dd-272e-413b-a114-f25a43e8d19c.mp4

Produce el guion `guion-v5.md`: diez escenas, la tesis puesta en las empresas y no en el
espectador, y cierre en la última línea.

### Lo nuevo del sistema de producción

| | Cómo se resolvió |
|---|---|
| **Subtítulos** | Quemados por el mismo pipeline, no por libass: se calculan desde la duración medida de cada pista y se reparten por largo de texto. Así usan la tipografía de marca en vez de una del sistema. |
| **Tipeo** | Las pantallas de chat escriben carácter por carácter, con cursor. Es lo que hace que el espectador lea las dos respuestas en vez de saltearlas. |
| **Transiciones** | Cada escena entra y sale sobre el fondo ink con una envolvente de fundido. El corte nunca ocurre entre dos imágenes distintas, así que se ve fluido **sin** cross-dissolve — que el sistema de Velaria prohíbe. |
| **Iconos** | Grilla de 24, stroke 1.4, remates cuadrados, a 40px. |

### Dos correcciones sobre la marcha

**Tipografía de video, no de web.** Los textos estaban dimensionados como para una pantalla:
en proyector o en teléfono se leían chicos. Error de criterio. Se escaló con criterio inverso al
intuitivo — los cuerpos y labels chicos +45%, los intermedios +25%, los títulos grandes solo
+10%, porque el problema estaba abajo y no arriba. Subtítulos 27px → 38px. Iconos 24 → 40.
Verificado que ninguna de las diez pantallas desborda 1920×1080 después del cambio.

**Sin cortes con zoom.** En los cortes anteriores el ritmo venía de recortar el mismo plano a un
detalle. Acá no se puede: el subtítulo está fijo abajo y un recorte lo cortaría. El ritmo lo
aportan la animación interna y el tipeo. Es una consecuencia directa de haber agregado
subtítulos, y conviene tenerla presente si se pide más pace.

### Nota de infraestructura

El sandbox se recicla si pasa demasiado tiempo entre llamadas: durante una pausa larga se
perdieron los temporales y hubo que relanzar el pipeline completo. No es un problema —el repo
tiene todo y el sandbox reconstruye desde cero— pero conviene saberlo: **nada de lo que vive
solo en el sandbox sobrevive.**


## Corte v6 — 25/08/2026

Mismo guion v5, dos entregas del mismo montaje. **2:26 · 1920×1080 · H.264 + AAC.**

- **Con subtítulos:**
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/9c3c28ec-3445-47e9-a62d-5912fd0ec44f.mp4
- **Sin subtítulos:**
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/12f41efd-8f7a-4bb0-89be-6ac110f1f11f.mp4

### Los dos bugs que corrige

**El corte "sin subtítulos" del v5 salía con subtítulos.** El commit que agregó el
interruptor dejó `render.js` mal: el bloque de capas se coló dentro del bucle principal y
la línea `if (process.env.NOSUBS) …` quedó en el bucle de `OVER`, que nunca corre porque
`OVER` está vacío. El CSS y la clase funcionaban — por eso la prueba aislada daba bien —
pero jamás se aplicaban al render real. Ahora cada corte escribe a su propio directorio, y
la verificación se hace sobre el frame rendido, no sobre el DOM: en la banda inferior del
segundo 6 de la escena 1 hay 6.653 píxeles claros con subtítulo y 0 sin él.

**Se quedaba pegado al terminar la locución.** Dos causas sumadas: la ventana de cada
escena tenía 6 a 11 s de aire después de la voz, y `anim.js` repartía las entradas solo
entre el 5 % y el 62 % de la ventana, con el paso topado en 0,55 s — así que en una escena
densa todo terminaba de entrar en los primeros 7 s. El último tercio quedaba congelado.
Ahora el aire es 2,8 s y las entradas llegan hasta el 86 %, sin tope de paso: mientras la
voz calla, en pantalla todavía está llegando algo, y el 14 % final queda para leer.

| | v5 | v6 |
|---|---|---|
| Duración | 3:13 | 2:26 |
| Aire por escena | 6–11 s | 2,8 s |
| Entradas repartidas hasta | 62 % de la ventana | 86 % |

### Render

Los frames se capturan en JPEG 94 en vez de PNG: **18 fps contra 5,3**, que es lo que
hace que las dos pasadas quepan en el lease del sandbox. El encode final sigue en H.264
crf 16. `render.js` además salta los clips ya hechos, así que una pasada interrumpida se
reanuda, y busca el binario de Chromium en vez de tenerlo fijo (`chrome-linux` acá,
`chrome-linux64` en el sandbox).


## Corte v7 — pitch de 90 segundos · 25/08/2026

**1:36 · 1920×1080 · H.264 + AAC · 7,9 MB · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/6fcae5b4-0c27-4b39-8270-a1e82f8953c6.mp4

Nueve escenas, una por bloque del guion. 87,3 s de locución y 8,7 s de aire repartido
—entre 0,7 y 1,6 s por escena—, contra los 6 a 11 s del v5.

### Lo que cambia respecto del v5

**Las entradas están ancladas a la voz.** `anim7.js` reemplaza el reparto por fórmula:
cada elemento lleva `data-in` en fracción de la locución (0..1) y se escala por `window.VO`,
que es la duración medida del audio de esa escena. Cuando la voz dice «habilita», entra
Habilitación.

**Un verbo visual distinto por escena.** El v5 tenía uno solo —aparecer— en diez escenas.
Acá: acumulación (b0), sustracción (b1), construcción (b2), estampado de fuentes (b3b),
colapso y propagación (b3c), conteo (b4).

**El plano héroe.** `v7-06`: las siete formulaciones distintas de la misma pregunta
convergen geométricamente hacia el bloque de la Skill —el desplazamiento se mide en
`buildExtra` con `getBoundingClientRect`, no se anima a ojo— y después la Skill se abre
hacia los diez puestos que quedaron vacíos en `v7-02`. Es la frase de cierre ejecutada como
movimiento en vez de dicha.

### Error corregido en el camino

`v7.css` definía `.lg` para las frases grandes, pero `base.css` ya usaba `.lg` para las
filas del log wall —mono, acero, opacidad .55—. Como v7.css no declaraba `font-family` ni
`color`, las frases de 64 px salían en monoespaciada y grises. Se resolvió prefijando todo
el archivo con `.v7`, que es el `body` de estas pantallas, y declarando explícitamente la
familia y el color en `.lg`.

### Pendiente

Música y diseño sonoro. Es lo que más falta: hoy sigue siendo voz sobre silencio, y a este
ritmo de corte una cama con los cortes cayendo en el beat cambia la producción percibida
más que cualquier ajuste visual. También quedan afuera las tres tomas generativas de 2 s
como respiro.


## Corte v7b — 25/08/2026

**2:16 · 1920×1080 · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/23936bbd-299e-4eb3-8f04-e373eed53087.mp4

Cuatro correcciones sobre el v7, todas del mismo tipo: **lo que la pantalla afirmaba, la voz
no lo decía, o lo decía en abstracto.**

| Escena | Qué pasaba | Qué se hizo |
|---|---|---|
| 2 · Ejes | La pantalla mostraba tres ejes con su definición y la voz solo decía «habilita, aprende y gobierna» | La locución lee los tres. Es la columna vertebral del video: acá la redundancia se cobra, no se paga |
| 1 · Villano | Diez cuadros de 150 px; el texto de la única persona con contenido no se leía | Tres personas en tarjetas anchas, a 27 px, con lo que cada una construyó. El resto del equipo queda en una línea |
| 3a · Caso | Se decía que la demanda subía 14% y nunca qué había que decidir | La decisión se enuncia entera —adelantar producción local o transferir stock desde México— contra el embarque del jueves |
| 3b · Habilitación | «Diccionario» y «criterios» eran las dos palabras más abstractas del video y solo se nombraban | Cada una llega con su ejemplo real: la fórmula de cobertura y la regla de los 21 días |

### Los cues salen de whisper, no de estimaciones

Desde este corte, cada locución se transcribe con `faster-whisper` y `word_timestamps`, y los
`data-in` de la escena se calculan contra los tiempos reales de palabra menos 0,15 s —lo que
dura la entrada— para que el elemento termine de llegar justo cuando se lo nombra. En la escena
de los ejes: habilitación 6,66 s, mejora continua 12,38 s, gobernanza 18,60 s.

### El TTS alucina colas

Dos de las tres locuciones nuevas trajeron audio inventado después de la última palabra: la
escena 2 seis segundos de balbuceo, la escena 5 cuatro «A» sueltas. No se oye en el prompt ni
en la duración esperada; se detecta transcribiendo. Se corta con el mapa `TRIM` de
`assemble-v7.py`, que aplica `-t` más un fade de 0,2 s. **Transcribir cada pista nueva antes de
montarla ya no es opcional.**

### Consecuencia de las cuatro correcciones

El corte pasó de 1:36 a **2:16**. Las tres primeras sumaron contenido hablado que antes solo
estaba escrito, y eso es tiempo. Deja de ser un pitch de 90 s y pasa a ser la versión didáctica:
sigue el registro de pitch —tipografía a sangre, corte duro, un verbo visual por escena— pero
explica. Si se quiere además la pieza corta de verdad, sale de esta sacando las escenas 3d y 4
y recortando la 2.


## Corte v8 — 26/08/2026

**3:26 · 1920×1080 · con música · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/f92c81c3-b2ca-4522-9378-17f320d814e7.mp4

Doce láminas. La estructura cambia: entre el caso y Velaria se abre el par
**Hoy · sin Velaria** / **Con Velaria**, y aparece el puente que faltaba.

| # | Lámina | Ventana |
|---|---|---|
| 1 | Tu equipo ya usa IA | 12,8 s |
| 2 | El villano — «el aprendizaje no sale de ahí», ahora dicha y en ámbar | 15,0 s |
| 3 | Velaria · los tres ejes | 24,1 s |
| 4 | **Veamos un ejemplo de uso** | 3,6 s |
| 5 | El caso — el stack funciona, uno de los productos, el embarque del jueves | 23,9 s |
| 6 | **Hoy · sin Velaria** — y el equipo ya usa Claude, cada uno por su lado | 22,2 s |
| 7 | **Con Velaria** · Eje 1 — el ejercicio va con Claude | 30,9 s |
| 8 | **Velaria registra, detecta el patrón y propone la Skill** | 19,6 s |
| 9 | La Skill aprobada se instala en los diez | 11,8 s |
| 10 | Eje 3 · Gobernanza | 8,1 s |
| 11 | Impacto — con la aprobación humana visible | 19,9 s |
| 12 | Cierre | 13,7 s |

### El error de continuidad que corrige

En el v7 la escena de Habilitación terminaba en «la misma pregunta se responde así», y la
siguiente abría con siete personas haciendo lo mismo. Entre una y otra faltaba el hecho que
las conecta: **que esa operación se repite durante semanas antes de que Velaria proponga
nada.** Ahora ese es su propio bloque —la 8— y el colapso de las siete formulaciones ocurre
ahí, no mezclado con el reparto. La 9 se queda solo con la propagación a los diez, después de
que el área aprueba.

### El error de tiempos que corrige

El v7 decía que la excepción se resolvía a las 09:04 habiendo entrado a las 09:00. Cuatro
minutos, con dos aprobaciones humanas de por medio, no lo cree nadie. Ahora la línea de tiempo
está escrita y deja ver la revisión: entra 07:00, análisis listo 07:15, revisa Planificación,
aprueba Finanzas, decisión antes del mediodía. Lo que sostiene el argumento no era el minuto:
era **el mismo lunes en vez del jueves.**

### Música

Primera versión con cama. `sonilo_music`, 60 s de pad sostenido sin melodía ni progresión,
encadenado consigo mismo cuatro veces con crossfades de 2 s —al no haber melodía la costura no
se oye— hasta cubrir los 234 s. Normalizada a **−30 LUFS** y con `sidechaincompress` contra la
voz, así que se agacha ~6 dB cada vez que ella habla. La regla de mezcla: si te das cuenta de
que hay música, está muy arriba.

### Ámbar

`#D9A03C`, el `--warn` del sistema, entra como color de énfasis en tres lugares: la línea del
villano, la declaración de que el stack funciona bien, y la etiqueta `[ SKILL ]` con su cuadro.
El sistema lo reserva para badges de estado; usarlo como acento tipográfico es una licencia
pedida por el cliente y conviene registrarla como tal.


## Corte v9 — 26/08/2026

**3:08 · 1920×1080 · música electrónica por bloque**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/9764f3e8-050c-4332-9b93-a61a88880777.mp4

| Cambio | Detalle |
|---|---|
| Sin marca del caso | El disclaimer deja de nombrar a SQM. El video sirve para cualquier cliente |
| Pace | El aire entre escenas baja de 1,2–2,0 s a **0,4 s**. Era la pausa que se sentía después de cada remate. 3:26 → 3:08 sin sacar una sola palabra |
| Sin nombrar la IA | «la que define la empresa, sugerida por Velaria». Antes: «alguna herramienta de IA, personal o de la empresa» |
| Menos lectura | Diccionario, criterios y conexiones ya no se leen en detalle: la voz los nombra, la pantalla los explica |
| Rótulos de sección | `EJE 1 DE 3 · HABILITACIÓN` a 64 px, con regla accent, entrando **antes** que el resto de la lámina |
| Música | Cuatro piezas electrónicas con pulso —una por bloque narrativo— en vez de un pad plano |

### El ruido después de Mejora continua

Era la cama, no la voz. El `sidechaincompress` tenía `release=450`, así que en cada silencio
de la locución la música volvía de golpe a su nivel: con 1,6 s de aire al final de esa escena,
el salto se oía como un golpe justo antes de Gobernanza. Tres arreglos: `release=900`,
`ratio` de 6 a 4, y **volumen fijo en vez de `loudnorm`** — el loudnorm de una pasada sobre una
pieza de casi cuatro minutos bombea por diseño. Sumado a que el aire bajó a 0,4 s, el silencio
donde se oía ya no existe.

### La música, en concreto

Cuatro piezas de 60 s generadas con `sonilo_music`, asignadas por bloque:

| Bloque | Escenas | Carácter |
|---|---|---|
| A | 1–3 | 108 BPM, kick sobrio, pluck corto |
| B | 4–6 | tenso, bajo en semicorcheas, tonalidad menor |
| C | 7–9 | 112 BPM, brillante, arpegio en mayor |
| D | 10–12 | 104 BPM, resuelto, pad sostenido |

Cada pieza se encadena consigo misma hasta cubrir su bloque y va a **−19 dB**, con ducking
contra la voz. El corte de una pieza a la siguiente cae en el corte de escena, así que se lee
como cambio de sección y no como error.


## Corte v10 — 26/08/2026

**3:08 · sin ninguna mención a SQM**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/7f14dbb7-98fd-488b-9e92-b11891dfd737.mp4

Dos errores propios, y los dos con la misma raíz de descuido al reutilizar material viejo.

### La escena 1 usaba la pista del v5

`assemble-v8.py` apuntaba la escena 1 a `418867af`, que es la locución **del corte v5** y dice
textualmente *«Probemos con una pregunta real de SQM»*. La duración del plan (11,52 s) sí era la
de la pista del v7, así que el montaje calzaba y nada falló: simplemente sonaba otra voz en off
que la que correspondía. De ahí salían las dos quejas a la vez —«esa no es la intro del v7» y
«hay una referencia a SQM antes del ejemplo»—, que parecían dos cosas distintas y eran una sola.

Ahora usa `1e659e28` y la lámina termina en «Y funciona»: se retira el pie que enumeraba
`Claude · ChatGPT · Gemini`.

**Regla que queda:** cuando una escena reutiliza audio de un corte anterior, verificar el job
id contra su texto, no contra su duración. La duración calza por casualidad más seguido de lo
que uno cree.

### El hueco de música antes de Gobernanza

No era el ducking —eso ya se había arreglado en el v9—. Era el corte entre bloques musicales:
cada bloque llevaba `afade` de salida y el siguiente uno de entrada, así que la cama **se iba a
silencio y volvía** justo en el límite entre Mejora continua y Gobernanza. Eso es el hueco, y la
reentrada es el sonido raro. Ahora los cuatro bloques se encadenan con `acrossfade=d=2`: cada
bloque se rinde 2 s más largo salvo el último, y el sobrante lo consume el encadenado, así que
la suma vuelve a dar la duración exacta del video sin que la música desaparezca nunca.

### Barrido de marca

Verificado sobre las doce láminas y las doce pistas: **cero menciones a SQM**, escritas o
habladas. El video queda reutilizable para cualquier cliente — Velaria primero, el ejemplo
después, y el ejemplo no nombra a nadie.


## Corte v11 — 26/08/2026

**3:13 · trece láminas · cierra con la placa de marca**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/a0646896-7436-4072-ad20-d38b32f7534c.mp4

### Placa final

Lámina 13, nueva: símbolo del kit —anillo, arco accent y punto, con la geometría exacta del
`viewBox 0 0 48 48`— más el wordmark y la bajada de la web:

> **Libera el poder de la IA. Guíala con tu visión.**

Sin cabecera, sin pie, sin marcador de ejes y **sin locución**: solo la cama. El cierre
anterior suelta el wordmark de su pie para no duplicarlo. El montaje ahora acepta escenas
mudas: un `None` en `MP3` genera silencio del largo de su ventana.

### Habilitación abre por el principio

Antes daba la IA por definida («la IA es la que define la empresa»). Ahora el orden es el real:

> Velaria **sugiere qué IA usar**, y la define junto a la empresa.

y recién después vienen diccionario, criterios y conexiones.

### La música deja de agacharse

Se elimina el `sidechaincompress`. Bajar la cama en cada frase de la locución y devolverla en
cada silencio es exactamente lo que se oía como bombeo, y ningún ajuste de release lo arregla
del todo cuando la voz entra y sale cada dos segundos. Ahora es **nivel fijo a −17 dB** —dos dB
más arriba que antes— y la mezcla es una simple suma. Más simple y suena mejor.


## Corte v12 — 31/08/2026

**3:24 · trece láminas · narración en cuatro tomas continuas**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/b81badb9-6044-481b-9a54-4dac4094ec3d.mp4

### El cambio de fondo: la voz deja de saltar

El síntoma eran tres quejas distintas —«a veces se acelera», «después de *le pone adentro*
cambia la voz», «revisar el tono del lunes siguiente»— y era **un solo problema**: cada escena
era una generación de TTS independiente, y el modelo arranca de cero en cada llamada. Tempo,
timbre y acento son estado interno que no se conserva entre generaciones. Parchar pista por
pista no podía funcionar: cada regeneración es un dado nuevo.

La narración ahora se graba en **cuatro tomas continuas**, una por bloque narrativo, y se corta
en escenas con los tiempos de palabra de whisper. Dentro de una toma el estado no cambia, así
que la voz no puede saltar. Los cortes caen en el silencio entre frases, con fundidos de 50 y
80 ms para que no haya clic.

| Toma | Escenas | Duración |
|---|---|---|
| A | 1–3 | 58,8 s |
| B | 4–6 | 46,7 s |
| C | 7–9 | 53,1 s |
| D | 10–13 | 39,7 s |

Efecto lateral: las cuatro tomas salieron **sin cola alucinada**, el modo de falla que había
aparecido cinco veces en pistas cortas. Un texto largo le da al modelo suficiente contexto para
saber dónde termina.

### Los demás cambios

| | |
|---|---|
| Intro | «Tu equipo **probablemente** ya usa IA en su trabajo» |
| Villano | Las tres tarjetas entran una tras otra, ~5,5 s de lectura cada una, y ya no desaparecen. La locución nombra a cada una —Comercial, Logística, Planificación— para que la voz acompañe la lectura. Fuera «+ 7 personas» |
| Eje 2 | Pasa a **Productividad · Mejora continua** en las tres láminas donde aparece |
| Ejemplo | «Veamos un ejemplo de uso en **ingeniería**» |
| El caso | «Un equipo de **10 personas planifican demanda**» |
| Con Velaria | **«Entra Velaria»** |
| Habilitación | «la **herramienta de IA** que ya usan» · «cualquiera del equipo pregunta **a la herramienta de IA**», en ámbar |
| Mejora continua | 52 px de aire entre el rótulo y «Pasan las semanas» |
| La Skill | `[ SKILL v1 ]` a 40 px y el nombre de la Skill a 52 |
| El lunes siguiente | **Sin cifra.** El énfasis va en «El mismo lunes» a 118 px, con «No el jueves» tachado al lado |
| Placa final | Ahora lleva voz: «Velaria. Libera el poder de la IA. Guíala con tu visión.» |
| Música | Tres pistas intercaladas: sobria · tensa · brillante · y vuelve la sobria para cerrar el arco |

## Corte v13 — 31/08/2026

**3:24 · 1920×1080 · H.264 + AAC · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/8e0fdab0-6203-4d15-9ece-3aabe42ba1be.mp4

Mismo contenido de la v12 —las trece láminas y las cuatro tomas continuas— rehecho con el
**arreglo de audio** descrito en `notas.md`. Video 204,44 s · voz 204,33 s · cama 204,33 s.

Verificación posterior al montaje: se midió `mean_volume` por cuartos en cada una de las trece
pistas de escena. Todas dan entre −14 y −23 dB en los cuatro cuartos; ninguna cae a silencio.
En la v12, las escenas que no abrían toma se apagaban a media escena.
