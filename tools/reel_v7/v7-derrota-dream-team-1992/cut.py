# Fotos de v7-derrota-dream-team-1992: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
# Las raw*.jpg vienen de Commons (Special:FilePath, ~1600 px) descargadas en el sandbox de Higgsfield.
# p2_cut.png, p3_cut.png y p4_cut.png se sacaron de raw2-4 con:
#   remove(im,session=new_session('isnet-general-use'),alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
from PIL import Image
import numpy as np, sys; sys.path.insert(0,'../bielsa'); from grade import grade
def hard(path, lo=120):
    a=np.array(Image.open(path)); a[...,3]=np.where(a[...,3]<lo,0,np.minimum(255,a[...,3].astype(int)*1.3)).astype(np.uint8); Image.fromarray(a).save(path)
# 1 · Dream Team en Barcelona 1992 (Ken Hackman, USAF, dominio público): fuera la franja de arriba con los aros y el rótulo de los Juegos
Image.open('photos/raw1.jpg').convert('RGB').crop((0,360,1044,1600)).save('photos/p1.jpg',quality=92)
grade('photos/p1.jpg','img/p1_g.jpg')
# 2 · Chuck Daly, 2006 (Chad J. McNeeley, US Navy, dominio público): fondo liso, va entera en la ficha (el recorte dejaba la chaqueta a medias)
Image.open('photos/raw2.jpg').convert('RGB').crop((40,0,425,560)).save('photos/p2.jpg',quality=95)
grade('photos/p2.jpg','img/p2_g.jpg',keep_blue=False)
# 3 · Krzyzewski, 2006 (DoD / William D. Moss, dominio público): recortado; fuera el atril con el sello y el fondo con logotipos
im=Image.open('photos/p3_cut.png').crop((380,0,1291,820)); im.save('photos/p3_cutc.png'); hard('photos/p3_cutc.png')
grade('photos/p3_cutc.png','img/p3_cut_g.png')
# 4 · Grant Hill, 2007 (Keith Allison, CC BY-SA 2.0): recortado, B/N (obra derivada, misma licencia)
hard('photos/p4_cut.png'); grade('photos/p4_cut.png','img/p4_cut_g.png',keep_blue=False)
