"""Preparación de fotos (v7-libreta-reep-1950). python3 cut.py
Las fotos se bajan en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor) y llegan por image_paths:
- County_ground_swindon_town_end.jpg → photos/town_end.jpg (640×480, original)
- Legal_pad_and_pencil.jpg → photos/pad.jpg (1600 px)
- Football_in_the_County_Ground_-_geograph.org.uk_-_2570682.jpg → photos/county2011.jpg (1600 px)
La libreta llena todo el encuadre (no hay fondo que quitar): va enmarcada, sin rembg."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image
grade('photos/town_end.jpg', 'img/town_end_g.jpg', keep_blue=True)
Image.open('photos/pad.jpg').crop((200, 330, 1500, 1200)).save('photos/pad_crop.jpg', quality=94)
grade('photos/pad_crop.jpg', 'img/pad_g.jpg', keep_blue=True)
Image.open('photos/county2011.jpg').crop((180, 120, 1500, 1000)).save('photos/county_crop.jpg', quality=94)
grade('photos/county_crop.jpg', 'img/county_g.jpg', keep_blue=False)
