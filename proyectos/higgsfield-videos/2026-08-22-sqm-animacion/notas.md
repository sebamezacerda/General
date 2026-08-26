# Caso sintético SQM × Velaria

- Para qué negocio: **VELARIA** (colaboración). Sistema de diseño y contexto en
  `proyectos/velaria/spec.md`.
- Objetivo del video: pieza de demostración/venta. Mostrar, sobre un caso sintético
  inspirado en las prioridades y operaciones públicas de SQM, cómo Velaria agrega
  una capa de inteligencia organizacional sobre un stack corporativo que ya funciona
  bien, y cómo eso se traduce en valor económico medible.
- Plataforma/formato: **16:9**, animación corporativa — limpia, tecnológica y realista.
- Duración objetivo: **2:30 – 3:00 min** (12 escenas, ~13–15 s por escena).
- Idioma: español neutro / locución en off.
- Estado: en progreso — guion cerrado, pendiente generación.

## Disclaimer obligatorio

Debe aparecer en pantalla al inicio (y conviene repetirlo en la descripción del video):

> Caso sintético basado en prioridades y operaciones públicas de SQM.
> Datos, usuarios e impactos económicos son ficticios.

## Estructura

| # | Escena | Idea central |
|---|--------|--------------|
| 1 | SQM hoy | La compañía ya está digitalizada; Velaria no reemplaza nada |
| 2 | El desafío | 10 personas, buena información, decisión distribuida |
| 3 | Una excepción | Brasil, Producto X, forecast +14% |
| 4 | Cómo se resuelve hoy | Orquestar conocimiento, personas y sistemas |
| 5 | Entra Velaria | Capa sobre el stack existente |
| 6 | Criterios y gobernanza | Políticas versionadas, permisos, trazabilidad |
| 7 | Velaria observa | Detecta 8 personas haciendo la misma tarea |
| 8 | Insight | Oportunidad detectada: Weekly S&OP Exception Review |
| 9 | MCP + Skill | Conector gobernado → Skill reutilizable |
| 10 | La semana siguiente | Se parte desde las decisiones, no desde la recopilación |
| 11 | De productividad a valor | El KPI pasa de horas a dólares |
| 12 | Cierre | De uso individual de IA a capacidad organizacional medible |

## Reglas de arte

**El arte sigue el sistema de diseño de Velaria** — documentado completo en
`proyectos/velaria/spec.md`. Ese documento manda sobre cualquier criterio de este proyecto.
Resumen operativo para el video:

- **Paleta estricta**: `ink #0B0F17` fondo · `ink2 #151C2B` paneles · `accent #2456D6` acción
  (uno solo por vista) · `accent-hi #7DA0F2` · `steel #8A94A6` labels técnicos ·
  `light #F5F7FA`. Estados solo en badges: ok `#3FB27F`, warn `#D9A03C`, err `#D95C4A`.
- **Tipografía**: IBM Plex Sans (títulos y cuerpo) + IBM Plex Mono CAPS con letter-spacing
  1.5–3px (labels, kickers, timestamps, navegación).
- **Todo es registro**: timestamps `14:32:08Z`, estados entre corchetes `[ ACTIVO ]` —
  nunca píldoras —, comentarios `// así`.
- **Nada flota**: sin sombras ni glow. La jerarquía sale de hairlines, planos ink/ink2 y
  densidad. Radios 0–2px.
- **El prompt manda**: acción primaria con prefijo `❯`, nav activa con `_` pestañeando.
- **Prohibido**: degradados, glassmorphism, orbes/blobs, glow, esquinas redondas, emojis,
  cerebros/chips/circuitos/redes neuronales, sombras blandas, píldoras de estado, más de un
  azul de acción por vista.
- Personas trabajando y decidiendo, nunca desplazadas por la máquina.
- Sin logos de terceros: los sistemas corporativos se nombran por categoría en mono caps.

### Dos reescrituras respecto del guion original

- **No hay redes de nodos.** Las escenas 2 y 4 pedían constelaciones y grafos conectados: eso
  cae en "redes neuronales" y "orbes", ambos prohibidos. Se reemplazan por estructuras de
  registro (grillas, tablas, líneas de log), que además son más fieles al principio "todo es
  registro".
- **Velaria no brilla.** La escena 5 pedía una capa luminosa descendiendo sobre el stack. Sin
  glow, la capa se expresa como un plano ink2 con un canto accent: jerarquía por plano y
  densidad, no por luz.

## Bitácora
- 2026-08-26: **corte v11** — 3:13. Cierra con la placa de marca y la bajada de la web.
  Habilitación abre en que Velaria sugiere qué IA usar. La música pasa a nivel fijo sin ducking.
- 2026-08-26: **corte v10** — 3:08. La escena 1 apuntaba a la locución del v5, que nombraba a
  SQM; corregida, y la intro termina en «Y funciona». Los bloques de música se encadenan en vez
  de fundirse a silencio. El video ya no menciona a SQM en ninguna parte.
- 2026-08-26: **corte v9** — 3:08. Sale el nombre de SQM, el aire baja a 0,4 s, la IA del
  ejercicio deja de nombrarse, los rótulos de eje se agrandan y entran primero, y la música
  pasa a cuatro piezas electrónicas por bloque. Se arregla el golpe de la cama al soltar el
  ducking en los silencios.
- 2026-08-26: **corte v8** — 3:26. Se abre el par «Hoy sin Velaria / Con Velaria», el ejercicio
  declara que la IA es Claude, y aparece el puente que faltaba: la operación se repite semanas
  antes de que Velaria proponga la Skill. Se corrigen los tiempos del impacto, que no daban
  espacio a la aprobación humana. Primera versión con música.
