# Clip de prueba: móvil girando despacio (6 s) + portátil (4 s), 25 fps
import sys, subprocess, os
from playwright.sync_api import sync_playwright
from photo import serve, FLAGS
port = serve(); OUT = sys.argv[1]; D = OUT + '_f'; os.makedirs(D, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(args=FLAGS); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto(f'http://127.0.0.1:{port}/tools/blackout/devices.html?w=1080&h=1920'); pg.wait_for_function('window.ready')
    pg.evaluate("Promise.all([setScreen('phone','/tools/app/reg-1.jpg'), setScreen('laptop','/tools/app/landing-bf.jpg')])")
    n = 0
    for i in range(150):
        t = i / 25; pg.evaluate(f"pose({{mode:'phone', t:{t+4}, spin:.35, amp:.3, dist:{.6 - .08 * t / 6}}})"); pg.locator('canvas').screenshot(path=f'{D}/{n:04d}.png'); n += 1
    for i in range(100):
        t = i / 25; pg.evaluate(f"pose({{mode:'laptop', t:{t}, spin:.3, amp:.25, dist:{1.1 - .1 * t / 4}}})"); pg.locator('canvas').screenshot(path=f'{D}/{n:04d}.png'); n += 1
    b.close()
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '25', '-i', f'{D}/%04d.png', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', OUT], check=True)
