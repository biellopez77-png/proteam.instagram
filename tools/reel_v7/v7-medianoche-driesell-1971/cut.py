"""Recortes y gradación de las fotos de v7-medianoche-driesell-1971 (rembg + ../bielsa/grade.py)."""
from PIL import Image
import sys, numpy as np; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
# 1 · Driesell con su «V» (c. 1969–70): el recorte con rembg arrastraba trozos de un jugador → foto enmarcada (ficha), mitad superior, B/N
Image.open('photos/vsign.jpg').convert('RGB').crop((0, 0, 928, 1060)).save('photos/vsign_crop.jpg', quality=92)
grade('photos/vsign_crop.jpg', 'img/vsign_g.jpg', keep_blue=False)
# 2 · Byrd Stadium (c. 1975): postal entera, B/N (la pista se redibuja en azul encima)
grade('photos/byrd.jpg', 'img/byrd_g.jpg', keep_blue=False)
# 3 · Driesell (c. 1976): portada, B/N
grade('photos/color.jpg', 'img/color_g.jpg', keep_blue=False)
# 4 · cronómetro (c. 1970, R. Henrik Nilsson, CC BY 4.0): esfera recortada en círculo, B/N
sw = Image.open('photos/stopwatch.jpg').convert('RGB'); w, h = sw.size
cx, cy, r = 490, 735, 455
c = sw.crop((cx - r, cy - r, cx + r, cy + r)); c.save('photos/stopwatch_crop.jpg', quality=92)
grade('photos/stopwatch_crop.jpg', 'img/sw_g.png', keep_blue=False)
a = Image.open('img/sw_g.png').convert('RGBA'); m = Image.new('L', a.size, 0)
from PIL import ImageDraw; ImageDraw.Draw(m).ellipse((4, 4, a.size[0] - 4, a.size[1] - 4), fill=255); a.putalpha(m); a.save('img/sw_g.png')
