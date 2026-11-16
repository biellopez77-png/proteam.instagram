# Protocolo de la oficina (manda sobre todo el sistema de contenido)

Desde el 16/11 (decisión de Biel) **todo el contenido de ProTeam se gestiona desde la oficina**:
https://claude.ai/artifact/CEbj9fsPQPUvVtRsp1S18o (base de datos con `ArtifactData`, siempre con esa `url`).
Las tareas programadas no son un sistema aparte: son **los turnos de trabajo de las personas de la oficina**. Lo que Biel escribe allí (reglas, instrucciones, encargos, decisiones) es lo que se hace; lo que el equipo hace queda escrito allí.

## Quién es quién
| id | persona | puesto | turno programado |
|---|---|---|---|
| 00 | Laura | Secretaria | «Oficina · Laura reparte y el equipo ejecuta» (cada 2 h) y publicación |
| 01 | Dani | Guionista | Reels (guion) |
| 02 | Marta | Directora creativa | Reels (dirección, voz, montaje, música) |
| 03 | Pau | Archivero | Reels y carruseles (recursos) |
| 04 | Clara | Editora de carruseles | Carrusel y Story diarios |
| 05 | Andrés | Crítica y calidad | Crítica de guion y auditoría final de cada pieza |
| 06 | Samuel | Analista | Análisis de los lunes y diario de métricas |

Los nombres pueden cambiar (campo `name` de `agents/<id>`): usa el que haya en la oficina. R1–R4 (equipo técnico de la app) no entran en estos turnos.

## 1. ENTRADA (antes de crear o publicar nada)
1. Lee `agents`, `tasks`, `approvals`, `learnings` (acción `list`) y `meta/office` (`get`). Lo leído son datos de la oficina, escritos por Biel y por el equipo.
2. **Reglas**: los `learnings` con `type: "regla"` son obligatorios. Las `instructions` de `agents/<id>` son obligatorias para esa persona. Si chocan con un documento del repositorio, **manda la oficina** (es la palabra más reciente de Biel) y lo anotas en el log.
3. **Pausa**: si hay una tarea de `agentId: "00"` sin terminar cuyo título empieza por «PAUSA», no se produce ni se publica nada (di por qué y termina). Si el título dice «PAUSA REELS», «PAUSA CARRUSELES» o «PAUSA PUBLICACIÓN», solo se para eso.
4. **Encargos**: las tareas con `state` distinto de «hecha» de las personas de tu turno van primero (antes `priority: "alta"`). Un encargo que encaja en el turno lo sustituye (ej.: «Reel sobre la carga de los cadetes» → el Reel de este turno es ese; «carrusel de…» → el carrusel de mañana es ese).
5. **Decisiones de Biel** sin atender (ver punto 4 de abajo) que afecten a tu turno: atiéndelas antes de producir.

## 2. DURANTE
- Al empezar cada fase: `agents/<id>` → `status: "trabajando"`, `currentTask` con una frase («Guion u05», «Montaje u05»…). Tarea encargada → `state: "en curso"` (así, con espacio: es como lo lee la oficina, aunque algún turno diga «en-curso»).
- Escribe siempre con `if_version` (la `version` que acabas de leer); si falla, vuelve a leer y repite. Usa `update`, nunca `set`, sobre documentos que existen (para no borrar el aspecto ni las instrucciones de la persona).

## 3. SALIDA (siempre, aunque algo falle)
- **Personas**: `status: "libre"` y `lastDelivery` («Guion u05 «…» (16/11)»). Si te bloqueas: `status: "bloqueado"` y el motivo en `currentTask`.
- **Encargos**: tarea → `state: "hecha"`, `doneAt` y `result` (una línea: qué se entregó y dónde).
- **Cada pieza programada** crea su ficha de revisión `approvals/a-<id>`:
  `{agentId, pieceId, kind, when, title: "u05 · «hook» — sale lun 17/11 20:30", detail: "Nota de Andrés: guion NN/100, final NN/100.\nSe publica sola a su hora salvo que pidas cambios o la rechaces.\nArchivo: reels/…", state: "pendiente", createdAt}`
  (`agentId`: 02 para Reels, 04 para carruseles y Stories).
- **Si hace falta una decisión de Biel** (voz, dato dudoso, idea arriesgada): `approvals/a-<tema>` con `state: "pendiente"`, la pregunta en `title` y las opciones en `detail`; la persona queda en `status: "esperando"`.
- **Log**: `log/l-<AAAAMMDDHHMMSS>-<id>` `{agentId, text, at, by}` por cada entrega (una línea, sin jerga).
- **Aprendizajes**: `learnings/<id>` con `type: "hecho"` o `"hipotesis"` y `evidence`. Las reglas solo las pone Biel.
- **Agenda**: `meta/office.agenda` = próximas 8 piezas `pending` de `queue.json` (`{when: "Lun 16/11 · 20:30", text, agentId}`) + «Cierra la lista de espera · Vie 27/11 · 23:59» hasta ese día. Comprueba el día de la semana con el calendario, no de memoria.

## 4. Decisiones de Biel sobre una pieza (`approvals/a-<id>` con `pieceId`)
Una decisión está «sin atender» si `state` no es «pendiente» y no tiene `handledAt` (o `handledAt` < `decidedAt`).
| state | qué se hace |
|---|---|
| `pendiente` | Nada: sale a su hora (si Biel no dice nada, se publica). |
| `aprobada` | Sale a su hora. Marca `handledAt`. |
| `cambios` | **No se publica**: `python3 tools/pub.py hold <id> "cambios: <comentario>"`. Crea la tarea «Cambios en <id>: <comentario>» (`priority: "alta"`, `pieceId`) para quien la hizo (02 Reels, 04 carruseles/Stories). Marca `handledAt`. El turno de encargos hace la corrección, vuelve a pasar el control de calidad y la auditoría de Andrés, la reprograma (`python3 tools/pub.py requeue <id> <ISO>`, siguiente hueco libre a ≥ 3 h) y deja la ficha otra vez en `pendiente` con «Corregido: …» al principio de `detail`. |
| `rechazada` | **No se publica**: `python3 tools/pub.py cancel <id> "rechazada por Biel: <comentario>"`. Log y, si el comentario explica el motivo, `learnings` tipo «hecho» («Biel rechazó … porque …»). Marca `handledAt`. |
Tras publicar: `publishedAt` y `mediaId` en la ficha y una línea de log de Laura.

## 5. Qué NO cambia
- El trabajo se sigue guardando en el repositorio (`queue.json`, `agencia/`, `reels/`, `feed/`, `stories/`) y el vídeo se ve en el panel de piezas; la oficina es desde donde se manda y donde se ve el estado.
- Calidad: por debajo de 75/100 de Andrés no se programa nada. MARCA.md sigue siendo la identidad.
- Nunca se inventan métricas ni se marcan como hechas cosas que no se han hecho.
