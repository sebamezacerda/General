# Guion v5 — Qué hace Velaria, explicado desde lo que la gente ya conoce

**Duración objetivo: ~3:15.** Diez escenas.

## La tesis del video

**Las empresas todavía no ven el valor de la IA bien aplicada.** No porque no la usen: la usan.
Pero la usan de a una persona por vez, como un asistente que responde preguntas sueltas. Ese es
un piso, no un techo. El video existe para mostrar el techo.

**Y el techo se mide en la última línea.** El video no puede terminar en «se ahorran horas»:
tiene que llegar a margen protegido, capital de trabajo liberado y costo evitado, con Finanzas
validándolo. Las horas son el mecanismo; la plata es el resultado. Un comité no aprueba
mecanismos.

## ⚠ Nota sobre la audiencia (contexto interno, NO contenido del video)

El nivel de referencia de la mayor parte de la audiencia es el uso individual de un asistente de
IA. Eso **condiciona cómo se explica**, pero **no se dice nunca en pantalla ni en la locución**:
decirle a un comité de SQM «ustedes solo conocen el chat» es condescendiente y además falso —
ahí hay gente que sabe mucho más.

Reglas que salen de esto:

- **No se nombran productos de terceros.** Ni ChatGPT ni Claude ni ninguno. Se dice «una IA».
- **No se describe cómo la gente usa la IA en su vida personal.** No viene al caso y baja el
  registro del video.
- **No se le dice al espectador lo que no entiende.** Se le muestra algo que sí entiende, y la
  diferencia habla sola.
- Todo concepto se explica por contraste con algo concreto y visible, nunca con una definición.

## El hilo conductor

**Una sola pregunta atraviesa el video:**

> «Subió 14% la demanda de Producto X en Brasil. ¿Qué hacemos?»

Se la hacemos dos veces: a una IA normal y a la misma IA con Velaria. Las dos respuestas se
muestran **escritas completas**. El video es la distancia entre esas dos respuestas.

## Regla de escritura

La locución nunca dice lo que la pantalla escribe. La voz enmarca; la pantalla explica. Por eso
el guion tiene 290 palabras y aun así el video dice más que el de 424.

---

## ESCENA 1 — Cómo está entrando la IA a las empresas (20s)

**Locución (28 pal.):**
> La inteligencia artificial ya está dentro de las empresas. Pero está entrando de a una persona
> por vez. Probemos con una pregunta real de SQM.

**En pantalla:** una ventana de chat común. La pregunta se escribe letra por letra:
`Subió 14% la demanda de Producto X en Brasil. ¿Qué hacemos?`

Y la respuesta se escribe completa, sin cortes:

> *«Para responder necesitaría conocer tu inventario actual, tu capacidad de producción, tus
> compromisos comerciales y tus costos logísticos. En general, ante un aumento de demanda se
> recomienda revisar el stock de seguridad…»*

---

## ESCENA 2 — Por qué esa respuesta está vacía (23s)

**Locución (34 pal.):**
> No está mal. Está vacía. Y no es un límite del modelo: no sabe nada de esta empresa. Cada
> persona completa a mano lo que falta, y arma su propia versión de la pregunta.

**En pantalla:** primero las tres carencias, con ejemplo concreto:

| Le falta | En concreto |
|---|---|
| **Contexto** | No sabe que acá «cobertura» es stock disponible ÷ demanda semanal proyectada |
| **Criterios** | No sabe que SQM no compromete capacidad de planta sin aprobación de Finanzas |
| **Acceso** | No puede leer el ERP, el TMS ni el CRM. Solo sabe lo que uno le pega en el chat |

Después, ocho versiones distintas de la misma pregunta, escritas una debajo de otra:
`8 personas · 8 formas de preguntar lo mismo · 0 quedan registradas`

Y el remate, que planta desde temprano dónde termina esto:
`Ocho respuestas distintas a la misma pregunta = ocho decisiones distintas.`

---

## ESCENA 3 — Qué instala Velaria (21s)

**Locución (28 pal.):**
> Velaria es eso que falta, puesto una sola vez para toda la empresa. No es otro chat: son cuatro
> piezas que se instalan sobre los sistemas que SQM ya tiene.

**En pantalla:** las cuatro, con ejemplo real en vez de definición:

