# UI de Velaria para el video — pantallas reales

Las escenas 8, 10, 11 y 12 muestran producto. En vez de pedirle un dashboard a un generador de
imágenes, están **construidas en HTML con los tokens exactos del sistema** y capturadas con
Chromium a 1920×1080.

Ventajas sobre generarlas con IA: tipografía IBM Plex real, hairlines de 1px reales, hex
exactos, cifras correctas del guion, y cero riesgo de texto inventado o esquinas redondeadas.
Además se re-renderizan en segundos cuando cambia un número.

## Uso

```bash
npm install @fontsource/ibm-plex-sans @fontsource/ibm-plex-mono playwright-core
cp node_modules/@fontsource/ibm-plex-sans/files/ibm-plex-sans-latin-{400,500,600}-normal.woff2 fonts/
cp node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-{400,500}-normal.woff2 fonts/
node shot.js          # -> screens/*.png
```

Las fuentes ya están versionadas en `fonts/`, así que para solo abrir los HTML en un navegador
no hace falta instalar nada.

## Pantallas

| Archivo | Escena | Qué muestra |
|---|---|---|
| `08-insight.html` | 8 | Oportunidad detectada: *Weekly S&OP Exception Review*, 4 métricas y la evidencia en registro |
| `10-bandeja.html` | 10.1 | Bandeja de excepciones de la semana, 27 detectadas / 5 requieren decisión |
| `10-caso.html` | 10.2 | El caso Brasil con sus tres alternativas y el costo de no actuar |
| `11-valor.html` | 11 | El KPI que cambia: valor económico dominante, horas subordinadas |
| `12-plataforma.html` | 12 | Las siete secciones de la plataforma, para el cierre |
| `04-dependencias.html` | 4.1 | Las seis fuentes que hay que consultar para responder una pregunta |
| `04-pregunta.html` | 4.2 | La pregunta que abre el video, sobre negro |
| `06-criterios.html` | 6.1 | Las cuatro políticas de gobernanza |
| `06-permisos.html` | 6.2 | Matriz de permisos por área |
| `07-registro.html` | 7.1 | Muro de log: cuatro semanas de uso acumulado |
| `07-patron.html` | 7.2 | El mismo muro, con ocho líneas alineándose en el patrón |
| `09-mcp.html` | 9.1 | El conector gobernado y su gate |
| `09-skill.html` | 9.2 | La Skill como pipeline de seis pasos |

## Decisiones de diseño

- **Un solo `#2456D6` por pantalla**, siempre el botón de acción primaria. El sistema dice
  "sobre ink usa `#7DA0F2`", así que los acentos estructurales (barra de nav activa, borde
  izquierdo de panel) van en accent-hi. El azul de acción queda reservado para la acción.
- **Estados entre corchetes** (`[ CRÍTICA ]`, `[ RECOMENDADA ]`), nunca píldoras.
- **Timestamps en todo**: cabecera, filas de log y pie del rail. "Todo es registro."
- **Nav activa con `_`** en accent-hi, como pide el sistema.
- **Radio 0 global** vía `*{border-radius:0}`: es imposible que se cuele una esquina redonda.
- Sin sombras, sin degradados, sin glow. La jerarquía sale de hairlines y planos ink/ink2.

## ⚠ Estas pantallas son una propuesta, no el producto

Están diseñadas desde el sistema visual y el guion, **sin acceso al `Velaria UI Manual`**
(la fuente de verdad de UI) ni a `velariaworks.com` — la política de red del entorno bloquea
la web. Si el producto real difiere en nomenclatura o estructura de navegación, hay que
ajustarlas antes de filmar.

Los nombres de sección salen del guion de la escena 12: Instalaciones, Criterios, Insights,
Skills, Marketplace, Registro, Valor.
