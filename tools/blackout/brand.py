"""Reels y vídeo horizontal de Black Friday: tele de tubo a pantalla completa (lo viejo) → móvil 3D girando despacio (ProTeam).
  python3 brand.py still spec.json t1 t2 ... prefijo
  python3 brand.py video spec.json out.mp4
spec: w,h,dur,d · dev/layers (pantalla vieja, screen.html) · cut (cambio) · trans (lo que tarda en alejarse) ·
      app: [[t, captura, scroll0, scroll1]] (tiempos absolutos) · words: [[t0, t1, html]] (pocas palabras, fuera del móvil) ·
      pose: {ry0, x, y, far} · audio, lineas (como screenreel)"""
import sys, io, json, subprocess, numpy as np, cv2
from PIL import Image
from playwright.sync_api import sync_playwright
from photo import serve
from crt import crt
from screenreel import audio
FPS = 30
APP = {}
def app_img(name):
    if name not in APP: APP[name] = np.asarray(Image.open(f'../app/{name}.jpg').convert('RGB')).astype(np.float32) / 255
    return APP[name]
ez = lambda x: 0 if x <= 0 else 1 if x >= 1 else x * x * (3 - 2 * x)

def old_frame(pgs, spec, t, i):
    r = pgs['old'].evaluate('([s, t]) => window.frame(s, t)', [spec, t])
    img = Image.open(io.BytesIO(pgs['old'].screenshot())).convert('RGB')
    if r['crt'] > .01: img = crt(img, r['crt'], t, i, curve=r['curve'] / max(r['crt'], 1e-3))
    return np.asarray(img).astype(np.float32) / 255

def app_content(spec, t, cw, ch):
    """Capturas de la app, una tras otra con un deslizamiento suave y un scroll lento."""
    A = spec['app']; k = 0
    for j, x in enumerate(A):
        if t >= x[0]: k = j
    def one(j):
        t0, name, s0, s1 = A[j]; t1 = A[j + 1][0] if j + 1 < len(A) else spec['dur']
        im = app_img(name); ih = int(im.shape[1] * ch / cw); sc = s0 + (s1 - s0) * ez((t - t0) / max(.1, t1 - t0))
        y0 = int((im.shape[0] - ih) * min(1, max(0, sc))); return cv2.resize(im[y0:y0 + ih], (cw, ch), interpolation=cv2.INTER_AREA)
    cur = one(k)
    if k > 0:
        p = ez((t - A[k][0]) / .6)
        if p < 1:
            prev = one(k - 1); off = int(cw * p)
            out = np.zeros_like(cur); out[:, :cw - off] = prev[:, off:] * (1 - .4 * p); out[:, cw - off:] = cur[:, :off]; return out
    return cur

def frame(pgs, spec, t, i):
    W, H = spec['w'], spec['h']; cut = spec['cut']
    if t < cut: return (old_frame(pgs, spec, t, i) * 255).astype(np.uint8)
    u = (t - cut) / spec.get('trans', 1.8); P = spec.get('pose', {})
    words = ''.join(h for a, b, h in spec.get('words', []) if a <= t < b)
    r = pgs['ph'].evaluate('(o) => window.pose(o)', {'u': u, 't': t - cut, 'html': words, **P})
    base = np.asarray(Image.open(io.BytesIO(pgs['ph'].screenshot())).convert('RGB')).astype(np.float32) / 255
    cw, ch = 900, 1940  # textura de pantalla (proporción del móvil)
    content = app_content(spec, t, cw, ch)
    k = ez(u / .55)  # lo viejo se funde en la app mientras la cámara se aleja
    if k < 1:
        old = cv2.resize(old_frame(pgs, spec, min(t, cut + .6), i), (cw, ch), interpolation=cv2.INTER_AREA)
        content = old * (1 - k) + content * k
    # reflejo del cristal que se mueve con el giro
    yy, xx = np.mgrid[0:ch, 0:cw].astype(np.float32); ph = (t - cut) * .15
    refl = np.clip(1 - np.abs((xx / cw * .7 + yy / ch * .5) - (.35 + .25 * np.sin(ph))) / .12, 0, 1)[..., None] * .07
    content = np.clip(content * .97 + refl, 0, 1)
    src = np.float32([[0, 0], [cw, 0], [cw, ch], [0, ch]]); dst = np.float32(r['quad'])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(content, M, (W, H), flags=cv2.INTER_LINEAR)
    mask = np.zeros((H, W), np.uint8); cv2.fillPoly(mask, [np.int32(np.round(r['outline']))], 255, lineType=cv2.LINE_AA)
    m = cv2.GaussianBlur(mask.astype(np.float32) / 255, (0, 0), .8)[..., None]
    out = base * (1 - m) + warped * m
    return (np.clip(out, 0, 1) * 255).astype(np.uint8)

def pages(p, port, spec):
    from photo import FLAGS
    b = p.chromium.launch(args=FLAGS); W, H = spec['w'], spec['h']
    old = b.new_page(viewport={'width': W, 'height': H}); old.goto(f'http://127.0.0.1:{port}/tools/blackout/screen.html'); old.wait_for_function('window.READY===true', timeout=60000)
    ph = b.new_page(viewport={'width': W, 'height': H}); ph.goto(f'http://127.0.0.1:{port}/tools/blackout/phone3d.html?w={W}&h={H}'); ph.wait_for_function('window.READY===true', timeout=120000)
    for pg in (old, ph): pg.on('pageerror', lambda e: print('ERR', e))
    return b, {'old': old, 'ph': ph}

if __name__ == '__main__':
    c = sys.argv[1]; spec = json.load(open(sys.argv[2])); port = serve()
    with sync_playwright() as p:
        b, pgs = pages(p, port, spec)
        if c == 'still':
            *ts, pre = sys.argv[3:]
            for t in ts: Image.fromarray(frame(pgs, spec, float(t), 0)).save(f'{pre}-{t}.jpg', quality=88)
        else:
            out = sys.argv[3]; wav = out.replace('.mp4', '.wav'); audio(spec, wav); N = int(spec['dur'] * FPS); W, H = spec['w'], spec['h']
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', wav,
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '22', '-maxrate', '9M', '-bufsize', '18M', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
            for i in range(N):
                ff.stdin.write(frame(pgs, spec, i / FPS, i).tobytes())
                if i % 90 == 0: print(f'{i}/{N}', flush=True)
            ff.stdin.close(); ff.wait(); print('ok', out)
        b.close()
