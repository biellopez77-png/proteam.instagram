# Backlog — equipo técnico

Estados: pendiente · en curso · hecho · bloqueado · a verificar · en PR

## Bloqueo (17/11 16:17)
Las sesiones programadas del equipo técnico no tienen `add_repo` ni acceso a biellopez77-png/proteamapp (GitHub responde «not configured for this session»; `git clone` pide credenciales). Mientras dure, los arreglos se dejan como parches en `revision/pendiente-push/` (aplicar con `git apply <parche>` en proteamapp, `bun run build`, commit en `main`, push y `deploy_project`). Para quitar el bloqueo: añadir proteamapp a los repositorios de la tarea programada.

Última zona auditada: ninguna todavía (la siguiente es «landing y lista de espera»).

## Tareas abiertas
| ID | Tarea | Agente | Estado | Notas |
|---|---|---|---|---|
| T-04 | Revisión de errores: corrección y textos (encargo de Biel 17/11) | R4 | pendiente | Siguiente turno; se suma a la lista de abajo |

## Tareas cerradas
| ID | Tarea | Agente | Estado | Notas |
|---|---|---|---|---|
| T-01 | Verificar el bloque «Rutinas» (04/11 + «sigue»/«acaba» hasta el 07/11) | R2 | hecho (16/11) | Cumplido. Estados unificados con `legacy_status`, CHECK y RLS individual correctos (SQL). Pendiente solo probar en pantalla la vinculación a mixta y la privacidad individual cuando existan datos reales |
| T-02 | Verificar «Personalidad + menú lateral fijo + estadística visual» (13/11) | R2 | hecho (16/11) | Cumplido: `shell.tsx` aside `fixed`; `match-presentation.ts` con 7 apartados y mismas cifras. Detalles → A-001, A-002 |
| T-03 | Google Sheets directo a Drive (OAuth `drive.file`) | R1 | cerrado (16/11) | No hace falta: la descarga .xlsx + sheets.new ya lo cubre |
| T-05 | Revisión de errores: análisis técnico (cálculo, datos, exportación) | R2 | hecho (17/11) | 10 hallazgos → A-003…A-010 (+ A-002 revisado). Código leído con `read_file` de Lovable (sin acceso a GitHub), 2 SELECT |
| T-06 | Revisión de errores: arquitectura (datos, sincronización, permisos, rendimiento) | R3 | hecho (17/11) | 93 tablas con RLS activo, políticas abiertas justificadas. 10 hallazgos → A-011…A-020. 5 SELECT |
| T-07 | Revisión de errores: lista única por gravedad | R1 | hecho (17/11) | Orden de abajo. Falta sumar la parte de textos (T-04, R4) |

## Hallazgos abiertos
| ID | Severidad | Resumen | Estado | Lote |
|---|---|---|---|---|
| A-001 | Baja | `src/components/shell.tsx`: aria-labels fijos fuera de `t()` («Menú», «Tancar menú», «Obrir menú», «Menú de navegació», «Navegació principal» en la barra inferior del jugador). Solo afecta a lectores de pantalla | pendiente | Arreglo pequeño. 17/11 12:20: no se pudo hacer, el turno no tenía acceso a biellopez77-png/proteamapp (sin `add_repo`) |
| A-002 | Baja | Confirmado (R2, 17/11): `src/lib/match-presentation.ts` (`matchPresentationSections`) devuelve «Jugadores» y «Comparativa» con `blocks: []`, y `src/lib/reports/pdf.ts` (`buildReportPdf`, bucle de secciones: `if (!s.blocks.length) text(ctx, EMPTY…)`) las imprime igualmente: el PDF del partido sale con dos apartados con título y «sin datos». Arreglo propuesto: rellenarlas con los datos que ya calcula `matchPresentation` (`positions`, `comparison`) o quitarlas del informe | a verificar | R2 17/11 14:30: en el `match-report.ts` actual «Jugadores» y «Comparativa» se rellenan y los apartados vacíos se filtran (`presentation.filter(s => s.blocks.length > 0)`); comprobar si `matchPresentationSections` se usa en otra ruta antes de tocar nada |

### Revisión de errores 17/11 (R1: lista única por gravedad; ningún bloqueante)
Pequeño = 1–2 archivos, sin BD/auth/permisos/pagos → `main`. Grande → rama `revision/<tema>` + PR para Biel.

