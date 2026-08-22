# Prompts — Caso sintético SQM × Velaria

**Método:** para cada escena se genera primero un **frame clave** (imagen 16:9) para validar
arte; recién aprobado se anima. Los textos en pantalla (cifras, tarjetas, dashboards) se
**agregan en post**, no se piden al modelo: los generadores de imagen escriben mal el texto y
acá las cifras tienen que ser exactas. En los prompts se pide el *espacio* para ese texto
(paneles vacíos, superficies limpias, negative space).

**Style token** — pegar al final de cada prompt de imagen:

```
STYLE: corporate 3D animation still, clean and technological, photoreal materials with
stylized simplification, cool corporate palette (deep navy #0B1F33, slate grey, white),
data accents in cyan and mint green, soft volumetric light, shallow depth of field,
minimal flat UI overlays with generous negative space, sans-serif typography, no logos,
no brand marks, no readable text, 16:9, cinematic, high detail.
```

**Reglas fijas**
- Sin logos ni marcas de terceros. Sin texto legible generado por el modelo.
- Personas: profesionales latinoamericanos, ropa de trabajo corporativa o industrial según área,
  mostrados trabajando y decidiendo (nunca desplazados por la máquina).
- Continuidad: misma paleta, misma calidad de luz y mismo lenguaje de UI en las 12 escenas.
- Cada escena ≈ 13–15 s → 2–3 tomas de ~5 s, o 1 toma + movimiento de cámara lento sobre el frame.

---

## Escena 1 — SQM hoy

**Toma 1.1 — aérea de faena**
```
Stylized aerial view of a vast lithium and chemical industrial operation in a desert salt
flat: evaporation ponds in gradient blues and turquoise, processing plants, haul trucks on
straight service roads, long shadows of late afternoon. Camera high and slowly descending.
Empty sky area in the upper third for overlay graphics.
```
Movimiento: descenso aéreo lento, muy estable. Modelo: —. Resultado: —

**Toma 1.2 — puerto y rutas**
```
Stylized aerial view of a bulk export port at dusk: loading terminal, stacked cargo, a
docked vessel, calm ocean beyond, faint shipping lanes suggested as soft light trails over
the water. Clean horizon, generous empty sky for overlay graphics.
```
Post: capas de UI ascendiendo desde la operación (tiles de BI, CRM, ERP, logística,
producción) — genéricas, sin marcas. Texto: `SQM YA FUNCIONA BIEN.`
Movimiento: travelling lateral lento. Modelo: —. Resultado: —

---

## Escena 2 — El desafío

**Toma 2.1 — los diez**
```
Ten professionals in different work environments shown as a connected constellation of
clean vignettes on a dark navy background: an office desk, a control room, a plant floor
with hi-vis vest and helmet, a port yard, a finance workstation. Each person lit by their
own screen, thin luminous lines linking the vignettes into one shared circuit. Symmetrical,
uncluttered composition, space around each vignette.
```
Post: etiquetas por área (Comercial, Demand Planning, Producción, Inventarios, Logística,
Puerto, Shipping, Finanzas, BI).
Movimiento: push-in muy lento mientras las líneas se encienden. Modelo: —. Resultado: —

---

## Escena 3 — Una excepción

**Toma 3.1 — mapa global**
```
Dark stylized 3D globe seen from space, continents as subtle matte relief, faint latitude
grid, cool navy background. A single region in South America glows softly in cyan, a thin
beam rising from it. Everything else dim. Large clean empty area to the right of frame.
```
Post: tarjeta `BRASIL · PRODUCTO X / Forecast +14% / Cobertura proyectada: 18 días`.
Movimiento: rotación suave del globo, el punto se enciende. Modelo: —. Resultado: —

---

## Escena 4 — Cómo se resuelve hoy

**Toma 4.1 — la red de dependencias**
```
Abstract corporate data visualization: one highlighted card node at center, six satellite
nodes arranged around it connected by thin animated light paths, each satellite represented
by a simple monochrome icon plate (factory, warehouse pallet, truck, handshake, coin, cargo
ship). Dark navy volumetric background, cyan connection glow, plenty of breathing room.
```
Post: rótulos Producción, Inventarios, Logística, Clientes, Costos, Próximos embarques.
Movimiento: las conexiones se trazan una a una; leve parallax. Modelo: —. Resultado: —

---

## Escena 5 — Entra Velaria

**Toma 5.1 — la capa**
```
Exploded horizontal-layer diagram floating in dark space: three lower slabs representing an
existing technology stack, rendered in muted slate grey with faint UI texture, intact and
solid. A fourth translucent luminous layer descends and settles above them, glowing soft
cyan, casting light down onto the layers below without altering them. Clean, architectural,
symmetric, wide empty margins.
```
Post: `VELARIA — Contexto · Criterios · Gobernanza · Observabilidad`.
Movimiento: la capa desciende y se asienta; luz se propaga hacia abajo. Modelo: —. Resultado: —

---

## Escena 6 — Criterios y gobernanza

**Toma 6.1 — políticas**
```
Four blank floating UI policy cards in a staggered arrangement over a dark navy gradient,
each card a clean rounded panel with a small icon plate at top-left and empty body space,
subtle drop shadow, thin cyan left border. Minimal, editorial, generous spacing.
```
Post: las 4 políticas + matriz de permisos por área (Comercial / Logística / Finanzas).
Movimiento: las tarjetas entran escalonadas. Modelo: —. Resultado: —

