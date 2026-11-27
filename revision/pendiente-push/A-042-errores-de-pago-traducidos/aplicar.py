#!/usr/bin/env python3
"""A-042 · Errores de pago en el idioma del entrenador (y sin detalles internos).

Uso, desde la raíz de proteamapp:  python3 <ruta>/aplicar.py
Luego: bun run build (i18n:check + vite build), git diff, rama revision/errores-pago-traducidos y PR.

1. src/lib/stripe.server.ts · getStripeErrorMessage devolvía el texto crudo del error
   (inglés de Stripe o «STRIPE_LIVE_API_KEY is not configured») al pagar o abrir el
   portal. Ahora lo apunta en el registro del servidor y devuelve una frase catalana
   (idioma fuente) que la capa de traducción pasa al idioma del entrenador.
2. src/lib/i18n/dict/{es,en,fr,pt,de,it}.json · traducciones de esa frase y de la que
   devuelve getCheckoutResult al volver del pago («No s'ha pogut comprovar l'estat del
   pagament…»), que no estaba en ningún diccionario y salía en catalán en /pricing.
3. src/routes/pricing.tsx · ese aviso pide «Torna-ho a provar», pero la página ya había
   borrado el session_id de la dirección antes de mirar el resultado: recargar no
   reintentaba nada. Ahora solo se limpia la dirección cuando la comprobación ha ido bien.
"""
import json, pathlib, sys

root = pathlib.Path(".")
server = root / "src/lib/stripe.server.ts"
OLD = '''export function getStripeErrorMessage(error: unknown): string {
  if (error && typeof error === "object" && "message" in error && typeof error.message === "string") return error.message;
  return "Stripe request failed";
}'''
NEW = '''/** Never show raw Stripe or configuration messages to the coach: log them, return copy. */
export function getStripeErrorMessage(error: unknown): string {
  console.error("[stripe]", error instanceof Error ? error.message : error);
  return "No s'ha pogut connectar amb el sistema de pagament. Torna-ho a provar.";
}'''

PAY = "No s'ha pogut connectar amb el sistema de pagament. Torna-ho a provar."
CHECK = "No s'ha pogut comprovar l'estat del pagament. Torna-ho a provar."
T = {
  "es": {PAY: "No se ha podido conectar con el sistema de pago. Inténtalo de nuevo.",
         CHECK: "No se ha podido comprobar el estado del pago. Inténtalo de nuevo."},
  "en": {PAY: "We couldn't connect to the payment system. Please try again.",
         CHECK: "We couldn't check the payment status. Please try again."},
  "fr": {PAY: "Impossible de se connecter au système de paiement. Réessaie.",
         CHECK: "Impossible de vérifier l'état du paiement. Réessaie."},
  "pt": {PAY: "Não foi possível ligar ao sistema de pagamento. Tenta novamente.",
         CHECK: "Não foi possível verificar o estado do pagamento. Tenta novamente."},
  "de": {PAY: "Das Zahlungssystem ist nicht erreichbar. Bitte versuche es erneut.",
         CHECK: "Der Zahlungsstatus konnte nicht geprüft werden. Bitte versuche es erneut."},
  "it": {PAY: "Non è stato possibile collegarsi al sistema di pagamento. Riprova.",
         CHECK: "Non è stato possibile verificare lo stato del pagamento. Riprova."},
}

src = server.read_text(encoding="utf-8")
if NEW in src:
    print("stripe.server.ts: ya aplicado")
elif src.count(OLD) == 1:
    server.write_text(src.replace(OLD, NEW), encoding="utf-8")
    print("stripe.server.ts: cambiado")
else:
    sys.exit("stripe.server.ts: no encuentro getStripeErrorMessage tal como estaba en 488db5e; revisar a mano")

pricing = root / "src/routes/pricing.tsx"
P_OLD = """      window.history.replaceState({}, "", "/pricing");
      await Promise.all([queryClient.invalidateQueries({ queryKey: ["public-account-summary"] }), queryClient.invalidateQueries({ queryKey: ["organization-billing"] })]);
      if ("error" in result && result.error) { toast.error(t(result.error)); return; }
"""
P_NEW = """      await Promise.all([queryClient.invalidateQueries({ queryKey: ["public-account-summary"] }), queryClient.invalidateQueries({ queryKey: ["organization-billing"] })]);
      // Keep session_id on error so reloading the page retries the check.
      if ("error" in result && result.error) { toast.error(t(result.error)); return; }
      window.history.replaceState({}, "", "/pricing");
"""
ps = pricing.read_text(encoding="utf-8")
if P_NEW in ps:
    print("pricing.tsx: ya aplicado")
elif ps.count(P_OLD) == 1:
    pricing.write_text(ps.replace(P_OLD, P_NEW), encoding="utf-8")
    print("pricing.tsx: cambiado")
else:
    sys.exit("pricing.tsx: no encuentro el bloque de 488db5e; revisar a mano")

for lang, add in T.items():
    p = root / f"src/lib/i18n/dict/{lang}.json"
    raw = p.read_text(encoding="utf-8")
    d = json.loads(raw)
    if json.dumps(d, ensure_ascii=False, indent=2) != raw.rstrip("\n") and json.dumps(d, ensure_ascii=False, indent=2) != raw:
        sys.exit(f"{p}: formato inesperado, no se toca")
    added = [k for k in add if k not in d]
    for k in added:
        d[k] = add[k]
    out = json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else "")
    p.write_text(out, encoding="utf-8")
    print(f"{lang}.json: {len(added)} claves nuevas")
