# Casa Sanz — Video Ad (Higgsfield)

## Objetivo
Producir un video vertical (9:16) para Instagram/Reels que promocione **Casa Sanz**,
restaurante vegano en Vitacura, Chile. El video debe comunicar que Casa Sanz no es
"la única opción vegana", sino una carta completa y variada, y cerrar con un CTA claro
para reservar.

## Para qué negocio
Casa Sanz — restaurante 100% vegano en Vitacura, Santiago de Chile. El video es
material de marketing (ads/orgánico) para redes sociales, orientado a atraer
comensales veganos y curiosos que hoy sienten que comer afuera implica conformarse
con "la única opción" del menú.

## Guión base: "El fin de la única opción"
7 planos, con textos en pantalla en español, sincronizados a una voz en off:
1. **Hook** — plato triste / solo, dramático (la frustración de tener una sola opción vegana).
2. Transición — "hasta que llegas acá".
3. Montaje de variedad — sushi, ramen, ravioles (para transmitir "carta completa").
4. Plato fermentado — "toda vegetal".
5. Cóctel — "nada aburrido" (a propósito puesto como último beat de comida, antes del cierre,
   para reforzar sensación de variedad).
6. Entrada/fachada de Casa Sanz — reveal del lugar.
7. Logo + CTA — "RESERVA AHORA".

## Estado actual (2026-08-02)
- Video ensamblado y funcional, con:
  - Grading de color unificado entre los 7 clips.
  - Efectos de cámara variados por plano (zoom in/out, pan) en vez de un único efecto repetido.
  - Cortes de plano resincronizados al ritmo real de la voz en off (timestamps por palabra vía
    transcripción Whisper), para más "pace".
  - Montaje de variedad de platos + cóctel como último beat antes del reveal del local.
  - CTA final: "RESERVA AHORA" (texto activo, en vez de "Solo con reserva").
  - Música de fondo (pista libre de derechos, subida por el usuario desde Pixabay).
  - Voz en off clonada: voz femenina chilena (clon de audio grabado por el usuario),
    ralentizada 15% (pitch-preserving) porque la grabación original era muy rápida
    para el ritmo visual del montaje.
- Última versión del video (voz chilena + música):
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/a8e16930-625b-48b6-b1e7-8c50b1a5c525.mp4
- Se corrió `virality_predictor` de Higgsfield sobre una versión anterior: hook_score muy bajo
  (19/100 → 21/100 tras un primer ajuste de brillo/texto del hook). Sigue siendo el punto más débil.

## Pendientes / temas abiertos
1. **Fidelidad del clon de voz**: el último clon de voz chilena femenina no está sonando
   suficientemente fiel a la persona real que grabó la muestra. Hay 3 clones guardados en la
   cuenta de Higgsfield (uno masculino, dos femeninos — la regrabación fue la elegida). Pendiente
   decidir si se regraba con audio más largo/limpio o se prueba otro motor de voz (elevenlabs vs
   seed_audio).
2. **Verificación vegana de 2 platos**: los ravioles y el plato de fermentados usados en el
   montaje de variedad no tienen confirmado que sean 100% libres de lácteo/huevo — riesgo
   reputacional relevante porque el hook entero del video es "100% vegano".
3. **Hook score bajo en el predictor**: la mejora estructural propuesta y no ejecutada es partir
   el hook de 3s en varios cortes rápidos en vez de un plano continuo, para intentar subir el
   hook_score de forma más significativa.
4. **QA visual**: el entorno de trabajo no tiene acceso a internet para reproducir/ver el video
   directamente (solo el sandbox de Higgsfield tiene salida a su CDN), así que todo el ajuste de
   encuadres/texto se hizo "a ciegas" — el usuario es quien hace la validación visual final de
   cada versión.

## Notas técnicas de producción
- Modelo de video usado inicialmente por error: `cinematic_studio_video_3_5` (solo acepta
  imágenes de referencia, no video) — causa raíz del problema inicial reportado por el usuario.
- Ensamblado final se hace 100% vía `ffmpeg` en un sandbox remoto de Higgsfield (no hay
  edición local), con transcripción `faster-whisper` para sincronizar cortes a la voz.
- Ver `prompts.md` en esta misma carpeta para el detalle de los prompts de generación usados.
