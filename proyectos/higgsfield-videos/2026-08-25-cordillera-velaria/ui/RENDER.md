# Render de las pantallas a video

Las 13 pantallas HTML están animadas y encodeadas a MP4 1920×1080 / 25fps / H.264.
**Sin créditos de Higgsfield y sin software de edición.**

```bash
node render.js               # todas
node render.js 07-patron     # una sola
```

Salida en `clips/`. `clips/_reel-pantallas.mp4` es el concatenado de las 13 (2:02).

## Cómo funciona la animación

`anim.js` **no usa el reloj real**. Expone `scrub(t, duracion)`: se le pide un instante y pinta
ese frame. El render pide t = 0, 1/25, 2/25… y captura cada uno. Consecuencias:

- El resultado es **reproducible frame a frame** — dos renders dan archivos idénticos.
- No hay riesgo de frames saltados por lentitud de la máquina.
- La duración de cada clip se fija desde `montaje.md`, no desde la animación.

El movimiento respeta el sistema: entradas lineales (opacidad + 10px de desplazamiento, sin
easing elástico) y una deriva de escala del 1,2% a lo largo del clip. En `07-patron` las ocho
líneas del patrón entran además desplazadas 70px y calzan en su posición.

## Dos obstáculos del entorno, resueltos

1. **El ffmpeg de Playwright** (`/opt/pw-browsers/ffmpeg-1011/`) es un build reducido: solo
   VP8/WebM y **sin ningún decodificador de PNG**, así que no puede leer una secuencia de
   frames. Se instala el completo desde npm: `@ffmpeg-installer/ffmpeg` (trae libx264).
2. **`document.fonts.ready`** devuelve un `FontFaceSet`, que Playwright no puede serializar
   como valor de retorno. Hay que envolverlo: `async () => { await document.fonts.ready; return true }`.
   Sin eso, el render corre antes de que carguen las IBM Plex y las capturas salen con la
   tipografía de fallback.

## Reparto de duración

Cada pantalla ocupa su ventana según `montaje.md`. Donde una escena tiene dos pantallas, se
reparten la locución por mitades.
