# Fotos de v7-tacos-berna-1954: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
# raw1/2/3 se bajaron de Commons en el sandbox de Higgsfield ya encuadradas: raw1 = grupo que celebra el 1-0 (Com M03-0108-005-0025, recorte 680x760+540+560 sobre 1920 px);
# raw2 = esfera del reloj del Wankdorf con 2-3 y «Ungarn / Deutschland», sin el rótulo de la marca de arriba (recorte 1336x1351+216+541, a 1100 px); raw3 = Com M03-0108-005-0014 a 1500 px.
from rembg import remove, new_session
from PIL import Image
import numpy as np, sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · los húngaros celebran el 1-0 (Comet Photo AG, CC BY-SA 4.0): recorte del grupo con rembg
c=remove(Image.open('photos/raw1.jpg').convert('RGB'),session=S,alpha_matting=True,alpha_matting_foreground_threshold=200,alpha_matting_background_threshold=20,alpha_matting_erode_size=4); a=np.array(c)   # matting más suave: con el de serie se perdían las cabezas
a[...,3]=np.where(a[...,3]<60,0,a[...,3])
Image.fromarray(a).save('photos/p1_cut.png')
# 2 · el reloj de la final (Sandstein, CC BY 3.0): en polaroid, solo la mitad alta de la esfera (sin el 2/3, sin «Ungarn / Deutschland» y sin la esfera pequeña con la marca): recorte 875x570+110+28
Image.open("photos/raw2.jpg").convert("RGB").crop((110,28,985,598)).save("photos/p2.jpg",quality=92)
# 3 · minuto 2 de la final, Fritz Walter al fondo a la izquierda (Comet Photo AG, CC BY-SA 4.0): mitad baja, el campo
Image.open('photos/raw3.jpg').convert('RGB').crop((0,430,1500,1213)).save('photos/p3.jpg',quality=92)
for k in (2,3): grade(f'photos/p{k}.jpg',f'img/p{k}_g.jpg')
grade('photos/p1_cut.png','img/p1_cut_g.png'); g=Image.open('img/p1_cut_g.png'); g=g.crop(g.getbbox()); g.save('img/p1_cut_g.png',optimize=True)
print(Image.open('img/p1_cut_g.png').size)
