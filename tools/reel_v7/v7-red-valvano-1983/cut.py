from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
s=new_session('isnet-general-use')
im=Image.open('photos/v82.jpg').convert('RGB')
o=remove(im,session=s,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# la chaqueta gris se pierde con isnet: alfa = máximo de isnet (pelo) y u2net_human_seg (cuerpo)
import numpy as np
h=remove(im,session=new_session('u2net_human_seg'))
a=np.maximum(np.array(o)[...,3],np.array(h)[...,3]); o.putalpha(Image.fromarray(a)); o.save('photos/v82_cut.png')
Image.open('photos/v83.jpg').convert('RGB').crop((150,60,1300,1500)).save('photos/v83_crop.jpg',quality=92)
Image.open('photos/news.jpg').convert('RGB').crop((115,320,915,1045)).save('photos/news_photo.jpg',quality=92)
Image.open('photos/news.jpg').convert('RGB').crop((30,90,1570,320)).save('photos/news_head.jpg',quality=92)
Image.open('photos/rey.jpg').convert('RGB').crop((0,0,1024,470)).save('photos/rey_crop.jpg',quality=92)
grade('photos/v82_cut.png','img/v82_cut_g.png'); g=Image.open('img/v82_cut_g.png'); g.resize((900,int(900*g.height/g.width)),Image.LANCZOS).save('img/v82_cut_g.png',optimize=True)
grade('photos/v83_crop.jpg','img/v83_g.jpg')
grade('photos/news_photo.jpg','img/news_photo_g.jpg',keep_blue=False)
grade('photos/news_head.jpg','img/news_head_g.jpg',keep_blue=False)
grade('photos/rey_crop.jpg','img/rey_g.jpg')
