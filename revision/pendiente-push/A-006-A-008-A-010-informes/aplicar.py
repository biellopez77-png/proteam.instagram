#!/usr/bin/env python3
"""A-006, A-008 y A-010 (informes PDF). Ejecutar en la raíz de proteamapp:
    python3 aplicar.py && bun run build
Cada sustitución debe encontrar su texto exactamente una vez; si no, no toca nada."""
import pathlib, sys

CAMBIOS = {
  "src/lib/reports/match-report.ts": [
    # A-006: los tramos abiertos del periodo actual se cerraban en el segundo 0
    # (liveClock.sec = 0) y esos jugadores salían con 0 minutos en el PDF.
    ("""  const aggMap = aggregate(events, stints, { period: m.period, sec: 0 });""",
     """  // A-006: los tramos sin salida del periodo actual se cierran con la última acción
  // registrada; con `sec: 0` esos jugadores salían con 0 minutos en el PDF.
  const liveSec = Math.max(
    0,
    ...events.filter((e) => e.period === m.period).map((e) => e.clock_sec),
    ...stints.filter((s) => s.period === m.period).map((s) => Math.max(s.in_sec, s.out_sec ?? 0)),
  );
  const aggMap = aggregate(events, stints, { period: m.period, sec: liveSec });"""),
    # A-010: el marcador de la cronología individual contaba solo los goles del jugador.
    ("""function timelineSection(events: MatchEvent[], players: MatchPlayer[], teamName: string, opponent: string): ReportSection {""",
     """function timelineSection(events: MatchEvent[], players: MatchPlayer[], teamName: string, opponent: string, onlyPlayerId?: string): ReportSection {"""),
    ("""    .filter((e) => !["period_start", "period_end", "match_end"].includes(e.type))
    .map((e) => {""",
     """    .filter((e) => !["period_start", "period_end", "match_end"].includes(e.type))
    .flatMap((e) => {"""),
    ("""      const p = e.player_id ? players.find((x) => x.id === e.player_id) : undefined;
      return {
        t: `${e.period}a · ${fmtClock(e.clock_sec)}`,""",
     """      // A-010: el marcador se calcula con todas las acciones; solo se filtran las filas.
      if (onlyPlayerId && e.player_id !== onlyPlayerId) return [];
      const p = e.player_id ? players.find((x) => x.id === e.player_id) : undefined;
      return [{
        t: `${e.period}a · ${fmtClock(e.clock_sec)}`,"""),
    ("""        note: txt(e.notes ?? null) ?? (e.shot_zone ? (SHOT_ZONES.find((z) => z.id === e.shot_zone)?.label ?? "") : ""),
      };
    });""",
     """        note: txt(e.notes ?? null) ?? (e.shot_zone ? (SHOT_ZONES.find((z) => z.id === e.shot_zone)?.label ?? "") : ""),
      }];
    });"""),
    ("""        timelineSection(mine, players, teamName, m.opponent),""",
     """        timelineSection(events, players, teamName, m.opponent, input.playerId),"""),
  ],
  "src/lib/reports/progress-report.ts": [
    # A-008: el informe de pista daba dos % de asistencia distintos. Se usa en todo
    # el informe el mismo cálculo que el resumen (`attendanceSummary`): sin contar
    # «pendent» y con «limitada» como asistencia.
    ("""    one(avgOf(reports.map((r) => r[k]).filter((v): v is number => typeof v === "number")));

  const sections: ReportSection[] = [""",
     """    one(avgOf(reports.map((r) => r[k]).filter((v): v is number => typeof v === "number")));
  const attendanceState = attendanceSummary(attendance);

  const sections: ReportSection[] = ["""),
    ("""            { label: "Assistència", value: pct(present + late, attendance.length) },""",
     """            { label: "Assistència", value: pct(attendanceState.attended, attendanceState.considered) },"""),
    ("""  const attendanceState = attendanceSummary(attendance);
  const ratingState = metricAverages(reports);""",
     """  const ratingState = metricAverages(reports);"""),
    ("""  const present = attendance.filter((a) => a.status === "present").length;
""", ""),
    ("""const ok = (s: string) => s === "present" || s === "tard";""",
     """const ok = (s: string) => s === "present" || s === "tard" || s === "limitada";"""),
    ("""      if (!d) continue;
      const b = bucket(d.slice(0, 7));""",
     """      if (!d || a.status === "pendent") continue;
      const b = bucket(d.slice(0, 7));"""),
    ("""                const p100 = rows2.length ? Math.round(((pr + lt) / rows2.length) * 100) : 0;""",
     """                const sum = attendanceSummary(rows2);
                const p100 = sum.attendancePct ?? 0;"""),
    ("""                    v: rows2.length ? `${p100}%` : "–",
                    tone: (!rows2.length ? "neutral" """,
     """                    v: sum.attendancePct != null ? `${p100}%` : "–",
                    tone: (sum.attendancePct == null ? "neutral" """),
  ],
}

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
nuevos = {}
for rel, subs in CAMBIOS.items():
    src = (root / rel).read_text()
    for old, new in subs:
        n = src.count(old)
        if n != 1:
            sys.exit(f"ERROR {rel}: el texto aparece {n} veces:\n{old[:120]}")
        src = src.replace(old, new)
    nuevos[rel] = src
for rel, src in nuevos.items():
    (root / rel).write_text(src)
    print("ok", rel)
