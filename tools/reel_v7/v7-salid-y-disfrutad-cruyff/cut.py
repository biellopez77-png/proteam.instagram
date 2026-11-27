from PIL import Image
import sys, numpy as np; sys.path.insert(0, '../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
def fadebase(p, n=160):
    im = Image.open(p); a = np.array(im); h = a.shape[0]
    a[..., 3] = (a[..., 3] * np.clip((h - np.arange(h)) / n, 0, 1)[:, None]).astype(np.uint8)
    Image.fromarray(a).save(p)
# 1 · Wembley por dentro (1956): polaroid, sin cielo de más
Image.open('photos/wembley.jpg').convert('RGB').crop((0, 120, 640, 463)).save('photos/wembley_crop.jpg', quality=95)
grade('photos/wembley_crop.jpg', 'img/wembley_g.jpg', keep_blue=False)
# 2 · Johan Cruyff (1994), en bici tras un entreno: en marco, sin recorte
Image.open('photos/cruyff.jpg').convert('RGB').crop((500, 130, 1330, 1020)).save('photos/cruyff_crop.jpg', quality=92)
grade('photos/cruyff_crop.jpg', 'img/cruyff_g.jpg', keep_blue=False)
# 3 · Ronald Koeman (1988, selección neerlandesa en Zeist): el recorte con rembg salía sucio (pelo y camisetas vecinas) → en marco, solo cara y cuello, sin escudo ni patrocinador
Image.open('photos/koeman.jpg').convert('RGB').crop((312, 70, 585, 478)).save('photos/koeman_crop.jpg', quality=95)
grade('photos/koeman_crop.jpg', 'img/koeman_g.jpg', keep_blue=False)
