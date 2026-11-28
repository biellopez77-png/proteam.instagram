"""Mezcla v7 · Lo que haces después · r2 (gancho nuevo «Perdieron 10 a 3 contra la URSS…»; Herb Brooks, 10-3 en el Madison Square Garden y 4-3 en Lake Placid, 1980). Se ejecuta en el sandbox de Higgsfield.
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01», «… Logo 03» y «… Logo 02», encadenadas con fundidos de 1,4 s) + SFX reales bajos + voz (ElevenLabs, Mateo).
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 27.9; DUR = OUT + 4.0   # la voz acaba en 26,38 s; remate quieto hasta 27,38, fundido a negro hasta 27,9 y el cierre (outro2.mp4, 4,0 s) desde negro
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); sti = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
M1 = ld('mus1.mp3'); M3 = ld('mus3.mp3'); M2 = ld('mus2.mp3')
put(mus, M1, 0.0, 1.0, dur=13.8, fi=.3, fo=1.4)
put(mus, M3, 12.4, 1.0, dur=13.8, fi=1.4, fo=1.4)
put(mus, M2, 24.8, 1.0, dur=DUR - 24.8, fi=1.4, fo=2.6)   # baja durante el cierre
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(56)) / .5, 0, 1) * np.clip((OUT - .3 - tt) / .8, 0, 1)   # sube un poco en «después» y baja al negro
env *= np.where(tt > OUT - .5, np.clip(1 - .55 * (tt - (OUT - .5)) / 1.0, .45, 1), 1)   # la música queda bajando bajo la voz del cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); PG = pk(ld('page.mp3'))
MD = pk(ld('medal.mp3')); CO = pk(ld('counter.mp3'))
for f in [5.22, 13.25, 19.15, 22.1, 24.12]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, CO, T(1) - .03, .035, dur=.35, fi=.01, fo=.15)   # latido del marcador en «diez a tres»
put(sfx, PG, T(6), .05); put(sfx, PG, T(7) + .1, .04); put(sfx, PG, T(8) + .15, .04)   # hojas del 9 al 22
put(sfx, CO, T(10) - .05, .05, dur=.4, fi=.01, fo=.15)    # 4-3 en «les ganaron»
put(sfx, SL, T(11) - .75, .05)                            # marquesina
put(sfx, SL, T(16) - .1, .06)                             # ficha del partido
put(sfx, SL, T(17) - .15, .07)                            # ficha de EE. UU.
put(sfx, SL, T(21) - .15, .06)                            # ficha de la URSS
for k in [22, 23, 24, 25]: put(sfx, MD, T(k) + .12, .09)  # cuatro medallas sobre la mesa
put(sfx, SH, T(27) - .2, .09)                             # foto de Herb Brooks (obturador)
put(sfx, SL, T(31) - .15, .08)                            # el recorte se desliza
put(sfx, MK, T(34), .05, dur=2.4, fi=.03, fo=.4)          # rotulador que subraya la cita
put(sfx, SH, T(42) - .5, .07)                             # foto del pabellón
put(sfx, SL, T(45) - .3, .08)                             # la portada se desliza
put(sfx, CO, T(46) - .05, .05, dur=.35, fi=.02, fo=.15); put(sfx, CO, T(47) + .1, .05, dur=.35, fi=.02, fo=.15)   # 4 a 3
put(sfx, SL, T(48) - .3, .05)                             # el 10-3 grande
put(sfx, MK, T(51) - .05, .07, dur=.6, fi=.02, fo=.2)     # rotulador que agrieta el 10-3
put(sfx, SL, T(53) - .6, .05)                             # Jim Craig detrás
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
