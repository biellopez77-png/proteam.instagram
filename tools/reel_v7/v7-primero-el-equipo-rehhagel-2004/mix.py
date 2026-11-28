"""Mezcla v7 · Primero, el equipo (Otto Rehhagel, Grecia 2004) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 03», encadenada consigo misma con fundidos de 1,4 s; distinta de la del último v7)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: v7-siete-segundos-dantoni/mix.py.
La voz acaba en 20,42 s; remate quieto hasta 21,5 s; fundido a negro de 21,5 a 22,0 s; outro2 (4 s, con su voz) desde 22,0 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.0; DUR = OUT + 4.0
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vn', '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: la misma pista tres veces, fundidos de 1,4 s (misma tonalidad)
M = ld('mus.mp3'); L = len(M) / SR; at = 0.0
for i in range(3):
    put(mus, M, at, 1.0, fi=(.3 if i == 0 else 1.4), fo=1.4); at += L - 1.4
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .15 * np.clip((tt - 17.4) / .4, 0, 1) * np.clip((19.2 - tt) / .4, 0, 1)            # baja un poco en la pausa de «Portugal...» y «Campeona»
env *= 1 + .3 * np.clip((tt - 19.2) / .5, 0, 1) * np.clip((20.4 - tt) / .5, 0, 1)             # sube 1 s con «Primero, el equipo»
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                   # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); ST = pk(ld('stamp.mp3'))
TO = pk(ld('token.mp3')); KI = pk(ld('kick.mp3')); CL = pk(ld('cloth.mp3')); PG = pk(ld('page.mp3')); SG = pk(ld('sting.mp3'))
for f in [3.75, 7.08, 10.28, 13.33, 17.38, 18.92]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, ST, T(8) - .08, .10, off=.8, dur=.5, fo=.2)       # «0» en EURO 1980
put(sfx, ST, T(12) - .08, .10, off=.8, dur=.5, fo=.2)      # «0» en MUNDIAL 1994
put(sfx, MK, E(12) - .1, .05, dur=.5, fi=.02, fo=.2)       # rotulador subraya la columna
put(sfx, SL, T(13) - .3, .07)                              # billete
put(sfx, ST, T(14) - .03, .08, off=.8, dur=.5, fo=.2)      # sello 2001
put(sfx, SH, T(18) - .3, .09, off=1.55, dur=.5, fo=.2)     # foto de Rehhagel
put(sfx, SL, T(19) - .1, .05)                              # ficha de prensa
put(sfx, SL, 7.15, .05)                                    # foto en la banda
put(sfx, TO, T(21) - .05, .06, dur=.8, fo=.3)              # marcaje: fichas
put(sfx, MK, T(24) - .05, .05, dur=.7, fi=.02, fo=.25)     # bloque atrás
put(sfx, KI, T(26) - .05, .09, dur=.6, fo=.2)              # balón parado
put(sfx, SL, 10.4, .05)                                    # tarjeta de la regla
put(sfx, CL, T(32) - .15, .08, off=.1, dur=1.0, fo=.3)     # camiseta
put(sfx, TO, T(33), .04, dur=.8, fo=.3)                    # los escudos se apartan
put(sfx, TO, T(41) - .12, .07, dur=.4, fo=.15)             # marcador Francia
put(sfx, TO, T(43) - .12, .07, dur=.4, fo=.15)             # marcador Chequia
put(sfx, SH, T(44) - .2, .08, off=1.55, dur=.5, fo=.2)     # foto de la final
put(sfx, TO, T(45) - .12, .06, dur=.4, fo=.15)             # 2-1 inaugural
put(sfx, TO, T(46) - .02, .06, dur=.4, fo=.15)             # 1-0 final
put(sfx, PG, 17.45, .10, off=.2)                           # portada que se abre
put(sfx, MK, T(52) - .05, .05, dur=1.0, fi=.02, fo=.3)     # pizarra: las once fichas se juntan
put(sfx, SG, OUT, .10, dur=4.0, fi=.05, fo=1.0)            # sting de piano bajo, bajo el cierre
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT)      # audio de outro2.mp4 («¿Te ha servido? Dale like y síguenos…»)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20)
ov = vox[int(OUT * SR):].copy(); vox *= vg
o_r = 20 * np.log10(np.sqrt((ov ** 2).mean()) + 1e-12); vox[int(OUT * SR):] = ov * 10 ** ((-19.5 - o_r) / 20)   # el cierre al nivel de la voz
mus *= 10 ** ((-31 - R(mus)) / 20)
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .85)
fo = int((DUR - .3) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
