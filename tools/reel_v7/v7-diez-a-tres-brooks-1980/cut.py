from PIL import Image
import sys, numpy as np, cv2; sys.path.insert(0,'../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
def fadebase(p, n=160):
    im = Image.open(p); a = np.array(im); h = a.shape[0]
    a[..., 3] = (a[..., 3] * np.clip((h - np.arange(h)) / n, 0, 1)[:, None]).astype(np.uint8)
    Image.fromarray(a).save(p)
# 1 · Herb Brooks (1983): solo cabeza y hombros, por encima del escudo de la chaqueta (sin logotipos)
im = Image.open('photos/brooks.jpg').convert('RGB').crop((40, 0, 693, 425))
remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save('photos/brooks_cut.png')
grade('photos/brooks_cut.png', 'img/brooks_g.png', keep_blue=False); fadebase('img/brooks_g.png', 120)
# 2 · pabellón de Lake Placid (actual): difuminados los anuncios y los aros de las vallas
a = cv2.imread('photos/arena.jpg')
for (x0, y0, x1, y1) in [(310, 622, 470, 668), (1150, 620, 1320, 676), (660, 335, 960, 368)]:
    a[y0:y1, x0:x1] = cv2.GaussianBlur(a[y0:y1, x0:x1], (0, 0), 9)
cv2.imwrite('photos/arena_clean.jpg', a[60:1000, 0:1600])
grade('photos/arena_clean.jpg', 'img/arena_g.jpg', keep_blue=False)
# 3 · USA–URSS, 22/2/1980 (Mike Ramsey con el disco)
Image.open('photos/match.jpg').convert('RGB').crop((0, 270, 1600, 1000)).save('photos/match_crop.jpg', quality=92)
grade('photos/match_crop.jpg', 'img/match_g.jpg', keep_blue=False)
# 4 · Jim Craig con la bandera (24/2/1980, tras el oro): en marco, sin recorte
Image.open('photos/craig.jpg').convert('RGB').crop((0, 0, 769, 1500)).save('photos/craig_crop.jpg', quality=92)
grade('photos/craig_crop.jpg', 'img/craig_g.jpg', keep_blue=False)
for n in ['arena_g.jpg', 'match_g.jpg', 'craig_g.jpg']:
    im = Image.open('img/' + n); im.thumbnail((1200, 1200)); im.save('img/' + n, quality=88)
