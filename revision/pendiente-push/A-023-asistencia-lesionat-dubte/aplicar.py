#!/usr/bin/env python3
"""A-023: al cerrar la sesión de pista, el estado previo «lesionat»/«dubte» se copiaba
tal cual a court_attendance.status (court.functions.ts, closeAttendance), y esos dos
valores no son estados de asistencia: el informe no los contaba ni como lesión ni como
asistencia y bajaban el % del jugador. Ahora:
  - al cerrar: disponible → present, lesionat → lesio, ausencias igual, dubte → sigue «pendent»
    (el entrenador decide; no se inventa asistencia);
  - al leer (attendanceSummary): las 4 filas antiguas (3 «lesionat», 1 «dubte») se leen como
    «lesio» y «pendent». No se toca la base de datos.
Uso (en la raíz de proteamapp): python3 aplicar.py && bun run build
"""
import pathlib, sys

def sub(path, old, new):
    p = pathlib.Path(path)
    s = p.read_text()
    if s.count(old) != 1:
        sys.exit(f"{path}: el fragmento no aparece exactamente una vez")
    p.write_text(s.replace(old, new))

# 1) court-model.ts: dos funciones puras junto a ATTENDANCE_STATUS
sub("src/lib/court-model.ts",
'''export const ATTENDANCE_TONE: Record<string, string> = {''',
'''/**
 * Pre-session status → attendance status when a session is closed with the
 * player still «pendent». «dubte» stays pending: nobody confirmed it.
 */
export function attendanceFromPreStatus(pre: string | null | undefined): string | null {
  switch (pre ?? "disponible") {
    case "disponible": return "present";
    case "lesionat": return "lesio";
    case "absencia_justificada":
    case "absencia_no_justificada": return pre as string;
    default: return null;
  }
}

/** Older rows stored a pre-session status as attendance («lesionat», «dubte»). */
export function normalizeAttendanceStatus(status: string): string {
  if (status === "lesionat") return "lesio";
  if (status === "dubte") return "pendent";
  return status;
}

export const ATTENDANCE_TONE: Record<string, string> = {''')

# 2) court.functions.ts: closeAttendance deja de copiar pre_status sin traducir
sub("src/lib/court.functions.ts",
'''    if (r.status === "pendent")
      patch["status"] = r.pre_status === "disponible" ? "present" : r.pre_status;''',
'''    if (r.status === "pendent") {
      const closed = attendanceFromPreStatus(r.pre_status);
      if (closed) patch["status"] = closed;
    }''')
sub("src/lib/court.functions.ts",
'''} from "@/lib/court-model";''',
'''} from "@/lib/court-model";
import { attendanceFromPreStatus } from "@/lib/court-model";''')

# 3) court-progress-dashboard.ts: lee las filas antiguas con su estado real
sub("src/lib/court-progress-dashboard.ts",
'''import { faultCounts, normalizeIncidentType } from "@/lib/court-model";''',
'''import { faultCounts, normalizeAttendanceStatus, normalizeIncidentType } from "@/lib/court-model";''')
sub("src/lib/court-progress-dashboard.ts",
'''export function attendanceSummary(rows: CourtAttendanceRow[]) {
  const present''',
'''export function attendanceSummary(input: CourtAttendanceRow[]) {
  const rows = input.map((row) => ({ ...row, status: normalizeAttendanceStatus(row.status) }));
  const present''')
print("A-023 aplicado: 3 archivos. Ahora: bun run build")
