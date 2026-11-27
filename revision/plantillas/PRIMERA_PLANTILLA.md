# «Primera plantilla» · la primera semana por deporte (Dani, 18/11)

Regalo exclusivo para la lista de espera (decisión de Biel, 18/11). Una semana tipo por deporte: 3 sesiones con objetivo, bloques y duración. **No se escribe nada en la base de datos sin el visto bueno de Biel**; el equipo técnico lo inserta el 27–28/11 en los equipos de la lista.

## Cómo encaja en la app (comprobado el 18/11 en la base de datos, solo lectura)
- `schedule_templates`: `team_id`, `name`, `notes`, `created_by`.
- `schedule_template_rows`: `template_id`, `team_id`, `weekday` (1 = lunes … 7 = domingo), `activity_type` (`sessio` o `partit`), `session_subtype` (`pista`, `fisic` o `mixta`), `start_time`, `end_time`, `title`, `location`, `sort_idx`, `every_n_weeks` (1–12), `routine_source` (`fixed` o `cycle`), `physical_min`.
- **Ojo:** una fila guarda día, hora, tipo y título, pero no tiene campo para el objetivo ni para los bloques. Aquí van así: el título de la sesión en `title` y el objetivo y los bloques en `notes` de la plantilla. Si el equipo técnico prefiere crear las sesiones con sus bloques, el contenido es el mismo.
- Días y horas por defecto: lunes, miércoles y viernes. Si el equipo ya tiene sus días en la app, se cambian `weekday`, `start_time` y `end_time` y no se toca nada más. No se añade fila de partido: cada equipo juega un día distinto.
- Archivos listos para insertar: `revision/plantillas/primera-plantilla-<deporte>.json` (`team_id` y `created_by` se rellenan al insertar).

## Fútbol 11 · infantil y cadete

### Lunes · Salida de balón ante presión (90 min)
**Objetivo:** Salir jugando desde el portero con un jugador libre en la primera línea.

| min | bloque | qué se hace |
|---|---|---|
| 15 | Activación | Rondos 4 contra 2 a dos toques, con movilidad de cadera y tobillo entre series. |
| 20 | Juego de posición 6 contra 4 | En campo propio: portero, línea de cuatro y pivote contra cuatro que presionan. Punto si cruzan el medio campo con pase o en conducción. |
| 25 | Partido condicionado 8 contra 8 | En tres cuartos de campo. Todo saque de puerta empieza en corto. El gol tras salir jugando vale doble. |
| 20 | Partido libre | Sin normas. Solo se corrige la salida de balón, en las pausas. |
| 10 | Vuelta a la calma | Estiramientos y dos preguntas: ¿dónde estaba el jugador libre?, ¿cuándo hay que jugar largo? |

### Miércoles · Presión tras pérdida (90 min)
**Objetivo:** Recuperar el balón en los seis segundos siguientes a perderlo.

| min | bloque | qué se hace |
|---|---|---|
| 15 | Activación y fuerza preventiva | Carrera suave, core, isquios y tobillo. Sin material. |
| 20 | Rondos 5 contra 3 con transición | Quien pierde el balón presiona cinco segundos junto a los dos más cercanos. |
| 25 | Juego 7 contra 7 con dos comodines | Espacio de 40 × 50 m. El gol vale doble si el balón se recupera en campo rival antes de seis segundos. |
| 20 | Partido con la norma | Mismo criterio a campo grande. Se cuenta en voz alta cada recuperación rápida. |
| 10 | Vuelta a la calma | Estiramientos y repaso: quién salta primero y quién cierra por dentro. |

### Viernes · Finalización y balón parado (75 min)
**Objetivo:** Llegar al partido con las jugadas claras y las piernas frescas.

| min | bloque | qué se hace |
|---|---|---|
| 10 | Activación con velocidad | Salidas de 5 a 10 m con estímulo visual. Pocas repeticiones y descanso completo. |
| 20 | Finalización por oleadas | 3 contra 2 y 2 contra 1 con remate antes de ocho segundos. |
| 25 | Balón parado | Dos córners a favor, uno en contra y un saque de banda en campo rival. Cada jugador sabe su sitio. |
| 15 | Partido corto | Dos partes de seis minutos, con el once probable. |
| 5 | Convocatoria y plan | Hora, lugar y las tres ideas del partido. |

## Fútbol 7 · benjamín y alevín

### Lunes · Abrir el campo (75 min)
**Objetivo:** Usar las bandas para encontrar espacio por dentro.

| min | bloque | qué se hace |
|---|---|---|
| 10 | Juego de activación | Pilla-pilla con balón: cada jugador conduce el suyo. |
| 15 | Rondos 3 contra 1 y 4 contra 2 | Dos toques como máximo. Cambia el del medio cada 45 segundos. |
| 20 | Juego 4 contra 4 con dos comodines por fuera | El gol solo vale si el balón ha pasado antes por un comodín de banda. |
| 25 | Partido 7 contra 7 con carriles | Carriles de banda marcados con conos: dentro del carril no se puede robar. |
| 5 | Cierre | Una pregunta: ¿cuándo estaba libre el de la banda? |

### Miércoles · Uno contra uno (75 min)
**Objetivo:** Atreverse a encarar y aprender a defender sin tirarse.

| min | bloque | qué se hace |
|---|---|---|
| 10 | Activación coordinativa | Conducción con cambios de dirección y de ritmo entre conos. |
| 15 | 1 contra 1 en carriles | Miniporterías. Quien ataca, luego defiende. |
| 20 | 2 contra 1 y 2 contra 2 con finalización | Decidir entre encarar o pasar. Portero en portería grande. |
| 25 | Partido 7 contra 7 | El gol después de un regate vale doble. |
| 5 | Cierre | Cada jugador dice un regate que le ha salido. |

