"""Preparación de fotos (v7-cuatro-casas-alemania-2014). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor), reducidas a ≤1300 px y traídas por image_paths:
- Germany_champions_2014_FIFA_World_Cup.jpg → photos/champions.jpg (1300×675)
- Kevin_Großkreutz_2014_FIFA_World_Cup_(cropped).jpg → photos/grosskreutz.jpg (763×1160, original)
- Bastian_Schweinsteiger_celebrates_at_the_2014_FIFA_World_Cup.jpg → photos/schweinsteiger.jpg (1300×802)
Schweinsteiger: recorte con rembg (u2net); Großkreutz: el recorte se llevaba a los compañeros de detrás, así que va enmarcado en la ficha. El escudo del pecho se difumina (sin escudos).
Campeones: foto enmarcada (portada de revista), sin recorte."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image, ImageFilter
from rembg import remove, new_session
def blur(im, box, k=9):
    im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(k)), box[:2]); return im
# Großkreutz: cabeza y pecho
g = Image.open('photos/grosskreutz.jpg').convert('RGB')
g = blur(g, (515, 670, 605, 820))
g = g.crop((110, 20, 660, 760))
g.save('photos/grosskreutz_crop.jpg', quality=94); grade('photos/grosskreutz_crop.jpg', 'img/grosskreutz_g.jpg', keep_blue=True)
# Schweinsteiger con la copa
s = Image.open('photos/schweinsteiger.jpg').convert('RGB')
s = blur(s, (915, 560, 965, 610), 6)
s = s.crop((620, 120, 1180, 802))
cut = remove(s, session=new_session('u2net')); cut.save('photos/schweinsteiger_cut.png'); grade('photos/schweinsteiger_cut.png', 'img/schweinsteiger_g.png', keep_blue=True)
# Campeones: encuadre
c = Image.open('photos/champions.jpg').convert('RGB').crop((0, 100, 1300, 675))
c.save('photos/champions_crop.jpg', quality=94); grade('photos/champions_crop.jpg', 'img/champions_g.jpg', keep_blue=True)
