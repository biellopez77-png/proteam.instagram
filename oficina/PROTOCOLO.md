# Protocolo de la oficina (manda sobre todo el sistema de contenido)

Desde el 16/11 (decisión de Biel) **todo el contenido de ProTeam se gestiona desde la oficina**:
https://claude.ai/artifact/CEbj9fsPQPUvVtRsp1S18o (base de datos con `ArtifactData`, siempre con esa `url`).
Las tareas programadas no son un sistema aparte: son **los turnos de trabajo de las personas de la oficina**. Lo que Biel escribe allí (reglas, instrucciones, encargos, decisiones) es lo que se hace; lo que el equipo hace queda escrito allí.

## Quién es quién
| id | persona | puesto | turno programado |
|---|---|---|---|
| 00 | Laura | Secretaria | encargos y correcciones (cada 2 h, 8:49–22:49) y publicación (11:23, 13:23, 17:23, 19:23, 20:23) |
| 01 | Dani | Guionista | Reels (7:37, 11:37, 16:37) y guiones por adelantado (9:53, 13:53, 18:53) |
| 02 | Marta | Directora creativa | Reels (dirección, voz, montaje, música) |
| 03 | Pau | Archivero | Reels y carruseles (recursos) |
| 04 | Clara | Editora de carruseles | 2 carruseles y 3 Stories al día (9:07 y 21:07) |
| 05 | Andrés | Crítica y calidad | Crítica de cada guion y auditoría final de cada pieza |
| 06 | Samuel | Analista | Radar de actualidad (6:47), bucle viral diario (22:41: ganadora, perdedora y encargos para mañana) y análisis de los lunes (9:13) |

**Plan de alcance (16/11):** cada persona tiene en `agents/<id>.instructions` sus reglas para conseguir visitas llenas (primer segundo, motivo para guardar o enviar, portada, series de la ganadora). `meta/office.winner` = `{id, title, why, at}` con la pieza ganadora del día.

**VOLUMEN MÁXIMO (Biel, 16/11 15:30) — manda sobre cualquier cuota, ritmo o regla de alcance anterior.** Biel: «necesitamos muchísimo contenido, cuanto más mejor». Parrilla diaria (hora de Madrid, todo en :30 para que la publicación de cada hora a las :23 lo saque a su hora):
| formato | horas | al día |
|---|---|---|
| Reels | 9:30 · 11:30 · 13:30 · 17:30 · 20:30 · 22:30 | 6 |
| Carruseles | 12:30 · 19:30 | 2 (todos los días) |
| Stories | 10:30 · 14:30 · 16:30 · 18:30 · 21:30 | 5 |
- Lo que sigue igual: umbral 75 de Andrés, nada inventado, tres deportes por igual, nada de Reels de marca o motivación vacía. Más volumen = más piezas buenas, no piezas peores. Un hueco sin pieza ≥ 75 se rellena con la siguiente de la reserva; si no hay, se queda vacío y se anota.
- Cómo se llega: el turno de Reels corre cada 3 horas (0:37, 3:37, 6:37, 9:37, 12:37, 15:37, 18:37, 21:37) y saca 1 Reel por turno, 2 si el segundo es un Reel de datos corto (8–15 s); el turno de Clara corre a las 9:07 y a las 21:07 (1 carrusel + hasta 3 Stories por turno); se mantiene una reserva de guiones criticados de al menos 8.
- Variedad obligatoria con tanto volumen: dos piezas seguidas no repiten deporte ni estructura; mezcla de Reels con voz (escena, dato, partido real) y Reels de datos cortos; Stories con encuestas, preguntas y avisos de lo que sale.
- Samuel mide cada semana si más piezas bajan las vistas medias por pieza (canibalización) y lo dice en su resumen con números; mientras tanto, se sigue el volumen máximo.

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

## 6. Estándar de calidad y skills (Biel, 16/11) — manda sobre las instrucciones anteriores de cada agente
- Cada persona trabaja con sus **instrucciones nuevas** de `agencia/agentes/` (empezando por `00_COMUN.md`) y con sus procedimientos de `agencia/skills/`. Si chocan con un texto antiguo, mandan estas.
- **Con música. Volumen máximo** (6 Reels, 2 carruseles y 5 Stories al día, ver la parrilla de arriba): se cubre con la reserva de piezas aprobadas, nunca aprobando peor. Hueco sin pieza ≥ 75 = hueco vacío, anotado en el log.
- **No se pregunta y no se inventa:** si falta un dato esencial, esa pieza no se hace, se elige otra y se deja una tarea para Laura con el título «FALTA (Biel): …».
- **Puntuación de Andrés desde el 16/11:** hook 15 · estrategia 15 · narrativa 15 · valor 15 · originalidad 15 · credibilidad y claridad 10 · ejecución visual 10 · CTA 5. Umbral 75 y bloqueantes de `agencia/skills/05-quality-gate.md`. En `score` se escribe la nota como siempre.
- **Todo Reel montado se analiza antes de auditarse:** `python3 tools/video_intel.py analyze reels/<archivo> --id <id> --tema "…" --modo detalle`, `voz <id> tools/reelNN/voz.tsv` y `rasgos <id>`. Marta mira las láminas y corrige; Andrés audita el vídeo real con marcas de tiempo (`intel/videos/<id>/observaciones.md`); Pau cataloga (`recursos.md`); Samuel usa `intel/aprendizaje/CARACTERISTICAS.csv`. Guía: `intel/README.md`.
- En la entrega de cada pieza van escritas las diez preguntas de control de `00_COMUN.md`.

## 7. Trabajo continuo, consignas y resúmenes (Biel, 16/11)
- No hay turnos de descanso: los encargos y consignas se revisan cada hora (7:49–23:49), los guiones cada hora (:08) y los carruseles y Stories cada hora (:31). El objetivo es tener la faena adelantada hasta 15 días.
- Biel ya no cambia el estado de las tareas en la oficina. Deja **consignas** en `tasks/<id>.consignas` (lista de {text, at, by}). Una consigna con `at` posterior a `consignaVistaAt` es una orden nueva: se aplica antes que nada, se explica en `result` y se pone `consignaVistaAt` = ahora.
- El estado (pendiente, en curso, hecha) lo pone siempre quien trabaja. Al cerrar una tarea se escribe `summary`: una línea de 15 palabras como máximo con lo entregado. Biel lee ese resumen; el detalle largo va en `result`.
- En la oficina, quien tiene tareas abiertas aparece trabajando en su mesa aunque su estado diga «libre»; solo va a descanso quien no tiene nada abierto.

## 8. Regla de alcance (Biel, 16/11 14:25) — manda sobre el «Ritmo» de arriba y sobre los textos antiguos
- Cada Reel abre en el segundo 0 con un número, un partido real o una escena concreta de entreno. Prohibidos los Reels de marca o motivación.
- Cada Reel acaba con una pregunta o reto para el cuerpo técnico; la descripción pide «Envíaselo a tu segundo entrenador» y lleva el CTA de comentar.
- **Carruseles solo martes y viernes** (11:00 y 19:00). El resto de días Clara convierte su idea en un Reel de datos de 8–15 s.
- **Una Story al día**, no tres.
- En cada Reel publicado, el turno de publicación deja un primer comentario nuestro: «Comenta tu deporte, categoría y días y te preparo la semana».
- Nadie crea tareas para Biel.
