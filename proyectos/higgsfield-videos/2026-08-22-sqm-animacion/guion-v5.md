# Guion v5 — Qué hace Velaria, explicado desde lo que la gente ya conoce

## El problema de los guiones anteriores

Arrancaban desde el vocabulario de Velaria — "capa de inteligencia organizacional", "criterios",
"gobernanza" — y trataban de explicarlo. Para un equipo comercial eso es ruido. Para el equipo de
tecnología de SQM quizás no, pero ellos no son quienes hay que convencer.

**La mayoría de las personas hoy conoce dos cosas de IA:**
1. Abrir ChatGPT o Claude y hacer una pregunta.
2. Conectar el banco a una app para bajar cartolas y ordenar sus finanzas.

Este guion se construye **entero** sobre esas dos referencias. Nada se explica en abstracto:
todo se explica como una diferencia contra algo que el espectador ya hizo.

## El hilo conductor

**Una sola pregunta atraviesa el video de principio a fin:**

> «Subió catorce por ciento la demanda de Producto X en Brasil. ¿Qué hacemos?»

Se la hacemos tres veces: a una IA normal, a una IA con Velaria, y a la Skill ya construida. Las
tres respuestas se muestran escritas. El video es la distancia entre esas tres respuestas.

---

## ESCENA 1 — Lo que ya sabemos hacer (22s)

**Locución:**
> Hoy casi todos usamos la inteligencia artificial de la misma manera: abrimos una ventana,
> escribimos una pregunta y recibimos una respuesta. Funciona. Probemos con una pregunta real
> de SQM.

**En pantalla:** una ventana de chat común y corriente. Se escribe la pregunta, letra por letra:
`Subió 14% la demanda de Producto X en Brasil. ¿Qué hacemos?`

Y aparece la respuesta genérica, escrita completa, palabra por palabra:

> *"Para responder necesitaría conocer tu inventario actual, tu capacidad de producción, tus
> compromisos comerciales y tus costos logísticos. En general, ante un aumento de demanda se
> recomienda revisar el stock de seguridad y evaluar aumentar la producción…"*

**El punto:** la respuesta no está mal. Está vacía. Y todos reconocen esa respuesta.

---

## ESCENA 2 — Por qué está vacía (26s)

**Locución:**
> No está mal. Está vacía. Y no es culpa del modelo: es que no sabe nada de SQM. No sabe qué
> significa cobertura acá, no sabe dónde vive el dato, y no sabe con qué criterio decide esta
> empresa.

**En pantalla:** tres carencias, escritas, cada una con su ejemplo concreto:

| Lo que le falta | En concreto |
|---|---|
| **Contexto** | No sabe que en SQM «cobertura» es stock disponible dividido por demanda semanal proyectada. Ni en qué sistema está ese dato. |
| **Criterios** | No sabe que SQM no compromete capacidad de planta sin aprobación de Finanzas. |
| **Acceso** | No puede leer el ERP, ni el TMS, ni el CRM. Solo sabe lo que uno le pega en el chat. |

---

## ESCENA 3 — Y cada uno lo resuelve por su cuenta (20s)

**Locución:**
> Entonces cada persona completa lo que falta a mano. Copia y pega datos, agrega de memoria las
> reglas de la empresa, y arma su propia versión de la pregunta.

**En pantalla:** las mismas ocho personas escribiendo ocho versiones distintas de la misma
pregunta, una debajo de la otra. Se lee lo distintas que son. Abajo:
`8 personas · 8 formas de preguntar lo mismo · 0 quedan registradas`

---

## ESCENA 4 — Qué es una capa de inteligencia organizacional (34s)

**Locución:**
> Velaria es eso que falta, puesto una sola vez para toda la empresa. No es otro chat. Es cuatro
> cosas que se instalan encima de los sistemas que SQM ya tiene.

**En pantalla:** las cuatro, escritas, cada una con un ejemplo real y no con una definición:

| | Qué es | Ejemplo en SQM |
|---|---|---|
| **Contexto** | El diccionario de la empresa | `cobertura = stock disponible / demanda semanal proyectada` · fuente: ERP |
| **Criterios** | Las reglas de decisión, escritas | `cobertura < 15 días → escalar a Finanzas` |
| **Conexiones** | Permisos de lectura a los sistemas | ERP · TMS · CRM · BI |
| **Registro** | Qué se preguntó, con qué fuente, quién decidió | `41.208 ejecuciones` |

---

## ESCENA 5 — Qué es una conexión, en cristiano (28s)

**Locución:**
> Una conexión funciona igual que cuando conectas tu banco a una aplicación de finanzas. No le
> entregas tu clave. Le das permiso para leer ciertas cuentas, para ciertas cosas, y se lo puedes
> quitar cuando quieras.

**En pantalla:** el paralelo, lado a lado. Es el corazón didáctico del video.

| Tu banco → app de finanzas | El ERP de SQM → Velaria |
|---|---|
| Lee tus movimientos | Lee stock y cobertura por centro |
| No puede transferir | No puede modificar una orden |
| Solo las cuentas que autorizaste | Solo las tablas que autorizó TI |
| Lo revocas cuando quieras | Se revoca cuando quieras |
| Queda registro de cada acceso | Queda registro de cada acceso |

**Y recién ahí se nombra:** `A esto le decimos MCP.` Primero se entiende, después se nombra —
nunca al revés.

---

## ESCENA 6 — La misma pregunta, ahora (26s)

**Locución:**
> Con eso puesto, volvamos a hacer la misma pregunta.

