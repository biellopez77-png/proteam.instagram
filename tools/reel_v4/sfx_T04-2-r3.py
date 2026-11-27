"""Efectos suaves de T04-2-r3 «Hasta Donnarumma»: aire en los cambios de zona, lápiz en el guante, la interrogación, las marcas y la libreta, papel en la lista y en la cinta. Sin golpes.
python3 sfx_T04-2-r3.py T04-2-r3/sfx.wav T04-2-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('apuntado')-.3,1.1,.4),(at('portero')-.3,1.0,.3),(at('y')-.3,1.0,.3),(at('final')-.4,1.4,.45),(at('2020')-.3,1.0,.3),(at('wembley')-.3,1.0,.3),
              (at('jordan')-.45,1.1,.3),(at('inglaterra')-.3,1.0,.3),(at('tanda')-.45,1.4,.4),(at('o')-.1,1.4,.3),(at('cada')-.35,1.2,.35),(at('y',2)-.3,1.2,.35),
              (at('nueve')-.35,1.6,.3),(at('toloi')-.3,1.0,.3),(at('paro')-.35,1.3,.4),(at('inglaterra',2)-.3,1.0,.3),(at('pero')-.3,1.0,.3),
              (at('ahora')-.45,1.5,.45),(at('dorsal')-.35,1.0,.25),(at('vuelta')-.35,1.2,.35),(at('solo',2)-.25,1.3,.4),(at('apuntalo')-.35,1.3,.4),(at('porque',2)+.05,1.8,.45)]:
    put(t,air(d),g)
put(at('y'),pencil(.6),.3)
put(at('penalti')-.1,pencil(.5),.28)
put(at('cada')+.3,pencil(.9),.22)
put(at('penaltis')+.95+.25,paper(1.4),.35)
for w in ['belotti','jorginho']: put(at(w)-.1,pencil(.4),.35)
for w,n in [('cada',2),('falta',2),('dorsal',1),('lado',1)]: put(at(w,n),pencil(.5),.32)
put(at('botella',3)-.2,paper(.6),.35)
put(at('nueve',2)-.2,pencil(.5),.3)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