| | Qué es | Ejemplo en SQM |
|---|---|---|
| **Contexto** | El diccionario de la empresa | `cobertura = stock disponible ÷ demanda semanal` · fuente: ERP |
| **Criterios** | Las reglas de decisión, escritas | `cobertura < 21 días → escalar a Finanzas` |
| **Conexiones** | Permisos de lectura a los sistemas | ERP · TMS · CRM · BI |
| **Registro** | Qué se preguntó, con qué fuente, quién decidió | `41.208 ejecuciones` |

---

## ESCENA 4 — Qué es una conexión (26s) ← la escena que hace entendible el resto

**Locución (36 pal.):**
> Una conexión es un permiso de solo lectura, acotado y revocable. Igual que cuando se autoriza a
> una aplicación a leer una cuenta bancaria: no entrega la clave, y se corta cuando se quiera.

**En pantalla:** el paralelo, lado a lado.

| Autorizar una app a leer una cuenta | El ERP de SQM → Velaria |
|---|---|
| Lee los movimientos | Lee stock y cobertura por centro |
| No puede transferir | No puede modificar una orden |
| Solo las cuentas autorizadas | Solo las tablas que autorizó TI |
| Se revoca cuando se quiera | Se revoca cuando se quiera |
| Queda registro de cada acceso | Queda registro de cada acceso |

**Y recién al final aparece la sigla:** `A esto le decimos MCP.`
Primero se entiende, después se nombra. Nunca al revés.

---

## ESCENA 5 — La misma pregunta, ahora (24s)

**Locución (30 pal.):**
> Misma IA, misma pregunta. Lo único que cambió es lo que sabe. Y no lo configuró nadie por su
> cuenta: los diez reciben lo mismo, con el alcance de su rol.

**En pantalla:** la misma ventana, la misma pregunta, y la respuesta escribiéndose:

> *«Cobertura en Brasil: 18 días, bajo el umbral de 21. Capacidad en planta local: disponible,
> semana 36. Compromisos en riesgo: 2. Alternativas: producción local US$ 17k · transferir desde
> México US$ 41k · no intervenir arriesga US$ 310k. Criterio aplicado: cobertura bajo 21 días
> escala a Finanzas. Fuentes: ERP, TMS, CRM. — 09:04:12Z»*

Y al cerrar, el alcance por rol en una línea:
`Logística ve capacidad y puerto · Finanzas ve margen · mismo contexto, mismos criterios`

---

## ESCENA 6 — Qué significa que Velaria observe (23s)

**Locución (36 pal.):**
> Velaria además mira cómo se usa. No lee conversaciones para vigilar a nadie: registra qué se
> pregunta, con qué fuentes y con qué frecuencia. Y busca lo que se repite.

**En pantalla:** primero lo que **no** hace, porque es la objeción que aparece sola:

| Sí registra | No hace |
|---|---|
| Qué fuentes se consultaron | Leer conversaciones privadas |
| Con qué criterio se decidió | Evaluar a las personas |
| Cuántas veces se repitió | Cruzar datos entre áreas sin permiso |

Después, las ocho formulaciones de la escena 2 se alinean:
`Mismo proceso · 8 personas · 5 áreas · 67 veces en 4 semanas`

> *No es un prompt repetido. Es un proceso que la empresa ya tiene y que nadie escribió.*

---

## ESCENA 7 — Cómo nace una Skill (22s)

**Locución (30 pal.):**
> Ese patrón se convierte en una capacidad de la empresa. Y no la escribe un algoritmo solo: la
> definen las personas que ya saben hacer ese trabajo.

**En pantalla:** los seis pasos, con responsable en cada uno:

| | Paso | Quién |
|---|---|---|
| 01 | Velaria propone el patrón detectado | Automático |
| 02 | Se define qué pasos tiene, qué fuentes usa y qué entrega | Experto del área + Forward Deployed Engineer |
| 03 | Se escriben los criterios que aplica | El área dueña |
| 04 | Se le dan accesos solo a las fuentes que necesita | TI |
| 05 | Se prueba contra casos históricos reales | El área + FDE |
| 06 | Se publica con dueño, versión y permisos | Gobernanza |

`Weekly S&OP Exception Review · v1 · dueña: Planificación · [ EN PRODUCCIÓN ]`

