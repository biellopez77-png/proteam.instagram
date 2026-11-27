#!/usr/bin/env python3
"""A-035 y M-017 (mejora continua, planificación: detalle de una actividad, 20/11 9:17 Madrid).

Archivo: `src/components/planning/activity-drawer.tsx` (panel lateral que se abre al
tocar una actividad en la agenda de Planificación).

A-035 (error, texto): la fila «Estat» pinta el código interno tal cual
(`<dd>{it.status}</dd>`). En BD hay sesiones de pista `programada` (24),
`finalitzada` (32), `esborrany` (1) y xerrades/dinàmiques `en_curs` (1) y
`planificada` (3): el entrenador ve «en_curs» o «finalitzada» en minúscula y sin
traducir en cualquier idioma. Los botones de estado del mismo panel sí usan
`EVENT_STATUS_LABEL`. Arreglo: etiqueta legible y traducida (`EVENT_STATUS_LABEL`
para actividades, mapa nuevo para pista); si llega un estado desconocido se ve
como antes.

M-017 (accesibilidad/uso): el panel (`role="dialog"`) no se cierra con Escape,
no tiene `aria-modal` y el botón «Eliminar» no se desactiva mientras borra (doble
toque = segundo borrado que acaba en error). Arreglo: Escape cierra, `aria-modal`,
«Eliminar» desactivado mientras `remove.isPending`.

Textos nuevos: «Programada» y «Finalitzada» (se añaden a los 7 diccionarios si
faltan). Sin BD, sin servidor.

Uso (en la raíz de proteamapp):  python3 aplicar.py && bun run build
"""
import json, pathlib, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
src = root / "src/components/planning/activity-drawer.tsx"
code = src.read_text(encoding="utf-8")

subs = [
    # 1. etiqueta del estado
    ("""          {it.status && (
            <>
              <dt className="text-muted-foreground">Estat</dt>
              <dd>{it.status}</dd>""",
     """          {it.status && (
            <>
              <dt className="text-muted-foreground">Estat</dt>
              <dd>{tr(statusLabel(it.type, it.status))}</dd>"""),
    # 2. Escape cierra el panel (hook antes del `return null`)
    ("""    setConfirmMsg(null);
    setShowResched(false);
  }, [entry]);
""",
     """    setConfirmMsg(null);
    setShowResched(false);
  }, [entry]);

  useEffect(() => {
    if (!entry) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [entry, onClose]);
"""),
    # 3. aria-modal
    ("""      role="dialog"
      aria-label="Detall de l'activitat"
    >""",
     """      role="dialog"
      aria-modal="true"
      aria-label="Detall de l'activitat"
    >"""),
    # 4. «Eliminar» sin doble borrado
    ("""                  if (confirm(`${tr("Segur que vols eliminar aquesta activitat?")}${physicalNote}`)) remove.mutate();
                }}
                className="inline-flex items-center gap-1.5 rounded-lg px-2.5 py-1.5 text-xs font-medium text-destructive hover:bg-destructive/10"
              >""",
     """                  if (confirm(`${tr("Segur que vols eliminar aquesta activitat?")}${physicalNote}`)) remove.mutate();
                }}
                disabled={remove.isPending}
                className="inline-flex items-center gap-1.5 rounded-lg px-2.5 py-1.5 text-xs font-medium text-destructive hover:bg-destructive/10 disabled:opacity-50"
              >"""),
    # 5. mapa de etiquetas
    ("""/** Side panel with the full detail and contextual actions of one activity. */""",
     """const COURT_STATUS_LABEL: Record<string, string> = {
  esborrany: "Esborrany",
  programada: "Programada",
  finalitzada: "Finalitzada",
};

/** Readable label for a stored status code; unknown codes are shown as they are. */
function statusLabel(type: string, status: string): string {
  const labels: Record<string, string> =
    type === "event" ? EVENT_STATUS_LABEL : type === "court" ? COURT_STATUS_LABEL : {};
  return labels[status] ?? status;
}

/** Side panel with the full detail and contextual actions of one activity. */"""),
]
for old, new in subs:
    if code.count(old) != 1:
        sys.exit(f"activity-drawer.tsx ha cambiado; no encuentro:\n{old[:120]}…\nrevisar a mano")
    code = code.replace(old, new)
src.write_text(code, encoding="utf-8")
print("activity-drawer.tsx: estado legible, Escape, aria-modal y «Eliminar» sin doble borrado")

T = {
    "Programada": dict(ca="Programada", es="Programada", en="Scheduled", fr="Programmée", pt="Agendada", de="Geplant", it="Programmata"),
    "Finalitzada": dict(ca="Finalitzada", es="Finalizada", en="Finished", fr="Terminée", pt="Concluída", de="Abgeschlossen", it="Terminata"),
}
for lang in ("ca", "es", "en", "fr", "pt", "de", "it"):
    p = root / "src/lib/i18n/dict" / f"{lang}.json"
    raw = p.read_text(encoding="utf-8")
    d = json.loads(raw)
    n = 0
    for key, tr in T.items():
        if not (isinstance(d.get(key), str) and d[key].strip()):
            d[key] = tr[lang]
            n += 1
    if n:
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
    print(f"{lang}: {n} textos añadidos")
