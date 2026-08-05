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
- 2026-08-05 (2): VIDEO v1 ENTREGADO. 8/8 bloques, 80s, 16:9, subtitulos "clean".
  Narracion final: voz clonada chilena de Sebastian (element f41d7f77) tras descartar
  Cillian (sonaba angloparlante) y Marisol. Ensamblado con finish_video.sh, todos los
  gates verdes. Entregable 720p: 5dcd4046-fa7f-4827-a4ca-76223144ef1c.
  Upscale Topaz 1080p en curso (job fecbe4bf-15e0-4eba-a4f3-77a095c76957).
  Guion v3 parametrizable en guion.md para la revision con el equipo.
- 2026-08-05 (3): Upscale Topaz 1080p COMPLETADO. Entregable final:
  hf_20260805_010623_fecbe4bf-15e0-4eba-a4f3-77a095c76957.mp4 (80s, 1080p, 16:9,
  subtitulos quemados, voz clonada chilena). Proyecto v1 cerrado; proximo paso es la
  revision del guion con el equipo (ver guion.md, bloques B1-B8 parametrizables).
- 2026-08-05 (4): Musica ad hoc generada con sonilo_music, 80s exactos, arco en tres
  partes que sigue el guion (tension sin resolver 0-20s / giro cuando aparece Velaria
  20-30s / momentum 30-70s / cierre 70-80s). Dos versiones: corporativa
  (774f7217-ac51-4fd4-b791-7f9cdf3aeb50) y ELECTRONICA elegida por Sebastian
  (0c0ef7bc-561c-472b-8a90-3715ece4e171). Video v3 con musica ducked bajo la voz:
  92513a10-881d-4340-98ef-3b4ba2a0d2d2 (720p). Upscale 1080p: job
  8190ed44-99d9-4160-9a68-3e8831636f28. Musica generada = sin problema de licencia.
- 2026-08-05 (5): Upscale 1080p CON MUSICA completado:
  hf_20260805_012714_8190ed44-99d9-4160-9a68-3e8831636f28.mp4
  PENDIENTE (decision de Sebastian): la musica queda inaudible porque el ensamblador
  la mezcla como cama a -24.6 dB y le hace ducking bajo la voz. Medido: el volumen
  medio con musica (-19.0/-18.7/-18.5 dB) es casi igual al de la version sin musica
  (-19.0 dB). Descartado el falso diagnostico de 96 kHz: la version que Sebastian si
  escucho tiene la misma codificacion. Opciones ofrecidas: (a) subir la musica 8-12 dB
  en la mezcla final, (b) abrir respiros instrumentales sin voz al inicio y al cierre
  (implica reescribir 2 lineas del guion y regenerar esas 2 tomas), o ambas.
- 2026-08-05 (6): MUSICA SUBIDA AL TOPE. Hallazgo tecnico: assemble_final.sh mide la
  cama contra la voz y la fija ~14 dB bajo el habla, asi que subir el archivo de entrada
  no sirve; el unico control es --music-vol (default 0.10, clampeado a 0.20 = +6 dB max).
  finish_video.sh NO expone ese flag, asi que se uso la cadena de abajo (documentada en
  SKILL.md para 're-assembly with a bed'): assemble_final.sh --music-vol 0.20 +
  audio_to_captions.py + burn_caps_clean.sh. Resultado: cama de -24.60 a -18.58 dB.
  Entregable 720p: 6cebef59-facb-4c24-b825-bb903540f9dd. Upscale 1080p job
  a03aca62-3838-4409-bc74-5be95f4fbfad.
  NO SE PUDO el respiro instrumental: el ensamblador exige 8.6-10.0 s de habla en CADA
  bloque de 10 s (gate duro), asi que no admite un tramo sin voz. Para un intro/outro
  instrumental real habria que editar fuera de este pipeline.
- 2026-08-05 (7): ENTREGABLE FINAL 1080p con musica al tope:
  hf_20260805_035002_a03aca62-3838-4409-bc74-5be95f4fbfad.mp4
  (80s, 1080p, 16:9, voz clonada chilena, musica electronica a -18.58 dB, subtitulos
  quemados). Este reemplaza a todas las versiones anteriores.
- 2026-08-05 (8): VERSION 2 COMPLETA (rebrief de Sebastian). Cambios: 60s (6 bloques),
  ambientacion de OFICINA REAL (monitores, archivadores, estanteria de biblioteca,
  muro de metricas), simbolo del ojo de Velaria en los bloques 3 y 6, arco mas
  dramatico (problema fuerte -> quiebre -> solucion), keywords de producto en la
  narracion (cuentas gobernadas, biblioteca, skills, integraciones, controles, linea
  base). Guion nuevo validado valid:true (sm2.json). Assets nuevos: office_wide
  d29bbdd9, desk_detail ec0713b9, velaria_stage 3e3fb2cb, library_wall 41668f99,
  dashboard_wall deeda5c6, screen_chat 6dd36e5e, screen_spreadsheet e3ad96fe,
  screen_slides 5b2f7caa, velaria_eye 2c41de99 (generado desde el SVG real de marca
  febdaf0f). Reusados: engineer, colleague, giant_hand, blue_folder, seal_stamp.
  Musica nueva de 60s con drop en el segundo 18: 4d8fb976.
  Entregable 720p: c8efc430-7e19-483e-9257-2229780288fb. Upscale job d5e67946.
  LIMITE CONOCIDO: no se pueden poner marcas reales (Word/Excel/Claude) ni texto
  legible en pantalla; se representan por su forma visual (grilla, slide, burbujas de
  chat) y las keywords viajan en la narracion + subtitulos.
- 2026-08-05 (9): ENTREGABLE FINAL v2 en 1080p:
  hf_20260805_153847_d5e67946-adcf-4579-9dee-b4ef223eac5a.mp4
  (60s, 1080p, 16:9, oficina, simbolo de marca en bloques 3 y 6, voz clonada chilena,
  musica electronica con drop en el segundo 18, subtitulos quemados).
  Este reemplaza a la v1 de 80s como version vigente.
