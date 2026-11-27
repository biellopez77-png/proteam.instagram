"""Recortes y gradación v7 · El balón del sábado (Hogan). Base: ../bielsa/grade.py
Hogan 1908 es una postal ovalada: isnet toma el óvalo entero como objeto, así que se recorta antes el interior
(fondo de papel liso) y se usa u2net_human_seg con alpha matting; corte recto por abajo."""
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
for n in ['golden', 'wembley', 'stamp']: Image.open(f'photos/{n}.jpg').convert('RGB').save(f'photos/{n}_rgb.jpg', quality=95)
im = Image.open('photos/hogan.jpg').convert('RGB').crop((230, 170, 1000, 1330))
cut = remove(im, session=new_session(sys.argv[1] if len(sys.argv) > 1 else 'u2net_human_seg'), alpha_matting=True,
             alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=15, alpha_matting_erode_size=8)
cut.save('photos/hogan_cut.png')
grade('photos/hogan_cut.png', 'img/hogan_g.png', keep_blue=False)
grade('photos/nl1910.jpg', 'img/nl1910_g.jpg', keep_blue=False)
for n in ['golden', 'wembley', 'stamp']: grade(f'photos/{n}_rgb.jpg', f'img/{n}_g.jpg', keep_blue=False)
