"""Preparación de fotos (v7-cinco-mejores-haskins-1966). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor) y traídas por image_paths:
- UTEP_1966_basketball.jpg → photos/utep1966.jpg (1925×1361, original)
- Bobby_Joe_Hill_1966.jpeg → photos/hill.jpg (301×415, original: va como ficha pequeña)
- Texas_western_v_utah_nevil_shed_1966.jpg → photos/shed.jpg (518×717, original)
- Adolph_Rupp_1967.jpeg → photos/rupp1967.jpg (602×1007, original)
Rupp: recorte con rembg (u2net_human_seg). Las demás van enmarcadas (fondo de pabellón o de periódico: el recorte no queda limpio)."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image
from rembg import remove, new_session
r = Image.open('photos/rupp1967.jpg').convert('RGB').crop((0, 0, 602, 900))
remove(r, session=new_session('u2net_human_seg')).save('photos/rupp_cut.png'); grade('photos/rupp_cut.png', 'img/rupp_g.png', keep_blue=True)
grade('photos/hill.jpg', 'img/hill_g.jpg', keep_blue=True)
Image.open('photos/shed.jpg').convert('RGB').save('photos/shed_rgb.jpg', quality=95); grade('photos/shed_rgb.jpg', 'img/shed_g.jpg', keep_blue=True)
Image.open('photos/utep1966.jpg').convert('RGB').crop((0, 60, 1925, 1361)).save('photos/utep_crop.jpg', quality=94); grade('photos/utep_crop.jpg', 'img/utep_g.jpg', keep_blue=True)
