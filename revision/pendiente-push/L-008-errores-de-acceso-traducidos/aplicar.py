#!/usr/bin/env python3
"""L-008 (mejora continua, landing y lista de espera, 20/11 18:17 Madrid).

Error: los fallos de acceso y alta del panel de la portada llegan al entrenador
en inglés crudo de Supabase. `AuthForm.submit` (`src/components/auth-overlay.tsx`,
`catch` de `submit`) hace `toast.error(t(err.message))`, y ninguno de los textos
de Supabase está en los diccionarios (`dict/es.json`, commit 488db5e: 0 resultados
para «Invalid login credentials», «Email not confirmed», «rate limit»,
«Password should», «User already registered»). Así:
- contraseña mal → «Invalid login credentials»;
- cuenta sin confirmar → «Email not confirmed», sin forma de pedir otro enlace.
  BD 20/11: 4 de 67 cuentas siguen sin confirmar desde el 17/11; no tienen equipo
  y por tanto NO están en la lista de espera;
- sin cobertura → «Failed to fetch».

Arreglo (1 archivo + 7 diccionarios, sin BD):
- Mensajes propios, traducidos, según el código de error de Supabase.
- «Email not confirmed»: reenvía el enlace de confirmación (`auth.resend`,
  type "signup") y enseña la pantalla «Revisa tu correo» que ya existe.
Compatible con L-001, L-007 y M-009/M-010 (tocan otras líneas del mismo archivo).

Uso (en la raíz de proteamapp):  python3 aplicar.py && bun run build
"""
import json, pathlib, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")

TR = {
    "Correo o contraseña incorrectos.": {
        "ca": "Correu o contrasenya incorrectes.",
        "en": "Wrong email or password.",
        "fr": "E-mail ou mot de passe incorrect.",
        "pt": "E-mail ou palavra-passe incorretos.",
        "de": "E-Mail oder Passwort falsch.",
        "it": "Email o password errati.",
    },
    "Tu cuenta aún no está confirmada. Te hemos enviado otro enlace.": {
        "ca": "El teu compte encara no està confirmat. T'hem enviat un altre enllaç.",
        "en": "Your account isn't confirmed yet. We've sent you another link.",
        "fr": "Votre compte n'est pas encore confirmé. Nous vous avons envoyé un nouveau lien.",
        "pt": "A tua conta ainda não está confirmada. Enviámos-te outro link.",
        "de": "Dein Konto ist noch nicht bestätigt. Wir haben dir einen neuen Link geschickt.",
        "it": "Il tuo account non è ancora confermato. Ti abbiamo inviato un altro link.",
    },
    "Demasiados intentos. Espera unos minutos y vuelve a probar.": {
        "ca": "Massa intents. Espera uns minuts i torna-ho a provar.",
        "en": "Too many attempts. Wait a few minutes and try again.",
        "fr": "Trop de tentatives. Attendez quelques minutes et réessayez.",
        "pt": "Demasiadas tentativas. Espera alguns minutos e tenta de novo.",
        "de": "Zu viele Versuche. Warte ein paar Minuten und versuche es erneut.",
        "it": "Troppi tentativi. Aspetta qualche minuto e riprova.",
    },
    "La contraseña es demasiado débil: usa al menos 8 caracteres.": {
        "ca": "La contrasenya és massa feble: fes servir almenys 8 caràcters.",
        "en": "The password is too weak: use at least 8 characters.",
        "fr": "Le mot de passe est trop faible : utilisez au moins 8 caractères.",
        "pt": "A palavra-passe é demasiado fraca: usa pelo menos 8 caracteres.",
        "de": "Das Passwort ist zu schwach: mindestens 8 Zeichen verwenden.",
        "it": "La password è troppo debole: usa almeno 8 caratteri.",
    },
    "Ya tienes una cuenta con este correo. Inicia sesión.": {  # misma clave que L-007
        "ca": "Ja tens un compte amb aquest correu. Inicia sessió.",
        "en": "You already have an account with this email. Sign in.",
        "fr": "Un compte existe déjà avec cet e-mail. Connectez-vous.",
        "pt": "Já existe uma conta com este e-mail. Inicie sessão.",
        "de": "Mit dieser E-Mail gibt es bereits ein Konto. Bitte anmelden.",
        "it": "Esiste già un account con questa email. Accedi.",
    },
    "Revisa el correo: no parece una dirección válida.": {
        "ca": "Revisa el correu: no sembla una adreça vàlida.",
        "en": "Check the email: it doesn't look like a valid address.",
        "fr": "Vérifiez l'e-mail : l'adresse ne semble pas valide.",
        "pt": "Revê o e-mail: não parece um endereço válido.",
        "de": "Prüfe die E-Mail: Die Adresse scheint ungültig zu sein.",
        "it": "Controlla l'email: non sembra un indirizzo valido.",
    },
    "Sin conexión. Revisa la cobertura y vuelve a probar.": {
        "ca": "Sense connexió. Revisa la cobertura i torna-ho a provar.",
        "en": "No connection. Check your signal and try again.",
        "fr": "Pas de connexion. Vérifiez le réseau et réessayez.",
        "pt": "Sem ligação. Verifica a rede e tenta de novo.",
        "de": "Keine Verbindung. Prüfe den Empfang und versuche es erneut.",
        "it": "Nessuna connessione. Controlla la rete e riprova.",
    },
}

