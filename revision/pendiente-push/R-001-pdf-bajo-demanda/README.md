# R-001 — La librería de PDF solo se descarga al abrir un informe

**Qué pasa hoy.** `src/components/report/report-export-button.tsx` (línea 7) importa `downloadReportPdf` y `shareReportPdf` de `@/lib/reports/pdf`, y ese archivo importa `jspdf` y `jspdf-autotable` (líneas 7–8). Todas las pantallas con el botón «Generar informe» cargan la librería de PDF al abrirse, aunque nadie pulse el botón. El Excel ya se hace bien (`workbook.ts`: `await import("write-excel-file/browser")`).

**Qué cambia.** Import dinámico (`loadPdf`) en el botón: el PDF se descarga al abrir la previsualización (precarga) o al pulsar «Descarregar PDF». Mismo resultado para el usuario, menos carga en cada pantalla del entrenador (en el banquillo, con 4G flojo).

**Comprobar al aplicar** (en proteamapp):

```bash
python3 <esta carpeta>/aplicar.py .
grep -rn 'lib/reports/pdf"' src | grep -v 'import("'   # debe salir vacío; si sale otro import estático, el ahorro es menor (no rompe nada)
bun run build                                           # en dist/ debe aparecer un chunk aparte con jspdf
```

Probar: abrir un partido → «Generar informe» → «Descarregar PDF» (escritorio) y «Compartir» en iPhone.

Probado sobre el código leído con `read_file` de Lovable (commit 578c7aa): las 5 sustituciones encajan una sola vez; una segunda ejecución se para sin tocar nada.
