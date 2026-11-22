"""Efectos suaves de T01-4-r2 «95 contra 37»: aire en los movimientos de cámara, lápiz en los dibujos y las rayas, papel en la ficha y la hoja. Sin golpes.
python3 sfx_T01-4-r2.py T01-4-r2/sfx.wav T01-4-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('los')-.35,.9,.25),(at('centros')-.4,.9,.25),(at('es')-.35,1.2,.35),(at('la')-.35,1.0,.3),(at('problema')-.5,1.4,.4),(at('nunca')-.4,.9,.25),
              (at('es',3)-.35,1.1,.35),(at('lo',2)-.35,1.0,.3),(at('y',4)-.35,.9,.2),(at('descanso',2)-.5,1.2,.35),(at('dos',2)-.4,.9,.25),(at('una',2)-.4,.9,.25),
              (at('tiros',2)-.4,.9,.25),(at('apuntalo')-.4,1.4,.4),(at('porque'),1.6,.4)]:
    put(t,air(d),g)
put(at('tiros')-.05,pencil(.5),.25); put(at('centros')+.1,pencil(.5),.25)
put(at('estudio')-.25,paper(.5),.25); put(at('pues')-.05,paper(.6),.3)
put(at('problema')+.2,pencil(.7),.28); put(at('tiro')-.1,pencil(.4),.25); put(at('palo')-.25,pencil(.6),.28)
for i in range(5): put(at('centran')-.15+i*.2,pencil(.35),.2)
for w in ['casillas','perdidas']: put(at(w)-.25,pencil(.7),.25)
for t0 in [at('raya')-.1+i*.26 for i in range(5)]+[at('cada',3)+.25,at('cada',3)+.55,at('tiros',2)-.6,at('tiros',2)-.4,at('tiros',2)-.2]: put(t0,pencil(.2),.24)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
