"""Mezcla v7 · El techo no lo pone la categoría (Brian Clough) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», desde 1,8 s) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/bielsa/mix3.py y v7-puerta-de-atras-carril/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)
r2 (28/11): remate quieto hasta 24,3 s, fundido a NEGRO 24,3–24,8 y outro2 desde 24,8 (su voz entra a ~25,1, 1,8 s después de «semana»)."""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 24.3; CL = OUT + 0.5; DUR = CL + 4.0   # la voz acaba en 23,28 s; remate quieto hasta 24,3; negro 24,3–24,8; outro2 (4,0 s) desde 24,8
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
put(mus, ld('mus.mp3'), 0.0, 1.0, off=1.8, dur=CL + 1.4, fi=.4, fo=1.8)   # baja durante el negro y se apaga dentro del cierre
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(53)) / .5, 0, 1) * np.clip((CL + .4 - tt) / 1.2, 0, 1)   # sube 1 s en «entrenas» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); ST = pk(ld('stamp.mp3'))
FL = pk(ld('flip.mp3')); ME = pk(ld('metal.mp3')); TO = pk(ld('token.mp3')); CR = pk(ld('crowd.mp3'))
for f in [1.3, 5.62, 9.86, 18.98]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, ST, E(0) - .02, .13)                      # sello «2.ª DIVISIÓN»
put(sfx, SH, T(2) - .3, .1)                        # foto de Clough (obturador)
put(sfx, SL, T(5) - .12, .08)                      # ficha de prensa
put(sfx, MK, T(7) - .2, .04, dur=.9, fi=.05, fo=.3)    # la escalera se dibuja
put(sfx, TO, T(9), .09, dur=1.6, fo=.4)            # la ficha FOREST se arrastra y sube
put(sfx, MK, E(12) - .05, .05, dur=.5, fi=.03, fo=.2)  # rotulador: el hueco mínimo
put(sfx, FL, T(14) - .2, .11)                      # hoja del calendario 1977 → 1978
put(sfx, SL, T(18) - .3, .09)                      # postal del City Ground
put(sfx, TO, T(19) + .1, .07, dur=.5, fo=.2)       # FOREST llega al 1.
put(sfx, MK, T(27) - .05, .04, dur=1.0, fi=.05, fo=.3)  # primera copa se dibuja
put(sfx, ME, T(31) - .25, .1)                      # placa MÚNICH 1979
put(sfx, MK, T(33) - .05, .04, dur=1.0, fi=.05, fo=.3)  # segunda copa
put(sfx, ME, T(35) - .25, .1)                      # placa MADRID 1980
put(sfx, ME, T(39) - .25, .06); put(sfx, ME, T(39) + .05, .06)   # los dos 1–0
put(sfx, CR, T(37) - .3, .05, off=20.0, dur=E(42) - T(37) + 1.0, fi=.6, fo=.8)  # grada muy baja
put(sfx, MK, T(44), .04, dur=1.2, fi=.05, fo=.3)   # la línea del techo
put(sfx, MK, T(48) - .05, .07, dur=.5, fi=.02, fo=.2)   # el techo se rompe
put(sfx, MK, T(53) - .05, .06, dur=1.5, fi=.05, fo=.3)  # L M X J V S D
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), CL, dur=4.0)                       # audio de outro2 «¿Te ha servido? Dale like y síguenos…»
put(sti, ld(sys.argv[3]), CL, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .85)
fo = int((DUR - .8) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
