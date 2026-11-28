"""Preparación de fotos (v7-escoba-all-blacks). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons, Special:Redirect/file; Commons no descarga desde nuestro contenedor) y traídas por image_paths:
- RWC_2011_final_FRA_-_NZL_McCaw_with_Ellis_Cup.jpg → photos/mccaw_copa.jpg (600×378, original)
- RWC_2011_final_FRA_-_NZL_All_Blacks_celebrate.jpg → photos/celebran.jpg (600×337, original)
- All_Blacks_Haka_at_Westpac_Stadium,_Wellington,_NZ.jpg → photos/haka.jpg (1400×934, original)
- Richie_McCaw_signing_autograph_..._(2015_RWC_All_Blacks_victory_parade_in_Wellington).jpg → photos/mccaw_desfile.jpg (reducida a 1600×1280)
Todas van enmarcadas (portada, foto de prensa, ficha): sin recorte con rembg, porque las fotos de grupo no dan un recorte limpio.
Se difuminan rótulos de patrocinadores y comercios y el helecho del pecho en la ficha de McCaw."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image, ImageFilter
def blur(im, box, k=9):
    im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(k)), box[:2]); return im
# 1 · McCaw con la copa (portada)
a = Image.open('photos/mccaw_copa.jpg').convert('RGB').crop((95, 0, 435, 378))
a.save('photos/mccaw_copa_crop.jpg', quality=95); grade('photos/mccaw_copa_crop.jpg', 'img/mccaw_copa_g.jpg')
# 2 · celebración final 2011 (ficha de prensa)
b = Image.open('photos/celebran.jpg').convert('RGB')
b = b.crop((0, 12, 600, 292))
b.save('photos/celebran_crop.jpg', quality=95); grade('photos/celebran_crop.jpg', 'img/celebran_g.jpg')
# 3 · haka en Wellington (foto de prensa): sin el videomarcador ni los anuncios de arriba
h = Image.open('photos/haka.jpg').convert('RGB')
h = h.crop((40, 240, 1400, 655))   # de la cintura arriba: fuera el videomarcador, los anuncios y la pancarta
h.save('photos/haka_crop.jpg', quality=94); grade('photos/haka_crop.jpg', 'img/haka_g.jpg')
# 4 · McCaw, desfile de 2015 (ficha): cabeza y pecho, sin el rótulo del comercio ni el helecho
m = Image.open('photos/mccaw_desfile.jpg').convert('RGB')
m = blur(m, (500, 330, 655, 530), 14); m = blur(m, (820, 320, 960, 470), 14); m = blur(m, (780, 480, 870, 540), 8)
m = m.crop((520, 120, 930, 660))
m.save('photos/mccaw_desfile_crop.jpg', quality=94); grade('photos/mccaw_desfile_crop.jpg', 'img/mccaw_ficha_g.jpg')
