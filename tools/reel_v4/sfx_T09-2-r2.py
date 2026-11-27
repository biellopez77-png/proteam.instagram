"""Efectos suaves de T09-2-r2 «El de siempre»: aire en los cambios de zona, papel en los carteles y los petos, lápiz en las notas, los cambios escritos y el círculo del 14. Sin golpes.
python3 sfx_T09-2-r2.py T09-2-r2/sfx.wav T09-2-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('primer')-.35,.8,.2),(at('dieciseis')-.35,.7,.15),(at('como')-.35,.9,.22),(at('juvenil')-.5,1.1,.3),(at('el',3)-.4,1.1,.28),
              (at('pero')-.35,1.0,.25),(at('y',4)-.35,1.0,.25),(at('tres',2)-.3,.9,.2),(at('no')-.4,1.1,.28),(at('y',6)-.35,.8,.15),
              (at('primero')-.35,.8,.18),(at('y',7)-.3,1.0,.25),(at('apuntalo')-.4,1.3,.38),(at('porque')+.0,1.5,.38)]:
    put(t,air(d),g)
put(at('primer')-.1,paper(.5),.22)
for k in range(3): put(at('como')-.25+.35*k,paper(.35),.18)
for k,w in enumerate([('minuto',2),('marcador',1),('mano',2)]): put(at(*w)-.1,pencil(.4),.2)
put(at('y',4)-.1,paper(.5),.2)
a,b=at('en',4)+.15,at('minuto',3)+.4
for i in range(14): put(a+i*(b-a)/14,pencil(.12),.17)
put(at('catorce',2)-.1,pencil(.5),.24)
put(at('hoja')-.2,paper(.8),.22)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
