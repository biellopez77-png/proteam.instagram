"""Recortes y gradación de las fotos de v7-jaula-footbonaut-dortmund-2012 (rembg + ../bielsa/grade.py)."""
from PIL import Image
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
# 1 · Klopp (2010): el micrófono lleva el logo del club → foto enmarcada, sin la parte baja; la ficha de prensa tapa la cabeza del micro
Image.open('photos/klopp.jpg').convert('RGB').crop((0, 30, 465, 520)).save('photos/klopp_crop.jpg', quality=92)
grade('photos/klopp_crop.jpg', 'img/klopp_g.jpg', keep_blue=False)
# 2 · Signal Iduna Park (2018): polaroid, B/N con el azul (el cielo)
Image.open('photos/stadium.jpg').convert('RGB').crop((0, 60, 1500, 844)).save('photos/stadium_crop.jpg', quality=92)
grade('photos/stadium_crop.jpg', 'img/stadium_g.jpg', keep_blue=True)
# 3 · Götze (2012): recorte con rembg, solo cara y cuello (sin escudo ni rayas)
remove(Image.open('photos/gotze.jpg').convert('RGB').crop((330, 0, 1270, 1150)), session=S).save('photos/gotze_cut.png')
grade('photos/gotze_cut.png', 'img/gotze_g.png', keep_blue=False)
# 4 · máquina de lanzar pelotas de tenis (1928): la máquina y el hombre que la maneja, B/N
Image.open('photos/machine.jpg').convert('RGB').crop((800, 360, 1330, 900)).save('photos/machine_crop.jpg', quality=92)
grade('photos/machine_crop.jpg', 'img/machine_g.jpg', keep_blue=False)
