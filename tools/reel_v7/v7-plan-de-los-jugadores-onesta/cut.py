"""Recortes y gradación de las fotos de v7-plan-de-los-jugadores-onesta (rembg + ../bielsa/grade.py)."""
from PIL import Image
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
# 1 · French time-out (A1B2C3D4, 30/1/2009, CC BY-SA 3.0): el corro, enmarcado, B/N con el azul de la equipación
Image.open('photos/timeout.jpg').convert('RGB').crop((40, 250, 880, 700)).save('photos/timeout_crop.jpg', quality=93)
grade('photos/timeout_crop.jpg', 'img/timeout_g.jpg')
# 2 · Claude Onesta May 2010 (Patrick Subotkiewiez, CC BY 2.0): recorte con rembg (fondo desenfocado), B/N
im = Image.open('photos/onesta.jpg').convert('RGB'); w, h = im.size; im = im.crop((8, 8, w - 8, h - 8))
im.save('photos/onesta_crop.jpg', quality=93)
remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save('photos/onesta_cut.png')
grade('photos/onesta_cut.png', 'img/onesta_g.png', keep_blue=False)
grade('photos/onesta_crop.jpg', 'img/onesta_frame_g.jpg', keep_blue=False)
# el recorte de Onesta empieza a 400 px: se quita el aire de arriba
c = Image.open('img/onesta_g.png'); c.crop((0, 370, 940, c.height)).save('img/onesta_g.png')
