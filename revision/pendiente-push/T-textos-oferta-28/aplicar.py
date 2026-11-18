#!/usr/bin/env python3
"""Textos públicos de la oferta (encargo de Biel, 18/11, tarea t-dir-copy-prueba).

Hasta el 27/11 23:59 (Madrid): «3 meses gratis si te apuntas antes del 28 de noviembre».
Desde el 28/11 00:00: «1 mes de prueba». El cambio va por fecha (blackoutActive), sin
tocar nada el día 28. Nunca se pone el precio en estos textos.

Toca: páginas de fútbol/baloncesto/balonmano, botón final del blog (PublicCta), los 3
artículos del blog, la hoja «Leyenda» del Excel de la plantilla y 6 textos nuevos en los
7 diccionarios. Uso (en la raíz de proteamapp):  python3 aplicar.py && bun run build
"""
import json, pathlib, sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
OFFER = "3 meses gratis si te apuntas antes del 28 de noviembre"
TRIAL_BTN = "Empieza con 1 mes de prueba"

def sub(path, pairs):
    p = ROOT / path
    s = p.read_text(encoding="utf-8")
    for old, new in pairs:
        n = s.count(old)
        if n != 1:
            sys.exit(f"ERROR {path}: el fragmento aparece {n} veces: {old[:70]!r}")
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")
    print("ok", path)

if "publicOffer" in (ROOT / "src/lib/blackout-friday.ts").read_text(encoding="utf-8"):
    sys.exit("Ya aplicado: no se hace nada.")

# 1. Fecha única de la oferta
sub("src/lib/blackout-friday.ts", [(
    "export function blackoutRemaining(",
    "/** Oferta pública (Biel, 18/11): 3 meses solo con la lista de espera hasta el 27/11;\n"
    " *  desde el 28/11, 1 mes de prueba. Nunca se pone el precio. Solo para textos en castellano\n"
    " *  (blog, Excel); en pantalla se usan literales para que pasen por los diccionarios. */\n"
    "export function publicOffer(now: number) {\n"
    f"  return blackoutActive(now) ? \"{OFFER}\" : \"1 mes de prueba\";\n"
    "}\n\n"
    "export function blackoutRemaining(",
)])

# 2. Páginas de deporte: botón, línea de la oferta y pregunta frecuente sin precio
sub("src/components/landing/sport-page.tsx", [
    ('import { absoluteUrl, publicHead } from "@/lib/site";',
     'import { absoluteUrl, publicHead } from "@/lib/site";\nimport { blackoutActive } from "@/lib/blackout-friday";'),
    ("export function SportPage({ c }: { c: SportPageContent }) {\n  return (",
     "export function SportPage({ c }: { c: SportPageContent }) {\n  const offer = blackoutActive(Date.now());\n  return ("),
    ('search={{ auth: "register" }}>Empieza gratis 3 meses <ArrowRight /></Link>',
     f'search={{{{ auth: "register" }}}}>{{offer ? "Apúntate a la lista de espera" : "{TRIAL_BTN}"}} <ArrowRight /></Link>'),
    ('<Link to="/pricing">Ver precios</Link></Button>\n            </div>',
     '<Link to="/pricing">Ver precios</Link></Button>\n            </div>\n'
     f'            {{offer && <p className="mt-3 text-sm text-muted-foreground">{OFFER}</p>}}'),
    ("            ))}\n          </div>\n        </section>\n      </main>",
     "            ))}\n"
     '            <div className="rounded-xl border border-border bg-card/60 p-4">\n'
     '              <h3 className="font-semibold">¿Hay prueba gratis?</h3>\n'
     f'              <p className="mt-2 text-sm leading-6 text-muted-foreground">{{offer ? "{OFFER}" : "1 mes de prueba"}}</p>\n'
     "            </div>\n"
     "          </div>\n        </section>\n      </main>"),
])

# 3. Rutas de deporte: descripción sin oferta (Google la guarda semanas) y fuera «¿Cuánto cuesta?» con precio
DESC = {
    "futbol": "App para entrenadores de fútbol y fútbol 7: planifica la temporada, prepara entrenamientos, controla la carga y analiza partidos con xG y duelos.",
    "baloncesto": "App para entrenadores de baloncesto: planifica la temporada, prepara entrenamientos y sigue eFG%, +/− y faltas en el partido en directo.",
    "balonmano": "App para entrenadores de balonmano: planifica la temporada, prepara entrenamientos y analiza paradas por zona, contraataques y exclusiones.",
}
FAQ = {
    "futbol": '    { q: "¿Cuánto cuesta?", a: "El primer equipo cuesta 9,90 € al mes o 95 € al año, con 3 meses gratis. Los equipos adicionales cuestan 7,50 € al mes." },\n',
    "baloncesto": '    { q: "¿Cuánto cuesta?", a: "El primer equipo cuesta 9,90 € al mes o 95 € al año, con 3 meses gratis. Los equipos adicionales cuestan 7,50 € al mes." },\n',
    "balonmano": '    { q: "¿Cuánto cuesta?", a: "El primer equipo cuesta 9,90 € al mes o 95 € al año, y el primer equipo tiene 3 meses gratis. Los equipos adicionales cuestan 7,50 € al mes." },\n',
}
for slug, d in DESC.items():
    sub(f"src/routes/{slug}.tsx", [(f'description: "{d} 3 meses gratis.",', f'description: "{d}",'), (FAQ[slug], "")])

