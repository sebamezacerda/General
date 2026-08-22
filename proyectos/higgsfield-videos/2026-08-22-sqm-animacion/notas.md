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
- 2026-08-22: se crea el proyecto a partir de la plantilla. Se recibe y documenta el guion
  completo (12 escenas, locución + texto en pantalla) en `guion.md`.
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
