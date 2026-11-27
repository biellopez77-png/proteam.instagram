"""Fotos de v7-once-de-casa-celtic: recorte (rembg) y gradación B/N con el azul (../bielsa/grade.py)."""
from PIL import Image
import sys, numpy as np; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
def fadebase(p, n=180):
    im = Image.open(p); a = np.array(im); h = a.shape[0]
    a[..., 3] = (a[..., 3] * np.clip((h - np.arange(h)) / n, 0, 1)[:, None]).astype(np.uint8)
    Image.fromarray(a).save(p)
# 1 · Jock Stein (Anefo, 1971): recortado hasta la cintura
im = Image.open('photos/stein.jpg').convert('RGB').crop((0, 0, 1137, 1250))
remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save('photos/stein_cut.png')
grade('photos/stein_cut.png', 'img/stein_g.png', keep_blue=False); fadebase('img/stein_g.png')
im = Image.open('img/stein_g.png'); im.thumbnail((900, 900)); im.save('img/stein_g.png', optimize=True)
# 2 · Estádio Nacional do Jamor (foto actual, en marco de postal)
Image.open('photos/jamor.jpg').convert('RGB').crop((0, 120, 1400, 980)).save('photos/jamor_crop.jpg', quality=92)
grade('photos/jamor_crop.jpg', 'img/jamor_g.jpg')
# 3 · Celtic Park (Thomas Nugent), pequeña en la esquina del mapa
Image.open('photos/park.jpg').convert('RGB').crop((40, 60, 1400, 645)).save('photos/park_crop.jpg', quality=92)
grade('photos/park_crop.jpg', 'img/park_g.jpg', keep_blue=False)
# 4 · Celtic Park, grada «Lisbon Lions» (Crowsus)
Image.open('photos/lions.jpg').convert('RGB').crop((0, 220, 1400, 1050)).save('photos/lions_crop.jpg', quality=92)
grade('photos/lions_crop.jpg', 'img/lions_g.jpg', keep_blue=False)
