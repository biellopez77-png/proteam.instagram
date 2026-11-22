#!/usr/bin/env python3
"""R-003 (20/11, turno 16:17 Madrid) — la portada deja de repintarse entera cada segundo (2 archivos, sin BD).

`src/routes/index.tsx` (LandingPage) llama a `useBlackoutRemaining()`, que hace `setRemaining`
cada segundo (`blackout-friday.tsx`, `setInterval(update, 1000)`). Como el estado vive en la
página, cada segundo se vuelve a pintar TODA la portada: los 4 mockups de la app, las secciones,
el pie y, si está abierto, el panel de alta (`AuthOverlay` recibe un `onClose` nuevo en cada
pintado). En un móvil modesto eso es trabajo continuo mientras el entrenador escribe su nombre
y su correo en el alta, que es justo la pantalla que importa hasta el 28.

Arreglo (sin cambiar nada de lo que se ve):
- `blackout-friday.tsx`: nuevo `useBlackoutCampaign()` (true/false; solo cambia una vez, al
  acabar la oferta) y nuevo `LiveBlackoutCountdown`, que es quien lleva el segundero.
- `index.tsx`: la página usa `useBlackoutCampaign()`; las dos cuentas atrás pasan a
  `<LiveBlackoutCountdown />`. Ahora cada segundo solo se repintan los 8 números.

Uso (en la raíz de proteamapp): python3 aplicar.py && bun run build
Va como PR (regla de Biel del 20/11: nada se publica sin su aprobación).
"""
import pathlib, sys

COUNTDOWN_LG = '{remaining ? <BlackoutCountdown remaining={remaining} /> : <div className="invisible" aria-hidden="true"><BlackoutCountdown remaining={[0, 0, 0, 0]} /></div>}'
COUNTDOWN_MD = '{remaining ? <BlackoutCountdown remaining={remaining} size="md" /> : <div className="invisible" aria-hidden="true"><BlackoutCountdown remaining={[0, 0, 0, 0]} size="md" /></div>}'

NEW_HOOKS = '''export function useBlackoutRemaining() {'''
ADDED = '''/** true mientras dura la oferta; solo cambia una vez (al acabar), así la página no se repinta cada segundo. */
export function useBlackoutCampaign() {
  const [active, setActive] = useState<boolean | null>(null);
  useEffect(() => {
    const update = () => setActive(blackoutActive(Date.now()));
    update();
    const timer = window.setInterval(update, 1000);
    return () => window.clearInterval(timer);
  }, []);
  return active;
}

/** Cuenta atrás con su propio segundero: cada segundo solo se repintan los números. */
export function LiveBlackoutCountdown({ size = "lg" }: { size?: "lg" | "md" }) {
  const remaining = useBlackoutRemaining();
  return remaining
    ? <BlackoutCountdown remaining={remaining} size={size} />
    : <div className="invisible" aria-hidden="true"><BlackoutCountdown remaining={[0, 0, 0, 0]} size={size} /></div>;
}

export function useBlackoutRemaining() {'''

CHANGES = {
    "src/components/landing/blackout-friday.tsx": [
        ('import { blackoutRemaining } from "@/lib/blackout-friday";',
         'import { blackoutActive, blackoutRemaining } from "@/lib/blackout-friday";', 1),
        (NEW_HOOKS, ADDED, 1),
    ],
    "src/routes/index.tsx": [
        ('import { AuthButtons, BlackoutCountdown, useBlackoutRemaining } from "@/components/landing/blackout-friday";',
         'import { AuthButtons, LiveBlackoutCountdown, useBlackoutCampaign } from "@/components/landing/blackout-friday";', 1),
        ('  const remaining = useBlackoutRemaining();\n  const campaign = !mounted || remaining !== null;',
         '  // Antes de montar (SSR) se pinta la campaña; después, solo cambia al acabar la oferta.\n  const campaign = useBlackoutCampaign() !== false;', 1),
        (COUNTDOWN_LG, '<LiveBlackoutCountdown />', 1),
        (COUNTDOWN_MD, '<LiveBlackoutCountdown size="md" />', 1),
    ],
}

for path, repl in CHANGES.items():
    p = pathlib.Path(path)
    s = p.read_text(encoding="utf-8")
    for old, new, n in repl:
        found = s.count(old)
        if found != n:
            sys.exit(f"{path}: se esperaban {n} coincidencias y hay {found}: {old[:70]}…")
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")
    print("ok", path)
