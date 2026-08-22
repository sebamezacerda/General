# VELARIA

- Qué es el proyecto: plataforma que agrega una capa de inteligencia organizacional sobre el
  stack tecnológico existente de una empresa — contexto, criterios, gobernanza y
  observabilidad sobre el uso de IA. Convierte patrones de uso en capacidades compartidas
  (Skills), las gobierna y mide el valor económico que generan.
- Mi rol: colaborador (invitado)
- Repo real del proyecto: `Velaria-HQ/velaria-delivery` (GitHub)
- Dónde trabajo esto: web (Claude Code) — video/marketing; el producto vive en el repo de arriba.
- Tagline: "Libera el poder de la IA. Guíala con tu visión."

## ⚠ Acceso desde sesiones de Claude Code

`Velaria-HQ/velaria-delivery` **no es accesible** desde sesiones ancladas al owner
`sebamezacerda` (este repo): el entorno no permite sumar repos de otro owner a una sesión
existente ("cross-tier adds are not supported"), y además la GitHub App de Claude no está
instalada en la organización `Velaria-HQ`. Que mi usuario de GitHub tenga acceso no se lo da
a la app — son permisos separados.

Para trabajar contra ese repo: abrir una sesión nueva con `Velaria-HQ/velaria-delivery` como
fuente inicial, previa autorización de la org por un owner. Mientras tanto, el sistema visual
queda copiado más abajo para que cualquier sesión futura pueda diseñar en marca sin ese acceso.

## Sistema de diseño (regla persistente)

> Copiado de `sistema visual.md` del repo `velaria-delivery`, a su vez copiado del repo de
> research el 2026-07-30. Todo diseño nuevo sigue este sistema. No preguntar por estilo salvo
> que el usuario pida salirse de él.

### Marca
- Símbolo: **ojo del velarium** — anillo fino (stroke 2.5 en viewBox 48), arco de acento
  (dasharray 30 90, offset 52, rotate -90), punto central r5. Favicon reforzado: anillo r18
  stroke 4 + punto r6 acento, sin arco.
- Wordmark: `velaria_` en **IBM Plex Mono 500**, minúsculas, letter-spacing ≈0.1em; el `_`
  final va en acento (sobre ink: accent-hi; en monocromo: color del texto). En UI viva el `_`
  puede pestañear (keyframes `vblink`: 0%,58% opacity 1 / 60%,100% opacity 0, 1.02s).

### Paleta (FINAL — no usar la antigua #2D6BFF/cobre)
| Token | Hex | Uso |
|---|---|---|
| `--ink` | `#0B0F17` | fondo oscuro |
| `--ink2` | `#151C2B` | paneles |
| `--accent` | `#2456D6` | acción primaria (**UN solo azul de acción por vista**) |
| `--accent-hi` | `#7DA0F2` | texto/acento azul sobre fondos oscuros |
| `--light` | `#F5F7FA` | fondo claro |
| `--text` | `#111827` | texto sobre claro |
| `--mute` | `#6B7280` | secundario sobre claro |
| `--steel` | `#8A94A6` | labels técnicos, metadatos (reemplazó al cobre) |

Estados **solo en badges**: ok `#3FB27F` · warn `#D9A03C` · err `#D95C4A`.
Hairlines sobre ink: `rgba(245,247,250,.08–.15)`. Bordes claros: `#E5E7EB`.

### Tipografía
- UI/títulos/cuerpo: **IBM Plex Sans** (decks legacy: Avenir Next, fallback Helvetica).
- Sistema/labels/kickers/timestamps/navegación: **IBM Plex Mono**, CAPS, letter-spacing 1.5–3px.

### Principios de UI (consola = oscura; docs/reportes = claros)
1. **Todo es registro**: timestamps mono `14:32:08Z`, estados entre corchetes `[ ACTIVO ]`
   (nunca píldoras), comentarios `// así`.
