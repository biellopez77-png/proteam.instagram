"""Ayudante de publicación (ahorra trabajo a las ejecuciones programadas).

  python3 tools/pub.py due            -> JSON con lo que toca publicar ahora (en orden) con URLs listas.
                                         Si imprime [] no hay nada que hacer.
  python3 tools/pub.py done ID MEDIA  -> marca publicada, escribe log.md
  python3 tools/pub.py fail ID "error"
  python3 tools/pub.py late           -> reprograma piezas con más de 6 h de retraso al siguiente hueco libre
  python3 tools/pub.py sheet          -> filas del Plan que deben quedar como Publicado/Fallido (id, fecha, hora, media_id)
"""
import json, sys, os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = os.path.join(R, 'queue.json')
TZ = ZoneInfo('Europe/Madrid')
CDN = 'https://cdn.jsdelivr.net/gh/biellopez77-png/proteam.instagram@main/'
RAW = 'https://raw.githubusercontent.com/biellopez77-png/proteam.instagram/main/'


def load(): return json.load(open(Q))
def save(q): json.dump(q, open(Q, 'w'), ensure_ascii=False, indent=1)
def now(): return datetime.now(TZ)
def when(i): return datetime.fromisoformat(i['when'])


def log(line):
    p = os.path.join(R, 'log.md'); s = open(p).read().split('\n')
    k = next(n for n, l in enumerate(s) if l.startswith('| ---')) + 1
    s.insert(k, line); open(p, 'w').write('\n'.join(s))


def due():
    n = now(); out = []; q = load()
    # Nunca repetir: un archivo ya publicado en el feed (reel, carrusel, imagen) no se vuelve a publicar.
    feed = {i['files'][0] for i in q if i['status'] == 'published' and i['kind'] != 'story'}
    for i in sorted(q, key=when):
        if i['status'] != 'pending': continue
        if i['kind'] != 'story' and i['files'][0] in feed:
            i['status'] = 'cancelled'; i['cancel_reason'] = 'repetido: ya publicado'; save(q); continue
        w = when(i)
        if n - timedelta(hours=6) <= w <= n + timedelta(minutes=25):
            out.append({'id': i['id'], 'kind': i['kind'], 'when': i['when'],
                        'urls': [CDN + f for f in i['files']], 'urls_raw': [RAW + f for f in i['files']],
                        'cover_url': CDN + i['cover'] if i.get('cover') else None,
                        'video': i['files'][0].endswith('.mp4'), 'caption': i.get('caption')})
    print(json.dumps(out, ensure_ascii=False, indent=1))


def mark(iid, status, val):
    q = load(); i = next(x for x in q if x['id'] == iid)
    i['status'] = status; t = now().strftime('%Y-%m-%dT%H:%M:%S%z')
    if status == 'published': i['media_id'] = str(val); i['published_at'] = t
    else: i['error'] = val
    save(q)
    log(f"| {now():%Y-%m-%d %H:%M} | {iid} {i['files'][0]} | {i['kind']} | {'publicado, media_id ' + str(val) if status == 'published' else 'fallo: ' + val} |")
    print('ok', iid, status)


def late():
    q = load(); n = now(); taken = {i['when'] for i in q if i['status'] == 'pending'}
    for i in sorted(q, key=when):
        if i['status'] == 'pending' and when(i) < n - timedelta(hours=6):
            w = when(i)
            while w < n or w.isoformat() in taken: w += timedelta(days=1)
            i['note'] = (i.get('note') or '') + f"; reprogramada (antes {i['when']})"; i['when'] = w.isoformat(); taken.add(i['when'])
            print('reprogramada', i['id'], i['when'])
    save(q)


def sheet():
    for i in load():
        if i['status'] in ('published', 'failed'):
            w = when(i); print(i['id'], w.strftime('%Y-%m-%d'), w.strftime('%H:%M'), 'Publicado' if i['status'] == 'published' else 'Fallido', i.get('media_id', ''), i['files'][0], sep='\t')


if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'due': due()
    elif c == 'done': mark(sys.argv[2], 'published', sys.argv[3])
    elif c == 'fail': mark(sys.argv[2], 'failed', sys.argv[3])
    elif c == 'late': late()
    elif c == 'sheet': sheet()
