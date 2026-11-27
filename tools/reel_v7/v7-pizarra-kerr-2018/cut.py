"""Recortes y gradación v7 · Cansados de mi voz (Kerr). Base: ../bielsa/grade.py
Kerr e Iguodala recortados con rembg (u2net_human_seg + alpha matting); Green y el corro van enmarcados (Green tiene detrás a un rival)."""
from rembg import remove, new_session
from PIL import Image
import sys; sys.path.insert(0,'../bielsa'); from grade import grade
s = new_session('u2net_human_seg')
for n in ['kerr', 'iguo']:
    im = Image.open(f'photos/{n}.jpg').convert('RGB')
    cut = remove(im, session=s, alpha_matting=True, alpha_matting_foreground_threshold=240,
                 alpha_matting_background_threshold=15, alpha_matting_erode_size=8)
    cut.save(f'photos/{n}_cut.png'); grade(f'photos/{n}_cut.png', f'img/{n}_g.png', keep_blue=True)
grade('photos/green.jpg', 'img/green_g.jpg', keep_blue=True)
grade('photos/corro.jpg', 'img/corro_g.jpg', keep_blue=True)
# Kerr: quita restos del público (se queda solo la mayor mancha del alfa)
import cv2, numpy as np
for n in ['kerr', 'iguo']:
    im = cv2.imread(f'img/{n}_g.png', cv2.IMREAD_UNCHANGED); a = im[..., 3]
    k, lab, st, _ = cv2.connectedComponentsWithStats((a > 40).astype(np.uint8))
    big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); keep = cv2.dilate((lab == big).astype(np.uint8), np.ones((9, 9), np.uint8))
    im[..., 3] = a * keep; cv2.imwrite(f'img/{n}_g.png', im)
# Kerr: corte por la cintura y fuera el aficionado de abajo a la izquierda
im = cv2.imread('img/kerr_g.png', cv2.IMREAD_UNCHANGED)[:1010]; im[850:, :135, 3] = 0; r = im[300:520, :320, :3]; im[300:520, :320, :3] = np.repeat(r.min(2, keepdims=True), 3, 2); cv2.imwrite('img/kerr_g.png', im)
