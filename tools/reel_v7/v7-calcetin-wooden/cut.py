# Fotos de v7-calcetin-wooden: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · John Wooden, anuario Southern Campus 1960 (Associated Students UCLA, dominio público): en ficha de prensa, encuadre sobre Wooden
#     (el traje claro sobre la pared clara no se deja recortar con rembg: el recorte salía con huecos)
Image.open('photos/raw1.jpg').convert('RGB').crop((380,120,1180,1150)).save('photos/p1.jpg',quality=92)
# 2 · Wooden con Alcindor, Shackelford, Heitz y Allen, 19/10/1965 (Los Angeles Times, CC BY 4.0): en marco de archivo, sin las gradas de arriba
Image.open('photos/raw2.jpg').convert('RGB').crop((0,230,1200,1490)).save('photos/p2.jpg',quality=92)
# 3 · Lew Alcindor con UCLA, c. 1966 (Malcolm W. Emmons, dominio público): recorte con rembg
cut(Image.open('photos/raw3.jpg').convert('RGB')).save('photos/p3_cut.png')
for k in (1,2): grade(f'photos/p{k}.jpg',f'img/p{k}_g.jpg')
for k in (3,):
    grade(f'photos/p{k}_cut.png',f'img/p{k}_cut_g.png'); g=Image.open(f'img/p{k}_cut_g.png'); g=g.crop(g.getbbox()); g.save(f'img/p{k}_cut_g.png',optimize=True)
