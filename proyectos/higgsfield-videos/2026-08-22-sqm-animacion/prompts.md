# Prompts — Caso sintético SQM × Velaria

> **Arte en marca.** Todo lo de acá sigue el sistema de diseño de Velaria
> (`proyectos/velaria/spec.md`). Ese documento manda: si un prompt contradice al sistema,
> gana el sistema.

## Cómo se produce

Para cada escena se genera primero un **frame clave** (imagen 16:9) para validar arte; recién
aprobado se anima. Los textos en pantalla (cifras, tarjetas, dashboards) se **agregan en post**
en IBM Plex Sans / IBM Plex Mono, no se le piden al modelo: los generadores escriben mal el
texto y acá las cifras tienen que ser exactas y la tipografía es parte de la marca. En los
prompts se pide el *espacio* para ese texto (planos vacíos, superficies limpias).

## Consecuencia dura del sistema

El sistema de Velaria prohíbe explícitamente **degradados, glassmorphism, orbes/blobs, glow,
esquinas redondas, sombras blandas y toda la iconografía de cerebros / chips / circuitos /
redes neuronales**. Eso descarta el 90% del lenguaje visual por defecto de los generadores de
video corporativo. Hay que pelearlo en cada prompt, y el negative prompt no es opcional.

Dos reescrituras de fondo respecto del guion original:

- **No hay redes de nodos.** Las escenas 2 y 4 pedían constelaciones y grafos: eso cae en
  "redes neuronales" y en "orbes". Se reemplazan por estructuras de registro — grillas,
  columnas, tablas, líneas de log. Es más fiel al principio "todo es registro" y además se lee
  mejor en video.
- **Velaria no brilla.** La escena 5 pedía una capa luminosa descendiendo. Sin glow, la capa se
  expresa como un **plano** ink2 con hairline y un canto accent: jerarquía por plano y
  densidad, no por luz. "Nada flota."

## Recursos de marca reales

El kit oficial está en `referencias/velaria-kit/` (SVGs de símbolo y wordmark, tokens CSS,
piezas aplicadas). La paleta del kit coincide exactamente con la que ya usábamos — no hay que
corregir nada de color.

### Geometría exacta del símbolo (ojo del velarium)

Sobre `viewBox 0 0 48 48`:

| Elemento | Spec | Significado |
|---|---|---|
| Anillo | `circle cx24 cy24 r19`, stroke `#F5F7FA`, width 2.5 | la lona tendida sobre la arena |
| Arco | mismo círculo, stroke `#2456D6`, dasharray `30 90`, dashoffset `52`, `rotate(-90 24 24)` | **el tramo que Velaria cubre** |
| Punto | `circle cx24 cy24 r5`, fill `#F5F7FA` | **la operación, intacta** |

**Esto es el video entero en un símbolo.** El punto central es SQM operando, que no se toca; el
arco azul es la porción que Velaria cubre. Es exactamente la tesis del guion — "SQM ya funciona
bien", "el stack queda intacto", "Velaria es una capa encima". Vale la pena que el cierre lo
haga explícito (ver toma 12.3).

### Wordmark

IBM Plex Mono 500, minúsculas, letter-spacing ≈0.1em (en el SVG de 520×120: `font-size 40`,
`letter-spacing 4`), fill `#F5F7FA`, con el `_` final en `#7DA0F2`. Área de respeto: la altura
del símbolo a cada lado. Tamaño mínimo del lockup: 24px de alto.

### El recurso recurrente: la banda con hairlines

Tanto el `og-image` como los banners del kit componen igual: **dos hairlines horizontales
encerrando una banda de contenido**, con el lockup a la izquierda y labels mono caps steel a la
derecha. Y la firma de correo usa `border-left: 3px solid #2456D6` como marca de bloque.

Conviene adoptar la banda como **marco persistente del video**: los rótulos de escena viven
siempre entre esas dos hairlines, en la misma posición, las 12 escenas. Da continuidad sin
agregar nada decorativo, y sale de las piezas reales de la marca en vez de inventarse.

### ⚠ Conflicto de tipografía a resolver

