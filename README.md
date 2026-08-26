# Índice global de proyectos

Repo global de Sebastián: specs, resúmenes y decisiones de sus proyectos con IA, para tener contexto cruzado entre terminal y web.

## Proyectos

- **Bidasoa** (terminal) — `proyectos/bidasoa/spec.md`
- **Casa Sanz** (terminal) — `proyectos/casa-sanz/spec.md`
- **VELARIA** (colaboración, invitado) — `proyectos/velaria/spec.md`. Repo real: `Velaria-HQ/velaria-delivery` (no accesible desde sesiones de este repo). Incluye el **sistema de diseño** completo, que rige todo diseño nuevo de Velaria.
- **Higgsfield — videos** (web) — `proyectos/higgsfield-videos/`. Los videos generados acá pueden ser para Bidasoa, para Casa Sanz, o generales — cada proyecto de video lo indica en su `notas.md`.
- **Velaria General** (video, web) — `proyectos/higgsfield-videos/2026-08-26-velaria-general/`.
  Genérico, sin caso de cliente: los cinco pasos de cómo funciona Velaria. 3:05, piel clara.
- **Caso sintético Minera Cordillera × Velaria** (video, web) — `proyectos/higgsfield-videos/2026-08-25-cordillera-velaria/`. Guion en `guion.md`, video de 3:41 con subtítulos.
- **Caso sintético SQM × Velaria** (video, web) — `proyectos/higgsfield-videos/2026-08-22-sqm-animacion/`. Guion cerrado en `guion.md`, prompts por escena en `prompts.md`.

## Cómo se relacionan

- Bidasoa y Casa Sanz son negocios que se trabajan en la terminal (Claude Code local), con acceso a archivos locales, scraping, etc.
- Higgsfield es un servicio en la nube para generar/editar video, orquestado acá en Claude Code web (más visual). No necesita acceso a archivos locales.
- Este repo es el punto de encuentro: cada proyecto (terminal o web) deja acá su resumen/spec, así cualquier sesión futura puede leer el contexto de los demás.

## Estructura

```
proyectos/
  bidasoa/
    spec.md
  casa-sanz/
    spec.md
  velaria/
    spec.md
  higgsfield-videos/
    _plantilla/           <- copiar para arrancar un video nuevo
      notas.md             <- para qué negocio es, objetivo, bitácora
      prompts.md            <- prompts usados (para reusar/iterar)
      referencias/
      exports/
    2026-08-01-nombre-del-video/
      ...
```

## Cómo arrancar un proyecto de video nuevo

1. Copiar `proyectos/higgsfield-videos/_plantilla` a `proyectos/higgsfield-videos/AAAA-MM-DD-nombre-del-video`.
2. Completar `notas.md`, indicando para qué negocio es (o "general").
3. Trabajar la generación en una sesión de Claude Code web, con Higgsfield conectado por MCP.

## Nota sobre archivos de video

Git no está pensado para versionar binarios grandes. `exports/` está en `.gitignore`: los videos finales quedan en tu disco, no se suben al repo.
