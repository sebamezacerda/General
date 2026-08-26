# Velaria General — video del mecanismo

Genérico, sin caso de cliente: los cinco pasos de cómo funciona Velaria. El guion original
está en `guion.md` tal como llegó, con la locución ya escrita — se usa textual.

## Un cambio sobre el guion original

**Las escenas 3 y 4 se fusionan en un solo paso.** Eran la misma situación contada en dos
tiempos: gente usando IA por su cuenta y gente usándola con licencias de la empresa. Son dos
variantes de lo mismo — dónde está tu equipo hoy — y el problema que las cierra es el mismo:
la IA no sabe nada de tu empresa.

La fusión además cierra una cuenta que el guion no cerraba. La escena 2 promete **cinco pasos**;
con 3 y 4 separadas quedaban seis bloques y ningún paso numerado. Ahora son exactos:

| Paso | Escena |
|---|---|
| 1 | Tu equipo ya está usando IA (por su cuenta · con licencias) |
| 2 | Las piezas |
| 3 | El conocimiento sube y vuelve |
| 4 | La base se arma sola |
| 5 | Se reparte y la empresa lo dirige |

Y permite el contador `PASO n DE 5` fijo en el encabezado, que es lo que hace legible un
paso a paso.

## Arte: piel clara

A diferencia del video de SQM, este va sobre **light** (`#F5F7FA`, texto `#111827`, bordes
`#E5E7EB`), siguiendo la sección *Slides* del sistema: portada y cierre sobre ink, contenido
sobre light, tarjetas blancas con barra superior accent. La escena 2 (la consola con la
pregunta) y el cierre van sobre ink.

## Bitácora
- 2026-08-26: **corte v2** — 2:57. Se anuncia el ejemplo (un equipo que hace cotizaciones), se
  quita el «acá» de tres frases, entra la música electrónica por bloques y el cierre suma la
  bajada de la web. La voz rara del final era cola alucinada del TTS: se corta.

## Estado

- [x] Locución generada, transcrita y medida
- [x] Nueve láminas construidas
- [x] Montaje
- [ ] Tomas reales de oficina — el guion trae un `Prompt visual` fotográfico por escena y
      todavía no están generadas. Hoy el corte es solo gráfico.
- [ ] Música: cama sobria y baja (el guion prohíbe explícitamente música épica)

## Reglas del guion que hay que respetar

- Nada de cifras de productividad en pantalla: no hay ninguna medida todavía.
- Sistemas rotulados genéricos: documentos, planillas, sistemas internos. Ningún dato de
  cliente, ni inventado.
- Voz de alguien explicando en una reunión, no de locutor de comercial.
- Versión técnica aparte (Claude Code, CLAUDE.md, skills, hooks, MCP) — **no mezclar** con
  esta. Está descrita al final de `guion.md`.
