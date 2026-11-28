"""Preparación de fotos (v7-una-mano-luisetti-1936). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor) y traídas por image_paths:
- Hank_Luisetti_1944.jpg → photos/l44.jpg (513×1740, original)
- Hank_Luisetti_1943.jpg → photos/l43.jpg (reducida a 1250 px)
- Madison_Square_Garden_1941_Postcard.jpg → photos/msg.jpg (reducida a 1300 px)
Luisetti 1944: se probó rembg (u2net_human_seg) y el recorte no queda limpio (trama de periódico, brazos cortados): va la foto enmarcada en ficha de prensa. Luisetti 1943: retrato enmarcado (ficha de prensa).
Postal del Garden: enmarcada como postal, B/N con el azul (los rótulos y banderas de la postal se quedan; no hay logos de club)."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image
grade('photos/l44.jpg', 'img/l44_g.jpg', keep_blue=True)
b = Image.open('photos/l43.jpg').convert('RGB'); b.crop((0, 0, 931, 1150)).save('photos/l43_crop.jpg', quality=94)
grade('photos/l43_crop.jpg', 'img/l43_g.jpg', keep_blue=True)
c = Image.open('photos/msg.jpg').convert('RGB'); c.save('photos/msg_crop.jpg', quality=94)
grade('photos/msg_crop.jpg', 'img/msg_g.jpg', keep_blue=True)
