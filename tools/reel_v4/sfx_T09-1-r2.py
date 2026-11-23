"""Efectos suaves de T09-1-r2 «La amarilla del minuto doce»: aire en los cambios de zona, papel en la libreta y la pizarra, lápiz en los choques, el círculo del gol y las tres líneas. Sin golpes.
python3 sfx_T09-1-r2.py T09-1-r2/sfx.wav T09-1-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('minuto')-.35,.8,.18),(at('central')-.4,.8,.15),(at('y')-.35,.9,.2),(at('empatando')-.4,.8,.15),(at('juvenil')-.45,1.1,.28),
              (at('era')-.35,1.0,.22),(at('una')-.4,1.0,.25),(at('el',3)-.35,1.0,.22),(at('tu',2)-.4,.8,.15),(at('en',3)-.4,1.0,.25),
              (at('y',4)-.35,.9,.2),(at('tu',3)-.4,.9,.2),(at('amarillas')-.35,.8,.15),(at('su',2)-.35,.8,.15),(at('y',6)-.3,.8,.15),
              (at('esa')-.4,1.0,.22),(at('apuntalo')-.4,1.3,.38),(at('porque',4)+.0,1.5,.38)]:
    put(t,air(d),g)
put(at('anoto')-.05,paper(.5),.26); put(at('tu',2)-.1,paper(.5),.2); put(at('en',3)-.1,paper(.6),.2)
put(at('gol')-.25,pencil(.8),.26)
for w in ['siguio','entrando','todas']: put(at(w)-.1,pencil(.5),.24)
for a,b in [(at('antes')-.05,at('quince')+.4),(at('amarillas')-.05,at('minuto',4)+.4),(at('su',2)-.05,at('fuerte')+.4),(at('y',6),at('llega')+.45)]:
    for i in range(8): put(a+i*(b-a)/8,pencil(.12),.16)
put(at('descanso',3)-.2,pencil(.5),.24)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
