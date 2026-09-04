# Generaciones — Velaria General

## Corte v1 — 26/08/2026

**3:05 · 1920×1080 · H.264 + AAC · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/d8c3fecb-2358-43b0-ab2f-21b628eff974.mp4

Nueve láminas. El guion apuntaba a 3:22 estimando 140 palabras por minuto; la locución medida
da 170,1 s de voz y 15,1 s de aire repartido, o sea 3:05.

| # | Lámina | Voz | Ventana |
|---|---|---|---|
| 1 | Qué hace Velaria | 28,5 s | 30,1 s |
| 2 | ¿Cómo funciona? · los cinco pasos | 6,6 s | 8,0 s |
| 3 | Paso 1 · Tu equipo ya usa IA | 28,8 s | 30,4 s |
| 4 | Paso 1 · El mismo problema | 21,1 s | 22,7 s |
| 5 | Paso 2 · Las piezas | 26,9 s | 28,7 s |
| 6 | Paso 3 · El conocimiento sube y vuelve | 22,3 s | 23,9 s |
| 7 | Paso 4 · La base se arma sola | 14,4 s | 15,9 s |
| 8 | Paso 5 · Se reparte y se dirige | 17,4 s | 19,2 s |
| 9 | Cierre | 4,2 s | 6,5 s |

## Locución

Voz Isabella con `text2speech_v2` variante `minimax`, la misma de los cortes de SQM. Texto
**textual del guion**, salvo la fusión de las escenas 3 y 4, que obligó a reescribir esas dos
pistas.

Las nueve pistas se transcribieron con `faster-whisper` y `word_timestamps` antes de montar.
De ahí salen los `data-in` de cada elemento y también la detección de colas alucinadas: la
pista del paso 4 terminaba en «Argen. Eso.» a los 14,56 s. Se corta en 14,4 s con fade.

## Error corregido en el camino

Las dos primeras láminas salieron sin doctype ni hoja de estilo —texto negro sobre blanco, sin
tipografía—. La causa: en el bloque que las escribía, un `cd` a un directorio inexistente
cortó por `&&` la asignación de la variable que llevaba el `<head>`, así que se expandió vacía.
Se detectó capturando frames antes de renderizar el corte completo, no después.

## Pendiente

- **Tomas reales de oficina.** El guion trae un `Prompt visual` fotográfico por escena —gente
  trabajando, luz de mañana, cámara quieta— y no están generadas. El corte de hoy es solo
  gráfico. Van como planos de respiro entre láminas, no como fondo con texto encima: el sistema
  prohíbe que algo flote.
- **Música.** Cama sobria y baja. El guion prohíbe explícitamente la música épica que sube.


## Corte v2 — 26/08/2026

**2:57 · diez láminas · con música**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/941ceeee-c056-45e5-a747-01802bc60783.mp4

| Cambio | Detalle |
|---|---|
| El ejemplo se anuncia | Lámina nueva antes de las piezas: **«Veamos un ejemplo: un equipo que hace cotizaciones.»** El guion original decía que la cotización es el hilo desde la escena 5, pero nunca lo declaraba: entraba de contrabando dentro de la explicación de las piezas |
| Sin «acá» | Tres frases lo tenían: «cómo se hacen las cosas acá» → «la forma en que se hacen las cosas» · «cómo se cotiza acá» → «cómo se cotiza» · «Y acá está lo importante» → «Y esto es lo importante» |
| Música | Las mismas cuatro piezas electrónicas del corte de SQM, una por bloque, encadenadas entre sí y a nivel fijo −17 dB sin ducking |
| El cierre | Suma la bajada de la web —«Guíala con tu visión.»— y se corta antes de la palabra «Velaria» suelta |

### La voz rara del final

No era acento: era **cola alucinada del TTS**. La pista del cierre dura 12,5 s pero la
locución real termina a los 5,1 s; los 7,4 s siguientes son balbuceo que el modelo inventa
después del texto. Es el mismo modo de falla que ya había aparecido dos veces en este proyecto,
y suena a idioma extranjero porque literalmente no es español: es fonética sin lengua.

El corte se hace **antes** de la palabra «Velaria» aislada, no después. Una marca suelta al
final de una frase es donde más drifta la prosodia del modelo, y en pantalla el wordmark ya
está: decirlo no aportaba nada y era el único punto de riesgo.

**Regla que queda para este proyecto:** ninguna pista se monta sin transcribirla antes. Las
colas no aparecen en la duración esperada ni en el prompt — solo en el transcript.