---

## ESCENA 8 — La decisión llega a tiempo (18s)

**Locución (26 pal.):**
> La excepción se decide el lunes, no el jueves. Y esos tres días son exactamente lo que separa
> proteger el margen de perderlo.

**En pantalla:** el caso, en plata:

| | Antes | Con la Skill |
|---|---|---|
| Cuándo se decide | Jueves — el embarque ya salió | Lunes 09:04 |
| Acción tomada | Ninguna a tiempo | Adelantar producción local |
| Costo de la acción | — | `US$ 17k` |
| **Margen preservado** | **`0`** | **`US$ 293k`** |

*(310k en riesgo − 17k de costo = 293k preservados. La aritmética se muestra: un comité la va a
hacer igual, y conviene que le dé.)*

---

## ESCENA 9 — Dónde se ve esto en la última línea (26s)

**Locución (34 pal.):**
> Una excepción no mueve una compañía. Lo que la mueve es que esto pase todas las semanas, en
> todas las áreas, y que Finanzas lo pueda validar.

**En pantalla:** `TRIMESTRE EN CURSO · VALIDADO CON FINANZAS`

| | |
|---|---|
| Margen identificado | `US$ 1,34 M` |
| Margen implementado | `US$ 590k` |
| **Validado por Finanzas** | **`US$ 447k`** |
| Capital de trabajo liberado | `US$ 620k` |
| Horas expertas liberadas | `1.120 h` |
| Excepciones resueltas por criterio | `22 de 27, sin intervención humana` |

Y la línea que ordena todo lo anterior:

> *No es productividad. Es margen, capital de trabajo y tiempo de decisión.*

**Por qué la fila de Finanzas va destacada:** es la única cifra que un CFO va a creer. Un número
de impacto que no pasó por Finanzas es una estimación del proveedor.

---

## ESCENA 10 — Cierre (14s)

**Locución (30 pal.):**
> Velaria no reemplaza los sistemas de SQM ni a las personas que saben hacer el trabajo. Toma lo
> que la empresa ya sabe hacer, lo escribe una vez, y lo vuelve una capacidad de toda la
> organización.

**En pantalla:** la frase que cierra la tesis, y después la placa de marca:

`De uso individual de IA · a capacidad organizacional`

---

## Notas de producción

- **Las escenas 1 y 5 son el video.** La misma pregunta, dos respuestas escritas completas. Ahí
  está el «ajá». El texto debe escribirse como en un chat —carácter por carácter— no aparecer de
  golpe: es lo que hace que se lea de verdad.
- **La escena 4 es la que vuelve entendible todo lo demás.** El paralelo del permiso bancario se
  usa solo como comparación de *cómo funciona una autorización* — nunca para decir que así usa la
  gente la IA. Si funciona, MCP deja de ser una sigla. La sigla va después de entenderlo.
- **Registro del video:** se le habla a un par, no a un principiante. El espectador nunca queda
  en el lugar del que no entiende; el que no entiende, en el relato, es la IA sin contexto.
- **La escena 6 responde una objeción antes de que se formule.** Cuando alguien escucha «Velaria
  observa cómo trabajas», lo primero que piensa es vigilancia. Decir qué NO hace vale más que
  tres frases sobre gobernanza.
- **Ritmo:** 10 escenas en ~195s = 20s por escena, contra 29s del v4. Las tablas necesitan aire
  para leerse; ese silencio es funcional, no una pausa mal medida.
- **Las ventanas de arriba son el objetivo, no el dato final.** Como en las versiones anteriores,
  la duración real de cada escena se fija con la locución ya generada y medida. Con 260 palabras
  la voz ocupa ~2:14, así que quedan ~46s repartidos como aire de lectura. Las escenas 8 y 9 son
  las más apretadas: si al medir la voz se pasan, se les recorta texto —son las que menos
  explican.
- Sin cifras nuevas inventadas: se reusan las del caso sintético ya definido, y la aritmética
  cierra entre escenas (310k en riesgo − 17k de costo = 293k preservados; 1,34M identificado →
  590k implementado → 447k validado).
- **El video termina en la última línea, no en el mecanismo.** Si hubiera que sacrificar una
  escena por tiempo, se saca la 3 o la 7 antes que la 8 o la 9.
