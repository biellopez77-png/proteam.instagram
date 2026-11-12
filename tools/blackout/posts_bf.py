"""Posts 4:5 de Black Friday con la misma identidad: tele a pantalla completa o móvil 3D sobre negro."""
import json
from PIL import Image
from playwright.sync_api import sync_playwright
from photo import serve
import brand
G = '0 0 10px rgba(61,255,168,.7)'
def crt_spec(dev, ch, mode, lines, small=True):
    L = [{'text': t, 'font': f, 'size': s, 'color': c, 'glow': G if c else None, 'at': 0, 'cps': 999} for (t, f, s, c) in lines]
    for l in L:
        if not l['color']: del l['color'], l['glow']
    return {'w': 1080, 'h': 1350, 'd': '0', 'dur': 10, 'cut': 99, 'dev': [[0, dev]], 'layers': [
        {'t0': 0, 't1': 99, 'type': 'osd', 'ch': ch, 'mode': mode}, {'t0': 0, 't1': 99, 'type': 'text', 'valign': 'flex-start', 'pad': '265px 90px', 'gap': 14, 'lines': L}], 'app': []}
P = {
 1: crt_spec('tv', 'CH 14', 'PLAY ▶', [('QUEDAN 14 DÍAS', 'VT', 62, '#3dffa8'), (' ', 'IT', 30, None), ('¿QUÉ SISTEMA', 'IT', 100, None), ('ESTÁS USANDO?', 'IT', 100, None), (' ', 'IT', 40, None),
      ('LIBRETA 1.0 · EXCEL 97 · VHS', 'VT', 58, None), (' ', 'IT', 30, None), ('6 MESES GRATIS PARA TU PRIMER EQUIPO', 'VT', 52, '#3dffa8'), ('PRO-TEAM.APP', 'VT', 64, None)]),
 3: crt_spec('tv', 'CH 04', 'PLAY ▶', [('QUEDAN 4 DÍAS', 'VT', 62, '#3dffa8'), (' ', 'IT', 30, None), ('6 MESES.', 'IT', 124, None), ('UNA', 'IT', 124, None), ('TEMPORADA.', 'IT', 124, None), (' ', 'IT', 20, None),
      ('GRATIS PARA TU PRIMER EQUIPO', 'VT', 56, '#3dffa8'), ('HASTA EL 27 · PRO-TEAM.APP', 'VT', 62, None)]),
 4: crt_spec('tvred', 'CH 00', 'REC ●', [('ÚLTIMO DÍA · HASTA LAS 23:59', 'VT', 62, '#3dffa8'), (' ', 'IT', 30, None), ('HOY SE', 'IT', 128, None), ('CORTA LA', 'IT', 128, None), ('SEÑAL.', 'IT', 128, None), (' ', 'IT', 20, None),
      ('6 MESES GRATIS · PRIMER EQUIPO', 'VT', 56, '#3dffa8'), ('PRO-TEAM.APP', 'VT', 64, None)]),
}
port = serve()
with sync_playwright() as p:
    for k, sp in P.items():
        b, pgs = brand.pages(p, port, sp)
        Image.fromarray(brand.frame(pgs, sp, 5.0, 1)).save(f'out/retro/postbf-{k}.jpg', quality=93); b.close()
    # post 2: móvil 3D sobre negro
    sp = {'w': 1080, 'h': 1350, 'd': '9', 'dur': 30, 'cut': 0, 'trans': 1.0, 'dev': [[0, 'tv']], 'layers': [], 'pose': {'ry0': -.3, 'y': -.012, 'far': .43},
          'app': [[0, 'res-0', .12, .12]], 'words': [[0, 99, '<div class="a" style="left:0;right:0;top:70px;text-align:center;font-family:IT;font-weight:900;font-size:96px;letter-spacing:-.04em;color:#fff">¿Estás actualizado?</div>'
          '<div class="a" style="left:0;right:0;top:1262px;text-align:center;font-family:VT;font-size:50px;letter-spacing:.06em;color:#3dffa8">6 MESES GRATIS · HASTA EL 27</div>']]}
    b, pgs = brand.pages(p, port, sp)
    Image.fromarray(brand.frame(pgs, sp, 6.0, 1)).save('out/retro/postbf-2.jpg', quality=93); b.close()
print('ok')
