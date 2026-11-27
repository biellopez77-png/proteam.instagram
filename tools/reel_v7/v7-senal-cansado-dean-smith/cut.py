"""Preparación de fotos (v7-senal-cansado-dean-smith). python3 cut.py
Fotos bajadas en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor) y traídas por image_paths:
- Dean_Smith_1973.jpg → photos/smith1973.jpg (1081×1600)
- Dean_Smith_Center_with_game_in_session.JPG → photos/center.jpg (1600×1200)
- Dean_Smith_1967.jpeg → photos/smith1967.jpg (1095×1600)
- Belmont_Bench_NCAA_Tournament.jpg → photos/belmont.jpg (descargada, NO se usa: llena de logotipos y de otro equipo; el aplauso se dibuja)
Sin escudos ni logotipos: de la foto del pabellón se recorta fuera el cartel publicitario de arriba y el logotipo del aro."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image
from rembg import remove, new_session
hs = new_session('u2net_human_seg')
# Dean Smith hacia 1973: recorte con rembg (fondo liso)
s = Image.open('photos/smith1973.jpg').convert('RGB')
remove(s, session=hs).resize((760, 1125), Image.LANCZOS).save('photos/smith1973_cut.png'); grade('photos/smith1973_cut.png', 'img/smith1973_g.png', keep_blue=True)
# Pabellón Dean Smith: tiro libre; fuera el cartel de arriba y el logotipo del aro
c = Image.open('photos/center.jpg').convert('RGB').crop((0, 150, 1400, 1200))
c.save('photos/center_crop.jpg', quality=94); grade('photos/center_crop.jpg', 'img/center_g.jpg', keep_blue=True)
# Dean Smith 1967 (Daily Tar Heel): enmarcada; fuera la cara borrosa de la izquierda
o = Image.open('photos/smith1967.jpg').convert('RGB').crop((330, 0, 1095, 1150))
o.save('photos/smith1967_crop.jpg', quality=94); grade('photos/smith1967_crop.jpg', 'img/smith1967_g.jpg', keep_blue=False)
