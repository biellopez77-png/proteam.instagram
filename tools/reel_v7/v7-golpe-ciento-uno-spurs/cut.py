from rembg import remove, new_session
from PIL import Image
s=new_session('isnet-general-use')
def cut(src,box,dst):
    im=Image.open(src).convert('RGB')
    if box: im=im.crop(box)
    im.save(dst.replace('_cut.png','.jpg'),quality=92)
    o=remove(im,session=s,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
    o.save(dst)
cut('photos/pop.jpg',None,'photos/pop_cut.png')
# Barr: ficha de prensa completa (el recorte quedaba blando)
# Duncan: sin recorte (ficha de prensa); recorte 0,380–1080,1483 en photos/duncan_crop.jpg
