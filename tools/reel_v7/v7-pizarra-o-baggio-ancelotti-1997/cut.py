"""Recortes y gradación de las fotos de v7-pizarra-o-baggio-ancelotti-1997 (rembg + ../bielsa/grade.py)."""
from PIL import Image
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
# 1 · Roberto Baggio, Italia 90 (dominio público): recorte con rembg, B/N con el azul de la camiseta
im = Image.open('photos/baggio.jpg').convert('RGB')
remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save('photos/baggio_cut.png')
grade('photos/baggio_cut.png', 'img/baggio_g.png')
grade('photos/baggio.jpg', 'img/baggio_frame_g.jpg')
# 2 · Carlo Ancelotti, 14/3/2017 (Rufus46): cabeza y hombros (sin piernas; el escudo queda pequeño y en gris), enmarcado, B/N sin color
Image.open('photos/ancelotti.jpg').convert('RGB').crop((330, 130, 790, 560)).save('photos/ancelotti_crop.jpg', quality=93)
grade('photos/ancelotti_crop.jpg', 'img/ancelotti_g.jpg', keep_blue=False)
# 3 · Stadio Ennio Tardini, 13/1/2008 (Wetto): polaroid, B/N
grade('photos/tardini.jpg', 'img/tardini_g.jpg', keep_blue=False)
