"""Fotos de v7-guerra-izzo-2000: recorte (rembg) y gradación (tools/reel_v7/bielsa/grade.py)."""
from PIL import Image
import sys, numpy as np; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
def fadebase(p, n=160):
    im = Image.open(p); a = np.array(im); h = a.shape[0]
    a[..., 3] = (a[..., 3] * np.clip((h - np.arange(h)) / n, 0, 1)[:, None]).astype(np.uint8)
    Image.fromarray(a).save(p)
# 1 · Tom Izzo (Pentágono, 2014): ya recortado en el sandbox por encima de los logos de la camiseta y sin el atril; rembg quita la bandera
im = Image.open('photos/izzo_pentagono.jpg').convert('RGB')
remove(im, session=S).save('photos/izzo_cut.png'); fadebase('photos/izzo_cut.png', 220)
grade('photos/izzo_cut.png', 'img/izzo_cut_g.png', keep_blue=False)
# 2 · Izzo dirige un entreno de Michigan State (2011): polaroid centrada en él
Image.open('photos/izzo_entreno.jpg').convert('RGB').crop((300, 360, 1180, 1063)).save('photos/entreno_crop.jpg', quality=93)
grade('photos/entreno_crop.jpg', 'img/entreno_g.jpg', keep_blue=False)
# 3 · Lucha por un rebote (All-Navy y Marine Corps, 2004): en marco, sin recorte (rembg con 5 jugadoras no queda limpio)
Image.open('photos/rebote_navy.jpg').convert('RGB').crop((560, 330, 1460, 1290)).save('photos/rebote_crop.jpg', quality=93)
grade('photos/rebote_crop.jpg', 'img/rebote_g.jpg', keep_blue=False)
