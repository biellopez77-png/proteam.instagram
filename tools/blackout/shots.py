from playwright.sync_api import sync_playwright
import pathlib
P = pathlib.Path(__file__).resolve().parent
S = {1: (1080, 1920), 2: (1080, 1350), 3: (1080, 1920), 4: (1080, 1350), 5: (1440, 900)}
N = {1: 'reel-portada-15', 2: 'post-silbato', 3: 'reel-excel', 4: 'post-ultimo-dia', 5: 'landing'}
with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    for k, (w, h) in S.items():
        pg = b.new_page(viewport={'width': w, 'height': h})
        pg.goto(f'file://{P}/maquetas.html?p={k}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(400)
        pg.locator(f'#p{k}').screenshot(path=str(P / 'out' / f'{k}-{N[k]}.png'))
    b.close()
