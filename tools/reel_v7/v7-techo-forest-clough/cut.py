from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
def cut(src, dst, box=None):
    im = Image.open(src).convert('RGB')
    if box: im = im.crop(box)
    remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save(dst)
# 1 · Brian Clough en Schiphol (1980): recorte de la figura, sin el abrigo de primer plano
cut('photos/clough.jpg', 'photos/clough_cut.png', (0, 0, 1061, 1380))
# 3 · Francis, Clough y Robertson (Ámsterdam, 1980): recorte de los tres
cut('photos/trio.jpg', 'photos/trio_cut.png', (100, 160, 1460, 1061))
# 2 · City Ground, 1978: postal (sin cielo de sobra)
Image.open('photos/city.jpg').convert('RGB').crop((0, 250, 1280, 857)).save('photos/city_crop.jpg', quality=92)
# 4 · estatua de Clough en Old Market Square (2015): foto en marco, la estatua y la plaza
Image.open('photos/statue.jpg').convert('RGB').crop((0, 300, 663, 1024)).save('photos/statue_crop.jpg', quality=92)
grade('photos/clough_cut.png', 'img/clough_g.png')
grade('photos/trio_cut.png', 'img/trio_g.png')
grade('photos/city_crop.jpg', 'img/city_g.jpg', keep_blue=False)
grade('photos/statue_crop.jpg', 'img/statue_g.jpg', keep_blue=False)
# limpieza del trío: fuera el poste de «No parking», la cadena y la rueda del coche; base fundida
import numpy as np
im = Image.open('img/trio_g.png'); a = np.array(im)
a[760:900, 30:160, 3] = 0; a[700:900, 870:968, 3] = 0
h = a.shape[0]; ramp = np.clip((h - np.arange(h)) / 150, 0, 1)[:, None]
a[..., 3] = (a[..., 3] * ramp).astype(np.uint8)
im2 = Image.fromarray(a); im2.save('img/trio_g.png')
im = Image.open('img/clough_g.png'); a = np.array(im); h = a.shape[0]
ramp = np.clip((h - np.arange(h)) / 160, 0, 1)[:, None]; a[..., 3] = (a[..., 3] * ramp).astype(np.uint8)
Image.fromarray(a).save('img/clough_g.png')
for n in ['clough', 'trio']:
    im = Image.open(f'img/{n}_g.png'); im.thumbnail((900, 900)); im.save(f'img/{n}_g.png', optimize=True)
