"""Cola de publicación v3 (Instagram por Windsor y kit de TikTok). Biel, 23/11.

NADA se publica mientras publicar/ESTADO.json tenga "publicar": false (lo cambia solo Biel).

  python3 tools/pub_v3.py add ID KIND CAPTION_FILE FILE [FILE...]   -> añade una pieza lista (KIND: reel|carrusel|story)
        Copia los archivos a publicar/media/ y la deja en estado «revisión» (sin fecha) hasta que Biel la apruebe.
  python3 tools/pub_v3.py approve ID [ISO]   -> la aprueba y la programa (por defecto, el siguiente hueco libre)
  python3 tools/pub_v3.py due                -> JSON con lo que toca publicar AHORA en Instagram, con URLs públicas.
                                                 Imprime [] si el interruptor está apagado o no hay nada.
  python3 tools/pub_v3.py done ID ig MEDIA_ID | done ID tiktok URL
  python3 tools/pub_v3.py fail ID ig|tiktok "error"
  python3 tools/pub_v3.py tiktok             -> prepara publicar/tiktok/<id>/ (vídeo + texto) de los reels aprobados sin publicar en TikTok
  python3 tools/pub_v3.py status             -> resumen de la cola
"""
import json, os, sys, shutil
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(R, 'publicar'); Q = os.path.join(D, 'cola.json'); E = os.path.join(D, 'ESTADO.json')
TZ = ZoneInfo('Europe/Madrid')
CDN = 'https://cdn.jsdelivr.net/gh/biellopez77-png/proteam.instagram@main/'
RAW = 'https://raw.githubusercontent.com/biellopez77-png/proteam.instagram/main/'
# Huecos por defecto (hora de Madrid). Los cambia la estrategia de relanzamiento.
SLOTS = {'reel': ['13:30', '20:30'], 'carrusel': ['11:00'], 'story': ['12:00', '18:00']}


def load(p, d): return json.load(open(p)) if os.path.exists(p) else d
def save(p, x): os.makedirs(D, exist_ok=True); json.dump(x, open(p, 'w'), ensure_ascii=False, indent=1)
def now(): return datetime.now(TZ)
def on(): return bool(load(E, {}).get('publicar'))


def next_slot(q, kind):
    taken = {i['ig'].get('when') for i in q if i['ig'].get('when')}
    d = now()
    for day in range(0, 60):
        for h in SLOTS[kind]:
            t = datetime.fromisoformat(f"{(d + timedelta(days=day)).date()}T{h}:00").replace(tzinfo=TZ)
            if t > d + timedelta(minutes=30) and t.isoformat() not in taken:
                return t.isoformat()
    raise SystemExit('sin huecos')


def cmd(a):
    q = load(Q, [])
    if a[0] == 'add':
        pid, kind, capf, files = a[1], a[2], a[3], a[4:]
        assert kind in SLOTS and files and not any(i['id'] == pid for i in q), 'id repetido o datos incompletos'
        dst = []
        for f in files:
            name = f"{pid}-{len(dst) + 1}{os.path.splitext(f)[1].lower()}" if len(files) > 1 else f"{pid}{os.path.splitext(f)[1].lower()}"
            os.makedirs(os.path.join(D, 'media'), exist_ok=True)
            shutil.copy(f, os.path.join(D, 'media', name)); dst.append(f"publicar/media/{name}")
        q.append({'id': pid, 'kind': kind, 'files': dst, 'caption': open(capf).read().strip(), 'state': 'revisión',
                  'ig': {'status': 'pendiente'}, 'tiktok': {'status': 'pendiente' if kind == 'reel' else 'no'}, 'added': now().isoformat()})
        save(Q, q); print('añadida', pid, dst)
    elif a[0] == 'approve':
        i = next(i for i in q if i['id'] == a[1]); i['state'] = 'aprobada'
        i['ig']['when'] = a[2] if len(a) > 2 else next_slot(q, i['kind']); save(Q, q); print(a[1], '→', i['ig']['when'])
    elif a[0] == 'due':
        if not on(): print('[]'); return
        out = [{'id': i['id'], 'kind': i['kind'], 'caption': i['caption'],
                'urls': [f if f.startswith('http') else CDN + f for f in i['files']], 'raw': [f if f.startswith('http') else RAW + f for f in i['files']]}
               for i in sorted(q, key=lambda i: i['ig'].get('when', '9'))
               if i['state'] == 'aprobada' and i['ig']['status'] == 'pendiente'
               and datetime.fromisoformat(i['ig']['when']) <= now()]
        print(json.dumps(out[:1], ensure_ascii=False, indent=1))  # una pieza por turno
    elif a[0] == 'done':
        i = next(i for i in q if i['id'] == a[1]); i[a[2]].update(status='publicada', ref=a[3], at=now().isoformat()); save(Q, q)
    elif a[0] == 'fail':
        i = next(i for i in q if i['id'] == a[1]); i[a[2]].update(status='fallida', error=a[3], at=now().isoformat()); save(Q, q)
    elif a[0] == 'tiktok':
        n = 0
        for i in q:
            if i['state'] == 'aprobada' and i['tiktok']['status'] == 'pendiente':
                k = os.path.join(D, 'tiktok', i['id']); os.makedirs(k, exist_ok=True)
                shutil.copy(os.path.join(R, i['files'][0]), os.path.join(k, os.path.basename(i['files'][0])))
                open(os.path.join(k, 'texto.txt'), 'w').write(i['caption'][:2200]); n += 1
        print('kits de TikTok:', n)
    elif a[0] == 'status':
        print('interruptor:', 'ENCENDIDO' if on() else 'apagado (no se publica nada)')
        for i in q: print(f"{i['id']:<24} {i['kind']:<9} {i['state']:<9} IG {i['ig']['status']:<10} {i['ig'].get('when', '')[:16]:<17} TikTok {i['tiktok']['status']}")


if __name__ == '__main__':
    cmd(sys.argv[1:] or ['status'])