# 4. Botón final del blog
sub("src/components/public/content-shell.tsx", [
    ("import { ArrowRight, Download } from 'lucide-react';",
     "import { ArrowRight, Download } from 'lucide-react';\nimport { blackoutActive } from '@/lib/blackout-friday';"),
    ("export function PublicCta({ template = false }: {template?:boolean}) {\n return ",
     "export function PublicCta({ template = false }: {template?:boolean}) {\n const offer = blackoutActive(Date.now());\n return "),
    ("{template ? 'Probar ProTeam: primer equipo 3 meses gratis' : 'Planifícalo en ProTeam'}",
     f"{{template ? (offer ? 'Apúntate a la lista de espera' : '{TRIAL_BTN}') : 'Planifícalo en ProTeam'}}"),
    ("<ArrowRight className=\"shrink-0\"/></Link></Button></div></section>;",
     f"<ArrowRight className=\"shrink-0\"/></Link></Button></div>{{template && offer && <p className=\"mt-3 text-sm text-muted-foreground\">{OFFER}</p>}}</section>;"),
])

# 5. Artículos del blog (solo castellano)
sub("src/lib/blog-posts.ts", [
    ("export const BLOG_DATE", "import { publicOffer } from '@/lib/blackout-friday';\nexport const BLOG_DATE"),
    ("**Prueba ProTeam App: tu primer equipo, 3 meses gratis.**", "**Prueba ProTeam App: {oferta}.**"),
    ("**prueba ProTeam App: tu primer equipo, 3 meses gratis**.", "**prueba ProTeam App: {oferta}**."),
    ("**Pruébalo gratis 3 meses con tu primer equipo.**", "**Pruébalo con tu primer equipo: {oferta}.**"),
    ("return markdown.replaceAll('{enlace_plantilla}', '/recursos/plantilla-planificacion')",
     "return markdown.replaceAll('{oferta}', publicOffer(Date.now())).replaceAll('{enlace_plantilla}', '/recursos/plantilla-planificacion')"),
])

# 6. Excel de la plantilla: el archivo se queda en el ordenador del entrenador, va con la fecha de descarga
sub("src/lib/planning-template.ts", [
    ("import type ExcelJS from 'exceljs';", "import type ExcelJS from 'exceljs';\nimport { publicOffer } from '@/lib/blackout-friday';"),
    ("'¿Quieres hacerlo sin fórmulas y para todo el club? Prueba ProTeam App: tu primer equipo, 3 meses gratis en pro-team.app',",
     "'¿Quieres hacerlo sin fórmulas y para todo el club? Prueba ProTeam App en pro-team.app: ' + publicOffer(Date.now()) + '.',"),
])

# 6b. Prueba del cambio de fecha
(ROOT / "src/lib/public-offer.test.ts").write_text("""import { describe, it, expect } from "vitest";
import { publicOffer } from "./blackout-friday";

describe("publicOffer", () => {
  it("3 meses solo hasta el 27/11 a las 23:59 de Madrid", () => {
    expect(publicOffer(Date.parse("2026-11-27T23:58:00+01:00"))).toBe("3 meses gratis si te apuntas antes del 28 de noviembre");
  });
  it("1 mes de prueba desde el 28/11 y nunca el precio", () => {
    const text = publicOffer(Date.parse("2026-11-28T00:00:00+01:00"));
    expect(text).toBe("1 mes de prueba");
    expect(text).not.toMatch(/€|\\d+,\\d{2}/);
  });
});
""", encoding="utf-8")
print("ok src/lib/public-offer.test.ts")

# 7. Diccionarios
NEW = {
    OFFER: {"ca": "3 mesos gratis si t'apuntes abans del 28 de novembre", "en": "3 months free if you sign up before 28 November",
            "fr": "3 mois gratuits si vous vous inscrivez avant le 28 novembre", "pt": "3 meses grátis se se inscrever antes de 28 de novembro",
            "de": "3 Monate kostenlos bei Anmeldung vor dem 28. November", "it": "3 mesi gratis se ti iscrivi prima del 28 novembre"},
    "1 mes de prueba": {"ca": "1 mes de prova", "en": "1-month trial", "fr": "1 mois d'essai", "pt": "1 mês de teste", "de": "1 Monat Testphase", "it": "1 mese di prova"},
    TRIAL_BTN: {"ca": "Comença amb 1 mes de prova", "en": "Start with a 1-month trial", "fr": "Commencez avec 1 mois d'essai",
                "pt": "Comece com 1 mês de teste", "de": "Mit 1 Monat Testphase starten", "it": "Inizia con 1 mese di prova"},
    "¿Hay prueba gratis?": {"ca": "Hi ha prova gratuïta?", "en": "Is there a free trial?", "fr": "Y a-t-il un essai gratuit ?",
                            "pt": "Existe teste grátis?", "de": "Gibt es eine kostenlose Testphase?", "it": "C'è una prova gratuita?"},
}
TAIL = {"ca": " 3 mesos gratis.", "en": " 3 months free.", "fr": " 3 mois gratuits.", "pt": " 3 meses grátis.", "de": " 3 Monate kostenlos.", "it": " 3 mesi gratis."}
for lang in ["ca", "es", "en", "fr", "pt", "de", "it"]:
    p = ROOT / f"src/lib/i18n/dict/{lang}.json"
    raw = p.read_text(encoding="utf-8")
    d = json.loads(raw)
    if "Apúntate a la lista de espera" not in d:
        sys.exit(f"ERROR {lang}: falta «Apúntate a la lista de espera»")
    for k, tr in NEW.items():
        d[k] = k if lang == "es" else tr[lang]
    for desc in DESC.values():
        old = d.get(desc + " 3 meses gratis.")
        if lang == "es":
            d[desc] = desc
        else:
            if not old or not old.endswith(TAIL[lang]):
                sys.exit(f"ERROR {lang}: descripción inesperada: {old!r}")
            d[desc] = old[: -len(TAIL[lang])]
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
    print("ok", p.relative_to(ROOT))
print("Hecho. Ahora: bun run build")
