"""Efecto de tele de tubo (CRT/VHS) para la identidad retro de ProTeam.
crt(img, a, t, seed): a = 0 (imagen limpia, «el futuro») … 1 (tele de 1998).
"""
import numpy as np, cv2
from PIL import Image

_M = {}
def _maps(w, h, k):
    key = (w, h, round(k, 3))
    if key not in _M:
        yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
        nx, ny = (xx - w / 2) / (w / 2), (yy - h / 2) / (h / 2)
        r2 = nx * nx * .55 + ny * ny * .45
        f = 1 + k * r2
        mx, my = (nx * f) * (w / 2) + w / 2, (ny * f) * (h / 2) + h / 2
        # máscara de pantalla con esquinas redondeadas y borde suave
        inside = (np.abs(mx - w / 2) < w / 2 - 6) & (np.abs(my - h / 2) < h / 2 - 6)
        m = inside.astype(np.float32)
        m = cv2.GaussianBlur(m, (0, 0), 6)
        vig = 1 - .55 * np.clip(np.sqrt(nx * nx + ny * ny) - .55, 0, 1) ** 1.4
        _M[key] = (mx, my, m * vig)
    return _M[key]

def crt(img, a=1.0, t=0.0, seed=0, curve=.12):
    src = np.asarray(img.convert('RGB')).astype(np.float32) / 255
    if a <= 0.001:
        return img.convert('RGB')
    h, w = src.shape[:2]; rng = np.random.default_rng(seed)
    x = src.copy()
    # fósforo: un poco de desenfoque y brillo
    x = cv2.GaussianBlur(x, (0, 0), 1.2 * a)
    # sangrado de color VHS: el croma se desplaza y se emborrona en horizontal
    s = int(round(5 * a))
    if s:
        x[..., 0] = np.roll(x[..., 0], s, 1); x[..., 2] = np.roll(x[..., 2], -s, 1)
        x[..., 0] = cv2.blur(x[..., 0], (int(6 * a) + 1, 1))
    # temblor de líneas (tracking) en una banda que se mueve
    band = int((t * 260) % (h + 300)) - 150
    y0, y1 = max(0, band), min(h, band + 60)
    if y1 > y0:
        x[y0:y1] = np.roll(x[y0:y1], int(rng.integers(6, 18) * a), 1); x[y0:y1] *= 1 + .12 * a
    # líneas de exploración y máscara de sombra RGB
    yy = np.arange(h)[:, None]; xx = np.arange(w)[None, :]
    scan = 1 - .32 * a * (yy % 4 < 2)
    triad = np.ones((1, w, 3), np.float32)
    for c in range(3): triad[0, :, c] = 1 - .18 * a * ((xx[0] % 3) != c)
    x = x * scan[..., None] * triad
    # resplandor
    hi = np.clip(x - .55, 0, 1); x = x + cv2.GaussianBlur(hi, (0, 0), 14) * .9 * a
    # ruido y parpadeo
    x = x + rng.normal(0, .035 * a, (h, w, 1)).astype(np.float32)
    x *= 1 + .025 * a * np.sin(t * 50)
    # curvatura del tubo
    mx, my, m = _maps(w, h, curve * a)
    x = cv2.remap(np.clip(x, 0, 1).astype(np.float32), mx, my, cv2.INTER_LINEAR, borderValue=(0, 0, 0))
    x = x * m[..., None] ** a
    return Image.fromarray((np.clip(x, 0, 1) * 255).astype(np.uint8))
