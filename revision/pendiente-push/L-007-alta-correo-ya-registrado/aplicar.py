#!/usr/bin/env python3
"""L-007 (mejora continua, landing y lista de espera, 19/11 8:17 Madrid).

Error: un entrenador que ya tiene cuenta confirmada vuelve a la portada, pulsa
«Apúntate a la lista de espera» y rellena el alta con el mismo correo. Supabase
(con confirmación por correo activada: 35 de 65 cuentas se confirmaron después
de crearse) no devuelve error en ese caso: devuelve un usuario sin identidades,
sin sesión, y NO envía ningún correo. `AuthForm.submit`
(`src/components/auth-overlay.tsx`, línea 70) solo mira `data.session`, así que
enseña «Revisa el teu correu» y el entrenador espera un enlace que nunca llega
(y puede pensar que la lista de espera no funciona).

Arreglo (1 archivo + 7 diccionarios, sin BD):
- Si `data.user.identities` viene vacío y no hay sesión → pasa a «Iniciar sesión»
  y avisa «Ya tienes una cuenta con este correo. Inicia sesión.»
Compatible con los scripts de L-001 y M-009/M-010 (tocan otras líneas del mismo
archivo); se puede aplicar antes o después.

Uso (en la raíz de proteamapp):  python3 aplicar.py && bun run build
"""
import json, pathlib, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
KEY = "Ya tienes una cuenta con este correo. Inicia sesión."
TR = {
    "es": KEY,
    "ca": "Ja tens un compte amb aquest correu. Inicia sessió.",
    "en": "You already have an account with this email. Sign in.",
    "fr": "Un compte existe déjà avec cet e-mail. Connectez-vous.",
    "pt": "Já existe uma conta com este e-mail. Inicie sessão.",
    "de": "Mit dieser E-Mail gibt es bereits ein Konto. Bitte anmelden.",
    "it": "Esiste già un account con questa email. Accedi.",
}

src = root / "src/components/auth-overlay.tsx"
code = src.read_text(encoding="utf-8")
REPL = [
    ('''        });
        if (error) throw error;
        if (data.session) {''',
     '''        });
        if (error) throw error;
        // Correo ya registrado y confirmado: Supabase devuelve un usuario sin identidades,
        // sin sesión y sin enviar correo. Sin este aviso el entrenador espera un enlace que no llega.
        if (!data.session && data.user && data.user.identities?.length === 0) {
          setMode("login");
          toast.error(t("Ya tienes una cuenta con este correo. Inicia sesión."));
          return;
        }
        if (data.session) {'''),
]
for old, new in REPL:
    if code.count(old) != 1:
        sys.exit(f"auth-overlay.tsx ha cambiado (no encuentro una vez: {old[:60]!r}); revisar a mano")
    code = code.replace(old, new)
src.write_text(code, encoding="utf-8")
print("auth-overlay.tsx: aviso de correo ya registrado")

for lang, value in TR.items():
    p = root / "src/lib/i18n/dict" / f"{lang}.json"
    raw = p.read_text(encoding="utf-8")
    d = json.loads(raw)
    if d.get(KEY):
        print(f"{lang}: ya estaba"); continue
    d[KEY] = value
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
    print(f"{lang}: clave añadida")
