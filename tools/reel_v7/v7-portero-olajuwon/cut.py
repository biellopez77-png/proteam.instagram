"""Recortes y gradación de las fotos de v7-portero-olajuwon (fotos del banco + ../bielsa/grade.py). Sin rembg: fotos enmarcadas."""
from PIL import Image
import sys; sys.path.insert(0, '../bielsa'); from grade import grade
C = {'guantes': ('PROTEAM_OBJETO_GUANTES_CONO_FOTO_001.jpg', (40, 60, 1160, 940)),
     'portera': ('PROTEAM_JUGADOR_PORTERA_FOTO_001.jpg', (380, 0, 1200, 800)),   # portera de espaldas, sin la atacante
     'carro': ('PROTEAM_OBJETO_BALONES_CARRO_FOTO_001.jpg', (0, 0, 1200, 800)),
     'pene': ('PROTEAM_JUGADOR_PENETRACION_FOTO_001.jpg', (180, 0, 1200, 821))}
for k, (f, box) in C.items():
    Image.open('photos/' + f).convert('RGB').crop(box).save(f'photos/{k}_crop.jpg', quality=93)
    grade(f'photos/{k}_crop.jpg', f'img/{k}_g.jpg', keep_blue=(k == 'pene'))