El `README.md` del kit dice **Avenir Next** para títulos/cuerpo y *mono del sistema* (SF Mono /
Menlo) para labels. El `sistema visual.md`, que es posterior (2026-07-30), dice **IBM Plex Sans**
e **IBM Plex Mono**, y degrada Avenir Next a "decks legacy".

Voy con **IBM Plex Sans + IBM Plex Mono**: es la fuente más nueva, es coherente con el wordmark
(que sí es Plex Mono en ambos documentos) y no depende de una tipografía de pago. Si el fundador
dice lo contrario, se cambia solo el estilo de texto en post — no afecta ningún prompt.

## Style token

Pegar al final de cada prompt de imagen:

```
STYLE: precise corporate 3D still, flat and technical, matte non-reflective materials,
hard even neutral light, orthographic or near-orthographic camera.
STRICT PALETTE: background #0B0F17, panel planes #151C2B, a single action blue #2456D6,
pale blue #7DA0F2 for accented marks, steel grey #8A94A6 for technical labels,
off-white #F5F7FA. Nothing outside this palette.
Hierarchy comes from 1px hairline rules in low-opacity off-white, from flat ink planes and
from density — never from depth, blur or light. Perfectly square corners, square stroke
caps, 1.5px strokes on a 24px grid. Rigid alignment to a grid, generous empty space
reserved for overlay typography. 16:9. No logos, no readable text, no brand marks.
```

## Negative prompt

Va en **todas** las tomas, sin excepción:

```
glow, bloom, lens flare, light rays, volumetric light, god rays, gradient, gradients,
glassmorphism, frosted glass, orbs, spheres, blobs, particles, sparkles, rounded corners,
soft shadows, drop shadow, neon, cyan, teal, purple, magenta, brain, neural network,
circuit board, microchip, robot, hologram, holographic, sci-fi HUD, bokeh, depth of field,
motion blur, emoji, glossy plastic, chrome, reflections
```

## Regla del acento único

