#!/usr/bin/env python3
"""A-009 · «Millor» de los tests físicos respeta si menos es mejor.

Uso (desde la raíz de proteamapp):  python3 <ruta>/aplicar.py
Cada sustitución exige que el texto original aparezca exactamente una vez;
si no, no escribe nada y dice cuál falla.
"""
import pathlib, sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")

EDITS = {
    "src/lib/progress.functions.ts": [
        (
            'if (!ids.length) return { players, tests: [], logs: [], sets: [], injuries: [], attendance: [], matchDays: [] };',
            'if (!ids.length) return { players, tests: [], logs: [], sets: [], injuries: [], attendance: [], matchDays: [], directions: {} as Record<string, "higher_better" | "lower_better"> };',
        ),
        (
            '''    const sessions = (sessionRows.data ?? []) as unknown as { id: string; session_date: string }[];
    const matches = (matchRows.data ?? []) as unknown as { id: string; match_date: string }[];
''',
            '''    // Sentido de cada test (catálogo del equipo y tests programados): en sprint o movilidad, menos es mejor.
    const [catalogDirs, assignmentDirs] = await Promise.all([
      context.supabase.from("test_catalog").select("name, unit_direction").eq("team_id", t),
      context.supabase.from("test_assignments").select("name, unit_direction").eq("team_id", t),
    ]);
    const directions: Record<string, "higher_better" | "lower_better"> = {};
    for (const row of [
      ...((assignmentDirs.data ?? []) as unknown as { name: string; unit_direction: string | null }[]),
      ...((catalogDirs.data ?? []) as unknown as { name: string; unit_direction: string | null }[]),
    ]) {
      if (row.unit_direction === "higher_better" || row.unit_direction === "lower_better") {
        directions[row.name.trim().toLowerCase()] = row.unit_direction;
      }
    }

    const sessions = (sessionRows.data ?? []) as unknown as { id: string; session_date: string }[];
    const matches = (matchRows.data ?? []) as unknown as { id: string; match_date: string }[];
''',
        ),
        (
            '''    return {
      players,
      tests: [
''',
            '''    return {
      players,
      directions,
      tests: [
''',
        ),
    ],
    "src/lib/reports/progress-report.ts": [
        (
            '''type Player = { id: string; name: string };
''',
            '''type Player = { id: string; name: string };

export type TestDirection = "higher_better" | "lower_better";
/** Clave con la que `getPhysicalProgress` devuelve el sentido de cada test. */
export const testDirectionKey = (name: string) => name.trim().toLowerCase();
''',
        ),
        (
            '''  playerId?: string | null;
};

const tonnage = ''',
            '''  playerId?: string | null;
  /** Sentido de cada test por `testDirectionKey(nombre)`; sin dato, más es mejor. */
  directions?: Record<string, TestDirection>;
};

const tonnage = ''',
        ),
        (
            '''              best: `${Math.max(...vals)} ${unit}`.trim(),''',
            '''              best: `${input.directions?.[testDirectionKey(n)] === "lower_better" ? Math.min(...vals) : Math.max(...vals)} ${unit}`.trim(),''',
        ),
    ],
    "src/routes/_authenticated/coach.progress.physical.tsx": [
        (
            'import { buildPhysicalProgressReport, PROGRESS_VARIANTS, type ProgressVariant } from "@/lib/reports/progress-report";',
            'import { buildPhysicalProgressReport, PROGRESS_VARIANTS, testDirectionKey, type ProgressVariant, type TestDirection } from "@/lib/reports/progress-report";',
        ),
        (
            '''const lowerIsBetter = (testName: string, unit: string | null | undefined) => {
  const normalized''',
            '''const lowerIsBetter = (testName: string, unit: string | null | undefined, directions?: Record<string, TestDirection>) => {
  const known = directions?.[testDirectionKey(testName)];
  if (known) return known === "lower_better";
  const normalized''',
        ),
        (
            'const direction = lowerIsBetter(activeTest, activeUnit) ? "lower" : "higher";',
            'const direction = lowerIsBetter(activeTest, activeUnit, data?.directions) ? "lower" : "higher";',
        ),
        (
            'buildPhysicalProgressReport({ players, tests, logs, sets, from, to, playerId: playerId || null }, variant)',
            'buildPhysicalProgressReport({ players, tests, logs, sets, from, to, playerId: playerId || null, directions: data?.directions }, variant)',
        ),
        (
            'const testChart = useMemo(() => buildTestChart(activeRows, chartPlayers, selectedVisible, showAverage, showBest), [activeRows, chartPlayers, selectedVisible, showAverage, showBest]);',
            'const testChart = useMemo(() => buildTestChart(activeRows, chartPlayers, selectedVisible, showAverage, showBest, direction === "lower"), [activeRows, chartPlayers, selectedVisible, showAverage, showBest, direction]);',
        ),
        (
            'players: ProgressPlayer[], selected: string[], showAverage: boolean, showBest: boolean): SeriesRow[] {\n  const dates = [...new Set(rows.map((row) => row.tested_at.slice(0, 10)))].sort();',
            'players: ProgressPlayer[], selected: string[], showAverage: boolean, showBest: boolean, lowerBetter = false): SeriesRow[] {\n  const dates = [...new Set(rows.map((row) => row.tested_at.slice(0, 10)))].sort();',
        ),
        (
            'const globalBest = allValues.length ? Math.max(...allValues) : null;',
            'const globalBest = allValues.length ? (lowerBetter ? Math.min(...allValues) : Math.max(...allValues)) : null;',
        ),
        (
            'if (showBest && globalBest !== null) item.teamBest = globalBest;\n    return item;',
            # Con un jugador elegido la línea es «Millor marca pròpia» (dataKey ownBest), que nunca se rellenaba.
            'if (showBest && globalBest !== null) { item.teamBest = globalBest; item.ownBest = globalBest; }\n    return item;',
        ),
    ],
}

out = {}
for rel, edits in EDITS.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    for old, new in edits:
        n = text.count(old)
        if n != 1:
            sys.exit(f"{rel}: el texto aparece {n} veces (se esperaba 1):\n{old[:120]}")
        text = text.replace(old, new)
    out[path] = text
for path, text in out.items():
    path.write_text(text, encoding="utf-8")
print("A-009 aplicado en", len(out), "archivos")
