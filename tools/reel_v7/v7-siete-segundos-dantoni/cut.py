"""Recortes y gradación de las fotos de v7-siete-segundos-dantoni (rembg + ../bielsa/grade.py)."""
from PIL import Image
import sys, numpy as np; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
def cut(src, dst):
    im = Image.open(src).convert('RGB')
    remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save(dst)
cut('photos/dantoni.jpg', 'photos/dantoni_cut.png')   # 1 · Mike D'Antoni (Keith Allison, 2007)
grade('photos/dantoni_cut.png', 'img/dantoni_g.png')
# 2 · Steve Nash (BrokenSphere, 2009): el recorte perdía la pelota y el brazo → foto enmarcada, B/N
Image.open('photos/nash.jpg').convert('RGB').crop((0, 0, 760, 1040)).save('photos/nash_crop.jpg', quality=92)
grade('photos/nash_crop.jpg', 'img/nash_g.jpg', keep_blue=False)
grade('photos/clock.jpg', 'img/clock_g.jpg', keep_blue=False)   # 3 · reloj de posesión (TonyTheTiger, 2013), en marco
# base de D'Antoni fundida (la foto acaba en la cintura)
for f, r in (('img/dantoni_g.png', 170),):
    a = np.array(Image.open(f)); h = a.shape[0]; ramp = np.clip((h - np.arange(h)) / r, 0, 1)[:, None]
    a[..., 3] = (a[..., 3] * ramp).astype(np.uint8); Image.fromarray(a).save(f)
