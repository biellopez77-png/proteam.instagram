# Fotos de v7-sistema-lobanovski: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · Valeri Lobanovski, 16/09/1985 (Rob Croes / Anefo, CC0): recortado con rembg
cut(Image.open('photos/raw1.jpg').convert('RGB')).save('photos/p1_cut.png')
# 2 · Lobanovski en la tribuna, 05/04/1975 (Rob Mieremet / Anefo, CC0): en marco de prensa, entera
Image.open('photos/raw2.jpg').convert('RGB').crop((0,60,995,1300)).save('photos/p2.jpg',quality=92)
# 3 · Dinamo de Kiev, 23/04/1975 (Anefo, CC0): en marco de archivo
Image.open('photos/raw3.jpg').convert('RGB').crop((0,120,1500,994)).save('photos/p3.jpg',quality=92)
grade('photos/p2.jpg','img/p2_g.jpg'); grade('photos/p3.jpg','img/p3_g.jpg')
grade('photos/p1_cut.png','img/p1_cut_g.png'); g=Image.open('img/p1_cut_g.png'); g=g.crop(g.getbbox()); g.save('img/p1_cut_g.png',optimize=True)
