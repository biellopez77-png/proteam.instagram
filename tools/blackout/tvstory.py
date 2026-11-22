"""Stories de cuenta atrás en la tele (CH 15 → CH 00)."""
import io, sys
from PIL import Image
from playwright.sync_api import sync_playwright
from photo import serve
from tvreel import tv_frame
FR = {15: ['TU EQUIPO', 'SIGUE EN 1998.'], 14: ['¿QUÉ SISTEMA', 'ESTÁS USANDO?'], 13: ['47 AUDIOS NO SON', 'UNA CONVOCATORIA.'], 12: ['¿ANALIZAS', 'COMO EN 1995?'],
      11: ['YOUR FUTURE', 'IS CALLING.'], 10: ['DEJA DE ENTRENAR', 'COMO EN LOS 90.'], 9: ['¿ESTÁS', 'ACTUALIZADO?'], 8: ['SIN TARJETA.', 'SIN LETRA PEQUEÑA.'],
      7: ['«LO TENGO EN', 'LA LIBRETA.»'], 6: ['¡Y NO SOLO', 'ESO!'], 5: ['CARGANDO', 'TEMPORADA 26/27'], 4: ['6 MESES.', 'UNA TEMPORADA.'],
      3: ['REBOBINA.', 'O AVANZA.'], 2: ['¡ÚLTIMAS', 'UNIDADES!'], 1: ['MAÑANA SE', 'CORTA LA SEÑAL.'], 0: ['HOY SE', 'CORTA LA SEÑAL.']}
port = serve()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 900})
    pg.goto(f'http://127.0.0.1:{port}/tools/blackout/pantalla.html'); pg.wait_for_function('window.READY===true')
    for d, (l1, l2) in FR.items():
        sz = 132 if max(len(l1), len(l2)) <= 13 else 104
        top = 'ÚLTIMO DÍA · HASTA LAS 23:59' if d == 0 else ('QUEDA 1 DÍA' if d == 1 else f'QUEDAN {d} DÍAS')
        spec = {'ch': f'CH {d:02d}', 'frames': [{'t0': 0, 'bg': 'red' if d == 0 else 'blue', 'mode': 'REC ●' if d <= 1 else 'PLAY ▶', 'lines': [
            {'text': top, 'font': 'VT', 'size': 60, 'y': 150, 'at': 0, 'cps': 999},
            {'text': l1, 'size': sz, 'y': 270, 'at': 0, 'cps': 999}, {'text': l2, 'size': sz, 'y': 270 + sz + 20, 'at': 0, 'cps': 999},
            {'text': '6 MESES GRATIS · PRIMER EQUIPO', 'font': 'VT', 'size': 58, 'y': 690, 'at': 0, 'cps': 999},
            {'text': 'PRO-TEAM.APP', 'font': 'VT', 'size': 70, 'y': 770, 'at': 0, 'cps': 999, 'cursor': True}]}]}
        pg.evaluate('([s, t]) => window.screen(s, t)', [spec, 5.0])
        scr = Image.open(io.BytesIO(pg.screenshot())).convert('RGB')
        Image.fromarray((tv_frame(scr, 1.0, d) * 255).astype('uint8')).save(f'out/retro/tvstory-{d:02d}.jpg', quality=92)
    b.close()
print('ok')
