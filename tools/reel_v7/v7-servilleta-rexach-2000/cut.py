"""Recortes y gradación de las fotos de v7-servilleta-rexach-2000 (rembg + ../bielsa/grade.py)."""
from PIL import Image
import sys, numpy as np; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
im = Image.open('photos/messi.jpg').convert('RGB')   # 1 · Leo Messi, 26/10/2005 (Josep Tomàs)
remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save('photos/messi_cut.png')
grade('photos/messi_cut.png', 'img/messi_g.png')
grade('photos/messi.jpg', 'img/messi_frame_g.jpg')    # versión enmarcada (portada de revista)
# 2 · Carles Rexach, 2008 (Tuvu13): foto pequeña → enmarcada, B/N
Image.open('photos/rexach.jpg').convert('RGB').resize((456, 630), Image.LANCZOS).save('photos/rexach_up.jpg', quality=93)
grade('photos/rexach_up.jpg', 'img/rexach_g.jpg', keep_blue=False)
