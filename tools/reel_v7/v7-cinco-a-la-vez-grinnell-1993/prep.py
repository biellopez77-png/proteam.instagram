import sys; sys.path.insert(0,'../bielsa')
from grade import grade
from PIL import Image
from rembg import remove, new_session
s=new_session('isnet-general-use')
# cronómetro: recorte rembg
w=Image.open('photos/watch.jpg').convert('RGB')
out=remove(w,session=s,alpha_matting=True); out.crop(out.getbbox()).save('photos/watch_cut.png')
# cartel: encuadre; 1925: sin cabecera
Image.open('photos/sign.jpg').crop((220,120,1240,560)).save('photos/sign_c.jpg',quality=92)
Image.open('photos/drake.jpg').convert('RGB').crop((20,20,1480,930)).save('photos/drake_c.jpg',quality=92)
# Taylor: el recorte rembg queda demasiado estrecho (brazos arriba); se usa la foto enmarcada
Image.open('photos/taylor.jpg').convert('RGB').crop((150,30,560,1120)).save('photos/taylor_c.jpg',quality=92)
grade('photos/taylor_c.jpg','img/taylor_g.png')
grade('photos/watch_cut.png','img/watch_cut_g.png')
grade('photos/sign_c.jpg','img/sign_g.png')
import numpy as np   # 1925: muy oscura; se aclara antes de graduar
a=np.clip(np.asarray(Image.open('photos/drake_c.jpg').convert('L'))/255/0.75,0,1)**0.55
Image.fromarray((a*255).astype('uint8')).convert('RGB').save('photos/drake_l.jpg',quality=92)
grade('photos/drake_l.jpg','img/drake_g.png',keep_blue=False)
