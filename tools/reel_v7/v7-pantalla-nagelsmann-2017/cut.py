"""Preparación de fotos (v7-pantalla-nagelsmann-2017). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor), traídas por image_paths (≤1600 px):
- JulianNagelsmann.jpg → photos/nagelsmann.jpg (855×1600)
- Thomas Tuchel coach Mainz05 at away match in Leverkusen 2014.jpg → photos/tuchel.jpg (738×1600)
- Rhein-Neckar-Arena 2015.jpg → photos/estadio.jpg (1080×810)
Nagelsmann y Tuchel: recorte con rembg (u2net_human_seg) de cintura para arriba. Tuchel: el escudo del chándal se difumina antes (sin escudos).
Estadio: recorte para la polaroid."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image, ImageFilter
from rembg import remove, new_session
S = new_session('u2net_human_seg')
n = Image.open('photos/nagelsmann.jpg').convert('RGB').crop((150, 50, 740, 880))
remove(n, session=S).save('photos/nagelsmann_cut.png'); grade('photos/nagelsmann_cut.png', 'img/nagelsmann_g.png', keep_blue=False)   # camisa a rayas: el azul salía a manchas
t = Image.open('photos/tuchel.jpg').convert('RGB')
import numpy as np
a = np.array(t).astype(np.float32); x0, y0, x1, y1 = 436, 362, 510, 486   # escudo del Mainz y patrocinador del pecho: se tapan con el tejido de al lado
src = a[y0:y1, x1 + 6:x1 + 6 + (x1 - x0)]                                   # franja de chaqueta a la derecha, misma altura
m = np.zeros(a.shape[:2], np.float32); m[y0:y1, x0:x1] = 1
import cv2; m = cv2.GaussianBlur(m, (0, 0), 6)[..., None]
fill = a.copy(); fill[y0:y1, x0:x1] = src
a = a * (1 - m) + fill * m; t = Image.fromarray(a.clip(0, 255).astype(np.uint8))
t = t.crop((130, 90, 700, 820))
c = np.array(remove(t, session=S)); c[500:, 432:, 3] = 0   # resto del banquillo a su izquierda
Image.fromarray(c).save('photos/tuchel_cut.png'); grade('photos/tuchel_cut.png', 'img/tuchel_g.png', keep_blue=True)
e = Image.open('photos/estadio.jpg').convert('RGB').crop((0, 0, 1080, 640))
e.save('photos/estadio_crop.jpg', quality=94); grade('photos/estadio_crop.jpg', 'img/estadio_g.jpg', keep_blue=True)
