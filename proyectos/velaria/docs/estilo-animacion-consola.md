# Estilo de animación — consola Velaria

> Reemplaza al estilo "pizarra y plumón" para los videos nuevos. Sale de
> `marca/sistema-visual.md` del repo velaria-delivery, no de una interpretación.
> Fecha: 2026-08-21.

## Las seis reglas

| Regla | Qué dice |
|---|---|
| **TÉCNICA** | Motion graphics editorial sobre fondo oscuro. Superficies planas y mate, sin volumen ni textura. Nada dibujado a mano, nada fotorrealista, nada 3D. |
| **COLOR** | `#0B0F17` de fondo, `#151C2B` para los planos que se levantan, acero `#8A94A6` para lo secundario y los metadatos, y **un solo cobalto `#2456D6` por toma**, en el elemento que importa. |
| **CÁMARA** | Fija. El movimiento lo ponen los elementos entrando, alineándose y encajando — nunca la cámara. |
| **GEOMETRÍA** | Esquinas rectas (radio 0–2px). Hairlines finísimos como única jerarquía. Iconos de stroke 1.5 con remates cuadrados. **Nada flota**: sin sombras, sin glow, sin reflejos. |
| **TEXTO** | Todo el texto va en post-producción con IBM Plex real. A la generación **no se le pide texto**: se le piden campos y bloques vacíos donde después se sobreimprime. |
| **SÍMBOLO** | El ojo del velarium sale del SVG real (`marca/velaria-kit/simbolo/`), nunca generado: anillo fino, arco cobalto, punto central. |

Paleta: `#0B0F17` ink · `#151C2B` ink2 · `#8A94A6` acero · `#2456D6` cobalto · `#7DA0F2` cobalto claro sobre oscuro.
Tipografía (solo en post): IBM Plex Sans para cuerpo, IBM Plex Mono CAPS con letter-spacing 1.5–3px para labels, estados y timestamps.

## Prohibido (del sistema de marca, literal)

Degradados, glassmorphism, orbes y blobs, glow, esquinas redondas, emojis, cerebros,
chips, circuitos, redes neuronales, sombras blandas gigantes, píldoras de estado, y más
de un azul de acción por vista.

## Master prompt (generación)

```
Editorial motion-graphics style on a near-black background, flat matte surfaces,
slightly lighter dark panels separating planes, a single cobalt blue accent used on
only one element per shot, everything else in cool grey, thin hairline rules as the
only hierarchy, hard ninety-degree corners, precise technical diagram look, locked
static camera, 24fps. No glow, no gradients, no reflections, no soft shadows, no
rounded corners, no legible text.
```

## Negative prompt

```
glow, bloom, light rays, lens flare, gradients, glassmorphism, blurred orbs, blobs,
soft shadows, rounded corners, neon, reflections, brain, chip, circuit board, neural
network, hologram, purple, teal, multiple blue tones, photorealistic, 3D render,
legible text, letters, words, watermark, camera shake
```

## Las dos rutas de producción

Este estilo no se produce igual que el de pizarra. Hay que elegir.

### Ruta A · Generado en Higgsfield (mismo flujo que la v1–v3)

- **Sirve para:** tomas ambientales, escritorios, personas, planos generales.
- **No sirve para:** nada que dependa de texto, de la geometría exacta del símbolo o de
  la precisión de los hairlines.
- **El glow se va a colar igual.** El negative prompt lo reduce, no lo elimina. En
  escena oscura con acento azul el motor tiende a iluminar.
- **Todo el texto va sobreimpreso después**: labels, estados, timestamps y el wordmark.

### Ruta B · Construido con los assets reales y grabado en pantalla

- Se arma como página con IBM Plex de verdad, los hex exactos y el SVG real del símbolo,
  se anima por CSS y se graba con Chromium headless.
- **Queda exacto**, porque no se parece al sistema de marca: *es* el sistema de marca.
- Cero personas y cero escenas ambientales. Es puro diagrama, interfaz y tipografía.
- Es la ruta que el sistema de marca pide de verdad: todo lo que él define —radios,
  hairlines, estados, el `_` pestañeando— existe como CSS, no como descripción.

### Ruta C · Mezcla (recomendada si el guion tiene personas)

Ambientes y personas por la ruta A; interfaces, métricas, símbolo y todo el texto por la
ruta B, montados encima. Es más trabajo de montaje, pero es la única forma de tener a la
vez gente en pantalla y un estilo fiel a la marca.

## Recomendación

**Si el guion nuevo es de producto, proceso o datos → ruta B.** El estilo consola nació
para eso y queda impecable, sin pelear contra el generador.

**Si el guion tiene personas y oficina → ruta C.** La A sola va a entregar algo que se
parece a Velaria de lejos pero incumple la mitad de las reglas de arriba.

La decisión se toma cuando llegue el guion, no antes.