HELPER = '''
/** Supabase auth errors come in raw English; map the known ones to our own translated texts. */
function authErrorText(err: unknown): string | null {
  const code = (err as { code?: string } | null)?.code ?? "";
  const msg = err instanceof Error ? err.message : "";
  if (code === "invalid_credentials" || /invalid login credentials/i.test(msg)) return "Correo o contraseña incorrectos.";
  if (code.startsWith("over_") || /rate limit/i.test(msg)) return "Demasiados intentos. Espera unos minutos y vuelve a probar.";
  if (code === "weak_password" || /password should/i.test(msg)) return "La contraseña es demasiado débil: usa al menos 8 caracteres.";
  if (code === "user_already_exists" || /already registered/i.test(msg)) return "Ya tienes una cuenta con este correo. Inicia sesión.";
  if (code === "email_address_invalid" || /invalid format|email address .* is invalid/i.test(msg)) return "Revisa el correo: no parece una dirección válida.";
  if (/failed to fetch|network/i.test(msg)) return "Sin conexión. Revisa la cobertura y vuelve a probar.";
  return null;
}
'''

src = root / "src/components/auth-overlay.tsx"
code = src.read_text(encoding="utf-8")
REPL = [
    ('''export type AuthMode = "login" | "register";
''',
     '''export type AuthMode = "login" | "register";
''' + HELPER),
    ('''    } catch (err) {
      toast.error(err instanceof Error ? t(err.message) : t("Error"));
    } finally {
      setLoading(false);''',
     '''    } catch (err) {
      const target = email.trim();
      // Cuenta sin confirmar: se reenvía el enlace y se enseña «Revisa tu correo».
      if ((err as { code?: string } | null)?.code === "email_not_confirmed" || (err instanceof Error && /email not confirmed/i.test(err.message))) {
        await supabase.auth.resend({ type: "signup", email: target, options: { emailRedirectTo: `${window.location.origin}/teams` } });
        setAwaitConfirm(target);
        toast.success(t("Tu cuenta aún no está confirmada. Te hemos enviado otro enlace."));
        return;
      }
      const known = authErrorText(err);
      if (known === "Ya tienes una cuenta con este correo. Inicia sesión.") setMode("login");
      toast.error(known ? t(known) : err instanceof Error ? t(err.message) : t("Error"));
    } finally {
      setLoading(false);'''),
]
for old, new in REPL:
    if code.count(old) != 1:
        sys.exit(f"auth-overlay.tsx ha cambiado (no encuentro una vez: {old[:60]!r}); revisar a mano")
    code = code.replace(old, new)
src.write_text(code, encoding="utf-8")
print("auth-overlay.tsx: errores de acceso traducidos y reenvío de confirmación")

for lang in ["es", "ca", "en", "fr", "pt", "de", "it"]:
    p = root / "src/lib/i18n/dict" / f"{lang}.json"
    raw = p.read_text(encoding="utf-8")
    d = json.loads(raw)
    added = 0
    for key, tr in TR.items():
        if d.get(key):
            continue
        d[key] = key if lang == "es" else tr[lang]
        added += 1
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
    print(f"{lang}: {added} claves añadidas")
