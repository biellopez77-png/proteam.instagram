# Fotos de v7-carteles-herrera: recortes, rembg y gradación (tools/reel_v7/bielsa/grade.py)
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
# 1 · Herrera en el banquillo de San Siro (c. 1961): recorte en marco (la grada y los demás detrás no se pueden quitar limpios)
Image.open('photos/raw1.jpg').convert('RGB').crop((260,330,760,980)).save('photos/p1_crop.jpg',quality=92)
# 2 · Herrera con sus jugadores (c. 1961): foto entera en marco
Image.open("photos/raw2.jpg").convert("RGB").resize((1100,708),Image.LANCZOS).save('photos/p2.jpg',quality=92)
# 3 · Inter 1965-66 con los trofeos: pequeña, en marco
Image.open('photos/raw3.jpg').convert('RGB').save('photos/p3.jpg',quality=95)
# 4 · Facchetti y Herrera (1964-65): recortados con rembg
s=new_session('isnet-general-use')
im=Image.open('photos/raw4.jpg').convert('RGB').crop((330,180,1100,1332))
o=remove(im,session=s,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
o.save('photos/p4_cut.png')
grade('photos/p1_crop.jpg','img/p1_g.jpg'); grade('photos/p2.jpg','img/p2_g.jpg'); grade('photos/p3.jpg','img/p3_g.jpg')
grade('photos/p4_cut.png','img/p4_cut_g.png'); g=Image.open('img/p4_cut_g.png'); g=g.crop(g.getbbox()); g.resize((640,int(640*g.height/g.width)),Image.LANCZOS).save('img/p4_cut_g.png',optimize=True)
