# Backlog — equipo técnico

Estados: pendiente · en curso · hecho · bloqueado · a verificar · en PR

## Tareas abiertas
| ID | Tarea | Agente | Estado | Notas |
|---|---|---|---|---|
| — | — | — | — | Sin tareas abiertas (17/11) |

## Tareas cerradas
| ID | Tarea | Agente | Estado | Notas |
|---|---|---|---|---|
| T-01 | Verificar el bloque «Rutinas» (04/11 + «sigue»/«acaba» hasta el 07/11) | R2 | hecho (16/11) | Cumplido. Estados unificados con `legacy_status`, CHECK y RLS individual correctos (SQL). Pendiente solo probar en pantalla la vinculación a mixta y la privacidad individual cuando existan datos reales |
| T-02 | Verificar «Personalidad + menú lateral fijo + estadística visual» (13/11) | R2 | hecho (16/11) | Cumplido: `shell.tsx` aside `fixed`; `match-presentation.ts` con 7 apartados y mismas cifras. Detalles → A-001, A-002 |
| T-03 | Google Sheets directo a Drive (OAuth `drive.file`) | R1 | cerrado (16/11) | No hace falta: la descarga .xlsx + sheets.new ya lo cubre |

## Hallazgos abiertos
| ID | Severidad | Resumen | Estado | Lote |
|---|---|---|---|---|
| A-001 | Baja | `src/components/shell.tsx`: aria-labels fijos fuera de `t()` («Menú», «Tancar menú», «Obrir menú», «Menú de navegació», «Navegació principal» en la barra inferior del jugador). Solo afecta a lectores de pantalla | pendiente | Arreglo pequeño. 17/11 12:20: no se pudo hacer, el turno no tenía acceso a biellopez77-png/proteamapp (sin `add_repo`) |
| A-002 | Baja | Confirmado (R2, 17/11): `src/lib/match-presentation.ts` (`matchPresentationSections`) devuelve «Jugadores» y «Comparativa» con `blocks: []`, y `src/lib/reports/pdf.ts` (`buildReportPdf`, bucle de secciones: `if (!s.blocks.length) text(ctx, EMPTY…)`) las imprime igualmente: el PDF del partido sale con dos apartados con título y «sin datos». Arreglo propuesto: rellenarlas con los datos que ya calcula `matchPresentation` (`positions`, `comparison`) o quitarlas del informe | pendiente | Arreglo pequeño (1 archivo); necesita acceso al repositorio de la app |

## Ideas aparcadas (no pedidas por Biel; no se hacen sin su OK)
-
