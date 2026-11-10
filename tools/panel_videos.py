"""Vídeos de los próximos Reels para el panel de Biel (pestaña Próximos, botón «Ver vídeo»).

  python3 tools/panel_videos.py prep            -> crea vistas previas ligeras (540x960) en .panel_videos/ (no se sube a git) de los
                                                  Reels pendientes que aún no están en el panel y lista sus rutas.
  python3 tools/panel_videos.py add ARCHIVO URL -> apunta en panel_videos.json la URL /_blob/... que devolvió la subida.
  python3 tools/panel_videos.py clean           -> quita de panel_videos.json lo que ya no está pendiente.

Después de `add`: subir panel_videos.json al panel como asset y poner su URL en datasets/videos (ver PLAYBOOK, «Panel»).
"""
import json, os, subprocess, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = os.path.join(R, 'panel_videos.json'); OUT = os.path.join(R, '.panel_videos')
load = lambda: json.load(open(J)) if os.path.exists(J) else []
save = lambda v: json.dump(v, open(J, 'w'), ensure_ascii=False, indent=1)
pend = lambda: [i['files'][0] for i in json.load(open(os.path.join(R, 'queue.json'))) if i['status'] == 'pending' and i['kind'] == 'reel']

c = sys.argv[1]
if c == 'prep':
    os.makedirs(OUT, exist_ok=True); have = {v['archivo'] for v in load()}
    for f in dict.fromkeys(pend()):
        if f in have: continue
        o = os.path.join(OUT, os.path.basename(f))
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', os.path.join(R, f), '-vf', 'scale=540:-2', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27',
                        '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', o], check=True)
        print(f, o, os.path.getsize(o), sep='\t')
elif c == 'add':
    v = [x for x in load() if x['archivo'] != sys.argv[2]] + [{'archivo': sys.argv[2], 'url': sys.argv[3]}]; save(v); print(len(v))
elif c == 'clean':
    p = set(pend()); v = [x for x in load() if x['archivo'] in p]; save(v); print(len(v))
