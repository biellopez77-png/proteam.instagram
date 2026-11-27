"""Fotos de v7-pantalla-gladiator-guardiola-2009: recorte (rembg) y gradación (tools/reel_v7/bielsa/grade.py)."""
from PIL import Image
import sys, numpy as np; sys.path.insert(0,'../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
# 3 · Guardiola en la banda del Camp Nou (16/05/2010): recorte de la figura (fuera el banquillo, el escudo y el rótulo)
im = Image.open('photos/guardiola_crop.jpg').convert('RGB')
remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save('photos/guardiola_cut.png')
grade('photos/guardiola_cut.png', 'img/guardiola_g.png', keep_blue=False)   # el traje cogía manchas azules
im = Image.open('img/guardiola_g.png'); a = np.array(im); h = a.shape[0]
ramp = np.clip((h - np.arange(h)) / 60, 0, 1)[:, None]; a[..., 3] = (a[..., 3] * ramp).astype(np.uint8)
Image.fromarray(a).save('img/guardiola_g.png', optimize=True)
# 1 · Estadio Olímpico (2007): polaroid con la grada y la cubierta, sin los rótulos del foso
Image.open('photos/olimpico.jpg').convert('RGB').crop((0, 40, 1600, 900)).save('photos/olimpico_crop.jpg', quality=92)
grade('photos/olimpico_crop.jpg', 'img/olimpico_g.jpg')
# 2 · Aficionados en el Olímpico (2012): fondo pequeño, grada y bandera
Image.open('photos/fans.jpg').convert('RGB').crop((200, 160, 1600, 951)).save('photos/fans_crop.jpg', quality=92)
grade('photos/fans_crop.jpg', 'img/fans_g.jpg')
# 4 · Final de Roma 2009: Guardiola abrazado, en portada; sin las vallas de publicidad del fondo
Image.open('photos/final2009.jpg').convert('RGB').crop((205, 200, 645, 515)).save('photos/final_crop.jpg', quality=95)
grade('photos/final_crop.jpg', 'img/final_g.jpg', keep_blue=False)
