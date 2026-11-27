"""Montaje base de los vídeos POV (P1–P4): el vídeo de Biel siempre visible y los gráficos de agencia/recursos/pov/ encima,
entrando en el segundo que marca planes.json. Cuando llegue la grabación solo hay que pasar los clips.

  python3 tools/reelPOV/montar.py P1 --clips toma1.mp4 toma2.mp4 [--margen 1] [--voz voz.wav] [--musica m.mp3] [--plan otro.json] [--salida reels/p1.mp4]
  python3 tools/reelPOV/montar.py P1 --prueba        (fondo de prueba, sin grabación: comprueba tiempos y posiciones)

Reglas que aplica: nunca dos gráficos a la vez (si se pisan, no monta); cada gráfico entra con su WebM (0,5 s), se queda fijo
y sale en seco en su corte; el fondo no se oscurece ni se tapa entero; música al 60 % cuando hay voz (−40 %).
La voz es la del clip (si Biel habla) o --voz (Mateo). Sin ninguna de las dos avisa: ningún Reel sale sin voz."""
import argparse, json, os, subprocess, sys, shutil, hashlib, html
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(os.path.dirname(H))
POV = os.path.join(R, 'tools', 'pov'); REC = os.path.join(R, 'agencia', 'recursos', 'pov'); CACHE = os.path.join(H, '_cache')
W, HH, FPS, ANIM = 1080, 1920, 30, 2.0

def run(cmd): subprocess.run(cmd, check=True)
def dur(f): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).decode().strip())
def has_audio(f): return bool(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'a', '-show_entries', 'stream=index', '-of', 'csv=p=0', f]).decode().strip())

def variante(g, texto=None, tachado=False):
    """WebM propio para g10 con otra palabra o para un gráfico tachado. Se guarda en _cache/."""
    if not texto and not tachado: return os.path.join(REC, g + '.webm')
    os.makedirs(CACHE, exist_ok=True)
    k = g + '-' + hashlib.md5(f'{texto}|{tachado}'.encode()).hexdigest()[:8]; out = os.path.join(CACHE, k + '.webm')
    if os.path.exists(out): return out
    src = open(os.path.join(POV, g + '.html'), encoding='utf-8').read()
    if texto: src = src.replace('>PALABRA<', '>' + html.escape(texto) + '<')
    if tachado: src = src.replace('</div></body>', '<svg style="position:absolute;inset:0" width="1080" height="1920"><line x1="110" y1="560" x2="970" y2="900" stroke="#ff4d4d" stroke-width="18" stroke-linecap="round" pathLength="1" stroke-dasharray="1" style="animation:tz .35s .9s ease-out both"/></svg><style>@keyframes tz{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}</style></div></body>')
    src = src.replace('href="base.css"', 'href="file://' + os.path.join(POV, 'base.css') + '"')
    hp = os.path.join(CACHE, k + '.html'); open(hp, 'w', encoding='utf-8').write(src)
    from playwright.sync_api import sync_playwright
    tmp = os.path.join(CACHE, '_f'); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': HH}); pg.goto('file://' + hp); pg.evaluate('document.fonts.ready')
        pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for i in range(int(ANIM * FPS)):
            pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={i * 1000 / FPS})"); pg.screenshot(path=os.path.join(tmp, f'{i:03d}.png'), omit_background=True)
        b.close()
    run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', os.path.join(tmp, '%03d.png'), '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '2M', out + '.tmp.webm']); os.replace(out + '.tmp.webm', out); shutil.rmtree(tmp)
    return out

