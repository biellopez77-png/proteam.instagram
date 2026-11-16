# SKILL · Quality Gate (05 Critical Lab)
**Para qué:** decidir con reglas fijas qué se publica, qué vuelve y qué se descarta, sin que la cuota mueva el listón.

## Herramientas
Críticas en `agencia/criticas/`, `queue.json` (`score`, `status`), `tools/pub.py` (`hold`, `requeue`), tareas de la oficina (ArtifactData `tasks`), `intel/videos/<id>/`.

## Puertas
| puerta | qué se audita | pasa con |
|---|---|---|
| 1 · Idea/guion (antes de producir) | concepto, hook, guion o mapa de diapositivas | ≥ 75 y ningún bloqueante |
| 2 · Pieza final (antes de programar) | vídeo real analizado, o JPG finales mirados | ≥ 75, ningún bloqueante y cobertura declarada |

## Bloqueantes (devuelven la pieza aunque la nota sea alta)
Dato, función, testimonio o resultado inventado · fecha u oferta distinta de MARCA.md (en voz o en pantalla) · interfaz inventada · texto con error ortográfico en pantalla · texto necesario ilegible o fuera de zona segura · fotograma 0 en negro o con texto pequeño · persona como aval · Reel sin análisis en `intel/videos/` · concepto repetido sin ángulo nuevo.

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
