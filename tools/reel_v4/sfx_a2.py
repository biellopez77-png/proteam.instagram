"""Efectos suaves de A1 v2: aire en los movimientos, un barrido en el paso rápido al 2006, lápiz en las rayas y un roce de papel. Sin golpes.
python3 sfx_a2.py a2/sfx.wav a2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
def sweep(d=.6):
    n=int(d*SR); y=bp(rng.standard_normal(n),600,7000); return y*env(n,2,.6)/(np.abs(y).max()+1e-9)
for t,d,g in [(at('lo')-.2,1.2,.45),(at('en')-.1,1.0,.35),(at('jens')-.1,1.4,.45),(at('leia')-.2,1.2,.35),(at('paro')-.4,1.2,.4),
              (at('ahora')-.6,1.6,.35),(at('tres')-.1,1.2,.3),(at('nadie')-.1,1.1,.3),(at('y',3)-.1,1.8,.35),(at('mientras')-.3,1.6,.35),
              (at('dale')-.4,1.5,.4),(at('rayas')-.4,1.2,.3),(at('lehmann',2)-.3,1.6,.45),(at('apuntalo')-.3,2.0,.4)]:
    put(t,air(d),g)
put(at('mundial')-.15,sweep(.7),.5)
for k,w in enumerate(['alemania','argentina']): put(at(w)-.2,air(.9,300,2600),.35)
put(at('lehmann',2),paper(),.35); put(at('en')+.1,paper(.35),.25)
for k in range(3): put(at('tres')+[0,.45,1.1][k],pencil(.5),.25)
s=at('seis'); put(at('dale')+.2,pencil(.9),.35); put(s-.1,pencil(.7),.25)
a0=at('raya'); a1=at('descanso',2)-.1
for k in range(10): put(a0+(a1-a0)*k/10,pencil(),.4)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
