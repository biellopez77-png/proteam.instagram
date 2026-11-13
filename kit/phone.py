"""Pone una captura real de la app en la pantalla verde de una foto.
   python3 phone.py FOTO.png CAPTURA.jpg SALIDA.png
Busca la zona verde (croma), saca sus 4 esquinas y deforma la captura en perspectiva;
el borde se recorta con la propia máscara verde (esquinas redondeadas del móvil)."""
import sys
import numpy as np
from PIL import Image, ImageFilter

foto, cap, out = sys.argv[1:4]
im = Image.open(foto).convert('RGB'); a = np.asarray(im).astype(int)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
m = (g > 140) & (g > r + 60) & (g > b + 60)
ys, xs = np.nonzero(m)
s, d = xs + ys, xs - ys
tl = (xs[s.argmin()], ys[s.argmin()]); br = (xs[s.argmax()], ys[s.argmax()])
tr = (xs[d.argmax()], ys[d.argmax()]); bl = (xs[d.argmin()], ys[d.argmin()])
# las esquinas redondeadas recortan los extremos: se estiman con rectas por los bordes
def edge_fit(pts_x, pts_y):
    return np.polyfit(pts_y, pts_x, 1)
rows = np.unique(ys)
left = np.array([xs[ys == y].min() for y in rows]); right = np.array([xs[ys == y].max() for y in rows])
cols = np.unique(xs)
top = np.array([ys[xs == x].min() for x in cols]); bot = np.array([ys[xs == x].max() for x in cols])
h = len(rows); w = len(cols); c1, c2 = int(h * .2), int(h * .8); k1, k2 = int(w * .2), int(w * .8)
L = np.polyfit(rows[c1:c2], left[c1:c2], 1); R = np.polyfit(rows[c1:c2], right[c1:c2], 1)
T = np.polyfit(cols[k1:k2], top[k1:k2], 1); B = np.polyfit(cols[k1:k2], bot[k1:k2], 1)
def inter(V, H):   # x = V0*y + V1 ; y = H0*x + H1
    y = (H[0] * V[1] + H[1]) / (1 - H[0] * V[0]); return (V[0] * y + V[1], y)
P = [inter(L, T), inter(R, T), inter(R, B), inter(L, B)]
c = Image.open(cap).convert('RGB')
cw, ch = c.size
# recorte de la captura a la proporción de la pantalla
sw = np.hypot(P[1][0] - P[0][0], P[1][1] - P[0][1]); sh = np.hypot(P[3][0] - P[0][0], P[3][1] - P[0][1])
want = cw / ch; have = sw / sh
if have > want: nh = int(cw / have); c = c.crop((0, 0, cw, nh))
else: nw = int(ch * have); c = c.crop(((cw - nw) // 2, 0, (cw - nw) // 2 + nw, ch))
cw, ch = c.size
# coeficientes de perspectiva (destino -> origen)
A = []; Bv = []
for (x, y), (u, v) in zip(P, [(0, 0), (cw, 0), (cw, ch), (0, ch)]):
    A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); Bv.append(u)
    A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); Bv.append(v)
coef = np.linalg.solve(np.array(A, float), np.array(Bv, float))
warp = c.transform(im.size, Image.PERSPECTIVE, tuple(coef), Image.BICUBIC)
mask = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
# un poco de brillo de pantalla y reflejo frío
warp = Image.blend(warp, Image.new('RGB', im.size, (40, 70, 160)), .06)
im.paste(warp, (0, 0), mask)
im.save(out)
print('ok', [tuple(map(int, p)) for p in P])
