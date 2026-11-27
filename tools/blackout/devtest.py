import sys, os
from playwright.sync_api import sync_playwright
from photo import serve, FLAGS
port = serve(); OUT = sys.argv[1]
shots = [('phone', 0, '/tools/app/reg-1.jpg'), ('phone', 9, '/tools/app/res-0.jpg'), ('laptop', 3, '/tools/app/landing-bf.jpg'), ('both', 2, None)]
with sync_playwright() as p:
    b = p.chromium.launch(args=FLAGS); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto(f'http://127.0.0.1:{port}/tools/blackout/devices.html?w=1080&h=1920'); pg.wait_for_function('window.ready')
    pg.evaluate("Promise.all([setScreen('phone','/tools/app/reg-1.jpg'), setScreen('laptop','/tools/app/landing-bf.jpg')])")
    for i, (m, t, img) in enumerate(shots):
        if img: pg.evaluate(f"setScreen('{'laptop' if m=='laptop' else 'phone'}','{img}')")
        pg.evaluate(f"pose({{mode:'{m}', t:{t}}})")
        pg.locator('canvas').screenshot(path=f'{OUT}/dev{i}.png')
    b.close()
