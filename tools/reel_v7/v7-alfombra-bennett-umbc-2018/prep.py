import sys; sys.path.insert(0,'../bielsa')
from grade import grade
from PIL import Image
from rembg import remove, new_session
s=new_session('isnet-general-use')
for n in ['bennett','jerome']:
    im=Image.open(f'photos/{n}.jpg').convert('RGB')
    out=remove(im,session=s,alpha_matting=True)
    bb=out.getbbox(); out.crop(bb).save(f'photos/{n}_cut.png')
# assistants: recorte del banquillo (derecha); spectrum: encuadre
a=Image.open('photos/assistants.jpg'); a.crop((600,560,1238,1560)).save('photos/assistants_c.jpg',quality=92)
Image.open('photos/spectrum.jpg').crop((0,0,1600,1067)).save('photos/spectrum_c.jpg',quality=92)
grade('photos/bennett_cut.png','img/bennett_cut_g.png')
grade('photos/jerome_cut.png','img/jerome_cut_g.png')
grade('photos/assistants_c.jpg','img/assistants_g.png')
grade('photos/spectrum_c.jpg','img/spectrum_g.png')
