from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
s=new_session('isnet-general-use')
im=Image.open('photos/sacchi.jpg').convert('RGB').crop((300,290,862,1200)); im.save('photos/sacchi_crop.jpg',quality=92)
o=remove(im,session=s,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10); o.save('photos/sacchi_cut.png')
Image.open('photos/sacchi.jpg').convert('RGB').crop((500,300,880,760)).save('photos/sacchi_face.jpg',quality=92)
Image.open('photos/cup.jpg').convert('RGB').crop((40,200,740,1420)).save('photos/cup_crop.jpg',quality=92)
grade('photos/sacchi_cut.png','img/sacchi_cut_g.png')
grade('photos/sacchi_face.jpg','img/sacchi_face_g.jpg')
grade('photos/fus.jpg','img/fus_g.jpg',keep_blue=False)
grade('photos/siro.jpg','img/siro_g.jpg')
grade('photos/cup_crop.jpg','img/cup_g.jpg')
