#!/usr/bin/env python3
"""S-004: la foto de un jugador solo se muestra si viene de nuestro almacén (player-photos)
o es una imagen incrustada. Hoy cualquier jugador puede poner en su perfil (photo_url) una
URL externa y la plantilla del entrenador la carga tal cual (IP del entrenador / imagen ajena).
Uso: python3 aplicar.py /ruta/a/proteamapp
"""
import sys, pathlib
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
f = root / "src/lib/photos.server.ts"
s = f.read_text()
old = '''export function resolvePhoto(value: string | null | undefined, map: Map<string, string>) {
  if (!value) return null;
  if (value.startsWith("http") || value.startsWith("data:")) return value;
  return map.get(value) ?? null;
}'''
new = '''/** Signed URLs of our own bucket (already resolved upstream) are the only remote photos allowed. */
function isOwnSignedPhotoUrl(value: string) {
  try {
    const u = new URL(value);
    return (
      u.protocol === "https:" &&
      u.hostname.endsWith(".supabase.co") &&
      u.pathname.startsWith(`/storage/v1/object/sign/${PHOTO_BUCKET}/`)
    );
  } catch {
    return false;
  }
}

export function resolvePhoto(value: string | null | undefined, map: Map<string, string>) {
  if (!value) return null;
  // profiles.photo_url is editable by the player: never load arbitrary external URLs.
  if (value.startsWith("data:image/")) return value;
  if (value.startsWith("http")) return isOwnSignedPhotoUrl(value) ? value : null;
  return map.get(value) ?? null;
}'''
if new in s:
    print("ya aplicado"); sys.exit(0)
assert s.count(old) == 1, "no encuentro resolvePhoto tal cual (commit fb80d88)"
f.write_text(s.replace(old, new))
print("S-004 aplicado en", f)
