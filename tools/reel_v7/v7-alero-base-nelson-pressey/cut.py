"""Recortes y gradación de las fotos de v7-alero-base-nelson-pressey (../bielsa/grade.py). Ver CREDITOS.md.
Las fotos de photos/ llegan reducidas a ≤ 1600 px desde el sandbox de Higgsfield."""
from PIL import Image, ImageFilter, ImageDraw
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
def blur(im, boxes, r=14, keep=()):
    """Difumina las cajas con borde suave; las elipses de `keep` quedan nítidas."""
    m = Image.new('L', im.size, 0); d = ImageDraw.Draw(m)
    for b in boxes: d.rectangle(b, fill=255)
    for e in keep: d.ellipse(e, fill=0)
    m = m.filter(ImageFilter.GaussianBlur(6))
    return Image.composite(im.filter(ImageFilter.GaussianBlur(r)), im, m)
# 1 · Don Nelson at Suns at Warriors 3-15-09 1 (BrokenSphere, CC BY-SA 3.0): sin el logo de la liga ni la gente del banquillo
im = Image.open('photos/nelson.jpg').convert('RGB')
im = blur(im, [(0, 40, 300, 320), (600, 0, 704, 360)], 16, keep=[(300, 70, 560, 430)])
im.crop((190, 50, 690, 760)).save('photos/nelson_crop.jpg', quality=94)
grade('photos/nelson_crop.jpg', 'img/nelson_g.jpg', keep_blue=False)
# 2 · US Cellular Arena (Sulfur, CC BY-SA 3.0): el antiguo MECCA; rótulo comercial, marcador con teléfono y publicidad difuminados
im = Image.open('photos/arena.jpg').convert('RGB')
im = blur(im, [(290, 335, 430, 395), (578, 335, 730, 412), (632, 410, 678, 450), (200, 488, 300, 560)], 12)
im.crop((0, 140, 1200, 640)).save('photos/arena_crop.jpg', quality=92)
grade('photos/arena_crop.jpg', 'img/arena_g.jpg', keep_blue=False)
# 3 · PresseyBanquet2016 (Larodman1, CC BY-SA 4.0): enmarcada; la gente del banquete de fondo, difuminada
im = Image.open('photos/pressey.jpg').convert('RGB')
from rembg import remove, new_session
mask = remove(im, session=new_session('u2net'), only_mask=True).filter(ImageFilter.GaussianBlur(3))   # la persona (rembg) queda nítida
im = Image.composite(im, im.filter(ImageFilter.GaussianBlur(24)), mask)
im.crop((330, 0, 1300, 1150)).save('photos/pressey_crop.jpg', quality=92)
grade('photos/pressey_crop.jpg', 'img/pressey_g.jpg', keep_blue=False)
# 4 · Hoja de anotación oficial, Bucks en 76ers, 28/03/1986 (NBA, dominio público): girada para leerse
im = Image.open('photos/hoja.jpg').convert('RGB').rotate(90, expand=True)
im.save('photos/hoja_rot.jpg', quality=92)
grade('photos/hoja_rot.jpg', 'img/hoja_g.jpg', keep_blue=False)
# 5 · Lipofsky Pippen (Steve Lipofsky, CC BY-SA 3.0): pequeña (299 px), ficha pequeña
grade('photos/pippen.jpg', 'img/pippen_g.jpg', keep_blue=False)
# 6 · Giannis Antetokounmpo (24845003687) (cropped) (Keith Allison, CC BY-SA 2.0): recorte rembg; marcas de la camiseta difuminadas
im = Image.open('photos/giannis.jpg').convert('RGB')
im = blur(im, [(440, 820, 560, 880), (730, 735, 845, 815), (100, 1350, 220, 1460)], 10)
cut = remove(im, session=new_session('u2net')).crop((0, 80, 1239, 1500))
cut.save('photos/giannis_cut.png')
grade('photos/giannis_cut.png', 'img/giannis_g.png', keep_blue=False)
