# Registro de arreglos de la app

Desde el 17/11 los arreglos se hacen en el código (biellopez77-png/proteamapp): 0 créditos de Lovable.

| Fecha | ID | Alcance | Commit / PR / message_id | Créditos | Resultado |
|---|---|---|---|---|---|
| 2026-11-03 | — | Rediseño de Inicio y Planificación (corrección) + export Excel/Sheets | umsg_01m6gpg660f4ma9t6hxftmnd4q | 19,7 | Hecho; Sheets queda en modo descarga |
| 2026-11-03 | — | Bienvenida lenta, verificación del zoom, «Minutos planificados vs reales», prueba de Excel | umsg_01m6hb406dem3sz5t9w3wpar2y | 12,9 | Hecho |
| 2026-11-04 | — | Rutinas, traducciones ca↔es, animación de carga | umsg_01m6kk1wr2fq5axfcp89jt9kdc | ? | Verificado (T-01) |
| 2026-11-17 | T-05, T-06, T-07 (A-003…A-021) | Revisión de errores encargada por Biel: análisis técnico (R2), arquitectura (R3) y lista por gravedad (R1). Solo análisis | — (código leído con `read_file` de Lovable; 7 SELECT) | 0 | Hecho: 19 hallazgos nuevos en BACKLOG, 5 de gravedad alta, ningún bloqueante. Sin arreglos: este turno tampoco tuvo acceso a biellopez77-png/proteamapp (no hay `add_repo` en la sesión programada) |
| 2026-11-17 | A-003, A-012 | Parches listos (Elena): paradas y goles encajados en el PDF del partido; sanciones repetidas al reenviar la cola del directo | `revision/pendiente-push/A-003-…patch`, `A-012-…patch` | 0 | Sin aplicar ni publicar: sin acceso a proteamapp. Probados con `git apply` contra el código actual (leído con `read_file` de Lovable); falta `bun run build` |