def main():
    a = argparse.ArgumentParser(); a.add_argument('plan_id'); a.add_argument('--clips', nargs='*', default=[]); a.add_argument('--margen', type=float, default=0.0, help='segundos que se quitan al principio y al final de cada toma')
    a.add_argument('--voz'); a.add_argument('--musica'); a.add_argument('--plan', default=os.path.join(H, 'planes.json')); a.add_argument('--salida'); a.add_argument('--prueba', action='store_true'); o = a.parse_args()
    P = json.load(open(o.plan, encoding='utf-8'))[o.plan_id]; G = sorted(P['graficos'], key=lambda g: g['de'])
    for x, y in zip(G, G[1:]):
        if y['de'] < x['a']: sys.exit(f"Dos gráficos a la vez: {x['g']} acaba en {x['a']} y {y['g']} entra en {y['de']}. Corrige planes.json.")
    os.makedirs(CACHE, exist_ok=True); fondo = os.path.join(CACHE, f'_fondo_{o.plan_id}.mp4'); vf = f'scale={W}:{HH}:force_original_aspect_ratio=increase,crop={W}:{HH},fps={FPS},setsar=1,format=yuv420p'
    if o.prueba:
        run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f"gradients=s={W}x{HH}:c0=0x8a6a4a:c1=0x2b3a4a:x0=0:y0=0:x1={W}:y1={HH}:speed=0.02:d={P['dur']}:r={FPS}", '-vf', "drawtext=text='FONDO DE PRUEBA %{pts\\:hms}':fontcolor=white@0.5:fontsize=44:x=60:y=140,format=yuv420p", '-an', fondo])
    else:
        if not o.clips: sys.exit('Faltan los clips de Biel (--clips) o usa --prueba.')
        partes = []
        for i, c in enumerate(o.clips):
            p = os.path.join(CACHE, f'_t{i}.mp4'); d = dur(c); aud = ['-c:a', 'aac', '-ar', '44100', '-ac', '2'] if has_audio(c) else ['-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest', '-c:a', 'aac']
            run(['ffmpeg', '-v', 'error', '-y', '-ss', str(o.margen), '-t', str(max(0.1, d - 2 * o.margen)), '-i', c] + (aud if has_audio(c) else aud[:4]) + ['-vf', vf, '-c:v', 'libx264', '-crf', '16', '-preset', 'fast'] + (aud[4:] if not has_audio(c) else []) + [p]); partes.append(p)
        lst = os.path.join(CACHE, '_lista.txt'); open(lst, 'w').write(''.join(f"file '{p}'\n" for p in partes)); run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', fondo])
    D = dur(fondo)
    if D + 0.5 < P['dur']: print(f"AVISO: el vídeo dura {D:.1f} s y el guion {P['dur']} s: ajusta los tiempos de planes.json a la voz real.")
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', fondo]; fc = []; last = '0:v'
    for i, g in enumerate(G):
        fin = min(g['a'], D)
        if g['de'] >= D: print(f"AVISO: {g['g']} entra en {g['de']} s, después del final ({D:.1f} s): no sale."); continue
        cmd += ['-c:v', 'libvpx-vp9', '-i', variante(g['g'], g.get('texto'), g.get('tachado', False))]; n = len([c for c in cmd if c == '-i']) - 1
        s = g.get('escala', 1); dy = g.get('dy', 0); hold = max(0, fin - g['de'] - ANIM) + 0.1
        esc = f',scale=iw*{s}:ih*{s}' if s != 1 else ''
        fc.append(f"[{n}:v]format=yuva420p{esc},tpad=stop_mode=clone:stop_duration={hold:.3f},setpts=PTS-STARTPTS+{g['de']}/TB[g{i}]")
        fc.append(f"[{last}][g{i}]overlay=x=(W-w)/2:y=(H-h)/2+{dy}:enable='between(t,{g['de']},{fin})':eof_action=pass[v{i}]"); last = f'v{i}'
    # sonido: voz (del clip o --voz) + música al 60 % si hay voz
    voz_clip = (not o.prueba) and has_audio(fondo); amap = None; ai = None
    if o.voz: cmd += ['-i', o.voz]; ai = len([c for c in cmd if c == '-i']) - 1; fc.append(f'[{ai}:a]aresample=44100,apad[vz]'); amap = '[vz]'
    elif voz_clip: fc.append('[0:a]aresample=44100[vz]'); amap = '[vz]'
    else: print('AVISO: sin voz (ni en el clip ni --voz). Sirve para revisar, no para publicar: ningún Reel sale sin voz.')
    if o.musica:
        cmd += ['-stream_loop', '-1', '-i', o.musica]; mi = len([c for c in cmd if c == '-i']) - 1
        fc.append(f"[{mi}:a]aresample=44100,volume={'0.6' if amap else '1'},afade=t=out:st={max(0, D - 1.2):.2f}:d=1.2[mu]")
        if amap: fc.append(f'{amap}[mu]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]'); amap = '[a]'
        else: amap = '[mu]'
    sal = o.salida or os.path.join(CACHE, f'{o.plan_id}-{"prueba" if o.prueba else "montaje"}.mp4'); os.makedirs(os.path.dirname(os.path.abspath(sal)), exist_ok=True)
    if fc: cmd += ['-filter_complex', ';'.join(fc)]
    cmd += ['-map', f'[{last}]' if last != '0:v' else '0:v'] + (['-map', amap] if amap else ['-an']) + ['-t', f'{D:.3f}', '-r', str(FPS), '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p'] + (['-c:a', 'aac', '-b:a', '192k'] if amap else []) + ['-movflags', '+faststart', sal]
    run(cmd); print('OK', sal, f'{dur(sal):.1f} s')
if __name__ == '__main__': main()
