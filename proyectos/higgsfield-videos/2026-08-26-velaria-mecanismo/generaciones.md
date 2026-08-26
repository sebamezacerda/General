# Generaciones

## Corte v1 — 26/08/2026

**3:05 · 1920×1080 · H.264 + AAC · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/d8c3fecb-2358-43b0-ab2f-21b628eff974.mp4

Nueve láminas. El guion apuntaba a 3:22 estimando 140 palabras por minuto; la locución medida
da 170,1 s de voz y 15,1 s de aire repartido, o sea 3:05.

| # | Lámina | Voz | Ventana |
|---|---|---|---|
| 1 | Qué hace Velaria | 28,5 s | 30,1 s |
| 2 | ¿Cómo funciona? · los cinco pasos | 6,6 s | 8,0 s |
| 3 | Paso 1 · Tu equipo ya usa IA | 28,8 s | 30,4 s |
| 4 | Paso 1 · El mismo problema | 21,1 s | 22,7 s |
| 5 | Paso 2 · Las piezas | 26,9 s | 28,7 s |
| 6 | Paso 3 · El conocimiento sube y vuelve | 22,3 s | 23,9 s |
| 7 | Paso 4 · La base se arma sola | 14,4 s | 15,9 s |
| 8 | Paso 5 · Se reparte y se dirige | 17,4 s | 19,2 s |
| 9 | Cierre | 4,2 s | 6,5 s |

## Locución

Voz Isabella con `text2speech_v2` variante `minimax`, la misma de los cortes de SQM. Texto
**textual del guion**, salvo la fusión de las escenas 3 y 4, que obligó a reescribir esas dos
pistas.

Las nueve pistas se transcribieron con `faster-whisper` y `word_timestamps` antes de montar.
De ahí salen los `data-in` de cada elemento y también la detección de colas alucinadas: la
pista del paso 4 terminaba en «Argen. Eso.» a los 14,56 s. Se corta en 14,4 s con fade.

## Error corregido en el camino

Las dos primeras láminas salieron sin doctype ni hoja de estilo —texto negro sobre blanco, sin
tipografía—. La causa: en el bloque que las escribía, un `cd` a un directorio inexistente
cortó por `&&` la asignación de la variable que llevaba el `<head>`, así que se expandió vacía.
Se detectó capturando frames antes de renderizar el corte completo, no después.

## Pendiente

- **Tomas reales de oficina.** El guion trae un `Prompt visual` fotográfico por escena —gente
  trabajando, luz de mañana, cámara quieta— y no están generadas. El corte de hoy es solo
  gráfico. Van como planos de respiro entre láminas, no como fondo con texto encima: el sistema
  prohíbe que algo flote.
- **Música.** Cama sobria y baja. El guion prohíbe explícitamente la música épica que sube.
