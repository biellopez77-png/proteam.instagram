"""Recortes y gradación de las fotos de v7-alinea-el-momento-ramsey-1966 (../bielsa/grade.py).
Fotos enmarcadas (sin rembg: retratos de archivo con fondo cargado). Greaves, recortado del retrato con Charlton (solo Greaves);
el balón de la final, con máscara circular (es una esfera)."""
from PIL import Image, ImageDraw, ImageFilter
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
Image.open('photos/greaves.jpg').convert('RGB').crop((0, 0, 700, 960)).save('photos/greaves_crop.jpg', quality=92)   # Greaves (Charlton queda fuera; solo asoma el borde de su abrigo abajo a la izquierda)
Image.open('photos/hurst.jpg').convert('RGB').crop((0, 0, 776, 1000)).save('photos/hurst_crop.jpg', quality=92)
Image.open('photos/ramsey.jpg').convert('RGB').crop((0, 0, 743, 1000)).save('photos/ramsey_crop.jpg', quality=92)
b = Image.open('photos/ball.jpg').convert('RGB'); m = Image.new('L', b.size, 0)
ImageDraw.Draw(m).ellipse((38, 28, 966, 952), fill=255); m = m.filter(ImageFilter.GaussianBlur(2))
b.putalpha(m); b.crop((30, 20, 974, 960)).save('photos/ball_cut.png')
grade('photos/greaves_crop.jpg', 'img/greaves_g.jpg', keep_blue=False)
grade('photos/hurst_crop.jpg', 'img/hurst_g.jpg', keep_blue=False)
grade('photos/ramsey_crop.jpg', 'img/ramsey_g.jpg', keep_blue=False)
grade('photos/ball_cut.png', 'img/ball_g.png', keep_blue=False)
import numpy as np   # el cuero del balón sale muy oscuro en B/N: se aclara (gamma 0,62) sin tocar el alfa
im = np.array(Image.open('img/ball_g.png')).astype(np.float32); im[..., :3] = 255 * (im[..., :3] / 255) ** .62
Image.fromarray(im.astype(np.uint8)).save('img/ball_g.png')
