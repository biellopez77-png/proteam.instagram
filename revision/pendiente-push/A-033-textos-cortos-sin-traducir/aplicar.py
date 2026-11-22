#!/usr/bin/env python3
"""A-033 / mejora continua (traducciones, 18/11 20:17): textos cortos (1–2
palabras) que salen en castellano en en, fr, pt, de e it.

T-04 rellenó los textos de 3 palabras o más; estos 8 se quedaron fuera y siguen
con el valor igual a la clave en `src/lib/i18n/dict/{en,fr,pt,de,it}.json`:

- Pie de todas las páginas públicas, también la portada
  (`src/components/public-footer.tsx`, líneas 17–18): «Ejercicios», «Plantilla gratis».
- Ficha pública de ejercicio (`src/routes/ejercicios.$slug.tsx`, línea 7): títulos
  «Objetivo», «Desarrollo», «Variantes».
- Blog (`src/routes/blog.index.tsx`, línea 6): «Leer artículo».
- Plantilla gratis (`src/routes/recursos.plantilla-planificacion.tsx`, línea 18):
  «Nombre» y el botón «Preparando plantilla…».

Además, en ca «Variantes» se quedó en castellano (en catalán es «Variants»).

Solo cambia claves cuyo valor sigue siendo la clave; conserva orden y final de
archivo. Las palabras que ya son correctas en el idioma (fr «Variantes», pt
«Objetivo», pt «Variantes») no se tocan.

Uso (en la raíz de proteamapp):  python3 aplicar.py && bun run build
"""
import json, pathlib, sys

T = {
    "Ejercicios": dict(en="Exercises", fr="Exercices", pt="Exercícios", de="Übungen", it="Esercizi"),
    "Plantilla gratis": dict(en="Free template", fr="Modèle gratuit", pt="Modelo grátis", de="Kostenlose Vorlage", it="Modello gratuito"),
    "Objetivo": dict(en="Objective", fr="Objectif", pt="Objetivo", de="Ziel", it="Obiettivo"),
    "Desarrollo": dict(en="Setup", fr="Déroulement", pt="Desenvolvimento", de="Ablauf", it="Svolgimento"),
    "Variantes": dict(en="Variations", fr="Variantes", pt="Variantes", de="Varianten", it="Varianti", ca="Variants"),
    "Leer artículo": dict(en="Read article", fr="Lire l'article", pt="Ler artigo", de="Artikel lesen", it="Leggi l'articolo"),
    "Nombre": dict(en="Name", fr="Nom", pt="Nome", de="Name", it="Nome"),
    "Preparando plantilla…": dict(en="Preparing template…", fr="Préparation du modèle…", pt="A preparar o modelo…", de="Vorlage wird vorbereitet…", it="Preparazione del modello…"),
}

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
total = 0
for lang in ("ca", "en", "fr", "pt", "de", "it"):
    p = root / "src/lib/i18n/dict" / f"{lang}.json"
    raw = p.read_text(encoding="utf-8")
    d = json.loads(raw)
    n = 0
    for key, tr in T.items():
        if lang not in tr:
            continue
        if key not in d:
            sys.exit(f"{lang}: falta la clave {key!r}; el diccionario ha cambiado, revisar a mano")
        if d[key] == key and tr[lang] != key:
            d[key] = tr[lang]
            n += 1
    if n:
        out = json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else "")
        p.write_text(out, encoding="utf-8")
    print(f"{lang}: {n} textos traducidos")
    total += n
print(f"Total: {total}")