## Corte v3 — 31/08/2026

**3:25 · 1920×1080 · H.264 + AAC · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/4f29ceb3-81f9-4c9b-bb3f-cc14e9971a7a.mp4

Once láminas. Video 204,72 s · voz 204,67 s · cama 204,67 s.

| # | Lámina | Ventana | Toma · corte |
|---|---|---|---|
| 1 | `m-01` Qué hace Velaria | 37,75 s | A 0,00–37,35 |
| 2 | `m-02` Cómo funciona · los cinco pasos | 6,50 s | A 37,35–43,45 |
| 3 | `m-03` Paso 1 · Tu equipo ya usa una herramienta de IA | 29,00 s | B 0,00–28,60 |
| 4 | `m-04` Paso 1 · Ahora entra Velaria | 19,05 s | B 28,60–47,25 |
| 5 | `m-04b` Paso 2 de 5 | 7,40 s | B 47,25–54,25 |
| 6 | `m-05` Paso 2 · Las cuatro piezas clave | 27,95 s | C 0,00–27,55 |
| 7 | `m-06` Paso 3 · Todo queda registrado | 22,64 s | C 27,55–49,79 |
| 8 | `m-07` Paso 4 · La base de conocimiento | 17,35 s | D 0,00–16,95 |
| 9 | `m-08` Paso 5 · El conocimiento se reparte | 20,20 s | D 17,05–18,60 + 19,85–38,10 |
| 10 | `m-08b` Una empresa no captura valor… | 10,25 s | D 38,10–47,95 |
| 11 | `m-09` Placa de marca | 6,58 s | D 47,95–53,53 |

La escena 9 se arma con **dos tramos**: la toma D traía un «Es.» suelto entre medio y se saca
recortando el hueco. `cortes-voz.json` pasó a formato multi-tramo `[toma, [[ini,fin], …]]` para
poder hacerlo sin regenerar la toma.

### Los cambios de la v3

| | |
|---|---|
| Portada | **QUÉ HACE VELARIA** más grande, en azul de marca, versalitas |
| Portada | «toma estos procesos y los **trabaja con IA**» |
| Eje 1 | Redacción de Habilitación alineada con la web |
| Cómo funciona | La locución **lee «Velaria»** en la frase |
| Pasos | **PASO N°1** más grande y leído en voz alta; mismo trato para el Paso 2 de 5 |
| Paso 1 | «Tu equipo **ya está usando** alguna herramienta de IA» |
| Piel | Fondo `#EDF1F7`, tarjetas con borde `#D7DEE8`, banda de paso sobre tinta: menos blanco, más contraste |
| Paso 1 | Se escribe y se lee **«ahora entra Velaria»**, con ejemplo concreto. Fuera «Todo lo que viene…» |
| Paso 2 | «Velaria incluye **4 piezas clave** que se escriben una sola vez» |
| Paso 2 | Fuera el texto gris repetido bajo cada tarjeta; los textos de abajo quedan destacados |
| Paso 3 | «Todo lo que hace cada persona **queda registrado**» |
| Paso 4 | «Con eso se comienza a crear algo fundamental: **la base de conocimiento de la empresa**». Fuera «se arma sola» |
| Paso 4 | «ya resolvió **otro colega**» |
| Paso 5 | **PROPUESTA DE SKILL** en ámbar, a la derecha |
| Paso 5 | «Y luego **el conocimiento se reparte**» |
| Paso 5 | «Quien dirige cada proyecto decide qué se activa, qué se automatiza, y mira el resultado en un **tablero de control**» |
| Cierre | Nueva lámina `m-08b`: «Una empresa no captura valor…», la del corte de SQM |
| Locución | Cuatro tomas continuas: sin alucinaciones, sin cambios de idioma, sin cambios de tempo |
| Música | Cuatro pistas intercaladas —sobria · tensa · brillante · resuelta— encadenadas con `acrossfade` |

## Corte v4 — 01/09/2026

**3:16 · 1920×1080 · H.264 + AAC · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/929a106d-d3be-484e-b4b6-82fbd2a84826.mp4

Doce escenas: la intro de marca más las once del corte v3. Video 196,12 s · voz 195,99 s ·
cama 195,99 s. Sin avisos de corte.

