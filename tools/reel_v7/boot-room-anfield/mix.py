"""Mezcla v7 · La Biblia del cuarto de las botas (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Calm, Piano 01» y «02») + SFX reales bajos + voz (ElevenLabs, Mateo).
python3 mix.py voz.mp3 tail.mp3 out.wav"""
import sys, subprocess, numpy as np
SR = 48000; OUT = 21.0; DUR = OUT + 5.61   # la voz acaba en 20,9 s; ahí entra el cierre (xfade 0,6 s)
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(at * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: dos piezas de la misma serie, encadenadas sin cortes; la 02 crece hacia «la Biblia» y cierra con la voz
put(mus, ld('m01.mp3'), 0.0, 1.0, off=0.5, fi=0.3)
put(mus, ld('m02.mp3'), 9.3, 1.0, fo=1.4)
W = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); BO = pk(ld('boots.mp3')); TK = pk(ld('token.mp3'))
BT = pk(ld('bottles.mp3')); SH = pk(ld('shutter.mp3')); PG = pk(ld('pages.mp3')); BK = pk(ld('bookopen.mp3'))
PN = pk(ld('pen.mp3')); ST = pk(ld('stamp.mp3'))
for f in [3.0, 6.2, 8.3, 13.4, 16.1, 18.15]: put(sfx, W, f - .25, .08, dur=1.5, fi=.05, fo=.5)   # aire en cada viaje
put(sfx, PA, 0.0, .12)                                   # ficha de Anfield
for k, (at, g) in enumerate([(2.62, .10), (2.82, .08), (2.98, .07)]): put(sfx, BO, at, g)        # botas sobre el estante
for k, at in enumerate([4.02, 4.18, 4.34, 4.50]): put(sfx, TK, at, .08, off=k * .9, dur=.3, fo=.05)  # fichas en el plano
put(sfx, TK, 5.02, .05, off=0, dur=.3, fo=.05)          # la séptima, fuera
put(sfx, BT, 5.25, .07, off=.15, dur=1.2, fo=.4)         # cajas con botellas
put(sfx, PA, 6.5, .10)                                   # foto de 1964
put(sfx, SH, 6.78, .09)                                  # obturador
put(sfx, PA, 7.55, .07)                                  # ficha de Ronnie Moran
put(sfx, PG, 9.2, .10, dur=1.1, fo=.3)                   # páginas que pasan con «cada día»
put(sfx, PN, 10.0, .08, dur=1.2, fi=.05, fo=.3)          # renglones escritos
put(sfx, PN, 11.5, .07, off=1.2, dur=.9, fi=.05, fo=.3)  # ✓ entrenó
put(sfx, PN, 12.94, .07, dur=.45, fo=.15)                # ✕ lesionado
put(sfx, PA, 14.0, .07)                                  # gráfico de forma
put(sfx, BK, 15.42, .12, dur=1.2, fo=.4)                 # abrían el libro
put(sfx, PA, 16.55, .08)                                 # tapa del libro
put(sfx, ST, 17.76, .22)                                 # sello «THE BOOT ROOM BIBLE»
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT + 0.3)
e = np.abs(vox[:, 0]); hop = 480; env = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
env = np.minimum(1, env / (np.percentile(env[env > 0], 90) + 1e-9)); sm = np.zeros_like(env)
for i in range(1, len(env)): a = .45 if env[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (env[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .8) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
