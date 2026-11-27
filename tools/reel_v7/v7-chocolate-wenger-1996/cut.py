# Fotos de v7-chocolate-wenger-1996: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
# raw1..raw4 se bajaron de Commons en el sandbox de Higgsfield (Special:FilePath ?width=1600) y se trajeron reducidas:
# raw1 = Ewood Park 2011 a 1400 px; raw2 = Arsene Wenger 2009, recorte 1700x2200+220+300 a 1000 px;
# raw3 = Arsene Wenger directs the troops, recorte 640x760+640+560 (sin vallas publicitarias); raw4 = Broccoli florets on ice, recorte 760x720+760+620.
from rembg import remove, new_session
from PIL import Image, ImageDraw, ImageFilter
import numpy as np, sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · Ewood Park (Ronnie Macdonald, CC BY 2.0): gradas y césped, sin la mitad del techo
Image.open('photos/raw1.jpg').convert('RGB').crop((0,300,1400,933)).save('photos/p1.jpg',quality=92)
# 2 · Wenger 2009 (Gordon Flood, CC BY 2.0): recortado
cut(Image.open('photos/raw2.jpg').convert('RGB')).save('photos/p2_cut.png')
# 3 · Wenger en la banda señalando (Ronnie Macdonald, CC BY 2.0): recortado
cut(Image.open('photos/raw3.jpg').convert('RGB')).save('photos/p3_cut.png')
# 4 · brócoli (Jeffery Martin, CC0): un círculo para el plato
b=Image.open('photos/raw4.jpg').convert('RGB').crop((40,40,640,640)).resize((520,520))
m=Image.new('L',b.size,0); ImageDraw.Draw(m).ellipse((6,6,514,514),fill=255); m=m.filter(ImageFilter.GaussianBlur(3)); b.putalpha(m); b.save('photos/p4.png')
grade('photos/p1.jpg','img/p1_g.jpg')
for k in ('p2_cut','p3_cut','p4'):
    grade(f'photos/{k}.png',f'img/{k}_g.png'); g=Image.open(f'img/{k}_g.png'); g=g.crop(g.getbbox()); g.save(f'img/{k}_g.png',optimize=True); print(k,g.size)
# 3b · la recortada queda oscura sobre el fondo: se usa también la foto entera graduada, en polaroid
grade('photos/raw3.jpg','img/p3_g.jpg')
