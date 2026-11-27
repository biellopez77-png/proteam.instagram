# Fotos de v7-sexto-hombre-auerbach: recortes, rembg y gradación (tools/reel_v7/bielsa/grade.py)
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · Auerbach y Bill Russell en el banquillo (Jack O'Connell / The Sporting News, 1956): en marco de prensa, entera
Image.open('photos/raw1.jpg').convert('RGB').save('photos/p1.jpg',quality=92)
# 2 · Frank Ramsey (autor desconocido, 1954-64): recortado con rembg
cut(Image.open('photos/raw2.jpg').convert('RGB')).save('photos/p2_cut.png')
# 3 · Celtics campeones 1959-60 (autor desconocido): en marco, sin el pie de foto
Image.open('photos/raw3.jpg').convert('RGB').crop((0,20,1400,900)).save('photos/p3.jpg',quality=92)
# 4 · John Havlicek (autor desconocido / The Sporting News, años 60): recortado con rembg
cut(Image.open('photos/raw4.jpg').convert('RGB')).save('photos/p4_cut.png')
grade('photos/p1.jpg','img/p1_g.jpg'); grade('photos/p3.jpg','img/p3_g.jpg')
for n in ['p2','p4']:
    grade(f'photos/{n}_cut.png',f'img/{n}_cut_g.png'); g=Image.open(f'img/{n}_cut_g.png'); g=g.crop(g.getbbox()); g.save(f'img/{n}_cut_g.png',optimize=True)
