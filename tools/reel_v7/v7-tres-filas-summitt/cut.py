# Fotos de v7-tres-filas-summitt: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · Pat Summitt en la banda, Texas-Tennessee, 14/12/2008 (aaronisnotcool, CC BY 2.0): encuadre sobre Summitt y recorte con rembg
Image.open('photos/raw1.jpg').convert('RGB').crop((360,130,960,1067)).save('photos/p1.jpg',quality=92)
c=cut(Image.open('photos/p1.jpg')); import numpy as np; a=np.array(c)
a[:170,:175,3]=0                                  # fuera el halo de la gorra del policía que queda detrás
a[...,3]=np.where(a[...,3]<120,0,a[...,3])        # sin restos semitransparentes
Image.fromarray(a).save('photos/p1_cut.png')
# 2 · Thompson-Boling Arena (TN 66, CC0): en polaroid, sin el rótulo grande del parqué de la izquierda
Image.open('photos/raw2.jpg').convert('RGB').crop((380,40,1600,1080)).save('photos/p2.jpg',quality=92)
# 3 · Pat Summitt, 24/06/2008 (Staff Sgt. Christina M. O'Connell, Ejército de EE. UU., dominio público; recorte de User:Blueag9): ficha a tamaño medio
Image.open('photos/raw3.jpg').convert('RGB').save('photos/p3.jpg',quality=95)
for k in (2,3): grade(f'photos/p{k}.jpg',f'img/p{k}_g.jpg')
grade('photos/p1_cut.png','img/p1_cut_g.png'); g=Image.open('img/p1_cut_g.png'); g=g.crop(g.getbbox()); g.save('img/p1_cut_g.png',optimize=True)