**Toma 6.2 — permisos y trazabilidad**
```
Abstract governance visual: three vertical lanes of light, each gated by a translucent
checkpoint plane; small tokens of light pass through some gates and are held at others.
Dark corporate background, cyan and mint accents, restrained and precise.
```

---

## Escena 7 — Velaria observa

**Toma 7.1 — semanas de trabajo**
```
Time-lapse feeling composition: the same ten professional vignettes as before, now with
small pulses of light emerging from each workstation and drifting upward into a shared dark
space above them. Sparse at first, then denser. Cool palette, soft bloom, wide empty upper
area where the pulses converge.
```
Movimiento: aceleración sutil, los pulsos convergen al final de la toma. Modelo: —. Resultado: —

**Toma 7.2 — convergencia**
```
Dozens of thin light trails in dark space gradually bending toward one another and merging
into a single bright braided line. Minimal, elegant, cyan on deep navy, high contrast.
```

---

## Escena 8 — Insight

**Toma 8.1 — dashboard**
```
Clean dark-mode analytics dashboard floating in space, shot at a slight angle: one large
empty hero panel at top, a row of four blank metric tiles below, thin dividers, no readable
text anywhere, all surfaces left empty for graphics. Soft screen glow, shallow depth of
field, premium enterprise software feel.
```
Post: `OPORTUNIDAD DETECTADA / Weekly S&OP Exception Review / 8 usuarios / 67 ejecuciones
similares / 5 fuentes involucradas / 112 horas de trabajo asociadas`.
Movimiento: el panel se endereza hacia frontal; tiles aparecen escalonados. Modelo: —. Resultado: —

---

## Escena 9 — MCP + Skill

**Toma 9.1 — conector gobernado**
```
Abstract connector visual: a luminous cyan conduit linking a soft glowing sphere on the left
to a rack of muted grey system blocks on the right, passing through a translucent gate ring
at the midpoint. Dark navy space, clean industrial-technical aesthetic, label plate area
left blank beneath the gate.
```
Post: etiqueta `MCP`.

**Toma 9.2 — la Skill**
```
Horizontal pipeline of six connected rounded nodes flowing left to right, each with a blank
label plate below it, a pulse of light traveling through the chain from first to last. Dark
navy background, cyan flow, mint highlight on the final node. Clean, schematic, wide format.
```
Post: Demanda → Inventario → Producción → Logística → Criterios → Impacto económico, y el
nombre `Weekly S&OP Exception Review`.
Modelo: —. Resultado: —

---

## Escena 10 — La semana siguiente

**Toma 10.1 — bandeja de excepciones**
```
Minimal dark-mode enterprise screen seen straight on, floating: a short list of blank rows
with status dots on the left, three empty summary figures across the top. Extremely clean,
lots of empty space, no readable text. Calm morning light quality.
```
Post: `27 excepciones detectadas / 5 requieren decisión / US$1,34M de impacto económico potencial`.

**Toma 10.2 — el caso Brasil abierto**
```
Detail panel opening over the previous screen: one hero card at top and three stacked option
rows below it, each row an empty rounded plate with a small leading indicator, the third row
tinted warm amber. Dark UI, precise alignment, everything left blank for overlay text.
```
Post: Alternativa A US$17k / Alternativa B US$41k / No intervenir: margen en riesgo US$310k.
Movimiento: apertura del panel, foco sobre la tercera fila. Modelo: —. Resultado: —

---

## Escena 11 — De productividad a valor

**Toma 11.1 — el KPI cambia**
```
Single dominant blank figure plate centered in dark space, with a small secondary plate
shrinking and receding into the background behind it. Beneath, a row of four small empty
metric chips. Mint green accent on the dominant plate. Financial, sober, high-end.
```
Post: `VALOR ECONÓMICO / Identificado US$1,34M / Implementado US$590k / Validado por Finanzas
US$447k / Capital de trabajo liberado US$620k / Capacidad recuperada 1.120 h`.
Movimiento: la métrica de horas se achica y retrocede; la de dólares crece al frente.
Modelo: —. Resultado: —

---

## Escena 12 — Cierre

**Toma 12.1 — el ecosistema**
```
Wide zoom-out revealing the full system as one ecosystem: the ten professional vignettes at
the base, the muted grey stack of existing systems above them, and the luminous translucent
layer crowning the composition, all connected by soft light. Symmetrical, architectural,
serene, deep navy background with wide empty sky above for the final title.
```
Movimiento: zoom out lento y continuo hasta plano general. Modelo: —. Resultado: —

**Toma 12.2 — placa final**
```
Empty dark navy field with a subtle radial glow at center and a faint horizon line, nothing
else. Pure negative space for a final title card.
```
Post: `VELARIA / De uso individual de IA a capacidad organizacional medible.`

---

## Locución

- Voz: masculina o femenina, español neutro, tono ejecutivo y calmado, ritmo pausado.
- Generar por escena (12 pistas) para poder ajustar timing sin re-renderizar todo.
- El texto exacto de cada locución está en `guion.md`.

## Pendiente antes de generar

- [ ] Elegir modelo de imagen y de video, y confirmar presupuesto de créditos.
- [ ] Validar frames clave de escenas 1, 5 y 8 (definen el arte del resto).
- [ ] Elegir voz de locución.
- [ ] Música: bed corporativo minimal, sin percusión agresiva; crescendo en escenas 11–12.
