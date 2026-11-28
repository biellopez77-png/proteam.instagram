"""Recortes y gradación de las fotos de v7-cuatro-porterias-wein (../bielsa/grade.py). Ver CREDITOS.md."""
from PIL import Image, ImageFilter
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import ImageDraw
def blur(im, boxes, r=14, keep=()):
    """Difumina las cajas con borde suave; las elipses de `keep` (caras, balón) quedan nítidas."""
    m = Image.new('L', im.size, 0); d = ImageDraw.Draw(m)
    for b in boxes: d.rectangle(b, fill=255)
    for e in keep: d.ellipse(e, fill=0)
    m = m.filter(ImageFilter.GaussianBlur(6))
    return Image.composite(im.filter(ImageFilter.GaussianBlur(r)), im, m)
# 1 · Alvaro Ardila and Horst Wein (Alvaro Andres Ardila Villamizar, CC BY-SA 4.0): solo Wein (sin la otra persona ni el diploma); logos del polo difuminados
im = Image.open('photos/wein.jpg').convert('RGB').crop((0, 0, 388, 610))
blur(im, [(315, 360, 388, 410), (22, 468, 72, 500)], 8).save('photos/wein_crop.jpg', quality=94)
grade('photos/wein_crop.jpg', 'img/wein_g.jpg', keep_blue=False)
# 2 · 02016 009 Sanok Kinderfussball Cup (Silar, CC BY-SA 4.0): ilustrativa; sin la pancarta naranja ni el adulto; patrocinadores y vallas difuminados
im = Image.open('photos/kids.jpg').convert('RGB')
im = blur(im, [(760, 165, 1525, 365), (0, 150, 175, 300), (850, 395, 965, 515), (1140, 375, 1330, 420), (1525, 385, 1715, 425), (730, 300, 820, 355), (640, 440, 675, 505)], 16,
         keep=[(805, 95, 970, 258), (805, 222, 915, 330), (600, 90, 785, 280), (1190, 262, 1330, 368)])
im.crop((380, 60, 1860, 1280)).save('photos/kids_crop.jpg', quality=92)
grade('photos/kids_crop.jpg', 'img/kids_g.jpg', keep_blue=False)
