# Guion v1 — Animación VELARIA para Abastible

> **BORRADOR CON SUPUESTOS.** Escrito antes de leer el repo VELARIA y las propuestas
> (Abastible/SQM), que aún no son accesibles. Todo lo marcado `[SUPUESTO]` o
> `[PLACEHOLDER]` debe validarse contra esos documentos antes de generar el video.

## Premisa

Audiencia: ejecutivos de Abastible. Perfil: usan IA de forma superficial (un chat de
vez en cuando) o cada persona por su cuenta, sin colaboración ni método. El video debe
hacer visible el costo de ese "antes" y el valor concreto del "después" con VELARIA.

Duración objetivo: 60–90s → 6–9 bloques de 10s (workflow Explainer, modo Animated).
Formato: 16:9. VO: español, tono cercano y directo (2ª persona), sin jerga técnica.
Estilo visual: Editorial Motion Graphics (adaptar paleta/tipografía al brand VELARIA
cuando tengamos las propuestas).

## Estructura (arco antes → quiebre → después)

### Bloque 1 — Hook (el "antes" reconocible)
VO: "En tu empresa ya usan inteligencia artificial. Pero cada uno por su lado."
Visual: oficina estilizada; varias personas, cada una con su propia burbuja de chat
IA flotando, desconectadas entre sí. Las burbujas no se tocan.

### Bloque 2 — El problema
VO: "Respuestas que se pierden, esfuerzos duplicados, y resultados que dependen de
quién pregunta. Así, la IA no mueve los números del negocio."
Visual: las burbujas se duplican, chocan, se desvanecen; un indicador/gráfico que no
sube. Sensación de ruido y fricción.

### Bloque 3 — El quiebre: aparece VELARIA
VO: "VELARIA convierte ese uso individual en una forma de trabajar. [SUPUESTO:
definición exacta del servicio — validar contra propuesta]"
Visual: logo/marca VELARIA ordena el caos: las burbujas dispersas se alinean en un
flujo común.

### Bloques 4–5 — La metodología (cómo funciona)
[PLACEHOLDER: pasos reales de la metodología VELARIA — sacar de repo/propuesta.
Hipótesis de trabajo: diagnóstico → diseño de flujos con IA por equipo →
implementación/acompañamiento → medición.]
VO (borrador): "Primero entendemos cómo trabaja tu equipo. Después diseñamos, junto a
ustedes, flujos donde la IA colabora con todos — no con cada uno por separado. Y
acompañamos hasta que sea parte del día a día."
Visual: 3–4 pasos como composición de motion graphics: mapa del equipo → flujo
compartido conectando personas + IA → métricas subiendo.

### Bloque 6 — El "después"
VO: "El resultado: un equipo que trabaja con la IA, no al lado de ella. Conocimiento
que queda en la empresa, y resultados que se pueden medir."
Visual: mismo equipo del bloque 1, ahora conectado a un solo sistema; el gráfico del
bloque 2 ahora sube.

### Bloque 7 — Cierre / CTA
VO: "VELARIA. [PLACEHOLDER: tagline real]. Conversemos."
Visual: logo VELARIA + [SUPUESTO: mención/guiño a Abastible, p.ej. paleta o texto
"para Abastible"] + contacto.

## Notas de producción (Higgsfield)

- Workflow: `faceless-channel-video` / tipo Explainer / motion_mode: animated.
- Estilo: preset "Editorial Motion Graphics" del catálogo (elegir en la galería de
  presets al iniciar la corrida real; ajustar con referencias de marca si las hay).
- Voz: elegir en el voice picker del workflow — español, masculina o femenina cálida
  y profesional. Pendiente preferencia de Sebastián.
- Subtítulos: sí (se ve mucho en mudo en contextos corporativos). Pendiente confirmar.
- El pipeline entrega UN archivo final con VO, música y upscale Topaz incluido.
