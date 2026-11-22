#!/usr/bin/env python3
"""R-001 (rendimiento): jsPDF + jspdf-autotable solo se descargan al pedir el PDF.

`src/components/report/report-export-button.tsx` importaba `@/lib/reports/pdf`
de forma estática (línea 7) y ese módulo importa `jspdf` y `jspdf-autotable`
(líneas 7–8 de `src/lib/reports/pdf.ts`). Así, cada pantalla con el botón
«Generar informe» (partido, jugador, tests, pista…) cargaba la librería de PDF
aunque el entrenador no generase nunca un informe. El Excel ya se carga bajo
demanda (`workbook.ts`, `import("write-excel-file/browser")`).

Cambio (1 archivo, sin textos ni BD): import dinámico del módulo de PDF; al
abrir la previsualización se precarga para que en iOS el «Compartir» siga
dentro del gesto del usuario. Si no se puede cargar al compartir, se usa el
compartir normal (enlace), como cuando el navegador no admite archivos.

Uso: python3 aplicar.py /ruta/a/proteamapp
"""
import pathlib, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
f = root / "src/components/report/report-export-button.tsx"
s = f.read_text()

REPL = [
    (
        'import { downloadReportPdf, shareReportPdf } from "@/lib/reports/pdf";\n',
        '',
    ),
    (
        'import { useI18n } from "@/lib/i18n";\n',
        'import { useI18n } from "@/lib/i18n";\n\n'
        '/** jsPDF + autotable are heavy: load them only when a report is opened. */\n'
        'const loadPdf = () => import("@/lib/reports/pdf");\n',
    ),
    (
        '      const how = await downloadReportPdf(spec);\n',
        '      const { downloadReportPdf } = await loadPdf();\n'
        '      const how = await downloadReportPdf(spec);\n',
    ),
    (
        '      if (await shareReportPdf(spec)) return;\n',
        '      const pdf = await loadPdf().catch(() => null);\n'
        '      if (pdf && (await pdf.shareReportPdf(spec))) return;\n',
    ),
    (
        '    if (!open) setBusy(false);\n  }, [open]);\n',
        '    if (!open) setBusy(false);\n'
        '    // Warm the PDF chunk while the preview renders, so the iOS share sheet\n'
        '    // still runs inside the tap\'s user activation.\n'
        '    else void loadPdf().catch(() => undefined);\n'
        '  }, [open]);\n',
    ),
]

for old, new in REPL:
    n = s.count(old)
    if n != 1:
        sys.exit(f"ERROR: se esperaba 1 coincidencia y hay {n}: {old!r}")
    s = s.replace(old, new)

assert '@/lib/reports/pdf"' not in s.replace('import("@/lib/reports/pdf")', ''), "queda un import estático"
f.write_text(s)
print("R-001 aplicado en", f)
