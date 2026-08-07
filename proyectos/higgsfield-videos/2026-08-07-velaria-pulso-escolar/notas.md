# VELARIA — Animación comercial, caso Pulso Escolar

- Para qué negocio: VELARIA (pieza comercial; Pulso Escolar aparece como cliente)
- Objetivo del video: mostrar el antes y el después de ordenar el uso de IA en un equipo
  de operaciones, cerrando con llamado a la acción de Velaria.
- Plataforma/formato: 16:9 YouTube / LinkedIn, 1920×1080, 24 fps, 60 s
- Referencias / inspiración: ficha de producción de la animación Abastibletec
  (https://claude.ai/code/artifact/60857888-2e43-4c0d-b291-58195e32792e).
  Formato de entrega en `proyectos/velaria/formato-ficha-produccion.md`.
- Estado: terminado

## Entregables

- Ficha de producción: https://claude.ai/code/artifact/0b04d466-35c9-44ff-8933-764372678b60
- Video HD 1920×1080: https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/hf_20260807_033920_cdb1acf9-0e62-4dd5-818b-da5d217eda6b.mp4
- Video liviano 1280×720: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/705e3cc3-2883-4db6-9485-f060787a2b02.mp4

## Ficha técnica

| | |
|---|---|
| Estilo | Whiteboard Doodle (pizarra y plumón), acento azul cobalto |
| Estructura | 6 bloques × 10 s · Gancho → El costo → El quiebre → Qué instala → El giro → Cierre |
| Hilo conductor | La libreta azul (cerrada en el suelo → abierta → gruesa → la abre alguien nuevo) |
| Narración | Voz Chilena Casa Sanz (clon propio), `voice_type: element` |
| Música | Instrumental electrónica generada a 60 s, agachada bajo la voz |
| Subtítulos | Quemados, look `clean`, en español |

## Bitácora

- 2026-08-07: producción completa en una sesión. Fuente: transcripción de cuatro notas de
  voz sobre el caso (~1.500 palabras), condensada a 6 líneas de narración.
  - La voz clonada lee a ~3,5 palabras/seg, más rápido que la calibración por defecto de
    27–32 palabras por bloque de 10 s. Las seis tomas iniciales salieron `rate=RUSHED`.
    Se recortaron las líneas a ~25 palabras y se regeneraron; quedaron 2,8–3,1 palabras/seg.
    **Para el próximo video con esta voz: escribir directo a 24–28 palabras por bloque.**
  - `finish_video.sh` no acepta `--music-vol` (ese flag es de `assemble_final.sh`).
  - El sandbox se recicla entre llamadas: el PUT a la URL presignada tiene que ir encadenado
    en el mismo comando que el `finish_video.sh`, o hay que rehacer el render.
  - El emblema de Velaria se dibujó a mano sin el vector original a la vista. Conviene
    revisarlo contra el archivo oficial antes de publicar.
