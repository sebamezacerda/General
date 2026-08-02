# Prompts usados — Casa Sanz (Higgsfield)

Registro de los prompts reales de generación usados en el proyecto, tal como quedaron
guardados en los jobs de Higgsfield.

## Plano 1 — Hook ("plato triste", versión dramática final)
- **Modelo:** `cinematic_studio_video_v2`
- **Duración:** 3s · **Aspect ratio:** 9:16
- **Prompt:**
  > A small, sad plate of plain undressed greens and steamed vegetables on a dim but visible
  > dark wooden restaurant table, warm moody light already illuminating the plate from the very
  > first frame — no black screen, no slow fade-in from darkness. The camera is already moving
  > fast toward the plate from frame one, an aggressive continuous dolly-in with visible motion
  > immediately, snapping to a hard stop with a subtle impact shake near the end. High contrast,
  > cinematic color grade, tense dramatic mood, sharp focus on the plate throughout.
- Nota: esta versión se generó después de que el `virality_predictor` mostrara un hook_score muy
  bajo (19/100). Se ajustó para que la iluminación sea visible desde el frame 1 (nada de fade-in
  desde negro) y el movimiento de cámara arranque inmediato — subió apenas a 21/100.

## Plano 2 — Mesa llena / abundancia (regeneración sin rostros)
- **Modelo:** `seedance_2_0` (con 1 video de referencia del usuario)
- **Duración:** 4s · **Aspect ratio:** 9:16 · **Resolución:** 720p
- **Prompt:**
  > A wooden restaurant terrace table completely covered edge to edge with plates of food, wine
  > glasses, and water carafes, warm string lights glowing above, evening ambience. The camera
  > starts low near the tabletop and cranes smoothly upward, revealing the full abundance of
  > dishes spread across the table. No people's faces are visible in the frame at any point —
  > diners are out of frame or only visible as blurred, faceless silhouettes at the edges. Warm
  > cinematic lighting, shallow depth of field, no text, no logos.
- Nota: se regeneró específicamente para evitar rostros reconocibles de comensales reales en el
  ad. Higgsfield sugirió un preset ("IN THE DARK") que se rechazó explícitamente
  (`declined_preset_id`) para forzar la generación literal del prompt.

## Planos 3–6 — Footage real de la biblioteca (sin generación nueva)
No se generaron con prompt de texto: se matchearon clips ya existentes en la biblioteca de medios
del usuario contra el guión, usando `video_analysis_create/status` (análisis de escenas por IA)
para identificar qué clip real correspondía a cada beat del guión (sushi, ramen, ravioles, plato
fermentado, cóctel, entrada del local).

⚠️ Nota de fiabilidad: se detectó que `video_analysis` puede alucinar timestamps de escenas más
allá de la duración real del clip (ej. describir una escena a los 0:15 en un clip de 2.79s real).
Por eso se descartó un beat planeado ("chef sirviendo un plato") que la IA describía pero que no
existía realmente en el clip corto.

## Plano 7 — Logo + CTA
Compuesto estático (no generado por IA de video): frame de fondo tomado del clip de entrada del
local + logo superpuesto + texto `RESERVA AHORA`, armado directamente con `ffmpeg` en el sandbox
(blur + oscurecido de fondo, overlay de logo, drawtext con fade-in).

## Voz en off (locución)
- **Modelo:** `seed_audio` (voice cloning por referencia de audio)
- **Voz:** `Voz Chilena Mujer Casa Sanz-1` (voice_id `6763642c-6a96-478c-9768-179791db8fcc`,
  voice_type `element` — clon de una grabación de una mujer chilena hecha por el usuario)
- **Guión / prompt:**
  > Cuando eres vegano y el menú tiene UNA opción. Hasta que llegas acá. Carta completa. Toda
  > vegetal. Nada aburrido. Casa Sanz, Vitacura. Reserva ahora.
- Resultado: 8.155s de audio, ritmo muy rápido → se ralentizó 15% (`atempo=0.85`,
  pitch-preserving) para dar tiempo a los cortes visuales.
- Se generaron y probaron previamente otras voces para el mismo guión: una voz femenina francesa
  y un clon de voz masculina chilena, antes de decidirse por el clon femenino chileno.

## Textos en pantalla (captions, español)
1. `SOLO UNA OPCIÓN.`
2. `Hasta que llegas acá.`
3. `Carta completa.`
4. `Toda vegetal.`
5. `Nada aburrido.`
6. `Casa Sanz · Vitacura`
7. `RESERVA AHORA`

## Música
Pista libre de derechos subida por el usuario desde Pixabay (`sunset-lo-fi-disco-569618`), usada
de fondo con loop + fade in/out y mezclada por debajo de la voz (`amix`, voz peso 1.0, música
peso 0.6, volumen base 0.20 antes del mix).