El sistema permite **un solo azul de acción (#2456D6) por vista**. En video eso es una
herramienta de dirección: en cada toma, ese azul marca el único elemento que la locución está
nombrando en ese momento. Todo lo demás vive en steel, ink2 y off-white. Cada escena indica
abajo cuál es su acento.

## Reglas fijas

- Sin logos ni marcas de terceros. Los sistemas corporativos (BI, CRM, ERP, WMS) se nombran por
  categoría, en mono caps, nunca con su logo real.
- Personas: profesionales latinoamericanos, ropa corporativa o industrial según área, mostrados
  trabajando y decidiendo — nunca desplazados por la máquina.
- Continuidad: misma paleta, misma luz plana y mismo lenguaje de UI en las 12 escenas.
- Cada escena ≈ 13–15 s → 2–3 tomas de ~5 s, o 1 toma con movimiento de cámara lento.
- Movimientos de cámara: lineales y lentos. Sin cámara en mano, sin whip pans, sin easing
  exagerado. El sistema es sobrio; la cámara también.

---

## Escena 1 — SQM hoy

**Acento único:** ninguno todavía. Esta escena es SQM sola; el azul de acción entra recién en
la escena 5, cuando entra Velaria. Acá manda el steel.

**Toma 1.1 — aérea de faena**
```
Stylized aerial view of a vast lithium operation in a desert salt flat: rectangular
evaporation ponds in a strict orthogonal grid, processing plants, haul trucks on straight
service roads. Shot from directly above, flat top-down composition, hard midday light, no
long dramatic shadows. Desaturated cool grade, near-monochrome, deep shadows reading almost
black. The pond grid itself provides the geometry. Empty flat terrain in the upper third
reserved for overlay graphics.
```
Movimiento: descenso vertical lento y constante, sin rotación. Modelo: —. Resultado: —

**Toma 1.2 — puerto**
```
Stylized aerial view of a bulk export terminal, shot top-down: loading pier, rectangular
stacks of cargo, one docked vessel, calm dark water. Strict geometric composition aligned to
frame edges. Desaturated cool grade, matte surfaces, no water sparkle, no sun glare. Large
area of flat dark water at frame left reserved for overlay graphics.
```
Post: capas de sistema entrando como **líneas de registro** en mono caps sobre el agua —
`// BI` `// CRM` `// ERP` `// LOGÍSTICA` `// PRODUCCIÓN`, cada una con timestamp, en steel.
Nada de tiles flotantes ni iconos de marca. Texto final: `SQM YA FUNCIONA BIEN.`
Movimiento: travelling lateral lineal. Modelo: —. Resultado: —

---

## Escena 2 — El desafío

**Acento único:** ninguno. Los diez están parejos; ninguno es todavía "la decisión".

**Toma 2.1 — la grilla de los diez**
```
A strict 5x2 grid of ten rectangular panels filling the frame, each panel a separate
photographic vignette of one professional at work: an office desk, a control room, a plant
floor with hi-vis vest and helmet, a port yard, a finance workstation. Panels separated by
1px hairline rules, no gaps, no rounded corners, no shadows, nothing floating. Each vignette
individually lit by its own screen, desaturated cool grade. A narrow empty band at the bottom
of each panel reserved for a label.
```
Post: label por área en mono caps + letter-spacing (COMERCIAL, DEMAND PLANNING, PRODUCCIÓN,
INVENTARIOS, LOGÍSTICA, PUERTO, SHIPPING, FINANZAS, BI). Timestamp mono en cada panel.
Movimiento: los paneles se encienden en secuencia; cámara fija. Modelo: —. Resultado: —

**Toma 2.2 — el proceso compartido**
```
The same 5x2 grid seen straight on, now with a single horizontal hairline running across all
ten panels at the same height, connecting them edge to edge. Flat, schematic, no glow on the
line. Everything else unchanged.
```

---

## Escena 3 — Una excepción

**Acento único:** el marcador de Brasil. Es la única cosa `#2456D6` de la toma.

**Toma 3.1 — mapa**
```
Flat schematic world map rendered as a fine dot matrix on a very dark background, seen
straight on, no perspective, no globe curvature. Continents defined only by the density of
the dots, in steel grey. One single region in South America marked by a solid square dot in
strong blue, with a thin square-capped rule extending horizontally from it toward empty space
at frame right. No glow around the marker. Entire right half of the frame left empty for an
overlay card.
```
Post: tarjeta `BRASIL · PRODUCTO X / Forecast: +14% / Cobertura proyectada: 18 días`, plano
ink2 con hairline, esquinas rectas, borde izquierdo accent. Estado entre corchetes, no píldora.
Movimiento: el marcador aparece, la línea se traza hacia la derecha. Modelo: —. Resultado: —

---

## Escena 4 — Cómo se resuelve hoy

**Acento único:** la fila de la excepción arriba; las seis consultas quedan en steel.

**Toma 4.1 — el registro de dependencias**
```
Dark technical console layout seen straight on: one wide highlighted row at the top in blue,
and beneath it six stacked empty rows separated by 1px hairlines, each row with a small
square-stroke icon plate at the left (factory, pallet, truck, handshake, coin, cargo ship)
drawn at 1.5px stroke weight with square caps. Flat planes, zero shadows, square corners,
strict left alignment, wide empty column at the right of every row reserved for values.
Monospaced-feeling rhythm, dense but orderly.
```
Post: rótulos Producción, Inventarios, Logística, Clientes, Costos, Próximos embarques, con
timestamps. Cada fila se resuelve con `[ OK ]` en verde badge.
Movimiento: las filas aparecen de a una, de arriba abajo. Cámara fija. Modelo: —. Resultado: —

**Toma 4.2 — la pregunta**
```
Almost entirely empty dark frame, a single thin horizontal hairline at lower third, vast
negative space above it. Flat, austere, nothing else in frame.
```
Post: `¿Cómo hacemos que la IA trabaje de acuerdo con la forma en que SQM realmente opera?`

---

## Escena 5 — Entra Velaria

**Acento único:** el canto de la capa Velaria.

**Toma 5.1 — la capa**
```
Exploded horizontal-layer diagram, near-orthographic, floating in flat dark space: three
lower slabs representing an existing technology stack, rendered as matte dark grey planes
with faint hairline texture, solid and intact, perfectly square edges. A fourth slab descends
and settles above them — same matte material, slightly lighter plane, distinguished only by a
crisp blue edge along its front face. It does not glow and it casts no light on the layers
below; it simply sits above them. Rigid alignment, architectural, symmetric, wide empty
margins left and right.
```
Post: `VELARIA` + `Contexto · Criterios · Gobernanza · Observabilidad` en mono caps.
Movimiento: la capa baja en línea recta y se detiene. Sin rebote. Modelo: —. Resultado: —

**Toma 5.2 — los diez habilitados**
```
Return to the 5x2 grid of ten professional panels from scene 2, now with a single continuous
blue hairline running along the top edge of the entire grid, spanning all ten panels. Nothing
else changed. Flat, no glow, no highlight on the people.
```

---

## Escena 6 — Criterios y gobernanza

**Acento único:** la barra superior de las tarjetas de política.

**Toma 6.1 — políticas**
```
Four blank rectangular policy cards arranged in a strict 2x2 grid on a flat dark background.
Each card is a matte panel with perfectly square corners, a 1px hairline border, a 3px solid
blue bar across its top edge, and a small square-stroke icon plate at top-left. Card bodies
completely empty. No shadows, no elevation, no rounded corners, nothing floating. Even
spacing, rigid grid alignment.
```
Post: las 4 políticas del guion, en IBM Plex Sans; kicker mono acero arriba de cada una.
Movimiento: las tarjetas aparecen en secuencia, sin escalado ni fade suave. Modelo: —. Resultado: —

**Toma 6.2 — permisos**
```
Dark permission matrix seen straight on: three labelled columns and several rows, cells
separated by 1px hairlines, each cell containing either a small solid square mark or nothing.
Completely flat, table-like, technical, no styling beyond the rules. Left column and header
row left empty for labels.
```
Post: columnas Comercial / Logística / Finanzas; estados entre corchetes `[ PERMITIDO ]`,
`[ REQUIERE APROBACIÓN ]`. Nunca píldoras.

---

## Escena 7 — Velaria observa

**Acento único:** la línea única del final de la toma 7.2.

**Toma 7.1 — semanas de uso**
```
Dark console screen filled top to bottom with dense rows of blank log lines, each row a short
horizontal steel-grey rule of varying length preceded by a fixed-width timestamp block. New
rows accumulate from the bottom upward. Strictly monospaced rhythm, flat, no glow, no
scrolling blur. Left margin column reserved for timestamps.
```
Post: fragmentos de consulta reales (forecast, stock, logística, margen) con `//` y timestamps.
Movimiento: acumulación acelerada de líneas, como un log corriendo. Modelo: —. Resultado: —

**Toma 7.2 — el patrón**
```
The same dense field of log rows, but now eight of the rows shift horizontally until they
align into perfect vertical registration with one another, forming one clean column while the
remaining rows stay ragged and dim. The eight aligned rows are drawn in blue, everything else
in steel grey. Flat, precise, no glow, no motion blur.
```
Movimiento: las ocho filas se desplazan y calzan. Modelo: —. Resultado: —

---

## Escena 8 — Insight

**Acento único:** el borde izquierdo del panel de oportunidad.

**Toma 8.1 — dashboard**
```
Clean dark-mode console dashboard seen perfectly straight on, filling the frame: a narrow
left navigation rail with blank label slots, one large empty hero panel at the top of the
main area with a 3px blue bar along its left edge, and a row of four blank metric cells below
it separated by 1px hairlines. Every surface empty, no readable text anywhere. Perfectly
square corners, matte planes, zero shadows, zero glow, nothing floating. Dense but orderly
enterprise console.
```
Post: `OPORTUNIDAD DETECTADA` como kicker mono acero; `Weekly S&OP Exception Review` en Plex
Sans; y las cuatro métricas — 8 usuarios / 67 ejecuciones similares / 5 fuentes involucradas /
112 horas de trabajo asociadas. Timestamp de detección arriba a la derecha.
Movimiento: las celdas se completan en secuencia; cámara fija. Modelo: —. Resultado: —

> ⚠ Esta toma, la 10 y la 12 deberían replicar componentes reales del `Velaria UI Manual`
> (fuente de verdad de UI). Ese archivo vive en el repo del fundador y no es accesible desde
> acá — validar antes de dar el arte por cerrado.

---

## Escena 9 — MCP + Skill

**Acento único:** el gate en 9.1; el último paso del pipeline en 9.2.

**Toma 9.1 — conector gobernado**
```
Flat schematic diagram, straight on: a square plate at frame left connected to a stack of
three matte grey system plates at frame right by a single straight horizontal rule with
square caps. At the midpoint of the rule sits a narrow vertical gate plate in blue, splitting
the line in two. No glow, no particles, no flow animation lines. Austere technical drawing
rendered in three dimensions with matte materials. Empty label band beneath the gate.
```
Post: etiqueta `MCP` en mono caps bajo el gate; `[ GOBERNADO ]` a la derecha.

**Toma 9.2 — la Skill**
```
Horizontal pipeline of six square plates in a straight row, evenly spaced, connected by short
straight square-capped rules. All plates matte dark grey except the last one, which is blue.
Each plate has an empty label band directly beneath it. Perfectly flat, orthographic, square
corners, no shadows, no glow, rigid spacing. Wide empty space above the row.
```
Post: Demanda → Inventario → Producción → Logística → Criterios → **Impacto económico**, y el
nombre `Weekly S&OP Exception Review` arriba, con `❯` de prefijo.
Movimiento: los seis plates aparecen de izquierda a derecha. Modelo: —. Resultado: —

---

## Escena 10 — La semana siguiente

**Acento único:** en 10.1 el contador de excepciones; en 10.2 la fila "no intervenir" — pero
esa va en warn/err de badge, así que el azul queda en el encabezado del caso.

**Toma 10.1 — bandeja de excepciones**
```
Minimal dark console screen seen perfectly straight on: three large empty figure slots across
the top separated by vertical hairlines, and beneath them a short list of blank rows, each row
preceded by a small solid square status mark and a fixed-width timestamp block. Enormous
amount of empty space, extreme restraint, 1px hairlines only. Square corners, matte, flat,
no shadows.
```
Post: `27 excepciones detectadas / 5 requieren decisión / US$1,34M de impacto económico
potencial`. Estados entre corchetes.

**Toma 10.2 — el caso Brasil**
```
Detail view of a single console record, straight on: a wide header plate at top with a 3px
blue left edge, and three stacked option rows below it separated by 1px hairlines, each row
an empty plate with a small square status mark at the left. The third row carries a solid
amber left border instead of blue. Flat, square, dense, no shadows, no rounded corners.
Right side of each row left empty for a figure.
```
Post: Alternativa A — US$17k · Alternativa B — US$41k · No intervenir: margen en riesgo —
US$310k (esta última con borde izquierdo `#D95C4A`, como línea de log de estado, no popup).
Movimiento: el registro se abre desde el encabezado hacia abajo. Modelo: —. Resultado: —

---

## Escena 11 — De productividad a valor

**Acento único:** la cifra dominante de valor económico.

**Toma 11.1 — el KPI cambia**
```
Flat dark composition, straight on: one large empty rectangular figure plate centered in
frame with a 3px blue bar along its top edge, and a much smaller empty plate beside it,
clearly subordinate in scale, in steel grey. Beneath them a row of four small empty metric
cells separated by vertical hairlines. Rigid grid, square corners, matte surfaces, no
shadows, no glow, no depth. Extensive empty space.
```
Post: `VALOR ECONÓMICO` como kicker mono acero. Identificado US$1,34M (la cifra dominante) /
Implementado US$590k / Validado por Finanzas US$447k / Capital de trabajo liberado US$620k /
Capacidad recuperada 1.120 h (esta última en la placa chica, en steel).
Movimiento: la placa de horas se reduce, la de dólares crece. Escalado lineal, sin easing
elástico. Modelo: —. Resultado: —

---

## Escena 12 — Cierre

**Acento único:** la capa Velaria arriba del stack; en la placa final, el `_` del wordmark.

**Toma 12.1 — el ecosistema**
```
Wide near-orthographic zoom-out revealing the whole system as one stacked structure: at the
base the 5x2 grid of ten professional panels, above it the three matte grey slabs of the
existing stack, and crowning it the fourth slab with its blue front edge. All layers
perfectly aligned on a shared vertical axis, connected by straight hairlines. Flat lighting,
matte materials, square edges, no glow, no shadows. Large empty area above the structure
reserved for a title.
```
Movimiento: zoom out lineal y continuo. Modelo: —. Resultado: —

**Toma 12.2 — nav de la plataforma**
```
Narrow dark navigation rail seen straight on, filling frame left, with seven evenly spaced
empty label slots separated by 1px hairlines, one slot marked by a solid blue square at its
left edge. Rest of frame flat empty dark space. Completely austere.
```
Post: Instalaciones · Criterios · Insights · Skills · Marketplace · Registro · Valor, en mono
caps. El item activo lleva `_` pestañeando (keyframes `vblink`).

**Toma 12.3 — placa final**

**No se genera con IA.** Se compone en post con los assets reales del kit, replicando la
maqueta de `referencias/velaria-kit/og/og-image.png`, que es la marca aplicada por sus propios
autores:

- Fondo `#0B0F17` plano — sin viñeta, sin degradado, sin textura.
- Dos hairlines horizontales `rgba(245,247,250,.10)` encerrando la banda de contenido.
- Kicker arriba, mono CAPS steel `#8A94A6`, letter-spacing ~3px.
- Lockup símbolo + `velaria_` alineado a la izquierda, con el `_` en `#7DA0F2`.
- Bajada en dos líneas: la primera en `#F5F7FA`, la segunda en `#7DA0F2` — así separa el OG el
  tagline ("Libera el poder de la IA." / "Guíala con tu visión.").
- Pie en mono steel con metadato: `velaria.ai · 2026`.

Texto: `De uso individual de IA` / `a capacidad organizacional medible.` (segunda línea en
accent-hi), y cierre con el tagline oficial.

**Animación del símbolo — el cierre del video.** Construir el ojo en el orden en que significa:

1. Aparece el **punto central** solo, quieto. *(la operación de SQM, que ya funciona)*
2. Se traza el **anillo** blanco alrededor, en sentido horario. *(el stack existente, intacto)*
3. Se dibuja el **arco azul** sobre el anillo — solo su tramo, `dasharray 30 90`. *(Velaria: no
   reemplaza el anillo, cubre un tramo de él)*
4. Entra el wordmark a la derecha; el `_` arranca a pestañear (`vblink`, 1.02s).

Sin glow en ninguno de los cuatro pasos, sin escalado elástico, sin fade suave. Trazado limpio,
tiempos parejos.

---

## Locución

- Voz: español neutro, tono ejecutivo y calmado, ritmo pausado. Sin música épica debajo.
- Generar por escena (12 pistas) para ajustar timing sin re-renderizar.
- El texto exacto está en `guion.md`.

## Post / motion

- Tipografía: **IBM Plex Sans** para títulos y cuerpo; **IBM Plex Mono CAPS** con
  letter-spacing 1.5–3px para labels, kickers, timestamps y navegación.
- Marco persistente: la banda entre dos hairlines, en la misma posición las 12 escenas.
- Timestamps visibles y consistentes a lo largo del video (`14:32:08Z`): son parte del sistema,
  no decoración.
- Estados **siempre entre corchetes** — `[ ACTIVO ]`, `[ OK ]`, `[ REQUIERE APROBACIÓN ]`.
  Nunca píldoras redondeadas.
- Transiciones: cortes secos o desplazamientos lineales. Sin cross-dissolves blandos, sin
  desenfoques de transición.
- Radios: 0–2px en todo. Si algo tiene esquina redondeada, está mal.

## Pendiente antes de generar

- [x] ~~Conseguir los SVG del ojo del velarium y del wordmark~~ → `referencias/velaria-kit/`
- [ ] Conseguir `Velaria UI Manual.dc.html` para validar las escenas 8, 10 y 12 contra
      componentes reales. **Es el único bloqueante de arte que queda.**
- [ ] Confirmar tipografía con el fundador: IBM Plex Sans (sistema visual) vs Avenir Next
      (README del kit). Ver "Conflicto de tipografía" arriba.
- [ ] Elegir modelo de imagen y de video, y confirmar presupuesto de créditos (~18 tomas).
- [ ] Validar frames clave de escenas 5, 8 y 12 — definen el arte del resto.
- [ ] Elegir voz de locución.
