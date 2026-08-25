# Caso sintético: Minera Cordillera × Velaria

- Para qué negocio: **VELARIA** (colaboración). Sistema de diseño en `proyectos/velaria/spec.md`.
- Objetivo: explicar qué hace Velaria en una operación minera, con un caso mucho más concreto
  que el de SQM. Todo es ficticio pero diseñado para parecer una operación real.
- Formato: 16:9, con subtítulos quemados.
- Estado: en producción.

## Por qué este caso funciona mejor que el anterior

El caso SQM quedó genérico porque los números eran plausibles pero abstractos. Cordillera trae
dos activos narrativos que el anterior no tenía:

1. **Pedro.** Un planificador encuentra una forma de preguntar que le baja una tarea de 90 a 20
   minutos. Organizacionalmente no pasa nada: nadie más aprendió. Explica el problema en diez
   segundos y sin jerga.
2. **El cambio de política.** El criterio MNT-04 pasa de v3.2 a v3.3 y los diez usuarios más
   todas las Skills empiezan a usar la regla nueva. Es el argumento que separa «tenemos buenos
   prompts» de «tenemos una capacidad de empresa».

## Decisión sobre las 38 horas

Los números de ahorro (57 h → 19 h) van en el video, pero **no como promesa principal**. Un
ahorro de horas invita a la pregunta equivocada. La promesa es la frase de cierre.

## Bitácora
- 2026-08-25: se crea el proyecto y se escribe `guion.md`.
- 2026-08-25: **corte v1 entregado** — 3:41 · 1920×1080 · con subtítulos.
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/b8c3c75a-5945-45f1-9f23-4a479639135d.mp4

  12 escenas. Locución medida: 134s; el resto es aire de lectura, que en este video pesa más
  que en los anteriores porque las pantallas llevan tablas densas (el Excel de las 09:00, los
  criterios, el comparativo de política).

  Reutiliza entero el sistema del proyecto SQM: `anim.js` con scrub determinista, subtítulos
  calculados desde la duración real de cada pista, tipeo carácter por carácter en la escena 8,
  y montaje en el sandbox de Higgsfield. No hubo que escribir infraestructura nueva — solo
  pantallas.