2. **Nada flota**: sin sombras ni glow en la consola; jerarquía por hairlines, planos ink/ink2
   y densidad. Radios 0–2px (slides hasta 4px).
3. **El prompt manda**: acción primaria con prefijo `❯` (`❯ DESPLEGAR`), etiquetas de botón en
   mono caps. La ubicación activa (nav) lleva `_` pestañeando. Foco = outline 1px accent-hi
   con offset 3px.
- Iconos: grilla 24px, stroke 1.5, remates cuadrados (`stroke-linecap="square"`), sin curvas
  decorativas. Set base en el manual (sección 09).
- Avisos = líneas de log con borde izquierdo de estado, no popups. Confirmación destructiva =
  tipear la palabra.

### Slides
Portada y cierre sobre ink; contenido sobre light. Kicker mono acero, tarjetas blancas con
barra superior 2–3px accent, barra de síntesis oscura con borde izquierdo accent y label
SÍNTESIS en acero.

### Prohibido
Degradados · glassmorphism · orbes/blobs · glow · esquinas redondas · emojis · cerebros/chips/
circuitos/redes neuronales · sombras blandas gigantes · píldoras de estado · más de un azul de
acción por vista.

### Archivos de referencia
- ✅ `velaria-kit/` — **disponible** en
  `proyectos/higgsfield-videos/2026-08-22-sqm-animacion/referencias/velaria-kit/`: SVGs de
  símbolo y wordmark (color, mono, favicon), tokens CSS, firma de correo, og-image, banners y
  avatares. La paleta del kit coincide exactamente con la de este documento.
- ❌ `Velaria UI Manual.dc.html` — componentes de plataforma (**fuente de verdad de UI**). No
  disponible. Es lo que falta para diseñar pantallas de producto en marca.
- ❌ `Velaria Brand Board.dc.html` — identidad y sistema de slides. No disponible.
- ❌ `Velaria Landing.dc.html` — patrón de landing/marketing. No disponible.

### Geometría del símbolo (del kit, exacta)
Sobre `viewBox 0 0 48 48`: anillo `circle cx24 cy24 r19` stroke `#F5F7FA` width 2.5 (*la lona
tendida sobre la arena*) · arco mismo círculo stroke `#2456D6` dasharray `30 90` dashoffset `52`
`rotate(-90 24 24)` (*el tramo que Velaria cubre*) · punto `circle cx24 cy24 r5` fill `#F5F7FA`
(*la operación, intacta*).

### ⚠ Conflicto de tipografía sin resolver
El `README.md` del kit indica **Avenir Next** (fallback Helvetica Neue) para títulos/cuerpo y
*mono del sistema* (SF Mono / Menlo) para labels. El `sistema visual.md`, posterior, indica
**IBM Plex Sans** e **IBM Plex Mono** y degrada Avenir Next a "decks legacy". Se adopta Plex por
ser lo más nuevo, coherente con el wordmark y libre. **Confirmar con el fundador.**

### Composición aplicada (deducida del kit)
El `og-image` y los banners componen igual: dos hairlines horizontales encerrando una banda,
lockup a la izquierda, labels mono caps steel a la derecha, tagline en dos líneas (la segunda en
`--accent-hi`), pie con metadato mono steel. La firma de correo usa `border-left: 3px solid
#2456D6` como marca de bloque — el mismo recurso que el `--accent` a la izquierda de los paneles.

## Resumen de estado
- 2026-08-22: se documenta el sistema de diseño acá para desbloquear el video "Caso sintético
  SQM × Velaria" (`proyectos/higgsfield-videos/2026-08-22-sqm-animacion/`).
- 2026-08-22: llega el `velaria-kit` completo y queda versionado en el proyecto de video.
  Confirma la paleta, aporta la geometría exacta del símbolo y el lockup. Pendientes: el
  `UI Manual` (para las escenas de dashboard) y resolver el conflicto de tipografía.
