# Guía de estilo del video — de dónde salió y cómo se aplica

`estilo-video-velaria.html` es la guía que escribió un compañero del equipo (llegó por
WhatsApp el 2026-08-05). Es una página empaquetada: el contenido va comprimido dentro
del JavaScript, así que **para leerla hay que abrirla en un navegador**, no con un
editor de texto.

Define el estilo visual de la animación comercial para Abastibletec: 16:9, 60 segundos,
seis bloques de diez, pizarra y plumón con un solo acento cobalto. Trae el prompt maestro
y un prompt por bloque, listos para pegar en Higgsfield.

## Las seis reglas

| Regla | Qué dice |
|---|---|
| TÉCNICA | Pizarra blanca y plumón: trazo negro suelto y seguro, dibujo plano 2D que se va trazando solo en cámara. Nada de fotorealismo ni 3D. |
| COLOR | Blanco de pizarra, trazo negro, y UN solo acento: azul cobalto `#2456D6`. Reservado para la carpeta, el símbolo y lo que importa en cada toma. |
| CÁMARA | Fija o con paneos mínimos. El movimiento lo pone el dibujo apareciendo, no la cámara. |
| HERRAMIENTAS | Se muestran, no se nombran: planilla = grilla, presentación = slide, asistente de IA = ventana con burbujas. Cero texto en escena. |
| HILO CONDUCTOR | La carpeta azul: cerrada en el suelo (B1–B2), se activa con Velaria (B3), se llena (B4–B5), se sella (B6). Visible en las seis tomas. |
| SÍMBOLO | El ojo del velarium a mano, respetando la construcción real: anillo fino, arco cobalto, punto central. Solo en B3 y B6. |

Paleta: `#FFFFFF` pizarra · `#1A1A1A` trazo plumón · `#2456D6` cobalto.

Negative prompt oficial: `photorealistic, 3D render, gradients, extra colors, shading,
legible text, letters, words, watermark, camera shake, glow`.

## Contraste con lo producido (2026-08-05)

La guía **coincide con el guion que ya teníamos**: la narración de los seis bloques es
idéntica palabra por palabra. Lo que aporta es el orden del estilo visual.

Se cumplía ya: técnica, color y acento único, herramientas mostradas sin nombrar, cero
texto en escena, hilo conductor de la carpeta, símbolo solo en B3/B6 y en el orden
anillo → arco → punto, 1920×1080 a 24 fps en 16:9, narración aparte y subtítulos quemados.

Diferencias detectadas:

1. **Cámara.** La guía pide estática (solo el cenital del B1 se mueve). La v2 usaba
   *slow push-in* y *gentle drift* en tomas de detalle. → Corregido en la v3.
2. **Clips de 5+5 s y control de motion 0.5–0.7.** El motor de este flujo genera los
   10 s de una vez y no expone un control de motion. No es incumplimiento: la guía
   describe otra herramienta. Conviene actualizarla.
3. **Wordmark vectorial sobreimpreso 2 s en edición.** Sigue pendiente; requiere un
   editor de video, no se puede generar.

## Versiones

- **v2** (`c8efc430…` / 1080p `hf_20260805_153847_d5e67946…`): antes de la guía.
- **v3**: regenerada siguiendo la guía al pie — prompts textuales del compañero, cámara
  clavada, una sola imagen de referencia de estilo + carpeta + emblema. Reutiliza las
  mismas voces y la misma música (la narración no cambió).
