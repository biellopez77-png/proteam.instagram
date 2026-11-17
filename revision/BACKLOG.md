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
| A-001 | Baja | `src/components/shell.tsx`: aria-labels fijos fuera de `t()` («Menú», «Tancar menú», «Obrir menú», «Menú de navegació», «Navegació principal» en la barra inferior del jugador). Solo afecta a lectores de pantalla | pendiente | Arreglo pequeño: ya se puede hacer en el código (APP_REPO.md) |
| A-002 | A verificar | `src/lib/match-presentation.ts` (`matchPresentationSections`): «Jugadores» y «Comparativa» van con `blocks: []` en el informe descargable. Mirar si el PDF los oculta o salen vacíos | a verificar | R2, leyendo `src/lib/reports/pdf.ts` en el repositorio |

## Ideas aparcadas (no pedidas por Biel; no se hacen sin su OK)
-
