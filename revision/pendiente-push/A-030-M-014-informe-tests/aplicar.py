#!/usr/bin/env python3
"""A-030 + M-014 · Informe PDF de tests físicos.
Uso: python3 aplicar.py <raíz de proteamapp>
A-030: el PDF de tests contaba a los entrenadores como plantilla («Plantilla», «Sense marca»
y una página vacía por entrenador en el informe individual), y la dirección «menos es mejor»
solo salía de los tests programados: un test hecho desde la biblioteca sin programar
(p. ej. «5-10-5 Shuttle») se ordenaba al revés.
M-014: «hoy» en tests programados y en el PDF se calculaba en UTC (entre las 00:00 y las
01:00/02:00 de Madrid el test de ayer seguía en «Propers i d'avui») y la fecha de la tarjeta
se leía en UTC (un día menos al oeste de Greenwich)."""
import sys, pathlib
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
CAMBIOS = {
 "src/routes/_authenticated/coach.tests.tsx": [
  ('import { dateLocale } from "@/lib/date-utils";',
   'import { dateLocale, todayISO } from "@/lib/date-utils";'),
  ('  const playersHeadFn = useServerFn(listPlayers);\n',
   '  const playersHeadFn = useServerFn(listPlayers);\n  const catalogHeadFn = useServerFn(listTestCatalog);\n'),
  ('  const { data: allPlayers = [] } = useQuery({ queryKey: ["players"], queryFn: () => playersHeadFn() });\n',
   '  const { data: allPlayers = [] } = useQuery({ queryKey: ["players"], queryFn: () => playersHeadFn() });\n'
   '  const { data: allCatalog = [] } = useQuery({ queryKey: ["catalog"], queryFn: () => catalogHeadFn() });\n'),
  ('                    players: allPlayers.map((p) => ({\n',
   '                    players: allPlayers.filter((p) => !p.roles.includes("coach")).map((p) => ({\n'),
  ('                    direction: Object.fromEntries(\n                      allAssignments.map((a) => [\n',
   '                    direction: Object.fromEntries(\n                      [...allCatalog, ...allAssignments].map((a) => [\n'),
  ('  const today = new Date().toISOString().slice(0, 10);\n  const upcoming = assignments.filter',
   '  const today = todayISO();\n  const upcoming = assignments.filter'),
  ('{new Date(a.test_date).toLocaleDateString(dateLocale(),',
   '{new Date(`${a.test_date}T00:00:00`).toLocaleDateString(dateLocale(),'),
 ],
 "src/lib/reports/tests-report.ts": [
  ('import { translate as tr } from "@/lib/i18n/translate";\n',
   'import { translate as tr } from "@/lib/i18n/translate";\nimport { todayISO } from "@/lib/date-utils";\n'),
  ('  const { assignments, players } = input;\n  const today = new Date().toISOString().slice(0, 10);',
   '  const { assignments, players } = input;\n  const today = todayISO();'),
 ],
}
for rel, pares in CAMBIOS.items():
    f = root / rel; s = f.read_text()
    for old, new in pares:
        n = s.count(old)
        if n != 1: sys.exit(f"{rel}: esperaba 1 coincidencia y hay {n}: {old[:70]!r}")
        s = s.replace(old, new)
    f.write_text(s); print("ok", rel)
