"""Recortes y gradación de las fotos de v7-comba-mikan-1942 (../bielsa/grade.py). Fotos enmarcadas, sin rembg:
el recorte de Mikan arrastraba a los jugadores que se le cruzan; la silueta del principio es dibujada."""
from PIL import Image
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
Image.open('photos/mikan.jpg').convert('RGB').crop((90, 140, 820, 1610)).save('photos/mikan_crop.jpg', quality=92)   # Mikan (#99) de cuerpo entero
Image.open('photos/meyer.jpg').convert('RGB').crop((110, 40, 1000, 760)).save('photos/meyer_crop.jpg', quality=92)   # Meyer, sin la mesa
Image.open('photos/lakers.jpg').convert('RGB').crop((0, 0, 1098, 650)).save('photos/lakers_crop.jpg', quality=92)    # sin el pie impreso
grade('photos/mikan_crop.jpg', 'img/mikan_g.jpg')
grade('photos/meyer_crop.jpg', 'img/meyer_g.jpg', keep_blue=False)
grade('photos/depaul.jpg', 'img/depaul_g.jpg', keep_blue=False)
grade('photos/lakers_crop.jpg', 'img/lakers_g.jpg', keep_blue=False)
