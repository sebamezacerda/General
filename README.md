# HIGGSFIELD — Proyectos de video

Repositorio para organizar los proyectos de video generados con Higgsfield, uno por carpeta.

## Estructura

```
proyectos/
  _plantilla/           <- copiar esta carpeta para arrancar un proyecto nuevo
    notas.md
    prompts.md
    referencias/
    exports/
  2026-08-01-video-area/
    notas.md             <- brief, objetivo, contexto del video
    prompts.md           <- prompts usados en Higgsfield (para reusar/iterar)
    referencias/         <- imágenes/videos de referencia subidos a Higgsfield
    exports/             <- videos finales descargados (ver nota sobre tamaño abajo)
```

## Cómo arrancar un proyecto nuevo

1. Copiar `proyectos/_plantilla` a `proyectos/AAAA-MM-DD-nombre-del-video`.
2. Abrir una terminal **en esa carpeta** y correr `claude`. Cada carpeta mantiene su propio historial de conversación, separado de los demás proyectos.
3. Trabajar la generación del video con las herramientas de Higgsfield desde ahí. Guardar prompts y notas relevantes en los `.md` de esa carpeta.

## Nota sobre archivos de video

Git no está pensado para versionar binarios grandes (videos pesan mucho). `exports/` está en `.gitignore` por defecto: los videos finales quedan en tu disco, no se suben al repo. Si igual querés versionarlos, hay que usar Git LFS — avisar si se necesita.
