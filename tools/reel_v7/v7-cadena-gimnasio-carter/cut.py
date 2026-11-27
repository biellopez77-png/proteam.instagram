"""Preparación de fotos (v7-cadena-gimnasio-carter). python3 cut.py
Las fotos se bajan y se recortan en el sandbox de Higgsfield (Commons no descarga desde nuestro contenedor):
- Richmond_High_School_2.jpg → photos/richmond.jpg (1400 px)
- Coach_Carter_at_an_interview_in_2014-_2014-08-21_16-05.jpg → photos/carter_crop.jpg (recorte de cabeza y hombros; logotipos de los micrófonos difuminados con máscara suave)
- Old_door_locked.jpg → photos/door.jpg (1400 px)
El recorte con rembg de Carter no queda limpio (los micrófonos van delante), así que va enmarcado."""
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from PIL import Image
r = Image.open('photos/richmond.jpg'); r.crop((0, 120, 1400, 988)).save('photos/richmond_crop.jpg', quality=94)
grade('photos/richmond_crop.jpg', 'img/richmond_g.jpg', keep_blue=True)
c = Image.open('photos/carter_crop.jpg'); c.crop((40, 20, 1060, 1060)).save('photos/carter_sq.jpg', quality=94)
grade('photos/carter_sq.jpg', 'img/carter_g.jpg', keep_blue=False)
grade('photos/door.jpg', 'img/door_g.jpg', keep_blue=False)
