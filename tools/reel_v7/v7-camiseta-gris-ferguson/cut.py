# Fotos de v7-camiseta-gris-ferguson: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
# Las raw*.jpg vienen de Commons (Special:FilePath) descargadas en el sandbox de Higgsfield
from rembg import remove, new_session
from PIL import Image, ImageFilter
import numpy as np, cv2, sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
def solo(path):
    g=np.array(Image.open(path)); n,lab,st,_=cv2.connectedComponentsWithStats((g[...,3]>0).astype(np.uint8))
    big=1+np.argmax(st[1:,cv2.CC_STAT_AREA]); g[...,3][lab!=big]=0; Image.fromarray(g).crop(Image.fromarray(g).getbbox()).save(path,optimize=True)
# 1 · Inside The Dell, marzo de 1997 (Colin Smith, CC BY-SA 2.0): la franja de vallas publicitarias va desenfocada (sin marcas legibles)
im=Image.open('photos/raw1.jpg').convert('RGB')
band=(0,146,633,166); im.paste(im.crop(band).filter(ImageFilter.GaussianBlur(2.5)),band[:2])
im=im.resize((im.width*2,im.height*2),Image.LANCZOS); im.save('photos/p1.jpg',quality=92)
grade('photos/p1.jpg','img/p1_g.jpg')
# 2 · Alex Ferguson, marzo de 1992 (Øyvind Vik, dominio público): recortado con rembg (la foto es pequeña: ficha chica)
im=Image.open('photos/raw2.jpg').convert('RGB'); im=im.resize((im.width*2,im.height*2),Image.LANCZOS); im.save('photos/p2.jpg',quality=95)
c=cut(im); a=np.array(c); a[...,3]=np.where(a[...,3]<120,0,a[...,3]); Image.fromarray(a).save('photos/p2_cut.png')
grade('photos/p2_cut.png','img/p2_cut_g.png',keep_blue=False); solo('img/p2_cut_g.png')
# 3 · The Dell, Milton Road End, 2000 (Dan Kerins, CC BY 2.5): encuadre del arco y la pared de ladrillo, sin el escudo ni el rótulo del club
Image.open('photos/raw3.jpg').convert('RGB').crop((560,430,1280,960)).save('photos/p3.jpg',quality=92)
grade('photos/p3.jpg','img/p3_g.jpg',keep_blue=False)
