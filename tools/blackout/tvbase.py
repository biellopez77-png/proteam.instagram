"""Renderiza la tele 3D (fondo gris) con pantalla verde y negra para sacar la máscara y las esquinas de la pantalla."""
import io, json, numpy as np, cv2
from PIL import Image
from playwright.sync_api import sync_playwright
from photo import serve, FLAGS
port = serve()
with sync_playwright() as p:
    b = p.chromium.launch(args=FLAGS)
    for name in ['green', 'black']:
        pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(f'http://127.0.0.1:{port}/tools/blackout/studio.html?s=tele&w=1080&h=1920&img=/tools/blackout/out/tv/{name}.png'); pg.wait_for_function('window.READY===true', timeout=120000)
        Image.open(io.BytesIO(pg.screenshot())).convert('RGB').save(f'out/tv/tv-{name}.png')
    b.close()
g = np.asarray(Image.open('out/tv/tv-green.png')).astype(int)
m = ((g[..., 1] > 150) & (g[..., 0] < 120) & (g[..., 2] < 120)).astype(np.uint8)
cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE); c = max(cnts, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(c)
mask = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 1.2)
cv2.imwrite('out/tv/mask.png', (mask * 255).astype(np.uint8))
json.dump({'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)}, open('out/tv/screen.json', 'w')); print(x, y, w, h)
