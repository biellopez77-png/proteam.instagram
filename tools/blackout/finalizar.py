"""Pasa los Reels terminados (tools/blackout/reels/bXX.mp4) a reels/ con el nombre de la cola, saca portada y los activa.
  python3 tools/blackout/finalizar.py"""
import json, os, re, subprocess
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); B = os.path.join(R, 'tools/blackout/reels')
q = json.load(open(os.path.join(R, 'queue.json'))); hechos = []
for i in q:
    if i.get('campana') != 'blackout' or i['kind'] != 'reel' or i['status'] not in ('borrador', 'pending'): continue
    ch = int(re.search(r'-ch(\d\d)-', i['files'][0]).group(1)); src = f'{B}/b{ch:02d}.mp4'; log = f'{B}/b{ch:02d}.log'
    dst = os.path.join(R, i['files'][0])
    if os.path.exists(dst): continue
    if not (os.path.exists(log) and any(l.startswith('ok') for l in open(log))): print('falta', i['id'], f'CH {ch:02d}'); continue
    st = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout.split()
    if 'audio' not in st or 'video' not in st: print('roto', src); continue
    subprocess.run(['cp', src, dst], check=True)
    spec = json.load(open(f'{B}/b{ch:02d}.json'))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(min(3.0, spec['cut'] - .5)), '-i', src, '-frames:v', '1', '-q:v', '2', os.path.join(R, i['cover'])], check=True)
    i['status'] = 'pending'; hechos.append(i['id'])
json.dump(q, open(os.path.join(R, 'queue.json'), 'w'), ensure_ascii=False, indent=1)
print('listos:', hechos)