| ID | Severidad | Resumen | Estado | Lote |
|---|---|---|---|---|
| A-003 | Alta | PDF del partido: «Aturades» y «Gols encaixats» siempre 0. `match-report.ts` `teamTotals` cuenta `save`/`goal_against` solo en `ours` (`side !== "them"`), pero se guardan con `side: them` (BD: 126 `save:them`, 266 `goal_against:them`, 0 propios). Reproducir: partido con paradas → PDF | parche listo | Pequeño (1 archivo): contar sobre `ev` como `teamMetrics`. 17/11 16:17: parche listo y probado contra el código actual → `revision/pendiente-push/A-003-paradas-y-goles-encajados-pdf.patch` (SQL de nuevo: 126 save:them, 266 goal_against:them). Falta aplicarlo: sin acceso a proteamapp |
| A-004 | Alta | PDF del partido ignora el deporte: `buildMatchReport` lee `m.sport_code` (no existe en `matches`) y `coach.matches.$id.tsx` no pasa `sportCode` de `getMatchLive` → baloncesto/fútbol con plantilla de balonmano («Gols 0», cuartos 3–4 como prórrogas en `absoluteSecond`) | pendiente | Pequeño (2 archivos): pasar `sportCode` |
| A-005 | Alta | Excel convierte miles en decimales: `workbook.ts` `typedValue`/`unitColumns` → «12.500» = 12,5 (es/ca) y «1,500» = 1,5 (en). Afecta a «Càrrega (kg·rep)» de `progress-report.ts` (`toLocaleString`) | pendiente | Pequeño (2 archivos) + caso en `workbook.test.ts` |
| A-011 | Alta | Equipo activo en cookie global `proteam_team` (`team-access.ts` `resolveMembership`, `selectTeam` `Path=/` 1 año): con dos pestañas en equipos distintos, lo creado en una se guarda en el otro equipo y las ediciones responden `ok` sin cambiar nada | pendiente | Grande (teamId explícito en funciones y claves de consulta) → PR |
| A-012 | Alta | Directo: reenvío desde la cola reaplica sanciones. `addMatchEvents` (`live-match.functions.ts`) llama a `match_apply_sanction` también con eventos duplicados ignorados → saca de pista y reexcluye; si falla, el `catch` borra por `client_id` eventos ya guardados | parche listo | Pequeño (1 archivo): sancionar solo filas nuevas. 17/11 16:17: `revision/pendiente-push/A-012-sanciones-reenvio-cola.patch` (`upsert…select("client_id")` → solo se sancionan y deshacen las filas nuevas). Falta aplicarlo: sin acceso a proteamapp |
| A-006 | Media | PDF: minutos de jugadores en pista a 0 en el periodo actual: `aggregate(events, stints, {period, sec: 0})` sin duración (`stintSecondsResolver` en `match-model.ts`); la pantalla usa `clock_sec` | pendiente | Pequeño (1 archivo) |
| A-007 | Media | Informe → filtro «1.ª/2.ª parte»: «Min» sigue siendo el partido entero (`coach.matches.$id.tsx` pasa `stints` sin filtrar; `rAggs` no se usa) | pendiente | Pequeño (1 archivo) |
| A-008 | Media | Informe de rendimiento de pista: dos % de asistencia distintos (`progress-report.ts` `pct(present+late, total)` frente a `attendanceSummary` del resumen) | pendiente | Pequeño (1 archivo) |
| A-009 | Media | Tests físicos del informe: «Millor» = `Math.max` aunque menos sea mejor (sprint 4,1 / 4,6 → 4,6) (`progress-report.ts`; `tests-report.ts` sí lo hace bien) | pendiente | Pequeño (2 archivos) |
| A-013 | Media | Control del directo no atómico: `requireOperator`/`claimMatchControl` leen `live_operator_id` y luego `update` sin condición → dos operadores a la vez | pendiente | Pequeño (1 archivo): `update` condicionado |
| A-014 | Media | `saveCallups` borra y recrea la convocatoria sin mirar errores ni conservar `is_goalkeeper`/`status`/`exclusion_*` → se pierden porteros y estados; si falla el `insert`, partido sin convocatoria | pendiente | Pequeño (1 archivo): `upsert` + borrar los que salen |
| A-015 | Media | Editar partido reescribe la fila con datos de la caché (`MatchForm.submit` en `coach.matches.index.tsx` + `saveMatch`): puede devolver a `scheduled` un partido empezado y cambia `created_by` al editor | pendiente | Pequeño (1–2 archivos) |
| A-016 | Media | Delegado y fisio con permisos de escritura de entrenador (`teams.ts` `STAFF_ROLES`; `requireStaff` protege borrar partido, `resetLiveSession`…), contra `ROLE_DESCRIPTIONS`; fisio `canEdit` falso pero `requireOperator` le deja | pendiente | Grande (permisos/RLS) y decisión de producto → R1 decide: delegado solo consulta, fisio sin directo (según `ROLE_DESCRIPTIONS`), en PR |
| A-017 | Media | `listTeamMembers` llama a `auth.admin.listUsers({perPage:1000})` en cada carga: trae todos los usuarios y con >1000 los correos salen vacíos | pendiente | Grande (auth) → PR |
| A-018 | Media | Errores sin comprobar que responden «ok»: `coachUpdatePlayer`, `savePrematch`, `resolveJoinRequest`, `inviteTeamMember`, `syncMicrocycleLink`, `setMatchPrep` (jugador recibe `ok` y la RLS no cambia nada) | pendiente | Pequeño por archivo; los de miembros (auth) en PR |
| A-010 | Baja | PDF individual: el marcador de la cronología cuenta solo los goles del jugador (`timelineSection(mine…)`) | pendiente | Pequeño |
| A-019 | Baja | Comparativa del PDF sin correcciones manuales de marcador (`teamMetrics` frente a `m.result.us` en pantalla) y etiquetas mezcladas ca/es («Mitjana», «Goles por partido») | pendiente | Pequeño |
| A-020 | Baja | Contadores «leer y escribir»: `coachAddSet` (`set_number = count+1`, renumera al reenviar) y `joinTeamWithCode` (`uses+1`, se pasa `max_uses`) | pendiente | Primero pequeño; segundo toca BD → PR |
| A-021 | Baja | Rendimiento: `createLiveSession` ~200 consultas sin transacción; `syncMatchResult` sin `fetchAll` (>1000 eventos); `invalidateQueries()` sin clave en `coach.matches.index.tsx` y `teams.tsx` | pendiente | Mixto |

## Ideas aparcadas (no pedidas por Biel; no se hacen sin su OK)
-