- 2026-08-25: **corte v7b** — 2:16. Se corrige lo que la voz dejaba sin decir: la locución lee
  los tres ejes, el problema de Brasil se enuncia entero, y diccionario y criterios llegan con
  su ejemplo real. El villano pasa de diez cuadros ilegibles a tres personas con lo que cada una
  construyó. Los cues salen de whisper. Deja de ser pitch de 90 s: es la versión didáctica.
- 2026-08-25: **corte v7 — pitch de 90 s** (1:36). Estructura nueva: reconocimiento →
  villano → Velaria y sus tres ejes (Habilitación · Mejora Continua · Gobernanza) → el caso
  atravesando los tres → impacto → cierre. Registro de pitch, no de explainer: la pantalla
  repite a la voz en las palabras clave, tipografía a sangre, corte duro. Se nombra Claude
  como la IA del ejemplo. Guion en `guion-v7.md`, motor nuevo en `ui/anim7.js`.
- 2026-08-25: **corte v6** — 2:26. Dos arreglos sobre el v5: (1) la version "sin
  subtitulos" salia con subtitulos porque `render.js` tenia el bucle principal roto y la
  linea de `NOSUBS` habia quedado en el bucle muerto de `OVER`; ahora cada corte escribe a
  su propio directorio (`clips` / `clips-nosubs`), verificado midiendo la banda inferior
  del frame rendido. (2) el tiempo muerto al final de cada lamina: el aire por escena baja
  de 6-11 s a 2,8 s y las entradas se reparten hasta el 86 % de la ventana, no el 62 %,
  sin tope superior de paso. Ademas el render captura en JPEG 94 (18 fps en vez de 5,3)
  y es reanudable, para que quepa en el lease del sandbox.
- 2026-08-22: se crea el proyecto a partir de la plantilla. Se recibe y documenta el guion
  completo (12 escenas, locución + texto en pantalla) en `guion.md`.
- 2026-08-22: se extiende el enfoque HTML a los diagramas (escenas 4, 6, 7 y 9). Quedan 13
  pantallas construidas y solo 6 tomas para generar con IA — las genuinamente fotográficas o
  volumétricas. Ver la tabla "Qué se genera y qué se construye" en `prompts.md`.
- 2026-08-22: las pantallas de producto (escenas 8, 10, 11 y 12) se construyen en HTML con los
  tokens exactos y se capturan con Chromium — ver `ui/`. Sale mejor que generarlas: tipografía
  Plex real, hairlines de 1px, cifras del guion correctas. Quedan como propuesta hasta poder
  contrastarlas con el UI Manual o la web (ambos inaccesibles por la política de red).
- 2026-08-23: **corte v5** — 3:13, con subtítulos quemados, tipeo en las pantallas de chat y
  transiciones fluidas. Produce el guion `guion-v5.md`. Tipografía reescalada para video.
- 2026-08-22: **corte v4** — reescritura: 1:47 en vez de 3:29, con el contenido escrito en
  pantalla y el paralelo hoy/Velaria como la misma tabla dos veces. Guion nuevo en `guion-v4.md`.
- 2026-08-22: **corte v3** — 29 planos en vez de 20 y sistema de animación acelerado. Se corrige
  un bug del v2: siete pantallas se reproducían hacia atrás al cerrar su escena.
- 2026-08-22: **corte v2** — se le da ritmo: contadores, capas de datos sobre los planos
  generados (incluida la tarjeta de Brasil que faltaba), y los planos dejan de congelarse.
- 2026-08-22: **corte v1 armado y entregado** — 3:29,4 a 1080p, con locución. Se montó en el
  sandbox de Higgsfield (`sandbox_exec`), que tiene ffmpeg y salida a internet y sí alcanza el
  CDN que esta sesión bloquea. Link y detalle en `generaciones.md`.
- 2026-08-22: ronda 1 de generación — 3 frames de validación (escenas 5, 8 y 12) con
  `recraft_v4_1 / utility`, que acepta paleta cerrada por parámetro. Detalle y checklist de
  auditoría en `generaciones.md`. Quedan sin auditar: el entorno bloquea el CDN de Higgsfield.
- 2026-08-22: llega el `velaria-kit` oficial y queda versionado en `referencias/velaria-kit/`.
  Confirma la paleta (coincide exacta), aporta la geometría del ojo del velarium y el lockup, y
  la maqueta del `og-image` pasa a ser la base de la placa final. Se adopta la banda entre
  hairlines como marco persistente del video. El cierre ahora construye el símbolo en el orden
  en que significa: punto (la operación) → anillo (el stack) → arco azul (Velaria cubre un
  tramo).
- 2026-08-22: llega el sistema de diseño real de Velaria (`sistema visual.md` de
  `Velaria-HQ/velaria-delivery`). Se reescriben **todos** los prompts: la primera versión usaba
  glow, degradados, esquinas redondeadas, redes de nodos y una paleta cyan/mint, todo prohibido
  por el sistema. El sistema queda copiado en `proyectos/velaria/spec.md` para que no dependa de
  acceder a ese repo. Falta: validar escenas de dashboard contra el `Velaria UI Manual`, elegir
  voz, generar y montar.

## Próximos pasos
1. Conseguir `Velaria UI Manual.dc.html` — es la fuente de verdad de UI y las escenas 8, 10 y
   12 muestran dashboard. Único bloqueante de arte que queda.
2. Confirmar tipografía: IBM Plex Sans (sistema visual, posterior) vs Avenir Next (README del
   kit). Se adopta Plex; falta el visto bueno del fundador.
3. Confirmar modelo de generación y presupuesto de créditos (~18 tomas).
4. Generar frames clave de las escenas 5, 8 y 12 para validar arte antes de animar el resto.
5. Animar cada frame aprobado y generar la locución (12 pistas).
6. Montaje, música y mezcla; export a `exports/` (no versionado).
