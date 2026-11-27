"""Preparación de fotos (v7-reglas-jordan-daly-1988). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor) y traídas por image_paths:
- Michael_Jordan_holds_up_his_Chicago_Bulls_jersey_on_September_12,_1984.jpg → photos/jordan.jpg (1000 px)
- Chuck_Daly_(cropped).jpg → photos/daly.jpg (408×580, original)
- Isiah-thomas_detroit-v-new-york_1985.jpg → photos/isiah.jpg (800 px)
- Pontiac_Silverdome,_Pontiac,_Michigan.jpg → photos/dome.jpg (1000 px)
Jordan y Daly, recortados con rembg; Isiah y el Silverdome, enmarcados (polaroid)."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image
from rembg import remove as _rm, new_session
S = new_session("u2net"); remove = lambda im: _rm(im, session=S)
Image.open('photos/jordan.jpg').convert('RGB').crop((0, 0, 1000, 1364)).save('photos/jordan_rgb.jpg', quality=95)
remove(Image.open('photos/jordan_rgb.jpg')).save('photos/jordan_cut.png')
grade('photos/jordan_cut.png', 'img/jordan_g.png', keep_blue=False)
remove(Image.open('photos/daly.jpg').crop((40, 0, 408, 580))).save('photos/daly_cut.png')
grade('photos/daly_cut.png', 'img/daly_g.png', keep_blue=True)
Image.open('photos/isiah.jpg').crop((400, 180, 800, 700)).save('photos/isiah_crop.jpg', quality=94)
grade('photos/isiah_crop.jpg', 'img/isiah_g.jpg', keep_blue=True)
Image.open('photos/dome.jpg').crop((40, 150, 960, 560)).save('photos/dome_crop.jpg', quality=94)
grade('photos/dome_crop.jpg', 'img/dome_g.jpg', keep_blue=True)
# rembg deja la camiseta blanca medio transparente: alfa binarizado, huecos rellenos y borde suave
import cv2, numpy as np
for n in ['jordan', 'daly']:
    im = cv2.imread(f'photos/{n}_cut.png', cv2.IMREAD_UNCHANGED); a = (im[..., 3] > 40).astype(np.uint8) * 255
    a = cv2.morphologyEx(a, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    ff = a.copy(); m = np.zeros((a.shape[0] + 2, a.shape[1] + 2), np.uint8); cv2.floodFill(ff, m, (0, 0), 255)
    a = a | cv2.bitwise_not(ff); a = cv2.GaussianBlur(a, (0, 0), 1.2)
    g = cv2.imread(f'img/{n}_g.png', cv2.IMREAD_UNCHANGED); g[..., 3] = a; cv2.imwrite(f'img/{n}_g.png', g)
