# Velaria — Kit de identidad (mini manual)

Símbolo: **ojo del velarium** (opción 2c) — anillo fino (la lona tendida sobre la arena),
arco azul (el tramo que Velaria cubre), punto central (la operación, intacta).

## Estructura
- `simbolo/` — isotipo solo, color y monocromo + favicon 16 px
- `wordmark-3d-plexmono/` — lockup definitivo: IBM Plex Mono Medium, minúsculas, guión bajo final en azul (`velaria_`)
- `tokens/velaria-colores.css` — paleta como variables CSS

## Tipografía
- Wordmark: **IBM Plex Mono 500**, minúsculas, letter-spacing ≈ 0.1em, underscore final en --accent — https://fonts.google.com/specimen/IBM+Plex+Mono
- Slides — títulos/cuerpo: **Avenir Next** (fallback: Helvetica Neue)
- Labels técnicos/kickers: **mono del sistema** (SF Mono / Menlo), CAPS, letter-spacing 2–3 px

⚠ Los SVG usan `<text>` con `@import` de Google Fonts: se ven correctos en navegador.
Para editarlos en Figma/Illustrator instala IBM Plex Mono (gratis) o pídeme la versión vectorizada.

## Reglas rápidas
- Ink domina; el azul (#2456D6) es la acción — sobre ink usa #7DA0F2; el acero (#8A94A6) marca labels y metadatos.
- Radios 0–4 px. Sin degradados, sin glow, sin líneas decorativas bajo títulos.
- Área de respeto del lockup: la altura del símbolo a cada lado.
- Tamaño mínimo: símbolo 16 px; lockup horizontal 24 px de alto.
