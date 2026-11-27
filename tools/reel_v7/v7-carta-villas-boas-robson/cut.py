"""Preparación de fotos (v7-carta-villas-boas-robson). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor) y traídas por image_paths:
- Model_of_Estádio_das_Antas_at_Museu_FC_Porto.jpg → photos/antas.jpg (975×1300)
- EK_voetbal_Engelse_trainer_Bobby_Robson,_Bestanddeelnr_934-2658.jpg → photos/robson.jpg (1062×1600)
- 2011_UEFA_Europa_League_Final_-_Opening_ceremony.jpg → photos/dublin.jpg (1400×1050)
- Villas-Boas.JPG → photos/avb.jpg (404×516, original)
Sin escudos ni logotipos: se difuminan el escudo del pecho y las marcas de Villas-Boas, el escudo y el logotipo
de las lonas de Dublín y los banderines/vitrina de la foto de la maqueta (se recorta solo la maqueta)."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image, ImageFilter
from rembg import remove, new_session
def blur(im, box, r=10):
    """difuminado con borde suave (sin cuadros visibles)"""
    bl = im.filter(ImageFilter.GaussianBlur(r)); m = Image.new('L', im.size, 0)
    m.paste(255, tuple(int(v) for v in box)); m = m.filter(ImageFilter.GaussianBlur(r * 1.2))
    im.paste(Image.composite(bl, im, m))
hs = new_session('u2net_human_seg')
# Estádio das Antas: solo la maqueta
a = Image.open('photos/antas.jpg').convert('RGB').crop((10, 450, 975, 1010))
a.save('photos/antas_crop.jpg', quality=94); grade('photos/antas_crop.jpg', 'img/antas_g.jpg', keep_blue=True)
# Bobby Robson (1988): recorte con rembg
r = Image.open('photos/robson.jpg').convert('RGB').crop((40, 160, 1062, 1600))
remove(r, session=hs).resize((818, 1152), Image.LANCZOS).save('photos/robson_cut.png'); grade('photos/robson_cut.png', 'img/robson_g.png', keep_blue=True)
# Villas-Boas (2011): cabeza y hombros (sin escudo, sin marcas, sin la mano con el micrófono)
v = Image.open('photos/avb.jpg').convert('RGB').crop((0, 0, 350, 352))   # hombros: el escudo y las marcas quedan fuera
remove(v, session=hs).save('photos/avb_cut.png'); grade('photos/avb_cut.png', 'img/avb_g.png', keep_blue=True)
# Dublín 2011: césped con la lona; sin escudo, sin logotipo del trofeo, vallas difuminadas
d = Image.open('photos/dublin.jpg').convert('RGB')
blur(d, (660, 524, 880, 588), 12); blur(d, (505, 415, 795, 490), 12); blur(d, (880, 372, 1400, 525), 6); blur(d, (200, 360, 900, 392), 6)
d.crop((40, 440, 1260, 800)).save('photos/dublin_crop.jpg', quality=94); grade('photos/dublin_crop.jpg', 'img/dublin_g.jpg', keep_blue=True)
