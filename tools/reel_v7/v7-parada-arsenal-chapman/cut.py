from rembg import remove, new_session
from PIL import Image
import numpy as np, sys; sys.path.insert(0,'../bielsa'); from grade import grade
im=Image.open('photos/chapman.jpg').convert('RGB'); im=im.resize((900,int(900*im.height/im.width)),Image.LANCZOS)
o=remove(im,session=new_session('isnet-general-use'),alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
h=remove(im,session=new_session('u2net_human_seg'))
a=np.maximum(np.array(o)[...,3],np.array(h)[...,3]); o.putalpha(Image.fromarray(a)); o.save('photos/chapman_cut.png')
Image.open('photos/interior.jpg').convert('RGB').crop((90,330,1600,820)).save('photos/interior_crop.jpg',quality=92)
Image.open('photos/tiles.jpg').convert('RGB').crop((200,150,1360,1064)).save('photos/tiles_crop.jpg',quality=92)
Image.open('photos/entrance.jpg').convert('RGB').crop((40,590,1560,1110)).save('photos/entrance_crop.jpg',quality=92)
grade('photos/chapman_cut.png','img/chapman_cut_g.png')
grade('photos/interior_crop.jpg','img/interior_g.jpg')
grade('photos/tiles_crop.jpg','img/tiles_g.jpg')
grade('photos/entrance_crop.jpg','img/entrance_g.jpg')
