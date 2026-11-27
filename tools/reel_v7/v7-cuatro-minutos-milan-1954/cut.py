# Fotos de v7-cuatro-minutos-milan-1954: rembg (isnet-general-use, alpha matting) y gradación (tools/reel_v7/bielsa/grade.py)
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
S=new_session('isnet-general-use')
cut=lambda im: remove(im,session=S,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=10)
# 1 · Milan (Indiana), 01/05/2016, Chris Flook (CC BY-SA 4.0): ficha de prensa «HOY», encuadre sobre la puerta del museo
Image.open('photos/raw1.jpg').convert('RGB').crop((300,0,1200,940)).save('photos/p1.jpg',quality=92)
# 2 · Bobby Plump, c. 1958, Phillips 66 (dominio público): recortado con rembg
cut(Image.open('photos/raw2.jpg').convert('RGB')).save('photos/p2_cut.png')
# 4 · postal del equipo de Milan, campeón de 1954 (Steve Shook / Groganphoto, CC BY 2.0): en marco
Image.open('photos/raw4.jpg').convert('RGB').save('photos/p4.jpg',quality=92)
for k in (1,4): grade(f'photos/p{k}.jpg',f'img/p{k}_g.jpg')
grade('photos/p2_cut.png','img/p2_cut_g.png'); g=Image.open('img/p2_cut_g.png'); g=g.crop(g.getbbox()); g.save('img/p2_cut_g.png',optimize=True)
