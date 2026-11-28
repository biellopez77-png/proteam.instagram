"""Fotos de v7-psicologo-feola-1958 (Marta A, 28/11). python3 cut.py
Bajadas en el sandbox de Higgsfield (Commons, Special:FilePath?width=1600) y traídas por image_paths:
- raw1.jpg  Vicente Feola 1958.jpg (Svenskt Pressfoto / Scanpix, dominio público), 468×661
- raw2.jpg  Pelé jump 1958.jpg (Scanpix, dominio público), 1200×1581
- raw3.jpg  Garrincha and Vavà 1958 World Cup final.jpg (Scanpix, dominio público), 411×220
- raw4.jpg  Winning brazilian National team 1958.jpg (Scanpix, dominio público), 600×400"""
from PIL import Image
import numpy as np, sys; sys.path.insert(0,'../bielsa'); from grade import grade
from rembg import remove, new_session
S=new_session('isnet-general-use')
def hard(im, lo=110):
    a=np.array(im); a[...,3]=np.where(a[...,3]<lo,0,np.minimum(255,a[...,3].astype(int)*1.3)).astype(np.uint8); return Image.fromarray(a)
# 1 · Feola en Hindås: recorte (cielo limpio) a 2× para la ficha; la polaroid lleva la foto entera
im=Image.open('photos/raw1.jpg').convert('RGB'); im.save('photos/p1.jpg',quality=94); grade('photos/p1.jpg','img/p1_g.jpg',keep_blue=False)
big=im.crop((200,0,468,661)).resize((536,1322),Image.LANCZOS)
hard(remove(big,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)).save('photos/p1_cut.png'); grade('photos/p1_cut.png','img/p1c_g.png',keep_blue=False)
# 2 · Pelé en la final: encuadre sobre Pelé (fuera el portero y el defensa de abajo)
Image.open('photos/raw2.jpg').convert('RGB').crop((600,120,1180,1000)).save('photos/p2.jpg',quality=94); grade('photos/p2.jpg','img/p2_g.jpg',keep_blue=False)
# 3 · Garrincha y Vavá en la final: entera (es pequeña), a 2×
Image.open('photos/raw3.jpg').convert('RGB').resize((822,440),Image.LANCZOS).save('photos/p3.jpg',quality=94); grade('photos/p3.jpg','img/p3_g.jpg',keep_blue=False)
# 4 · vuelta de honor: entera
Image.open('photos/raw4.jpg').convert('RGB').save('photos/p4.jpg',quality=94); grade('photos/p4.jpg','img/p4_g.jpg',keep_blue=False)
