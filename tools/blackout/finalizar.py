"""Copia los episodios renderizados a reels/ con el nombre de la cola, saca la portada y lista lo que falta.
  python3 tools/blackout/finalizar.py"""
import json, os, subprocess, re
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
q = json.load(open(os.path.join(R, 'queue.json')))
for i in q:
    if i.get('campana') != 'blackout' or i['kind'] != 'reel' or i['id'] == 'bf01': continue
    ch = int(re.search(r'-ch(\d\d)-', i['files'][0]).group(1)); src = os.path.join(R, f'tools/blackout/reels/e{ch:02d}.mp4')
    dst = os.path.join(R, i['files'][0]); cov = os.path.join(R, i['cover'])
    if os.path.exists(dst): continue
    ok = os.path.exists(src) and subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout.strip()
    if not ok: print('falta', i['id'], f'CH {ch:02d}'); continue
    if not any(x['type'] == 'audio' for x in [{'type': l} for l in subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout.split()]):
        print('sin audio', src); continue
    subprocess.run(['cp', src, dst], check=True)
    spec = json.load(open(src.replace('.mp4', '.json'))); sc = spec['ep']['scenes']; t = sc[1]['t0'] + 1.0
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', src, '-frames:v', '1', '-q:v', '2', cov], check=True)
    print('listo', i['id'], i['files'][0])
