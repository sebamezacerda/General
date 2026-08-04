# Guion v2 — Animación VELARIA para Abastible

> Basado en el repo velaria-delivery (metodología + sistema visual) y la propuesta
> enviada a Abastibletec. NOTA: este repo es público, así que acá no van precios ni
> cifras internas del cliente; la versión de producción con detalles vive en la
> sesión de trabajo.

## Concepto

El video cuenta el **antes/después** que vive un equipo que trabaja con VELARIA,
usando el contraste "HOY / CON VELARIA" de la propuesta comercial. Audiencia: gente
que usa IA de forma superficial o cada uno por su cuenta. Cero jerga técnica en la
narración; lo técnico va como texto de pantalla al estilo consola.

- Duración: ~80s → 8 bloques de 10s (workflow Explainer de Higgsfield, modo Animated)
- Formato: 16:9 · VO en español · subtítulos sí
- Estilo visual: sistema VELARIA (estética de consola/registro) sobre el preset
  Editorial Motion Graphics:
  - Fondos ink `#0B0F17` / paneles `#151C2B`; acento azul cobalto `#2456D6` /
    `#7DA0F2`; acero `#8A94A6` para labels
  - Tipografía mono (IBM Plex Mono) en CAPS para labels; `❯` como prefijo de acción;
    estados entre corchetes `[ OK ]`; timestamps `14:32:08Z`
  - PROHIBIDO (regla de marca): degradados, glow, esquinas redondas, orbes,
    cerebros/chips/circuitos/redes neuronales, emojis
  - Wordmark: `velaria_` minúsculas con `_` pestañeando; símbolo: ojo del velarium

## Los 8 bloques

### B1 — HOY, el desorden (hook)
VO: "En tu empresa la IA ya llegó. Pero llegó desordenada: cada persona con su
cuenta, a su manera, cada uno por su lado."
Visual: plano oscuro tipo consola; varias ventanas de chat aisladas, sin conexión
entre ellas. Label: `HOY`.

### B2 — El costo invisible
VO: "El conocimiento duerme en carpetas que nadie consulta. Los mismos cálculos se
rehacen a mano una y otra vez. Lo que aprende uno, se queda en uno. Y nadie sabe
cuánto tiempo se va en cada entrega."
Visual: carpetas apiladas en gris; dos personas rehaciendo el mismo documento en
paralelo; un contador de horas que nadie mira. Estados `[ SIN REGISTRO ]`.

### B3 — Aparece VELARIA
VO: "Velaria convierte ese uso individual en un sistema de trabajo: gobernado,
compartido y medido."
Visual: el wordmark `velaria_` sobre ink; las ventanas dispersas se alinean en una
grilla ordenada; el `_` pestañea. Aparece el ojo del velarium.

### B4 — Frente 1: Gobernanza
VO: "Primero, gobernanza: la política de la empresa se carga en la herramienta y se
cumple en automático. Cada sesión queda registrada: quién hizo qué y bajo qué criterio."
Visual: un documento "política" que se inserta en la herramienta; líneas de log
apareciendo con timestamps y `[ OK ]`.

### B5 — Frente 2: Habilitación
VO: "Segundo, habilitación: lo que descubre una persona se vuelve pieza del equipo —
plantillas, cálculos validados, integraciones — y la mejora de uno le llega al resto."
Visual: una pieza (bloque) sale del escritorio de un ingeniero y se replica al resto
del equipo vía un marketplace/estante común.

### B6 — Frente 3: Productividad medida
VO: "Y tercero, productividad: medida como resultado del negocio, siempre contra la
línea base. No es una sensación: es un número."
Visual: dashboard estilo consola con barras y métricas subiendo contra una línea
base marcada. Labels mono: `RESULTADO · CONTRA LÍNEA BASE`.

### B7 — La persona al mando (human in the loop)
VO: "La IA prepara el trabajo pesado. La decisión, siempre, es de tu equipo. Nada
sale sin el visto bueno de una persona."
Visual: un flujo se detiene en un nodo `[ REVISIÓN ]`; una persona aprueba con `❯`;
el flujo continúa.

### B8 — Cierre / CTA
VO: "Un piloto corto, con diagnóstico primero y un número sobre la mesa antes de
decidir. Velaria. Libera el poder de la IA. Guíala con tu visión."
Visual: portada sobre ink: `velaria_` + tagline; label `❯ PONERLE FECHA AL DIAGNÓSTICO`.

## Fuente del mensaje (trazabilidad)

- "HOY / CON VELARIA": sección "Qué logra Velaria" de la propuesta Abastibletec.
- Tres frentes (Gobernanza / Habilitación / Productividad): sección "La capa".
- Human in the loop: sección "El punto delicado".
- Diagnóstico gratis con número al día 14: "El objetivo del piloto" y "Próximo paso".
- Estética: `marca/sistema-visual.md` + tokens `velaria-colores.css` del repo
  velaria-delivery.
