# Oficina ProTeam HQ en la nube (v5, 16/11)

**Dónde está:** https://claude.ai/artifact/CEbj9fsPQPUvVtRsp1S18o (artifact `5afa986a-12dd-4dee-883b-b2c379e3938c`, privado de Biel).
Vive fuera de la app ProTeam: en Lovable no se toca nada (los agentes R solo hacen mantenimiento, sugerencias y análisis).

## Desde el 16/11: todo el contenido se gestiona desde aquí
Decisión de Biel: el sistema de creación de contenido y la oficina son lo mismo. Las personas de la oficina son los trabajadores y las tareas programadas son sus turnos. Reglas completas: `oficina/PROTOCOLO.md`.

| Turno (tarea programada) | Quién | Cuándo (Madrid) |
|---|---|---|
| Producir un Reel | Dani, Andrés, Marta y Pau | 7:37 y 16:37 |
| Carrusel y Story del día siguiente | Clara (con Pau y Andrés) | 21:07 |
| Publicar y diario de métricas | Laura | 11:23, 13:23, 19:23 y 20:23 |
| Correcciones de Contenido, encargos y parte del día | Laura reparte, cada persona ejecuta | cada 2 h, de 8:49 a 22:49 |
| Análisis y aprendizaje | Samuel | lunes 9:13 |

Qué puede hacer Biel desde la oficina y qué pasa después:
- **Encargar** (pestaña Tareas de una persona, o pidiéndoselo en el chat): lo ejecuta esa persona en el siguiente turno de encargos y el resultado aparece en la tarea («Entregado: …»). Un encargo de Reel o de carrusel lo recoge su turno fijo.
- **Nada se aprueba: todo sale solo.** El equipo no pregunta; ante una duda elige lo más razonable y lo apunta en el historial.
- **Contenido** (pestaña «Contenido» o tocando el estudio creativo en la planta): todo lo pendiente de subir (Reels con su vídeo, carruseles diapositiva a diapositiva, Stories y posts), agrupado por día, con su hora, su texto y la nota de Andrés, y lo publicado en los últimos 7 días con sus vistas. En cada pieza: «Corregir» (escribes qué cambiar: se para antes de salir y la rehace quien la hizo; vuelve a la cola corregida) o «No publicar». Hay que corregir antes de la ejecución de publicación que la sacaría (11:23, 13:23, 19:23 o 20:23); la propia tarjeta dice la hora límite.
- **Reglas** (Aprendizajes → Regla) e **instrucciones extra** de cada persona (Más): obligatorias para todos los turnos; mandan sobre los documentos del repositorio.
- **Parar**: tarea para Laura cuyo título empiece por «PAUSA» (o «PAUSA REELS», «PAUSA CARRUSELES», «PAUSA PUBLICACIÓN»). Se reanuda al marcarla como hecha.
- El equipo técnico (R1–R4) no entra en estos turnos.

## Cómo es
- **Oficina realista y minimalista:** planta con paredes, puertas y salas (estudio creativo, sala de reuniones acristalada, calidad y datos, producción y archivo, equipo técnico, recepción con el logo y tu despacho).
- **Personas, no robots:** cada agente es una persona sentada en su puesto. Trabajando teclea, disponible está relajada, bloqueada se lleva la mano a la cabeza y si te necesita se levanta y saluda.
- **Al entrar te saluda Laura (la Secretaria)** con el resumen del día y acciones rápidas.
- **Al tocar a alguien:** Chat (con voz), Tareas (encargos, resultados y fichas de revisión), Perfil y Más (nivel, estado, instrucciones, aprendizajes, historial).
- **Panel** y **Aprendizajes**.

Límites: la voz de Claude no está en la app móvil ni en Safari; el dictado solo en Chrome y la app de escritorio. Los encargos no son instantáneos: se ejecutan en el siguiente turno.

## Plantilla (nombres editables desde Perfil)
| zona | id | nombre | puesto | skill |
|---|---|---|---|---|
| Recepción | 00 | Laura | Secretaria | turnos de publicación y de encargos |
| Estudio creativo | 01 | Dani | Guionista | proteam-content-lab |
| Estudio creativo | 02 | Marta | Directora creativa | proteam-creative-direction |
| Estudio creativo | 04 | Clara | Editora de carruseles | proteam-carousel-lab |
| Calidad y datos | 05 | Andrés | Crítica y calidad | proteam-critical-lab |
| Calidad y datos | 06 | Samuel | Analista de rendimiento | proteam-performance-lab |
| Producción | 03 | Pau | Archivero | proteam-resource-bank |
| Equipo técnico | R1 | Jordi | Coordinador técnico | proteam-revision-team |
| Equipo técnico | R2 | Nuria | Analista técnica | proteam-revision-team |
| Equipo técnico | R3 | Óscar | Arquitecto de la app | proteam-revision-team |
| Equipo técnico | R4 | Elena | Correctora | proteam-revision-team |
| Despacho | — | Biel | CEO | — |

## Datos (ArtifactData con la url de la oficina)
- `agents/<id>`: `status` (libre, trabajando, esperando, bloqueado), `currentTask`, `lastDelivery`, `instructions`, aspecto y voz.
- `tasks/<id>`: `{agentId, title, detail, priority, state: pendiente | en curso | hecha, by, createdAt, result, doneAt, pieceId}`.
- `pieces/<id>`: lo que sale (sincronizado desde `queue.json` con `tools/office_pieces.py`): `kind, when, status, title, caption, agentId, score, media[], cover, mediaId` + lo que escribe Biel (`fix`, `fixState: pedida | quitar`, `fixAt`) + lo que escribe el equipo (`fixState: en curso | corregida | quitada`, `fixNote`, `fixDoneAt`).
- `approvals/<id>`: solo para lo que de verdad no se puede resolver sin Biel (créditos, credenciales).
- `learnings/<id>`: `{agentId, text, type: regla | hecho | hipotesis, evidence, at, by}` (las reglas solo las pone Biel).
- `log/<id>`: `{agentId, text, at, by}`. `chats/<id>`: conversaciones.
- `meta/office`: `briefNote`, `briefAt`, `agenda`, `metrics`, `metricsAt`.

Cualquier agente activado a mano en un chat sigue también `oficina/PROTOCOLO.md` (ENTRADA y SALIDA).

## Calidad y análisis de vídeo (16/11)
El equipo trabaja con las instrucciones de `agencia/agentes/` y los procedimientos de `agencia/skills/`. Nada sale por debajo de 75 (escala nueva de Andrés) ni con un bloqueante; un hueco sin pieza válida queda vacío y anotado. Cada Reel se analiza con `tools/video_intel.py` y Andrés audita el vídeo real con marcas de tiempo (`intel/videos/<id>/observaciones.md`). Lo que el equipo no puede resolver sin Biel aparece como tarea de Laura titulada «FALTA (Biel): …».
