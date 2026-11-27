"""Preparación de fotos (v7-walkie-luis-enrique-2022). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor), traídas por image_paths:
- Luis_Enrique_2014.jpg → photos/le.jpg (744×1232, original)
- Ciudad_del_Fútbol.jpg → photos/ciudad.jpg (1300 px)
- Baofeng_UV-5R_transceiver.jpg → photos/walkie.jpg (1100 px)
Luis Enrique: recorte con rembg (u2net_human_seg) de cintura para arriba. Walkie: fondo blanco de estudio → alfa por umbral.
Ciudad del Fútbol: recorte del edificio; el escudo de la fachada se difumina (sin escudos)."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image, ImageFilter
import numpy as np, cv2
# Luis Enrique
from rembg import remove, new_session
le = Image.open('photos/le.jpg').convert('RGB').crop((30, 40, 744, 700))
cut = remove(le, session=new_session('u2net_human_seg'))
cut.save('photos/le_cut.png'); grade('photos/le_cut.png', 'img/le_g.png', keep_blue=True)
# walkie: fondo blanco → transparente (suave)
w = np.array(Image.open('photos/walkie.jpg').convert('RGB')).astype(np.float32)
d = 255 - w.min(axis=2); a = np.clip((d - 18) / 40, 0, 1)
a = cv2.GaussianBlur(a, (0, 0), 1.2); a = (a * 255).astype(np.uint8)
im = np.dstack([w.astype(np.uint8), a]); ys, xs = np.where(a > 20)
im = im[ys.min() - 4:ys.max() + 4, xs.min() - 4:xs.max() + 4]
cv2.imwrite('photos/walkie_cut.png', cv2.cvtColor(im, cv2.COLOR_RGBA2BGRA)); grade('photos/walkie_cut.png', 'img/walkie_g.png', keep_blue=True)
# Ciudad del Fútbol
c = Image.open('photos/ciudad.jpg').convert('RGB')
box = (603, 390, 651, 500); c.paste(c.crop(box).resize((6, 14)).resize((48, 110), Image.BILINEAR).filter(ImageFilter.GaussianBlur(6)), box[:2])
c.crop((150, 120, 1300, 900)).save('photos/ciudad_crop.jpg', quality=94); grade('photos/ciudad_crop.jpg', 'img/ciudad_g.jpg', keep_blue=True)
