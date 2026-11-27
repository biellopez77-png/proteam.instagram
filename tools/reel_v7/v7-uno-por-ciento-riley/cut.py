# Fotos de v7-uno-por-ciento-riley: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
# Las raw*.jpg vienen de Commons (Special:FilePath, 1600-1920 px) descargadas en el sandbox de Higgsfield, ya encuadradas allí
from rembg import remove, new_session
from PIL import Image
import numpy as np, sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · Kareem Abdul-Jabbar (Steve Lipofsky, CC BY 3.0): encuadrado sobre Kareem, en ficha de prensa
Image.open('photos/raw1.jpg').convert('RGB').crop((40,0,982,1360)).save('photos/p1.jpg',quality=92)
# 2 · Pat Riley, 06/04/1989 (Lacy Atkins / Los Angeles Times, CC BY 4.0): sin Magic Johnson (borde derecho) y recortado con rembg
Image.open('photos/raw2.jpg').convert('RGB').crop((0,40,830,1500)).save('photos/p2.jpg',quality=92)
c=cut(Image.open('photos/p2.jpg')); a=np.array(c); a[...,3]=np.where(a[...,3]<120,0,a[...,3]); Image.fromarray(a).save('photos/p2_cut.png')
# 3 · Magic Johnson (Steve Lipofsky, CC BY-SA 3.0): ficha
Image.open('photos/raw3.jpg').convert('RGB').save('photos/p3.jpg',quality=95)
# 4 · Desfile del título, 17/06/1987 (Joe Kennedy / Los Angeles Times, CC BY 4.0): la carroza con los jugadores y el trofeo
Image.open('photos/raw4.jpg').convert('RGB').crop((0,120,993,1120)).save('photos/p4.jpg',quality=92)
for k in (1,3,4): grade(f'photos/p{k}.jpg',f'img/p{k}_g.jpg')
grade('photos/p2_cut.png','img/p2_cut_g.png'); g=Image.open('img/p2_cut_g.png'); g=g.crop(g.getbbox()); g.save('img/p2_cut_g.png',optimize=True)
# Kareem: el azul solo en la camiseta (el fondo oscuro de la grada daba manchas azules)
import cv2
grade('photos/p1.jpg','photos/p1_bn.jpg',keep_blue=False)
A=cv2.imread('img/p1_g.jpg').astype(np.float32); B=cv2.imread('photos/p1_bn.jpg').astype(np.float32); h,w=A.shape[:2]
m=np.zeros((h,w),np.float32); m[int(.44*h):int(.97*h),int(.18*w):int(.62*w)]=1; m=cv2.GaussianBlur(m,(0,0),25)[...,None]
cv2.imwrite('img/p1_g.jpg',(A*m+B*(1-m)).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,92])
# Riley: fuera las motas sueltas del recorte (solo queda la figura grande)
g=np.array(Image.open('img/p2_cut_g.png')); n,lab,st,_=cv2.connectedComponentsWithStats((g[...,3]>0).astype(np.uint8))
big=1+np.argmax(st[1:,cv2.CC_STAT_AREA]); g[...,3][lab!=big]=0; Image.fromarray(g).save('img/p2_cut_g.png',optimize=True)
