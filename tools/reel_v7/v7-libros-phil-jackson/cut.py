# Fotos de v7-libros-phil-jackson: recortes, rembg y gradación (tools/reel_v7/bielsa/grade.py)
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
# 1 · Phil Jackson (Keith Allison, 2009): recortado con rembg (u2net_human_seg; isnet-general-use dejaba el fondo oscuro)
im=Image.open('photos/raw1.jpg').convert('RGB').crop((0,180,1371,1600)); im.thumbnail((1000,1000))
remove(im,session=new_session('u2net_human_seg')).save('photos/p1_cut.png')
# 2 · Shaquille O'Neal en la final de 2000 (Bigmoe797): en marco, de la cabeza a la cintura, sin el jugador de detrás
# (rembg le cortaba la cabeza o metía la camiseta del compañero, así que va como foto de prensa enmarcada)
Image.open('photos/raw2.jpg').convert('RGB').crop((30,30,460,860)).save('photos/p2.jpg',quality=92)
# 3 y 4 · portadas (dominio público): enteras
Image.open('photos/raw3.jpg').convert('RGB').resize((1000,614),Image.LANCZOS).save('photos/p3.jpg',quality=92)
Image.open('photos/raw4.jpg').convert('RGB').save('photos/p4.jpg',quality=92)
grade('photos/p1_cut.png','img/p1_cut_g.png'); g=Image.open('img/p1_cut_g.png'); g=g.crop(g.getbbox()); g.save('img/p1_cut_g.png',optimize=True)
grade('photos/p2.jpg','img/p2_g.jpg'); grade('photos/p3.jpg','img/p3_g.jpg'); grade('photos/p4.jpg','img/p4_g.jpg')