### Viernes · Jugar con el portero y saques (75 min)
**Objetivo:** Empezar en corto y tener dos saques preparados.

| min | bloque | qué se hace |
|---|---|---|
| 10 | Activación | Pases por parejas en movimiento, con las dos piernas. |
| 15 | Salida en corto 3 contra 1 | El portero y dos defensas contra un delantero: llegar a medio campo con el balón controlado. |
| 15 | Saques | Un saque de banda y un saque de esquina. Dos repeticiones por cada lado. |
| 30 | Partido 7 contra 7 | Todos rotan de posición y juegan los mismos minutos. |
| 5 | Cierre | Hora y lugar del partido. Recordar los dos saques. |

## Baloncesto · infantil y cadete

### Lunes · Defensa del uno contra uno y ayudas (90 min)
**Objetivo:** Parar el balón sin falta y llegar a la ayuda a tiempo.

| min | bloque | qué se hace |
|---|---|---|
| 15 | Activación con balón | Manejo, cambios de mano y movilidad de cadera y tobillo. |
| 15 | 1 contra 1 desde 45 grados | Tres botes como máximo. El defensor gana si no hay bandeja. |
| 20 | 2 contra 2 y 3 contra 3: ayudar y recuperar | Posición respecto al balón y a tu jugador. Se para para corregir distancias. |
| 25 | 4 contra 4 en media pista | La defensa puntúa: tres paradas seguidas y cambia con el ataque. |
| 15 | Tiros libres y estiramientos | Dos tiros libres después de cada esprint. Se apunta el porcentaje. |

### Miércoles · Contraataque y transición (90 min)
**Objetivo:** Correr con orden: primer pase, calles ocupadas y decisión rápida.

| min | bloque | qué se hace |
|---|---|---|
| 15 | Activación | Ruedas de pase en carrera a todo campo. |
| 20 | 2 contra 1 y 3 contra 2 continuo | El que tira baja a defender. Sin bote de más. |
| 20 | 3 contra 2 y vuelta en 2 contra 1 | Quien pierde el balón o tira se queda fuera en la vuelta. |
| 25 | 5 contra 5 a todo campo | La canasta antes de ocho segundos vale tres puntos. |
| 10 | Vuelta a la calma | Estiramientos y repaso de quién saca y quién corre cada calle. |

### Viernes · Juego sin balón: cortes y espacios (90 min)
**Objetivo:** Moverse después de pasar y dejar libre el centro.

| min | bloque | qué se hace |
|---|---|---|
| 10 | Tiro por parejas | Tiros cercanos y de media distancia. Cambio a los cinco aciertos. |
| 20 | Pasar y cortar | Primero 3 contra 0 y después 3 contra 3 sin bote. |
| 20 | 4 contra 4 con dos botes como máximo | Quien pasa, corta o bloquea lejos del balón. Nadie se queda quieto. |
| 25 | 5 contra 5 con saques | Un saque de fondo y uno de banda, dos repeticiones cada uno, y partido. |
| 15 | Tiros libres y plan de partido | Diez tiros libres por jugador y las tres ideas del partido. |

## Balonmano · infantil y cadete

### Lunes · Defensa abierta y recuperación de balón (90 min)
**Objetivo:** Defender hacia delante: piernas, línea de pase y robo.

| min | bloque | qué se hace |
|---|---|---|
| 15 | Activación con balón | Pases en desplazamiento y juego de los diez pases. |
| 15 | 1 contra 1 defensivo en carril | Posición básica, desplazamientos y contacto con el brazo, sin agarrar. |
| 20 | 2 contra 2 y 3 contra 3 en medio campo | Defensa adelantada: disuadir e interceptar la línea de pase. |
| 25 | 6 contra 6 con defensa 3:3 o individual | Robo y gol de contraataque valen doble. |
| 15 | Lanzamientos y estiramientos | Lanzamientos por puestos con portero y vuelta a la calma. |

### Miércoles · Contraataque: primera y segunda oleada (90 min)
**Objetivo:** Salir rápido tras recuperar y llegar con superioridad.

| min | bloque | qué se hace |
|---|---|---|
| 15 | Activación | Pase largo del portero al extremo y finalización. |
| 20 | 2 contra 1 y 3 contra 2 a todo campo | Sin botar si hay compañero libre por delante. |
| 20 | Repliegue: 4 contra 3 con un defensor que llega tarde | El ataque tiene seis segundos para lanzar. |
| 25 | Partido 6 contra 6 | El gol antes de tres pases desde la recuperación vale doble. |
| 10 | Vuelta a la calma | Estiramientos y repaso de las calles de carrera. |

### Viernes · Ataque posicional: fijar y pasar (90 min)
**Objetivo:** Atacar el intervalo, fijar al defensor y soltar el balón a tiempo.

| min | bloque | qué se hace |
|---|---|---|
| 15 | Activación y lanzamiento | Ciclo de pasos y lanzamiento por puestos. |
| 20 | 2 contra 2 por zonas | Fijar al impar y pasar al compañero libre. |
| 20 | 3 contra 3 con pivote | Cruce entre primeras líneas y continuidad con el pivote. |
| 25 | Partido 6 contra 6 | Con siete metros y dos saques de golpe franco preparados. |
| 10 | Plan de partido | Hora, lugar y las tres ideas del partido. |

## Control
- 4 deportes × 3 sesiones; los minutos de los bloques suman la duración de cada sesión (comprobado al generar los archivos).
- Sin material especial: balones, conos, petos y porterías.
- Balonmano: defensa abierta en infantil y cadete, en la línea del Reel «Tu 6:0 gana en infantiles».
- Nada de funciones de la app prometidas: es contenido de entreno.
