# Fotos de v7-general-michels: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · retrato de Rinus Michels, 14/08/1966 (Joost Evers / Anefo, CC0): recortado con rembg
cut(Image.open('photos/raw1.jpg').convert('RGB')).save('photos/p1_cut.png')
# 2 · Michels en el banquillo, 24/01/1965 (Eric Koch / Anefo, CC0): en marco de archivo, encuadre sobre Michels
Image.open('photos/raw2.jpg').convert('RGB').crop((300,60,1200,923)).save('photos/p2.jpg',quality=92)
# 3 · entrenamiento del Ajax, 09/04/1969 (Joost Evers / Anefo, CC0): en marco, encuadre sobre Michels
Image.open('photos/raw3.jpg').convert('RGB').crop((150,250,790,1330)).save('photos/p3.jpg',quality=92)
# 4 · Michels y Van Praag detrás de la Copa de Europa, Schiphol, 03/06/1971 (Anefo, CC0): en portada de revista
Image.open('photos/raw4.jpg').convert('RGB').crop((0,200,932,1180)).save('photos/p4.jpg',quality=92)
for k in (2,3,4): grade(f'photos/p{k}.jpg',f'img/p{k}_g.jpg')
grade('photos/p1_cut.png','img/p1_cut_g.png'); g=Image.open('img/p1_cut_g.png'); g=g.crop(g.getbbox()); g.save('img/p1_cut_g.png',optimize=True)
