"""Filas de la pestaña Plan del panel a partir de queue.json (publicadas + programadas; sin canceladas).
  python3 tools/plan_sheet.py old.json > rows.json   (old.json = respuesta de get_values de Plan, para conservar piezas y predicciones)"""
import json, re, sys, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
q = json.load(open(os.path.join(R, 'queue.json')))
old = json.load(open(sys.argv[1]))['values']; H = old[0]
prev = {}
for r in old[1:]:
    d = dict(zip(H, r + [''] * (len(H) - len(r)))); prev[d['id'].lstrip('0')] = d
TIPO = {'reel': 'Reel', 'story': 'Story', 'carousel': 'Carrusel', 'image': 'Imagen'}
EST = {'published': 'Publicado', 'pending': 'Programado', 'borrador': 'Programado', 'failed': 'Fallido'}
def first(c): return re.sub(r'[^\w¿?¡!.,:;«»()%\-–·\' ]+$', '', (c or '').split('\n')[0]).strip()
out = [H]
for i in sorted(q, key=lambda x: x['when']):
    if i['status'] == 'cancelled' or i['id'] in ('t01', 't01s'): continue
    p = prev.get(i['id'].lstrip('0'), {})
    fecha, hora = i['when'][:10], i['when'][11:16]
    bf = i.get('campana') == 'blackout'
    pilar = p.get('pilar') or ('Black Friday' if i['when'] < '2026-11-28' else 'Marca') if bf else p.get('pilar', 'Fidelizar')
    if bf and not p: pilar = 'Black Friday' if i['when'] < '2026-11-28' else 'Marca'
    if i.get('campana') == 'focos': pilar = 'Black Friday'
    if p and i['status'] == 'published': pieza = p['pieza']
    elif i['kind'] == 'story':
        m = re.search(r'bf-ch-(\d+)', i['files'][0]); pieza = f'Story: canal CH {m.group(1)} (cuenta atrás)' if m else 'Story'
        if i.get('campana') == 'focos': pieza = 'Story · ' + {'k03': 'Se encienden los focos', 'k07': 'Crea tu cuenta. Sal al campo.'}.get(i['id'], 'Lista de espera')
    elif i['id'] == 'bf01': pieza = 'Lanzamiento Black Friday: actualización disponible (CH 15)'
    else:
        tag = {'br': 'R', 'bv': 'Vídeo de marca V', 'bp': 'P'}.get(i['id'][:2], '')
        if i.get('campana') == 'focos' and i['kind'] == 'story': pieza = 'Story · ' + {'k03': 'Se encienden los focos', 'k07': 'Crea tu cuenta. Sal al campo.'}.get(i['id'], 'Lista de espera')
        if not (i.get('campana') == 'focos' and i['kind'] == 'story'): pieza = (tag + i['id'][2:] + ' · ' if tag else '') + first(i.get('caption'))
    if i['status'] == 'borrador' and i.get('campana') == 'focos': pieza += ' (borrador: falta tu visto bueno)'
    out.append([i['id'], fecha, hora, TIPO[i['kind']], pieza, pilar, EST[i['status']], str(i.get('media_id', '')),
                p.get('pred_min', ''), p.get('pred', ''), p.get('pred_max', ''), i['files'][0]])
print(json.dumps(out, ensure_ascii=False))
