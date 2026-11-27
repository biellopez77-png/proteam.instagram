# Fotos de v7-no-se-entrena-phog-allen: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
# Las raw*.jpg vienen de Commons (Special:FilePath), descargadas en el sandbox de Higgsfield y reducidas a 1600 px
from rembg import remove, new_session
from PIL import Image
import numpy as np, cv2, sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · James Naismith con balón y cesta (dominio público): recortado con rembg, de cuerpo entero
c=cut(Image.open('photos/raw1.jpg').convert('RGB')); a=np.array(c); a[...,3]=np.where(a[...,3]<120,0,a[...,3])
n,lab,st,_=cv2.connectedComponentsWithStats((a[...,3]>0).astype(np.uint8)); big=1+np.argmax(st[1:,cv2.CC_STAT_AREA]); a[...,3][lab!=big]=0
Image.fromarray(a).save('photos/p1_cut.png')
grade('photos/p1_cut.png','img/p1_cut_g.png'); g=Image.open('img/p1_cut_g.png'); g=g.crop(g.getbbox()); g.save('img/p1_cut_g.png',optimize=True)
# 2 · Primer borrador de las 13 reglas (J. Naismith, dic. 1891, dominio público): la primera hoja, como un folio
Image.open('photos/raw2.jpg').convert('RGB').crop((0,0,800,975)).save('photos/p2.jpg',quality=92)
# 3 · Phog Allen, 1953 (dominio público): ficha (fotografía de periódico; sin recorte)
Image.open('photos/raw3.jpg').convert('RGB').save('photos/p3.jpg',quality=95)
# 4 · Equipo de Kansas, 1924 (Squires Studio, dominio público): solo la foto, sin titular ni pie del periódico
Image.open('photos/raw4.jpg').convert('RGB').crop((50,118,1556,1262)).save('photos/p4.jpg',quality=92)
for k in (2,3,4): grade(f'photos/p{k}.jpg',f'img/p{k}_g.jpg')
