"""Fotos de v7-cena-popovich-2013 (Marta A, 28/11). python3 cut.py
Bajadas en el sandbox de Higgsfield (Commons, Special:FilePath) y traídas por image_paths:
- raw1.jpg  Gregg Popovich sideline.jpg (Mike, CC BY-SA 2.0), 896×1100
- raw2.jpg  San Antonio Spurs Coaching staff.JPG (Zereshk, CC BY-SA 3.0), 1200×900
- raw3.jpg  ... White House January 2015 P011215ps-0517.jpg (foto oficial de la Casa Blanca, dominio público), 1100×733
- raw4.jpg  Popovich cross armed.JPG (Zereshk, CC BY-SA 3.0), 1000×914
p1_cut.png y p4_cut.png: rembg isnet-general-use con alpha matting (240/10/10)."""
from PIL import Image
import numpy as np, sys; sys.path.insert(0,'../bielsa'); from grade import grade
def hard(im, lo=110):
    a=np.array(im); a[...,3]=np.where(a[...,3]<lo,0,np.minimum(255,a[...,3].astype(int)*1.3)).astype(np.uint8); return Image.fromarray(a)
# 1 · Popovich en la banda: de la cabeza a las rodillas (fuera el rótulo del suelo)
hard(Image.open('photos/p1_cut.png').crop((270,60,640,780))).save('photos/p1c.png'); grade('photos/p1c.png','img/p1_g.png')
# 4 · Popovich de brazos cruzados: de la cabeza a la cintura, sin la mano del espectador de detrás
im=hard(Image.open('photos/p4_cut.png').crop((270,80,560,640))); a=np.array(im); a[:250,262:,3]=0; Image.fromarray(a).save('photos/p4c.png'); grade('photos/p4c.png','img/p4_g.png')
im=Image.open('photos/p4c.png'); a=np.array(im); a[330:440,222:,3]=0; Image.fromarray(a).save('photos/p4c.png'); grade('photos/p4c.png','img/p4_g.png')   # fuera la mano de debajo del codo
# 2 · cuerpo técnico en el banquillo (2010): entera en la ficha, encuadrada en el banquillo
Image.open('photos/raw2.jpg').convert('RGB').crop((0,150,1100,830)).save('photos/p2.jpg',quality=92); grade('photos/p2.jpg','img/p2_g.jpg',keep_blue=False)
# 3 · campeones de 2014 en la Casa Blanca: solo Popovich y los jugadores (fuera el presidente, el atril con el sello y el público)
Image.open('photos/raw3.jpg').convert('RGB').crop((395,195,1000,425)).save('photos/p3.jpg',quality=92); grade('photos/p3.jpg','img/p3_g.jpg',keep_blue=False)
