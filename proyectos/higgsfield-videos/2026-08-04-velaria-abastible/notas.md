# Animación VELARIA → Abastible

- Para qué negocio: VELARIA (venta del servicio a Abastible/Abastibletec)
- Objetivo del video: que un cliente corporativo NO experto en IA entienda en ~80s
  qué hace VELARIA y vea con claridad el **antes** (cada persona usando IA por su
  cuenta, sin colaboración) y el **después** (sistema gobernado, compartido y medido).
- Plataforma/formato: 16:9 horizontal, ~80s, VO español, subtítulos.
- Guion: `guion.md` (v2, basado en la propuesta real y el sistema visual de marca).
- Referencias / inspiración:
  - Video de referencia del cliente: https://www.youtube.com/watch?v=AfTU_796XaM
    (análisis en Higgsfield id `7595ca4e-41de-4e44-9d79-f673546dc3e3`, en cola lenta)
  - Sistema visual VELARIA: `marca/sistema-visual.md` del repo velaria-delivery
    (estética consola: ink #0B0F17, cobalto #2456D6, IBM Plex Mono, sin degradados
    ni esquinas redondas ni cerebros/circuitos)
- Motor/flujo en Higgsfield: workflow `faceless-channel-video`, tipo **Explainer**,
  modo **Animated**, preset base Editorial Motion Graphics adaptado a la marca.
  Pipeline: style anchor → asset roster → guion por bloques → generación por lotes
  → VO → ensamblado → upscale Topaz → entrega.
- Confidencialidad: este repo es PÚBLICO → acá no van precios, cifras de clientes ni
  material interno de velaria-delivery. El video de producción sí puede usar los
  datos del cliente (es para Abastible), pero no se versionan acá.
- Estado: guion listo, esperando OK para producir en Higgsfield.

## Bitácora
- 2026-08-04 (1): Setup del proyecto, workflow Explainer estudiado, análisis del
  video de referencia lanzado. Guion v1 con supuestos.
- 2026-08-04 (2): Recibidos el repo velaria-delivery (zip) y las propuestas
  Abastible/SQM (PDF) subidos por Sebastián a la sesión. Guion v2 escrito con el
  contenido real: estructura HOY/CON VELARIA + tres frentes (gobernanza,
  habilitación, productividad) + human in the loop + cierre con tagline oficial.
- 2026-08-05: Producción lanzada en Higgsfield. Sebastián eligió estilo
  **Whiteboard Doodle** en la galería (reemplazó al default Editorial). Ancla de
  estilo + 12 assets generados (2 personajes, 6 escenarios, 4 props; hilo
  conductor: dossier azul). Guion de 8 bloques validado (valid:true). 7/8 bloques
  de video generados con gemini_omni; el bloque 5 quedó bloqueado por falta de
  créditos (quedaban 9). Pendiente al recargar: bloque 5, narración seed_audio
  (voz Cillian, español), ensamblado con subtítulos, upscale Topaz 1080p, entrega.
