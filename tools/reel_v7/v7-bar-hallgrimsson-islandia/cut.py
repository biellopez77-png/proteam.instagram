"""Preparación de fotos (v7-bar-hallgrimsson-islandia). python3 cut.py"""
from PIL import Image, ImageFilter
import sys, numpy as np; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
# 1 · Laugardalsvöllur (Hlynz, 2007): sin el público de primer plano y con parte del cielo; vallas publicitarias suavizadas (sin logotipos legibles)
im = Image.open('photos/stadium.jpg').convert('RGB')
for band in [(0, 735, 1600, 800), (150, 650, 1100, 690)]: im.paste(im.crop(band).filter(ImageFilter.GaussianBlur(6)), band[:2])
im.crop((0, 300, 1600, 1100)).save('photos/stadium_crop.jpg', quality=94)
grade('photos/stadium_crop.jpg', 'img/stadium_g.jpg', keep_blue=True)
# 2 · Heimir Hallgrímsson (Svetlana Beketova, 2018): cabeza y hombros, por encima del texto de la acreditación; recorte con rembg
h = Image.open('photos/heimir.jpg').convert('RGB').crop((0, 0, 478, 440))
h.save('photos/heimir_crop.jpg', quality=95)
cut = remove(h, session=new_session('isnet-general-use'))
a = np.array(cut); H = a.shape[0]; n = 90
a[..., 3] = (a[..., 3] * np.clip((H - np.arange(H)) / n, 0, 1)[:, None]).astype(np.uint8)   # base fundida
Image.fromarray(a).save('photos/heimir_cut.png')
grade('photos/heimir_cut.png', 'img/heimir_g.png', keep_blue=False)
grade('photos/heimir_crop.jpg', 'img/heimir_frame_g.jpg', keep_blue=False)