| | |
|---|---|
| Intro | `intro.html`, 2,4 s sin voz, la misma que abre el corte de SQM (descrita en su `generaciones.md`) |
| Portada | Fuera «Qué hace Velaria»: queda **el símbolo y VELARIA**, nada más |
| PROCESO | Las etiquetas de la derecha pasan a chip azul de marca sobre `#DDE6F8`, con borde |
| PASOS → **ETAPAS** | En las once láminas y en la locución: «En cinco etapas», «ETAPA N°1», «Por eso la etapa 2» |
| Propuesta de Skill | Deja de ser una etiqueta al margen: bloque `.skillbox` ámbar con borde izquierdo de 10 px, **PROPUESTA DE NUEVO SKILL** a 34 px y el nombre de la Skill al lado. La voz lo dice |
| Velocidad | `atempo=1.08` sobre cada toma |
| Cadencia | Las pausas acotadas a 0,20–0,40 s con el mismo `ritmo.json` de SQM |
| Cues | Los 60 `data-in` del corte recalculados uno por uno sobre los `word_timestamps` de las tomas ya aceleradas y normalizadas |

### Los ruidos después de «cómo estaba antes»

Eran reales y estaban en la toma: 3,2 segundos entre 20,3 y 23,6 con media de −24 dB pero
**picos a −2 dB**. No era una pausa, era un artefacto del modelo. La toma regenerada no lo trae.

### Cinco tomas, no cuatro

La toma D salió con «Etapa número cinco» repetido tres veces y **cuarenta segundos de balbuceo**
en medio. Se partió en dos: D llega hasta el tablero de control y E toma el cierre. Menos texto
por generación, menos superficie para que el modelo se descarrile. Las dos salieron limpias.

| Toma | Escenas | Job |
|---|---|---|
| A | 2–3 | `4bca9323-3906-443d-800e-8b54a03ba989` |
| B | 4–6 | `3a9106d6-a91b-4b8d-8c2a-9ad45659c07c` |
| C | 7–8 | `ec2d957c-1494-4913-a24f-ef2f363f1489` |
| D | 9–10 | `65586801-8ac0-43dc-8d40-eaf08ac169b0` |
| E | 11–12 | `defa80a2-5bfa-45e6-9175-bf7724ec7929` |

Verificación de audio: `mean_volume` por cuartos en las once pistas con voz, todo entre −14 y
−21 dB; ninguna cae a silencio.

## Corte v5 — 01/09/2026

**3:16 · 1920×1080 · H.264 + AAC · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/8e44a192-4cbc-472a-9845-fd7ae7710b30.mp4

Solo composición: la narración, los cortes y los cues son los mismos del v4.

### El pie que se perdía

Se auditaron las once láminas por medición —contraste calculado de cada texto contra el fondo
efectivo, y posición de cada caja contra el borde de cuadro— en vez de mirarlas. Dos hallazgos:

**`m-01` empujaba el pie fuera del video.** El pie terminaba en 1096 px sobre un cuadro de 1080:
la línea «Tres frentes» estaba literalmente cortada. La causa es que `.stage` es `flex:1` y, al
no caber, crecía y desplazaba el pie. Se le puso `min-height:0` y se recuperó altura donde no
cuesta lectura: `.row` de 18 a 13 px de padding, `.card` de 26/28 a 22/26, el cuerpo de tarjeta
de 29 a 28 px, el interlineado de `.t2` de 1,28 a 1,24. Ahora **las once láminas cierran el pie
en 977–1025**, la misma posición en todas.

