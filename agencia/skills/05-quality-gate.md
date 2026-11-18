# SKILL · Quality Gate (05 Critical Lab)
**Para qué:** decidir con reglas fijas qué se publica, qué vuelve y qué se descarta, sin que la cuota mueva el listón.

## Herramientas
Críticas en `agencia/criticas/`, `queue.json` (`score`, `status`), `tools/pub.py` (`hold`, `requeue`), tareas de la oficina (ArtifactData `tasks`), `intel/videos/<id>/`.

## Puertas
| puerta | qué se audita | pasa con |
|---|---|---|
| 1 · Idea/guion (antes de producir) | concepto, hook, guion o mapa de diapositivas | ≥ 75 y ningún bloqueante |
| 2 · Pieza final (antes de programar) | vídeo real analizado, o JPG finales mirados | ≥ 75, ningún bloqueante y cobertura declarada |

## Encaje de fase (lanzamiento 18→28/11, Biel 17/11) — va antes que la nota
Cada crítica empieza con dos líneas: **Fase del día en que sale** (según `agencia/LANZAMIENTO.md`) y **Encaje de fase: sí / no**, con el porqué. Si es «no», la pieza no se programa ese día aunque pase de 75: se mueve al día de su fase (`pub.py requeue`) o pasa a borrador (`pub.py hold`). En `queue.json` cada pieza lleva `fase`.
Cómo se reconoce la fase: pantalla de la app, «en la app de ProTeam se hace así» o «ProTeam por dentro» → solución (nunca antes del mar 24 por la tarde); escena o dato del problema sin la app → problema; algo que se puede usar sin vender → nutrición; qué llega el 28 sin explicar la app → impacto. Stories: solo la fase del día. Un contador o un «quedan N días» tiene que ser verdad el día en que sale.

## Bloqueantes (devuelven la pieza aunque la nota sea alta)
Dato, función, testimonio o resultado inventado · fecha u oferta distinta de MARCA.md (en voz o en pantalla) · interfaz inventada · texto con error ortográfico en pantalla · texto necesario ilegible o fuera de zona segura · fotograma 0 en negro o con texto pequeño · persona como aval · Reel sin análisis en `intel/videos/` · pieza fuera de la fase de su día · el nombre de Biel o «el fundador» · precio · concepto repetido sin ángulo nuevo · **exceso de texto (Biel, 18/11):** más de una idea por diapositiva, Story o plano; bloques o párrafos; frases largas; subtítulo debajo de cada línea. Medida: Story ≤ 4 bloques de texto y una sola pregunta; diapositiva ≤ 2 frases cortas; Reel, un titular corto por plano. Prueba: la sigue sin ayuda alguien que ya está en la cuenta y alguien que llega hoy (se dice en una línea qué es ProTeam y cuándo abre).

## Veredictos
- **PUBLICABLE** (≥ 75, sin bloqueantes): `score` en `queue.json`; sigue su hora.
- **NECESITA CAMBIOS** (60–74, o ≥ 75 con bloqueante): no se programa (o `python3 tools/pub.py hold <id> "<motivo>"` si ya estaba en cola). Devolución con ficha.
- **NO PUBLICABLE** (< 60, o problema de idea): se descarta; vuelve a 01 o 04 como idea nueva, no como arreglo.

## Ficha de devolución (tarea de prioridad alta para quien hizo la pieza, con `pieceId`)
`Devuelta <id> · nota <n> · veredicto`
1. Bloqueantes (cada uno con dónde: segundo, lámina, diapositiva).
2. Correcciones obligatorias, numeradas: qué, dónde, cómo se comprobará.
3. Lo que no se toca.
4. Plazo: antes del turno de publicación que la sacaría.

## Segunda auditoría
Se comprueba **cada corrección numerada**, una a una (hecha / no hecha / hecha a medias), sobre la pieza nueva (vídeo reanalizado: nuevo sha256, nuevas láminas). Retoque cosmético = no hecha. Máximo dos vueltas: a la tercera, NO PUBLICABLE.

## Cuota (decisión de Biel: se mantiene)
Si una pieza cae, el hueco lo cubre la **reserva** (guiones y carruseles ya aprobados en puerta 1). Si no hay reserva, el hueco queda vacío y se anota en el log: nunca se aprueba para llenar. La reserva mínima es de 4 guiones ≥ 75; por debajo, se avisa a 01 con tarea de prioridad alta.

## Registro
Crítica guardada, `score` y `title` en `queue.json`, fila en `HISTORIAL.md` (con «escala 16/11»), log de la oficina con veredicto en una línea.

## Control
¿He aplicado los bloqueantes antes de mirar la nota? ¿La devolución es ejecutable sin preguntarme nada? ¿He cedido por la hora?
