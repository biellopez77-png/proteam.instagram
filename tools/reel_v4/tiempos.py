"""Voz ×1.08 (REEL_ESTILO) y tiempos de palabra (Scribe) → <id>/voz.wav y <id>/times.js.
python3 tiempos.py bq|bm"""
import json, sys, subprocess, re, unicodedata
k = sys.argv[1]; SP = float(__import__("os").environ.get("SP", 1.08)); O = .06
subprocess.run(['mkdir', '-p', k]); subprocess.run(f'ffmpeg -v error -y -i {k}_voz.mp3 -af "adelay=60|60,atempo={SP}" -ar 44100 -ac 2 {k}/voz.wav', shell=True, check=True)
W = [w for w in json.load(open(f'{k}_words.json'))['words'] if w['type'] == 'word']
norm = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode())
L = [[norm(w['text']), round(w['start'] / SP + O, 3), round(w['end'] / SP + O, 3)] for w in W]
dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'{k}/voz.wav']))
open(f'{k}/times.js', 'w').write('window.WORDS=' + json.dumps(L) + ';window.VEND=' + str(round(dur, 3)) + ';\n'); print(k, dur, len(L))
