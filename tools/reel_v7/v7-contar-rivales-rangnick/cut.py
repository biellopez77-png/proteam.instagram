# Fotos de v7-contar-rivales-rangnick: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
# Las raw*.jpg vienen de Commons (Special:FilePath, 1600 px) descargadas en el sandbox de Higgsfield
from rembg import remove, new_session
from PIL import Image
import numpy as np, cv2, sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
def solo(path):   # fuera las motas sueltas del recorte: solo queda la figura grande
    g=np.array(Image.open(path)); n,lab,st,_=cv2.connectedComponentsWithStats((g[...,3]>0).astype(np.uint8))
    big=1+np.argmax(st[1:,cv2.CC_STAT_AREA]); g[...,3][lab!=big]=0; Image.fromarray(g).crop(Image.fromarray(g).getbbox()).save(path,optimize=True)
# 1 · Ralf Rangnick, 20/09/2018 (Steffen Prößdorf, CC BY-SA 4.0): recortado con rembg, sin el rótulo del banquillo
Image.open('photos/raw1.jpg').convert('RGB').crop((150,0,1500,1067)).save('photos/p1.jpg',quality=92)
c=cut(Image.open('photos/p1.jpg')); a=np.array(c); a[...,3]=np.where(a[...,3]<120,0,a[...,3]); Image.fromarray(a).save('photos/p1_cut.png')
grade('photos/p1_cut.png','img/p1_cut_g.png'); solo('img/p1_cut_g.png')
# 2 · Backnang, vista aérea, 31/07/2020 (Jedesto, CC BY-SA 4.0): encuadre sobre la ciudad, B/N sin azul (el cielo no se tiñe)
Image.open('photos/raw2.jpg').convert('RGB').crop((350,330,1350,910)).save('photos/p2.jpg',quality=92)
grade('photos/p2.jpg','img/p2_g.jpg',keep_blue=False)
# 3 · Valeri Lobanovski, 16/09/1985 (Rob Croes / Anefo, CC0): recortado con rembg
Image.open('photos/raw3.jpg').convert('RGB').crop((0,0,1300,1733)).save('photos/p3.jpg',quality=92)
c=cut(Image.open('photos/p3.jpg')); a=np.array(c); a[...,3]=np.where(a[...,3]<120,0,a[...,3]); Image.fromarray(a).save('photos/p3_cut.png')
grade('photos/p3_cut.png','img/p3_cut_g.png',keep_blue=False); solo('img/p3_cut_g.png')
# 4 · Dinamo de Kiev, 23/04/1975 (Anefo / Nationaal Archief, CC0): los once, como recorte de periódico
Image.open('photos/raw4.jpg').convert('RGB').crop((330,180,1480,1000)).save('photos/p4.jpg',quality=92)
grade('photos/p4.jpg','img/p4_g.jpg',keep_blue=False)
for f in ['img/p1_cut_g.png','img/p3_cut_g.png']:
    im=Image.open(f); 
    if im.width>900: im.resize((900,int(im.height*900/im.width)),Image.LANCZOS).save(f,optimize=True)