**En pantalla:** la misma ventana de chat, la misma pregunta, y la respuesta nueva escribiéndose:

> *"Cobertura actual en Brasil: 18 días, bajo el umbral de 21 definido por Planificación.
> Capacidad disponible en planta local: sí, semana 36. Compromisos con clientes en riesgo: 2.
> Alternativas: adelantar producción local, US$ 17k. Transferir desde México, US$ 41k. No
> intervenir pone en riesgo US$ 310k de margen. Criterio aplicado: cobertura bajo 21 días escala
> a Finanzas. Fuentes: ERP, TMS, CRM. — 09:04:12Z"*

**El punto:** es la misma IA. Lo que cambió es lo que sabe.

---

## ESCENA 7 — Y para los diez, igual (22s)

**Locución:**
> Y esto no lo configuró cada persona por su cuenta. Los diez reciben el mismo contexto y los
> mismos criterios, con el alcance que le corresponde a su rol.

**En pantalla:** la misma pregunta hecha por dos roles distintos, con dos respuestas correctas y
distintas:

- **Logística** ve capacidad de embarque y ventana de puerto. No ve margen.
- **Finanzas** ve margen en riesgo y costo de cada alternativa. No ve datos de clientes.

`Mismo contexto · mismos criterios · distinto alcance`

---

## ESCENA 8 — Qué significa que Velaria observe (30s)

**Locución:**
> Velaria además mira cómo se está usando. No lee lo que la gente escribe para vigilarla: registra
> qué se pregunta, con qué fuentes y con qué frecuencia. Y busca lo que se repite.

**En pantalla:** primero, de forma explícita, **qué NO hace** — porque es la objeción que aparece
sola en la cabeza de cualquiera:

| Sí registra | No hace |
|---|---|
| Qué fuentes se consultaron | Leer conversaciones privadas |
| Con qué criterio se decidió | Evaluar a las personas |
| Cuántas veces se repitió | Compartir datos entre áreas sin permiso |

Después, el hallazgo: las ocho formulaciones distintas de la escena 3 se alinean.
`Mismo proceso · 8 personas · 5 áreas · 67 veces en 4 semanas`

> *Eso no es un prompt repetido. Es un proceso que la empresa ya tiene y que nadie escribió.*

---

## ESCENA 9 — Cómo nace una Skill (36s)

**Locución:**
> Cuando aparece un patrón así, se convierte en una capacidad de la empresa. Una Skill. Y no la
> escribe un algoritmo solo: la definen las personas que ya saben hacer ese trabajo.

**En pantalla:** los seis pasos, escritos, uno por uno — esto es lo que pediste explicar en
detalle:

| | Paso | Quién |
|---|---|---|
| 01 | Velaria propone el patrón detectado | Automático |
| 02 | Se define qué pasos tiene, qué fuentes usa y qué entrega | Experto del área + Forward Deployed Engineer |
| 03 | Se escriben los criterios que aplica | El área dueña del proceso |
| 04 | Se le dan accesos solo a las fuentes que necesita | TI |
| 05 | Se prueba contra casos históricos reales | El área + FDE |
| 06 | Se publica con dueño, versión y permisos | Gobernanza |

`Weekly S&OP Exception Review · v1 · dueña: Planificación · [ EN PRODUCCIÓN ]`

---

## ESCENA 10 — Qué cambia el lunes (24s)

**Locución:**
> Desde entonces, nadie vuelve a armar esa pregunta a mano. El lunes a las nueve la excepción ya
> está analizada, con sus alternativas y su costo. La persona no recopila: decide.

**En pantalla:** la bandeja del lunes, y el comparativo:

| | Antes | Con la Skill |
|---|---|---|
| Quién la ejecuta | 5 personas | 1 persona decide |
| Cuánto demora | 5 h 30 min | 1 min 30 s |
| Cuándo se decide | Jueves | Lunes 09:04 |
| Queda registro | No | Sí, con autor y criterio |

---

## ESCENA 11 — Cierre (18s)

**Locución:**
> Velaria no reemplaza los sistemas de SQM, ni a las personas que saben hacer el trabajo. Toma lo
> que la empresa ya sabe hacer, lo escribe una sola vez, y lo pone a disposición de todos.

**En pantalla:** placa de marca.

---

## Notas de producción

- **Duración estimada:** ~4:10 de locución + aire ≈ **4:30**. Es más largo que el v4 (1:47) a
  propósito: este video tiene otro trabajo. El v4 era institucional; este es **explicativo**, y
  lo que se pidió fue explicar el mecanismo con más detalle, no menos.
  Si hay que acortar, las escenas 3 y 7 son las que menos daño hacen al sacarlas (−42s → 3:48).
- **Las escenas 1 y 6 son las más importantes del video.** La misma pregunta, dos respuestas
  escritas completas. Ahí está el «ajá». Merecen tiempo en pantalla y que el texto se escriba
  como se escribe en un chat, no que aparezca de golpe.
- **La escena 5 es la que hace entendible todo lo demás.** Si el paralelo del banco funciona,
  MCP deja de ser una sigla. Va antes de nombrar la sigla, nunca después.
- **La escena 8 responde una objeción antes de que se formule.** Cuando alguien escucha «Velaria
  observa cómo trabajas», lo primero que piensa es vigilancia. Decir explícitamente qué NO hace
  vale más que tres frases sobre gobernanza.
- Sin cifras nuevas inventadas: se reusan las del caso sintético ya definido.
