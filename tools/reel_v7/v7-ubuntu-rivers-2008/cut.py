from PIL import Image
import sys, numpy as np; sys.path.insert(0,'../bielsa'); from grade import grade
from rembg import remove, new_session
S = new_session('isnet-general-use')
def cut(src, dst, box=None):
    im = Image.open(src).convert('RGB')
    if box: im = im.crop(box)
    remove(im, session=S, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=8).save(dst)
def fadebase(p, n=160):
    im = Image.open(p); a = np.array(im); h = a.shape[0]
    a[..., 3] = (a[..., 3] * np.clip((h - np.arange(h)) / n, 0, 1)[:, None]).astype(np.uint8)
    Image.fromarray(a).save(p)
# 1 · Doc Rivers (2007): figura recortada hasta la cintura, sin el jugador de atrás
cut('photos/rivers.jpg', 'photos/rivers_cut.png', (100, 100, 900, 1250))
# 2 · Desmond Tutu: retrato en marco (solapa del libro), sin recortar el fondo
Image.open('photos/tutu.jpg').convert('RGB').crop((0, 60, 1067, 1400)).save('photos/tutu_crop.jpg', quality=92)
# 3 · Paul Pierce con el trofeo (desfile, 19/6/2008)
cut('photos/pierce.jpg', 'photos/pierce_cut.png', (0, 40, 1067, 1250))
# 4 · plantilla campeona en la Casa Blanca: solo jugadores y cuerpo técnico, sin el presidente ni el atril
Image.open('photos/group.jpg').convert('RGB').crop((150, 0, 1010, 700)).save('photos/group_crop.jpg', quality=92)
grade('photos/rivers_cut.png', 'img/rivers_g.png'); fadebase('img/rivers_g.png')
grade('photos/tutu_crop.jpg', 'img/tutu_g.jpg', keep_blue=False)
grade('photos/pierce_cut.png', 'img/pierce_g.png'); fadebase('img/pierce_g.png', 200)
grade('photos/group_crop.jpg', 'img/group_g.jpg')
for n in ['rivers', 'pierce']:
    im = Image.open(f'img/{n}_g.png'); im.thumbnail((900, 900)); im.save(f'img/{n}_g.png', optimize=True)
# Rivers: el azul solo en la corbata y la camisa (el resto del traje, en B/N, para que no salgan motas azules en la raya diplomática)
import cv2
grade('photos/rivers_cut.png', 'photos/rivers_bw.png', keep_blue=False); grade('photos/rivers_cut.png', 'photos/rivers_bl.png')
bw = cv2.imread('photos/rivers_bw.png', cv2.IMREAD_UNCHANGED).astype(np.float32); bl = cv2.imread('photos/rivers_bl.png', cv2.IMREAD_UNCHANGED).astype(np.float32)
m = np.zeros(bw.shape[:2], np.float32); m[380:1010, 480:625] = 1; m = cv2.GaussianBlur(m, (0, 0), 8)[..., None]
out = bw * (1 - m) + bl * m; cv2.imwrite('img/rivers_g.png', out.astype(np.uint8)); fadebase('img/rivers_g.png')
im = Image.open('img/rivers_g.png'); im.thumbnail((900, 900)); im.save('img/rivers_g.png', optimize=True)