**Seis textos por debajo del mínimo de contraste.** Todos eran `--steel` (#8A94A6), que funciona
sobre tinta pero no sobre el fondo claro:

| | antes | ahora |
|---|---|---|
| Pie de lámina, las once | 2,70:1 | **5,4:1** |
| «Algunos · por su cuenta» y el otro encabezado de columna | 3,06:1 | **4,9:1** |
| Los números 01–04 de la cadena de la etapa 4 | 3,06:1 | **4,9:1** |
| «EQUIPO» en las seis fichas de la etapa 5 | 3,06:1 | **4,9:1** |
| Los separadores `·` de la cadena de etapas | 3,08:1 | **6,3:1** |

Se agregó `--mute2: #55606F` para eso: el steel de marca se reserva para las láminas oscuras.

### Los otros dos cambios

| | |
|---|---|
| «1 de 5» | El «DE 5» estaba en gris a 22 px y desterrado al margen derecho con `margin-left:auto`. Ahora va **pegado al número, a 38 px y en `--accent-hi`**: la banda se lee «ETAPA N°1 DE 5» como una sola unidad |
| Barras de la cabecera | Fuera. El contador de cinco barras arriba a la derecha decía lo mismo que la banda de etapa, y dos indicadores del mismo dato compiten entre sí |

## Corte final — 04/09/2026

**3:15.2 · 1920×1080 · H.264 + AAC · sin subtítulos**

https://d2ol7oe51mr4n9.cloudfront.net/user_3GZDp50cX9i6ZJdtP9xYJIH5Moh/339ccaa0-9bf0-4d99-803f-2fb9534071b1.mp4

Doce escenas. Video 195,20 s · voz 195,16 s. Sin avisos de corte.

### El escaneo

Antes de renderizar se pasaron las dos animaciones por todos los modos de falla que
aparecieron en el proyecto. Medido, no mirado.

| Qué se buscó | Cómo | Resultado |
|---|---|---|
| Texto cortado o fuera de cuadro | Caja real de cada **nodo de texto** con `Range`, en tres momentos de cada lámina | Ninguno en los 27 planos |
| Contraste ilegible | Luminancia relativa de cada texto contra su fondo efectivo | Todo sobre 4,5:1 |
| Alucinaciones de voz | Transcripción completa con `faster-whisper`, más detector de repeticiones, balbuceo y cola larga | Ninguna. Colas de 0,18 a 0,52 s |
| Voces apuradas | Caracteres hablados por segundo de cada frase contra la mediana de su toma | Corregidas, ver abajo |
| Cortes de audio extraños | Nivel medido en una ventana de 120 ms alrededor de **cada frontera de escena** | Todas en silencio, −51 a −68 dB |
| Escenas mudas | `mean_volume` por cuartos en cada pista de escena | Ninguna |

La banda de etapa de General aparece como «fuera de cuadro» en la auditoría de cajas:
es un falso positivo. Es una banda a sangre con `margin: 0 -90px` que el `overflow:hidden`
recorta por diseño; su texto está a 90 px del borde.

### Las frases apuradas

El detector encontró frases corriendo entre un 12 % y un 26 % sobre la mediana de su
toma. Se frenan con una restricción dura: **la duración de salida de cada escena queda
idéntica**, y lo que se gana frenando se paga comprimiendo las pausas de esa misma
escena. Así el corte, el plan y los cues siguen siendo válidos sin re-derivar nada.

Cuando el presupuesto de pausas de una escena no alcanza, el freno se recorta a lo que
la escena puede pagar en vez de estirarla. Es la razón de que algunas frases queden
frenadas a la mitad de lo ideal: se prefirió no mover ni un cue.

La partición sale de las **frases de whisper**, no de `silencedetect`. Ese fue el error
del primer intento —sus tramos parten frases por la mitad y el ritmo medido sobre un
fragmento no significa nada— y por eso aquella pasada empeoraba la dispersión en vez de
mejorarla. Cada límite cae en el punto medio del silencio entre frase y frase.

### Las fronteras que no estaban en silencio

En General, los cortes de escena 7|8 y 11|12 caían sobre la cola de la palabra anterior,
a −22,7 y −25,7 dB. Eran cortes audibles. Se movieron al silencio real: 26,79 → 27,06 y
8,35 → 8,50. Después del re-cálculo del ritmo, un barrido automático reubicó ocho
fronteras más —de las dos animaciones— al punto de silencio más cercano.

### La música

Cuatro pistas de librería que trajo el cliente. Llegaron cinco archivos, pero
`Audio_3` y `Audio_5` son idénticos (mismo MD5), así que son cuatro piezas.

| Bloque | Pista | BPM | Pulso | Por qué ahí |
|---|---|---|---|---|
| 1 · planteo | m3 | 90 | 0,8 dB | La más plana; no compite con el planteo |
| 2 · la fricción | m1 | 100 | 2,7 dB | Sube la tensión donde se muestra el problema |
| 3 · el giro | m2 | 121 | **16,0 dB** | El pulso más marcado, justo cuando entra Velaria |
| 4 · cierre | m4 | 102 | 2,6 dB | La más abierta arriba; aguanta la placa de marca |

Cada pieza se encadena consigo misma con `acrossfade` de 2 s hasta cubrir su bloque; el
número de repeticiones sale de la duración real de cada pista, que va de 30 s a 2:34.
Antes de la mezcla se les abre el carril a la voz: −2 dB en 900 Hz y −3 dB en 2200 Hz,
más un corte bajo los 38 Hz. Nivel fijo a −17 dB, sin ducking.

**Nota sobre los 124 BPM que había propuesto:** no se aplicó. Las pistas están entre 90 y
121 BPM y llevarlas a 124 exigía estirar hasta un 38 %, que destruye el material. Se
respetó el tempo natural de cada una.
