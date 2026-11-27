"""Preparación de fotos (v7-senor-cinco-a-cero-hiddink). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor), recortadas allí y traídas por image_paths:
- Guus_Hiddink_(1986).jpg (a 1600 px) → recorte 1200×1380 (cabeza y hombros; fuera el patrocinador y la marca de la chaqueta) → photos/hiddink.jpg
- Park_Ji-Sung_20080429.jpg (a 1600 px) → recorte 740×900 (cara y cuello; fuera el logotipo de la chaqueta de al lado y la mano) → photos/park.jpg
- Seoul_Plaza_2002_FIFA_World_Cup.jpg (a 1600 px) → franja inferior de la multitud, sin los rótulos de los edificios → photos/plaza.jpg
- 2002 FIFA 한일월드컵-시청 거리응원 (1).jpg (a 1600 px) → franja inferior (ayuntamiento y multitud) → photos/calle.jpg
Se difuminan la pancarta y el logotipo del círculo central de la foto de la calle."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image, ImageFilter, ImageEnhance
from rembg import remove, new_session
def blur(im, box, r=10):
    bl = im.filter(ImageFilter.GaussianBlur(r)); m = Image.new('L', im.size, 0)
    m.paste(255, tuple(int(v) for v in box)); m = m.filter(ImageFilter.GaussianBlur(r * 1.2))
    im.paste(Image.composite(bl, im, m))
hs = new_session('u2net_human_seg')
h = Image.open('photos/hiddink.jpg').convert('RGB').resize((900, 1035), Image.LANCZOS)
remove(h, session=hs).save('photos/hiddink_cut.png'); grade('photos/hiddink_cut.png', 'img/hiddink_g.png', keep_blue=True)
grade('photos/park.jpg', 'img/park_g.jpg', keep_blue=True)   # enmarcada: el recorte con rembg no queda limpio (se lleva el fondo oscuro)
grade('photos/plaza.jpg', 'img/plaza_g.jpg', keep_blue=True)
c = Image.open('photos/calle.jpg').convert('RGB')
blur(c, (200, 200, 340, 320), 14); blur(c, (440, 615, 560, 645), 10); blur(c, (0, 600, 60, 700), 10)
c.save('photos/calle_b.jpg', quality=92); grade('photos/calle_b.jpg', 'img/calle_g.jpg', keep_blue=True)
