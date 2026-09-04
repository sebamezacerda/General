# Pipeline de re-ritmo y montaje

Tres etapas, cada una autocontenida, porque el sandbox de Higgsfield se
descarta a los ~10 segundos de terminar una llamada y no sobrevive entre
llamadas. Nada se puede dejar "a medias" ahi.

| Etapa | Donde corre | Que necesita | Que produce |
|---|---|---|---|
| **A** `etapa-a-ritmo.py` | sandbox (tiene `faster-whisper`) | `cfg.json`, `ritmo-viejo.json`, `cortes-viejos.json`, `plan-viejo.json`, `cues-viejos.json` | JSON por stdout: ritmo, cortes, plan, cues y la medicion |
| **render** `rend.js` | local (Chromium en `/opt/pw-browsers`) | el HTML ya parcheado con los VO y cues nuevos | los clips y el video mudo |
| **B** `etapa-b-montaje.py` | sandbox (tiene `ffmpeg`) | `cfg.json` con la URL del video mudo, `ritmo.json`, `cortes-voz.json`, `plan.json` | el corte final, subido |

El video mudo viaja de local al sandbox por Higgsfield: `media_upload` da una
URL firmada de S3, se sube con `curl -X PUT` y el sandbox la baja por
CloudFront. Es el unico camino: el proxy de salida local no llega a CloudFront
y el sandbox no llega al repo.

## Como se normaliza la velocidad de la voz

Se mide **silabas por segundo** de cada frase —grupos vocalicos, no
caracteres: «que» y «aeropuerto» tienen 3 y 10 letras pero 1 y 5 golpes— y se
compara contra la **mediana ponderada por duracion de todo el video**.

Eso ultimo es el punto. La correccion anterior media cada frase contra la
mediana de *su propia toma*, y una toma que corria rapida entera se quedaba
rapida: el espectador escucha el video como una sola pieza, no toma por toma.

- Dentro de ±8 % de la mediana no se toca nada. Esa variacion es prosodia.
- Fuera de la banda, la frase se lleva al borde de la banda, con tope en
  `atempo` de 0,80 a 1,25. Mas que eso suena procesado.
- Las pausas entre frases se acotan a 0,20–0,40 s aparte.

La particion sale de las **frases de whisper**, no de `silencedetect`: los
tramos de `silencedetect` cortan frases por la mitad y el ritmo medido sobre
medio enunciado no significa nada. Ese fue el error del primer intento, que
empeoraba la dispersion en vez de mejorarla.

## Como se re-derivan los cortes y los cues

Cambiar el ritmo mueve todos los tiempos, asi que hay que rehacer cortes,
ventanas del plan, `window.VO` y cada `data-in`. Se hace con un mapa exacto:

```
t (reloj viejo) --inversa del ritmo viejo--> s (fuente) --ritmo nuevo--> t'
```

Un cue es una fraccion de la locucion de su lamina, asi que el camino completo
es fraccion vieja -> tiempo absoluto en la toma -> mapa -> fraccion nueva.
Camina los tramos uno a uno porque una escena puede estar hecha de dos trozos
no contiguos de la misma toma (SQM v8-08).

Despues, cada frontera de escena se mueve al punto mas callado de su entorno
(±0,30 s). Un corte sobre la cola de una palabra se oye como un chasquido; en
silencio es invisible. El nivel se mide con una envolvente RMS calculada en
numpy sobre la pista entera: mil llamadas a `ffmpeg` para sondear niveles
tardan mas que decodificar el wav completo.

## Trampas ya pisadas

- **`atrim` + `asetpts` ANTES del fade.** Con `-ss`/`-to` de salida los filtros
  siguen viendo los timestamps del original y el fade de cierre se dispara
  antes de tiempo: asi es como se apagaba la voz a media escena en el v12.
- **Nada de `-v error` al medir con `volumedetect`.** Imprime en nivel info; con
  `-v error` el filtro corre pero no dice nada, el regex no encuentra el valor y
  la verificacion devuelve 0,0 dB para todo, es decir, no verifica nada.
- **`atempo` solo acepta factores entre 0,5 y 100.**
- **El render se reparte entre procesos con `xargs -P`,** pero cada proceso lee
  `rend.js` al arrancar: si se edita el archivo con procesos en vuelo, los
  viejos siguen con el codigo viejo.
