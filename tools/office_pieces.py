"""Sección «Contenido» de la oficina (https://claude.ai/artifact/CEbj9fsPQPUvVtRsp1S18o): sincroniza queue.json -> colección `pieces`.

  python3 tools/office_pieces.py prep        -> crea en .office_media/ las vistas previas que aún no se han subido
                                                (Reels a 540 px, imágenes a 1080 px) y lista ARCHIVO_ORIGEN<TAB>VISTA_PREVIA.
                                                Súbelas con Artifact (publish, url de la oficina, asset true, file_paths) y apunta cada una:
  python3 tools/office_pieces.py add ARCHIVO_ORIGEN URL   -> guarda la URL /_blob/... en office_media.json
  python3 tools/office_pieces.py docs DIR    -> DIR = carpeta donde ArtifactData list (collection pieces, out_dir) dejó los documentos.
                                                Escribe .office_media/writes.json: la lista `writes` lista para ArtifactData batch
                                                (update con if_version si existe, set si es nueva). Solo toca campos de la cola, nunca
                                                los de Biel (fix, fixState, fixAt) ni los del equipo (fixNote, fixDoneAt).
  python3 tools/office_pieces.py fixes DIR   -> lista las correcciones de Biel sin atender: id<TAB>fixState<TAB>comentario<TAB>agentId

Piezas incluidas: todo lo pending y borrador del formato actual, más lo publicado, fallido o cancelado en los últimos 7 días.
Formato actual = piezas con campana «unrespiro» (Reels) o «carrusel» (carruseles, posts y Stories de Clara).
"""
import json, os, subprocess, sys, glob
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TZ = ZoneInfo('Europe/Madrid')
OUT = os.path.join(R, '.office_media'); J = os.path.join(R, 'office_media.json')
CDN = 'https://cdn.jsdelivr.net/gh/biellopez77-png/proteam.instagram@main/'
media = lambda: json.load(open(J)) if os.path.exists(J) else {}


def current(i):
    return i.get('campana') in ('unrespiro', 'carrusel')


def pieces():
    q = json.load(open(os.path.join(R, 'queue.json'))); n = datetime.now(TZ); out = []
    for i in q:
        if not current(i): continue
        w = datetime.fromisoformat(i['when'])
        if i['status'] in ('pending', 'borrador') or w > n - timedelta(days=7): out.append(i)
    return out


def files_of(i):
    f = list(i.get('files') or [])
    if i.get('cover'): f.append(i['cover'])
    return f


def preview(src):
    os.makedirs(OUT, exist_ok=True); base = src.replace('/', '__'); s = os.path.join(R, src)
    if src.endswith('.mp4'):
        o = os.path.join(OUT, base)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', s, '-vf', 'scale=540:-2', '-c:v', 'libx264', '-preset', 'veryfast',
                        '-crf', '27', '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', o], check=True)
    else:
        o = os.path.join(OUT, os.path.splitext(base)[0] + '.jpg')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', s, '-vf', "scale='min(1080,iw)':-2", '-q:v', '4', o], check=True)
    return o


AGENT = {'reel': '02', 'carousel': '04', 'story': '04', 'image': '04'}


def doc(i, m):
    url = lambda f: m.get(f) or (CDN + f)
    cap = i.get('caption') or ''
    title = i.get('title') or (cap.split('\n')[0] if cap else (i.get('note') or i['id']))
    d = {'kind': i['kind'], 'when': i['when'], 'status': i['status'], 'title': title[:200], 'caption': cap,
         'note': i.get('note') or '', 'agentId': i.get('agentId') or AGENT.get(i['kind'], '02'),
         'media': [url(f) for f in i.get('files') or []], 'cover': url(i['cover']) if i.get('cover') else '',
         'score': i.get('score') or '', 'mediaId': i.get('media_id') or '', 'publishedAt': i.get('published_at') or '',
         'error': i.get('error') or i.get('cancel_reason') or '', 'syncedAt': datetime.now(TZ).isoformat(timespec='seconds')}
    return d


def existing(d):
    ex = {}
    for p in glob.glob(os.path.join(d, '**', '*.json'), recursive=True):
        try: x = json.load(open(p))
        except Exception: continue
        did = x.get('id') or os.path.splitext(os.path.basename(p))[0]
        ex[did] = x
    return ex


c = sys.argv[1]
if c == 'prep':
    m = media()
    for i in pieces():
        for f in files_of(i):
            if f not in m and os.path.exists(os.path.join(R, f)): print(f, preview(f), sep='\t')
elif c == 'add':
    m = media(); m[sys.argv[2]] = sys.argv[3]; json.dump(m, open(J, 'w'), ensure_ascii=False, indent=1); print('ok', len(m))
elif c == 'docs':
    ex = existing(sys.argv[2]); m = media(); w = []
    for i in pieces():
        d = doc(i, m); e = ex.get(i['id']); os.makedirs(os.path.join(OUT, 'docs'), exist_ok=True)
        fp = os.path.join(OUT, 'docs', i['id'] + '.json'); json.dump(d, open(fp, 'w'), ensure_ascii=False)
        if e: w.append({'op': 'update', 'collection': 'pieces', 'doc_id': i['id'], 'file_path': fp, 'if_version': e.get('version')})
        else: w.append({'op': 'set', 'collection': 'pieces', 'doc_id': i['id'], 'file_path': fp})
    p = os.path.join(OUT, 'writes.json'); json.dump(w, open(p, 'w'), ensure_ascii=False)
    print(p, len(w), 'escrituras')
elif c == 'fixes':
    for k, x in existing(sys.argv[2]).items():
        dd = x.get('data', x); st = dd.get('fixState')
        if st in ('pedida', 'quitar'): print(k, st, (dd.get('fix') or '').replace('\n', ' '), dd.get('agentId', ''), sep='\t')
