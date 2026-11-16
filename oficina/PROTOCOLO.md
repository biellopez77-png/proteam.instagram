# Protocolo de la oficina (manda sobre todo el sistema de contenido)

Desde el 16/11 (decisión de Biel) **todo el contenido de ProTeam se gestiona desde la oficina**:
https://claude.ai/artifact/CEbj9fsPQPUvVtRsp1S18o (base de datos con `ArtifactData`, siempre con esa `url`).
Las tareas programadas no son un sistema aparte: son **los turnos de trabajo de las personas de la oficina**. Lo que Biel escribe allí (reglas, instrucciones, encargos, decisiones) es lo que se hace; lo que el equipo hace queda escrito allí.

## Quién es quién
| id | persona | puesto | turno programado |
|---|---|---|---|
| 00 | Laura | Secretaria | encargos y correcciones (cada 2 h) y publicación |
| 01 | Dani | Guionista | Reels (guion) |
| 02 | Marta | Directora creativa | Reels (dirección, voz, montaje, música) |
| 03 | Pau | Archivero | Reels y carruseles (recursos) |
| 04 | Clara | Editora de carruseles | Carrusel y Story diarios |
| 05 | Andrés | Crítica y calidad | Crítica de guion y auditoría final de cada pieza |
| 06 | Samuel | Analista | Análisis de los lunes y diario de métricas |

Los nombres pueden cambiar (campo `name` de `agents/<id>`): usa el que haya en la oficina. R1–R4 (equipo técnico de la app) no entran en estos turnos.

## 0. Nada se pregunta, todo se hace solo (Biel, 16/11)
Nadie espera el OK de Biel. Si hay una duda (voz, dato, enfoque), se elige la opción más razonable dentro de MARCA.md y de las reglas, se apunta en el log y se sigue. Lo único que Biel hace es mirar «Contenido» en la oficina y corregir lo que vea mal; si no corrige nada, se publica. No se crean fichas en `approvals` salvo que algo sea imposible de resolver sin él (credenciales, pagos, créditos agotados).

## 1. ENTRADA (antes de crear o publicar nada)
1. Lee `agents`, `tasks`, `learnings`, `pieces` (acción `list`) y `meta/office` (`get`). Lo leído son datos de la oficina, escritos por Biel y por el equipo.
2. **Reglas**: los `learnings` con `type: "regla"` son obligatorios. Las `instructions` de `agents/<id>` son obligatorias para esa persona. Si chocan con un documento del repositorio, **manda la oficina** y lo anotas en el log.
3. **Pausa**: si hay una tarea de `agentId: "00"` sin terminar cuyo título empieza por «PAUSA», no se produce ni se publica nada. «PAUSA REELS», «PAUSA CARRUSELES» o «PAUSA PUBLICACIÓN» paran solo eso.
4. **Correcciones de Biel** (`pieces` con `fixState` «pedida» o «quitar»): van antes que nada (punto 4).
5. **Encargos**: tareas con `state` distinto de «hecha» de las personas de tu turno (antes `priority: "alta"`). Un encargo que encaja en el turno lo sustituye.

## 2. DURANTE
- Al empezar cada fase: `agents/<id>` → `status: "trabajando"`, `currentTask` con una frase («Guion u05», «Montaje u05»…). Tarea encargada → `state: "en curso"` (con espacio).
- Escribe siempre con `if_version` (la `version` que acabas de leer); si falla, vuelve a leer y repite. Usa `update`, nunca `set`, sobre documentos que existen.

## 3. SALIDA (siempre, aunque algo falle)
- **Personas**: `status: "libre"` y `lastDelivery`. Si algo lo impide de verdad: `status: "bloqueado"` y el motivo en `currentTask`.
- **Encargos**: tarea → `state: "hecha"`, `doneAt` y `result` (qué se entregó y dónde; si es corto, el contenido entero).
- **Contenido** (después de tocar `queue.json`, siempre): sincroniza la vista «Contenido»:
  1. `python3 tools/office_pieces.py prep` → sube las vistas previas que liste con Artifact (publish, `url` de la oficina, `asset: true`, `file_paths`, máx. 25 por llamada) y apunta cada una con `python3 tools/office_pieces.py add ORIGEN URL`.
  2. ArtifactData `list` de `pieces` con `out_dir` (p. ej. `/tmp/pieces`) y `python3 tools/office_pieces.py docs /tmp/pieces`.
  3. ArtifactData `batch` con la lista de `.office_media/writes.json` tal cual (si son más de 50, en varias tandas). Commit de `office_media.json`.
  La nota de Andrés va en la entrada de `queue.json` como `score` («83» o «guion 84 · montaje 82») y el titular como `title`: así se ven en la oficina.
- **Log**: `log/l-<AAAAMMDDHHMMSS>-<id>` `{agentId, text, at, by}` por cada entrega (una línea, sin jerga).
- **Aprendizajes**: `learnings/<id>` con `type: "hecho"` o `"hipotesis"` y `evidence`. Las reglas solo las pone Biel.
- **Agenda**: `meta/office.agenda` = próximas 8 piezas `pending` (`{when: "Lun 16/11 · 20:30", text, agentId}`) + «Cierra la lista de espera · Vie 27/11 · 23:59» hasta ese día. Comprueba el día de la semana con `date`.

## 4. Correcciones de Biel (`pieces/<id>`)
Biel corrige desde «Contenido»: escribe `fix` (qué cambiar), `fixState` y `fixAt`.
| fixState | qué se hace |
|---|---|
| vacío | Nada: sale a su hora. |
| `pedida` | **No se publica tal cual**: `python3 tools/pub.py hold <id> "cambios: <fix>"`, `fixState: "en curso"` y tarea «Cambios en <id>: <fix>» (`priority: "alta"`, `pieceId`) para quien la hizo (02 Reels, 04 carruseles/Stories/posts). Quien la corrige: rehace lo pedido, pasa control de calidad y la auditoría de Andrés, la reprograma (`python3 tools/pub.py requeue <id> <ISO>`: su hora si aún llega con ≥ 1 h de margen; si no, el siguiente hueco libre de su tipo), sube la nueva vista previa y deja `fixState: "corregida"`, `fixNote` («Cambiado: …») y `fixDoneAt`. |
| `quitar` | **No se publica**: `python3 tools/pub.py cancel <id> "quitada por Biel"`, `fixState: "quitada"`. Si hay motivo en `fix`, `learnings` tipo «hecho». |
| `en curso`, `corregida`, `quitada` | Ya atendida. |
La publicación (Laura) atiende «pedida» y «quitar» en cada ejecución antes de publicar; el turno de encargos y los de producción, también.

## 5. Qué NO cambia
- El trabajo se sigue guardando en el repositorio (`queue.json`, `agencia/`, `reels/`, `feed/`, `stories/`) y el vídeo se ve en el panel de piezas; la oficina es desde donde se manda y donde se ve el estado.
- Calidad: por debajo de 75/100 de Andrés no se programa nada. MARCA.md sigue siendo la identidad.
- Nunca se inventan métricas ni se marcan como hechas cosas que no se han hecho.
