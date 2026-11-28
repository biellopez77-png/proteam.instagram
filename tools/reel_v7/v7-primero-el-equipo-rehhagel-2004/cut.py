"""Recortes y gradación de las fotos de v7-primero-el-equipo-rehhagel-2004 (rembg + ../bielsa/grade.py)."""
from PIL import Image
import sys, numpy as np; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
# 1 · Otto Rehhagel (Jörg Zägel, 2010): recorte con rembg, base fundida
im = Image.open('photos/rehhagel.jpg').convert('RGB')
remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save('photos/rehhagel_cut.png')
grade('photos/rehhagel_cut.png', 'img/rehhagel_g.png')
a = np.array(Image.open('img/rehhagel_g.png')); h = a.shape[0]; ramp = np.clip((h - np.arange(h)) / 220, 0, 1)[:, None]
a[..., 3] = (a[..., 3] * ramp).astype(np.uint8); Image.fromarray(a).save('img/rehhagel_g.png')
# 2 · Rehhagel en la banda (Stelios Tsaousidis, 2008): enmarcada, encuadre en Rehhagel y los jugadores griegos
Image.open('photos/banda.jpg').convert('RGB').crop((150, 0, 654, 515)).save('photos/banda_crop.jpg', quality=92)
grade('photos/banda_crop.jpg', 'img/banda_g.jpg')
# 3 · Banderas en la final (Jarrett Campbell, 2004): encuadre del césped y las banderas
Image.open('photos/final.jpg').convert('RGB').crop((150, 280, 1350, 900)).save('photos/final_crop.jpg', quality=92)
grade('photos/final_crop.jpg', 'img/final_g.jpg')
# 4 · Cabezazo de Charisteas (Fritz Duras, 2004): enmarcada, pequeña (640×480)
grade('photos/charisteas.jpg', 'img/charisteas_g.jpg')
