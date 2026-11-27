"""Efectos suaves de T01-1-r1 «Fuera del papel»: aire en los movimientos de cámara, lápiz en la hoja y en los círculos, papel en el gran papel y en la hoja. Sin golpes.
python3 sfx_T01-1-r1.py T01-1-r1/sfx.wav T01-1-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('y')-.3,1.0,.3),(at('dos')-.3,1.0,.3),(at('argentina')-.35,.9,.25),(at('el',2)-.3,1.1,.3),(at('cuarto')-.3,.9,.25),
              (at('pero')-.35,1.1,.3),(at('sabia')-.3,.9,.25),(at('ahora')-.4,1.4,.4),(at('tienes')-.3,.9,.25),(at('el',5)-.3,.9,.25),
              (at('y',4)-.35,1.1,.3),(at('tu',3)-.35,.9,.25),(at('tienes',3)-.3,.9,.25),(at('antes')-.3,.9,.25),(at('dorsal')-.3,.9,.25),
              (at('descanso',2)-.4,1.1,.3),(at('apuntalo')-.35,1.4,.4),(at('porque')+.05,1.6,.4)]:
    put(t,air(d),g)
put(at('el',2)-.1,paper(.6),.3); put(at('deja')-.05,paper(.6),.3); put(at('lehmann')-.1,paper(.4),.2)
for i in range(7): put(at('siete')-.05+i*.2,pencil(.15),.15)
put(at('no',2)-.1,pencil(.5),.25); put(at('lado')-.6,pencil(.6),.25)
for w in ['nueve','diez','siete']: put(at(w,1 if w!='siete' else 2)-.1,pencil(.45),.25)
put(at('renglon')-.2,pencil(.5),.25); put(at('apunta')-.05,pencil(1.4),.3)
for w in ['dorsal','pie','jugada']: put(at(w)-.1,pencil(.35),.25)
put(at('lee')-.2,pencil(.5),.28)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
