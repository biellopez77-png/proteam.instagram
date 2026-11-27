"""Efectos suaves de T01-4-r3 «Gol, palo, árbitro»: aire en los movimientos de cámara, lápiz en los dibujos y las rayas, papel en la ficha y la hoja. Sin golpes.
python3 sfx_T01-4-r3.py T01-4-r3/sfx.wav T01-4-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('es')-.35,1.2,.35),(at('tienes')-.35,.9,.25),(at('le')-.35,1.2,.35),(at('podian')-.4,.9,.25),(at('cuatro')-.45,1.0,.3),(at('no')-.45,1.3,.35),
              (at('apuntas')-.4,1.0,.3),(at('vestuario')-.4,1.0,.3),(at('segunda')-.4,.9,.25),(at('tu',2)-.45,1.2,.3),(at('seis')-.4,.9,.25),(at('campo')-.4,.9,.25),
              (at('descanso')-.4,.9,.25),(at('apuntalo')-.4,1.4,.4),(at('porque'),1.6,.4)]:
    put(t,air(d),g)
put(at('estudio')-.3,paper(.5),.25); put(at('preparala')-.05,paper(.6),.3)
put(at('importante')-.1,pencil(.6),.25); put(at('podian'),pencil(.8),.22); put(at('arbitro',2)+.05,pencil(.5),.25)
for i in range(5): put(at('centrado')-.1+i*.15,pencil(.3),.2)
for i in range(6): put(at('seis')-.15+i*.1,pencil(.35),.16)
put(at('campo')+.05,pencil(.35),.24)
for i in range(9): put(at('rayas')-.15+i*.13,pencil(.12),.24)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
