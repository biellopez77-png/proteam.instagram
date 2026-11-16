import numpy as np, sys
from scipy.io import wavfile
for f in sys.argv[1:]:
    sr, x = wavfile.read(f); x = x.astype(np.float32) / 32768
    h = int(.01 * sr); e = np.array([np.sqrt(np.mean(x[i:i+h]**2)) for i in range(0, len(x)-h, h)])
    th = max(e.max() * .03, .004); s = e > th
    segs = []; on = None
    for i, v in enumerate(s):
        if v and on is None: on = i
        if not v and on is not None:
            segs.append([on, i]); on = None
    if on is not None: segs.append([on, len(s)])
    m = []
    for a, b in segs:
        if m and a - m[-1][1] < 14: m[-1][1] = b
        else: m.append([a, b])
    print('==', f, len(x)/sr)
    print('  '.join(f'{a/100:.2f}-{b/100:.2f}' for a, b in m if b - a > 4))
