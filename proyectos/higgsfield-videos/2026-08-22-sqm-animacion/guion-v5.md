# Guion v5 — Qué hace Velaria, explicado desde lo que la gente ya conoce

**Duración objetivo: 3:00.** Nueve escenas.

## Por qué los guiones anteriores quedaron genéricos

Arrancaban desde el vocabulario de Velaria — «capa de inteligencia organizacional», «criterios»,
«gobernanza» — y trataban de explicarlo. Para un equipo comercial eso es ruido. Para el equipo de
tecnología de SQM quizás no, pero ellos no son a quienes hay que convencer.

**La mayoría de las personas hoy conoce dos cosas de IA:**

1. Abrir ChatGPT o Claude y hacer una pregunta.
2. Conectar el banco a una app para bajar cartolas y ordenar sus finanzas.

Este guion se construye **entero** sobre esas dos referencias. Nada se explica en abstracto: todo
se explica como una diferencia contra algo que el espectador ya hizo.

## El hilo conductor

**Una sola pregunta atraviesa el video:**

> «Subió 14% la demanda de Producto X en Brasil. ¿Qué hacemos?»

Se la hacemos dos veces: a una IA normal y a la misma IA con Velaria. Las dos respuestas se
muestran **escritas completas**. El video es la distancia entre esas dos respuestas.

## Regla de escritura

La locución nunca dice lo que la pantalla escribe. La voz enmarca; la pantalla explica. Por eso
el guion tiene 290 palabras y aun así el video dice más que el de 424.

---

## ESCENA 1 — La pregunta (20s)

**Locución (24 pal.):**
> Hoy casi todos usamos la inteligencia artificial igual: abrimos una ventana y preguntamos.
> Probemos con una pregunta real de SQM.

**En pantalla:** una ventana de chat común. La pregunta se escribe letra por letra:
`Subió 14% la demanda de Producto X en Brasil. ¿Qué hacemos?`

Y la respuesta se escribe completa, sin cortes:

> *«Para responder necesitaría conocer tu inventario actual, tu capacidad de producción, tus
> compromisos comerciales y tus costos logísticos. En general, ante un aumento de demanda se
> recomienda revisar el stock de seguridad…»*

---

## ESCENA 2 — Por qué esa respuesta está vacía (23s)

**Locución (32 pal.):**
> No está mal. Está vacía. No sabe nada de SQM. Y como no sabe, cada persona completa lo que
> falta a mano, y arma su propia versión de la pregunta.

**En pantalla:** primero las tres carencias, con ejemplo concreto:

| Le falta | En concreto |
|---|---|
| **Contexto** | No sabe que acá «cobertura» es stock disponible ÷ demanda semanal proyectada |
| **Criterios** | No sabe que SQM no compromete capacidad de planta sin aprobación de Finanzas |
| **Acceso** | No puede leer el ERP, el TMS ni el CRM. Solo sabe lo que uno le pega en el chat |

Después, ocho versiones distintas de la misma pregunta, escritas una debajo de otra:
`8 personas · 8 formas de preguntar lo mismo · 0 quedan registradas`

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

**Locución (38 pal.):**
> Una conexión funciona igual que cuando conectas tu banco a una app de finanzas. No le entregas
> tu clave: le das permiso para leer ciertas cuentas, y se lo puedes quitar cuando quieras.

**En pantalla:** el paralelo, lado a lado.

| Tu banco → app de finanzas | El ERP de SQM → Velaria |
|---|---|
| Lee tus movimientos | Lee stock y cobertura por centro |
| No puede transferir | No puede modificar una orden |
| Solo las cuentas que autorizaste | Solo las tablas que autorizó TI |
| Lo revocas cuando quieras | Se revoca cuando quieras |
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

## ESCENA 8 — Qué cambia el lunes (13s)

**Locución (30 pal.):**
> Desde entonces nadie vuelve a armar esa pregunta a mano. El lunes a las nueve la excepción ya
> está analizada. La persona no recopila: decide.

**En pantalla:**

| | Antes | Con la Skill |
|---|---|---|
| Quién ejecuta | 5 personas | 1 persona decide |
| Cuánto demora | 5 h 30 min | 1 min 30 s |
| Cuándo se decide | Jueves | Lunes 09:04 |
| Queda registro | No | Sí, con autor y criterio |

---

## ESCENA 9 — Cierre (8s)

**Locución (26 pal.):**
> Velaria no reemplaza los sistemas de SQM ni a las personas que saben hacer el trabajo. Toma lo
> que la empresa ya sabe, lo escribe una vez, y lo pone a disposición de todos.

**En pantalla:** placa de marca.

---

## Notas de producción

- **Las escenas 1 y 5 son el video.** La misma pregunta, dos respuestas escritas completas. Ahí
  está el «ajá». El texto debe escribirse como en un chat —carácter por carácter— no aparecer de
  golpe: es lo que hace que se lea de verdad.
- **La escena 4 es la que vuelve entendible todo lo demás.** Si el paralelo del banco funciona,
  MCP deja de ser una sigla. Va antes de nombrarla.
- **La escena 6 responde una objeción antes de que se formule.** Cuando alguien escucha «Velaria
  observa cómo trabajas», lo primero que piensa es vigilancia. Decir qué NO hace vale más que
  tres frases sobre gobernanza.
- **Ritmo:** 9 escenas en 180s = 20s por escena, contra 29s del v4. Las tablas necesitan aire
  para leerse; ese silencio es funcional, no una pausa mal medida.
- **Las ventanas de arriba son el objetivo, no el dato final.** Como en las versiones anteriores,
  la duración real de cada escena se fija con la locución ya generada y medida. Con 260 palabras
  la voz ocupa ~2:14, así que quedan ~46s repartidos como aire de lectura. Las escenas 8 y 9 son
  las más apretadas: si al medir la voz se pasan, se les recorta texto —son las que menos
  explican.
- Sin cifras nuevas: se reusan las del caso sintético ya definido.
