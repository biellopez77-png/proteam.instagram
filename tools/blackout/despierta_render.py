import sys, os, subprocess, shutil, json, numpy as np, wave
from playwright.sync_api import sync_playwright
from photo import serve
W, H, FX, OUT = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
DUR, FPS = 20.5, 25; port = serve(); D = OUT + '_f'; os.makedirs(D, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
    pg.goto(f'http://127.0.0.1:{port}/tools/blackout/despierta.html?w={W}&h={H}&fx={FX}'); pg.wait_for_function('window.ready')
    chars = pg.evaluate('window.chars')
    for i in range(int(DUR * FPS)):
        pg.evaluate(f'frame({i / FPS})'); pg.screenshot(path=f'{D}/{i:05d}.png')
    b.close()
# sonido: teclas (ruido corto filtrado), zumbido de monitor y corte de señal
SR = 48000; a = np.zeros(int(SR * DUR)); rng = np.random.default_rng(3)
t = np.arange(int(SR * DUR)) / SR; a += .012 * np.sin(2 * np.pi * 50 * t) + .006 * np.sin(2 * np.pi * 15734 * t)
for c in chars:
    n = int(SR * .028); s = int(c * SR); env = np.exp(-np.linspace(0, 9, n)); click = rng.normal(0, 1, n) * env
    click = np.convolve(click, np.ones(4) / 4, 'same') * (.22 + rng.random() * .12); a[s:s + n] += click[:len(a) - s]
s0, s1 = int(18.6 * SR), int(19.6 * SR); a[s0:s1] += rng.normal(0, .18, s1 - s0) * np.linspace(.3, 1, s1 - s0)
a[s1:] *= 0; a = np.clip(a, -1, 1)
wav = OUT + '.wav'
with wave.open(wav, 'w') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((a * 32767).astype(np.int16).tobytes())
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', f'{D}/%05d.png', '-i', wav, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', OUT], check=True)
shutil.rmtree(D); os.remove(wav); print('ok', OUT)
