"""Wikimedia Commons desde el sandbox de Higgsfield (el contenedor de los turnos no llega a Commons; el sandbox sí).

Uso, SIEMPRE dentro de mcp__Higgsfield__sandbox_exec:
  curl -s https://raw.githubusercontent.com/biellopez77-png/proteam.instagram/main/tools/commons_sandbox.py -o cs.py
  python3 cs.py search "handball Spain national team" [n]   -> candidatas: título, tamaño, licencia, autor
  python3 cs.py get "File:Nombre.jpg" NOMBRE_PROTEAM          -> bank/NOMBRE_PROTEAM.jpg (1080 px de ancho, <=250 KB) + .json con licencia
Después, en una llamada en primer plano: sandbox_exec con image_paths ["bank/NOMBRE.jpg"] (máx. 512 KB en total por llamada,
2 fotos). La imagen vuelve como archivo a ~/.claude/projects/*/tool-results/mcp-Higgsfield-*: cópiala a banco/fotos/NOMBRE.jpg y
apunta la fila del inventario con los datos del .json (imprímelo con `cat bank/NOMBRE.json`).
Solo licencias libres (CC BY, CC BY-SA, CC0, dominio público). Una petición cada pocos segundos.
"""
import json, sys, time, urllib.parse, urllib.request, re, os, subprocess
UA = {'User-Agent': 'ProTeamBank/1.0 (https://github.com/biellopez77-png/proteam.instagram)'}
API = 'https://commons.wikimedia.org/w/api.php?'
OK = re.compile(r'^(cc[- ]by|cc[- ]by[- ]sa|cc0|public domain|pd)', re.I)


def api(**p):
    p['format'] = 'json'; time.sleep(1.5)
    return json.load(urllib.request.urlopen(urllib.request.Request(API + urllib.parse.urlencode(p), headers=UA), timeout=40))


def clean(h): return re.sub('<[^>]+>', '', h or '').strip()


def info(titles):
    r = api(action='query', titles='|'.join(titles), prop='imageinfo', iiprop='url|size|extmetadata', iiurlwidth=1080)
    out = []
    for p in r.get('query', {}).get('pages', {}).values():
        if 'imageinfo' not in p: continue
        ii = p['imageinfo'][0]; m = ii.get('extmetadata', {})
        g = lambda k: clean(m.get(k, {}).get('value', ''))
        out.append({'title': p['title'], 'w': ii['width'], 'h': ii['height'], 'license': g('LicenseShortName'), 'author': g('Artist'),
                    'date': g('DateTimeOriginal'), 'desc': g('ImageDescription')[:200], 'page': ii['descriptionurl'], 'thumb': ii.get('thumburl') or ii['url'],
                    'free': bool(OK.match(g('LicenseShortName')))})
    return out


c = sys.argv[1]
if c == 'search':
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    r = api(action='query', list='search', srnamespace=6, srsearch=sys.argv[2] + ' filetype:bitmap', srlimit=n)
    t = [x['title'] for x in r['query']['search']]
    for x in info(t) if t else []:
        if x['w'] >= 1000: print(json.dumps({k: x[k] for k in ('title', 'w', 'h', 'license', 'free', 'author', 'date', 'desc')}, ensure_ascii=False))
elif c == 'get':
    x = info([sys.argv[2]])[0]
    if not x['free']: sys.exit('licencia no libre: ' + x['license'])
    os.makedirs('bank', exist_ok=True); raw = 'bank/_raw'; out = 'bank/%s.jpg' % sys.argv[3]
    time.sleep(1.5); open(raw, 'wb').write(urllib.request.urlopen(urllib.request.Request(x['thumb'], headers=UA), timeout=60).read())
    for q in (85, 78, 70, 62):
        subprocess.run(['convert', raw, '-auto-orient', '-resize', '1080x>', '-strip', '-quality', str(q), out], check=True)
        if os.path.getsize(out) <= 250_000: break
    x['file'] = sys.argv[3] + '.jpg'; x['bytes'] = os.path.getsize(out)
    json.dump(x, open('bank/%s.json' % sys.argv[3], 'w'), ensure_ascii=False); print(json.dumps(x, ensure_ascii=False))
