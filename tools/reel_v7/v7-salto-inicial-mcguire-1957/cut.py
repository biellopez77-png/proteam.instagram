"""Recortes y gradación de las fotos de v7-salto-inicial-mcguire-1957 (rembg + ../bielsa/grade.py)."""
from PIL import Image
import sys, numpy as np; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
def cut(src, dst):
    im = Image.open(src).convert('RGB')
    remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save(dst)
for n in ('wilt', 'mcguire', 'kearns'):
    cut(f'photos/{n}.jpg', f'photos/{n}_cut.png')
# 4 · programa de la NCAA (1963): solo el titular y la foto del equipo, en papel
Image.open('photos/ncaa.jpg').convert('RGB').crop((40, 40, 1080, 770)).save('photos/ncaa_crop.jpg', quality=92)
grade('photos/ncaa_crop.jpg', 'img/ncaa_g.jpg', keep_blue=False)
# Chamberlain: el recorte perdía la pierna levantada → plano hasta el pantalón, base fundida
# McGuire: recorte (solo él, sin Buck Freeman), base fundida; Kearns: entero, sin el reflejo del suelo
from PIL import Image as _I
w = _I.open('photos/wilt_cut.png'); w.crop((0, 0, w.width, int(w.height * .66))).save('photos/wilt_cut2.png')
k = _I.open('photos/kearns_cut.png'); k.crop((0, 0, k.width, 800)).save('photos/kearns_cut2.png')
for s, d in (('wilt_cut2', 'wilt_g'), ('mcguire_cut', 'mcguire_g'), ('kearns_cut2', 'kearns_g')):
    grade(f'photos/{s}.png', f'img/{d}.png')
for f, r in (('img/wilt_g.png', 160), ('img/mcguire_g.png', 200)):
    a = np.array(Image.open(f)); h = a.shape[0]; ramp = np.clip((h - np.arange(h)) / r, 0, 1)[:, None]
    a[..., 3] = (a[..., 3] * ramp).astype(np.uint8); Image.fromarray(a).save(f)
