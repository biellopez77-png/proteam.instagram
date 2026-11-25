from rembg import remove, new_session
from PIL import Image
import sys, numpy as np; sys.path.insert(0,'../bielsa'); from grade import grade
s=new_session('isnet-general-use'); h=new_session('u2net_human_seg')
def cut(src,dst,box=None):
    im=Image.open(src).convert('RGB')
    if box: im=im.crop(box)
    o=remove(im,session=s,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
    hh=remove(im,session=h)
    a=np.maximum(np.array(o)[...,3],np.array(hh)[...,3]); o.putalpha(Image.fromarray(a)); o.save(dst)
cut('photos/k1.jpg','photos/k1_cut.png',(150,60,1600,1200))      # Cameron Indoor, 2011: sin el fondo de logos
Image.open('photos/k2.jpg').convert('RGB').crop((470,40,1070,700)).save('photos/k2_crop.jpg',quality=92)   # West Point, 2010: en foto enmarcada, sin el escudo del atril
Image.open('photos/k3.jpg').convert('RGB').crop((0,0,1100,1235)).save('photos/k3_crop.jpg',quality=92)
grade('photos/k1_cut.png','img/k1_cut_g.png'); g=Image.open('img/k1_cut_g.png'); g.resize((900,int(900*g.height/g.width)),Image.LANCZOS).save('img/k1_cut_g.png',optimize=True)
grade('photos/k2_crop.jpg','img/k2_g.jpg')
g=Image.open('photos/k3_crop.jpg'); g.resize((760,int(760*g.height/g.width)),Image.LANCZOS).save('photos/k3_small.jpg',quality=90)
grade('photos/k3_small.jpg','img/k3_g.jpg',keep_blue=False)
# limpieza a mano de restos del fondo que rembg deja: logo a la derecha (k1) y piedra a la izquierda (k2)
def clean(f, cond):
    im=np.array(Image.open(f)); H,Wd=im.shape[:2]; y,x=np.mgrid[0:H,0:Wd]; m=cond(x,y,im); im[...,3][m]=0; Image.fromarray(im).save(f,optimize=True)
clean('img/k1_cut_g.png', lambda x,y,im: (x>735)&(y<455+(x-735)*0.3))
#clean('img/k2_cut_g.png', lambda x,y,im: (((x<62)&(y<330))|((x<125)&(y>=330)&(y<480)))&(np.abs(im[...,2].astype(int)-im[...,0].astype(int))<25))
