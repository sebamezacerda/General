# VELARIA · Formato "Ficha de producción" (v2)

Formato de entrega para animaciones producidas con Higgsfield. Se publica como artifact
HTML. Referencia canónica: la ficha del video de Abastibletec (agosto 2026).

## Estructura de la ficha (secciones, en orden)

1. **Masthead** — wordmark `velaria_` (guion bajo parpadeante en azul acento) alineado a la
   izquierda, kicker `Ficha de producción · v2` a la derecha. Debajo: `h1` con el nombre del
   video y un *standfirst* de una o dos frases que dice qué muestra el video y qué trae la ficha.
2. **Ver el video** — lista de enlaces de acción. Uno por versión: alta definición y versión
   liviana para mensajería. Cada fila: `❯ Reproducir` · descripción · meta (`1920×1080 · 60s`).
3. **Especificaciones** — grilla de pares dato/valor. Los ocho campos fijos:
   Duración · Formato · Resolución · Estilo visual · Color de acento · Narración · Música · Subtítulos.
4. **El guion** — un párrafo *lead* que nombra el **hilo conductor** (un objeto físico que
   aparece en todos los bloques, escala y se resuelve al final). Después un bloque por cada
   diez segundos, cada uno con:
   - riel izquierdo: id (`B1`), timecode (`00:00–00:10`), rol (Gancho / El costo / El quiebre /
     Qué instala / El giro / Cierre);
   - la línea de narración, con barra azul a la izquierda;
   - `En pantalla:` la descripción visual del bloque, en gris.
5. **Decisiones de producción** — notas con etiqueta en versalitas mono, una por decisión no
   obvia (limitaciones del generador, cómo se resolvió la marca, cómo se compuso la música).
6. **Qué se puede ajustar** — tabla `Cambio · Qué implica · Costo relativo`, con la nota de que
   los cambios se piden por número de bloque ("cambiar el texto del B4").
7. **Footer** — `Velaria Technologies · <mes año>` y, en mono gris, `// producido con Higgsfield`.

## Tokens de diseño

| token | claro | oscuro |
|---|---|---|
| `--bg` | `#F5F7FA` | `#0B0F17` |
| `--panel` | `#FFFFFF` | `#151C2B` |
| `--text` | `#111827` | `#F5F7FA` |
| `--mute` | `#6B7280` | `#98A2B3` |
| `--steel` (etiquetas) | `#8A94A6` | `#8A94A6` |
| `--accent` (azul cobalto) | `#2456D6` | `#7DA0F2` |
| `--rule` | `#E5E7EB` | `rgba(245,247,250,.12)` |

- Tipografía: sans del sistema para el cuerpo; **mono para toda etiqueta**, kicker, timecode,
  id de bloque y cifras de tabla (`font-variant-numeric: tabular-nums`).
- Etiquetas y encabezados de sección: mono, 10–13px, MAYÚSCULAS, `letter-spacing` 1.8–2.4px,
  color `--steel`. Los `h2` llevan una regla horizontal que se estira a la derecha.
- Ancho de contenido `max-width: 820px`. Bordes de 1px, `border-radius: 2px`, nada de sombras.
- Soporta claro y oscuro: `prefers-color-scheme` más overrides `:root[data-theme="..."]`.

## Convenciones de producción del video

- **Seis bloques de diez segundos = 60s.** 16:9, 1920×1080, 24 fps.
- **Estilo visual:** pizarra y plumón, con un único color de acento (azul cobalto de marca).
- **Narración:** voz chilena clonada. **Subtítulos quemados** en la imagen.
- **Música** compuesta a medida para los 60 segundos, no recortada de librería: arranca seca,
  corta en seco antes del quiebre, entra el bombo cuando aparece la solución, se retira al final.
- **Hilo conductor obligatorio:** un objeto físico presente en los seis bloques, que escala de
  forma monótona y se resuelve en el cierre (en Abastibletec: una carpeta azul, cerrada en el
  suelo al principio, sellada al final).
- **Las herramientas se muestran, no se nombran.** El generador rechaza marcas reales y el texto
  dibujado sale ilegible: la planilla es una grilla de celdas, la presentación es un slide con
  barra de título y gráfico, los asistentes de IA son ventanas con burbujas.
- **Las palabras clave viajan en los subtítulos**, no en la imagen, porque el subtítulo sí es
  texto limpio.
- Arco de los seis bloques: Gancho → El costo → El quiebre → Qué instala → El giro → Cierre.
