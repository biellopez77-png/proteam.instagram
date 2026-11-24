"""B/N de negros profundos; solo sobrevive el azul (equipación, detalles), llevado al azul de marca. Máscara suavizada."""
import cv2, numpy as np, sys
def grade(src, dst, keep_blue=True):
    im = cv2.imread(src, cv2.IMREAD_UNCHANGED)
    a = im[..., 3] if im.shape[2] == 4 else None
    bgr = im[..., :3].astype(np.float32) / 255
    g = cv2.cvtColor((bgr*255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)/255
    g = np.clip((g - 0.06) / 0.88, 0, 1); g = g**1.18                         # negros profundos
    g = g*g*(3-2*g)*0.55 + g*0.45                                            # curva en S suave
    out = np.dstack([g, g, g])
    if keep_blue:
        hsv = cv2.cvtColor((bgr*255).astype(np.uint8), cv2.COLOR_BGR2HSV).astype(np.float32)
        h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
        m = ((h > 95) & (h < 128) & (s > 95) & (v > 45)).astype(np.float32)
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        m = cv2.GaussianBlur(m, (0, 0), 3.5)
        brand = np.array([255, 109, 99], np.float32)/255   # #636DFF en BGR
        light = np.array([255, 168, 106], np.float32)/255  # #6AA8FF
        lum = np.clip(g*1.25, 0, 1)[..., None]
        col = brand*(1-lum)*1.1 + light*lum
        col = col*(0.35+0.75*lum)
        out = out*(1-m[..., None]) + col*m[..., None]
    out = (np.clip(out, 0, 1)*255).astype(np.uint8)
    if a is not None: out = np.dstack([out, a])
    cv2.imwrite(dst, out)
if __name__ == '__main__':
    for n in ['portrait_cut', 'pose2_cut', 'full_cut', 'profile_cut', 'card', 'profile']:
        src = f'photos/{n}.png' if 'cut' in n else f'photos/{n}.jpg'
        grade(src, f'photos/{n}_g.png')
