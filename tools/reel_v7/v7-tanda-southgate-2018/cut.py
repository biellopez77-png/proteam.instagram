"""Recortes y gradación de las fotos (v7-tanda-southgate-2018)."""
from PIL import Image
from rembg import remove, new_session
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
S = new_session('isnet-general-use')
# 1 · Southgate en el entrenamiento (13/6/2018): solo él (la marca de agua de abajo a la izquierda queda fuera del recorte)
a = Image.open('photos/southgate_entreno.jpg').convert('RGB').crop((560, 20, 1320, 1000))
import os
if not os.path.exists('photos/entreno_cut.png'): remove(a, session=S).save('photos/entreno_cut.png')
# 2 · Southgate en el césped del Spartak (3/7/2018): rembg dejaba trozos de otra persona y manchas en el chaleco,
#     así que va enmarcada (recorte vertical centrado en él), en B/N sin azul
b = Image.open('photos/southgate_moscu.jpg').convert('RGB').crop((20, 20, 440, 1000)); b.save('photos/moscu_crop.jpg', quality=92)
# 3 · Pickford le da el balón a Dier: foto enmarcada (polaroid), sin recorte de fondo
#     (el anuncio del fondo se desenfoca para que no destaque ninguna marca)
from PIL import ImageFilter
c = Image.open('photos/pickford_dier.jpg').convert('RGB')
box = (430, 280, 660, 530); c.paste(c.crop(box).filter(ImageFilter.GaussianBlur(14)), box[:2])
c = c.crop((0, 60, 1400, 1100)); c.thumbnail((1100, 1100)); c.save('photos/pickford_crop.jpg', quality=92)
grade('photos/entreno_cut.png', 'img/entreno_g.png')
grade('photos/moscu_crop.jpg', 'img/moscu_g.jpg', keep_blue=False)
grade('photos/pickford_crop.jpg', 'img/pickford_g.jpg')
