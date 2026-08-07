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

---

# v2 — versión en inglés, vectorial isométrico

Rehecha a pedido: narración en inglés y objetos tecnológicos (ventanas de aplicación,
iconos de carpeta Mac y PC, racks, cursor) en vez de papeles y biblioratos.

- Ficha de producción: https://claude.ai/code/artifact/14e889e0-1da6-44f7-90ef-fdd8a86a333b
- Video HD 1920×1080: https://d8j0ntlcm91z4.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/hf_20260807_135848_a2ce1d5c-462b-477b-8f79-a6aba2d85f76.mp4
- Video liviano 1280×720: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/fbee7f78-911e-4b9f-a0dd-4f03ebc40124.mp4

| | |
|---|---|
| Estilo | Isometric Flat Vector, acento azul cobalto |
| Hilo conductor | Icono de carpeta azul cobalto (reemplaza a la libreta de papel) |
| Narración | Inglés, voz preset **Bram** `549ff70a-3ee7-4f04-a4d9-89a24fab7709` (`preset`) |
| Subtítulos | Quemados, look `clean`, en inglés |

## Bitácora v2

- **Logos de marcas reales: no se pueden.** El generador rechaza marcas en las
  instrucciones y el texto dibujado sale ilegible; aparte es un problema de licencia en una
  pieza comercial. Las herramientas se representan por forma: barra verde + grilla de celdas
  = planilla, barra naranja + gráfico de barras = presentación, barra azul + líneas =
  documento. Carpeta con pestaña redondeada = Mac, carpeta manila = PC.
- **Cambiar solo los objetos no bastaba**: la pizarra y plumón es analógica por naturaleza.
  El isométrico hace que ventanas, racks e iconos se vean nativos.
- **Bram lee a 3,00 palabras/seg**, justo en el centro del rango calibrado. La banda nominal
  de 27–32 palabras le sirve sin ajustes, a diferencia del clon chileno (3,5).
- **El ensamblador exige 8,6–10,0 s de habla por bloque**, un piso más estricto que el
  `rate=ok` de `speech_metrics.sh`. B2 (8,445 s) y B3 (8,562 s) pasaban la métrica de ritmo
  pero rebotaron en el ensamblado. Se arreglan **agregando contenido real**, nunca estirando
  el audio. Conviene apuntar a 27–28 palabras y verificar antes de lanzar el render, que
  toma ~3 minutos y falla entero por una sola toma corta.
- **Declinar el preset de antemano funciona**: pasar `declined_preset_id` en el primer envío
  de `generate_video_batch` evita la vuelta completa de rechazo y reenvío.
