"""Efectos suaves de T01-3-r1 «Minuto cuarenta y seis»: aire en los cambios de zona, papel en el marcador y la hoja, lápiz en flechas, lista y libreta. Sin golpes.
python3 sfx_T01-3-r1.py T01-3-r1/sfx.wav T01-3-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('seis')-.3,.9,.2),(at('gol')-.25,1.1,.35),(at('banda')-.35,.9,.2),(at('estaba')-.5,1.2,.35),(at('pizarra')-.3,.9,.2),
              (at('rebobina')-.45,1.3,.35),(at('hasta')-.35,.9,.2),(at('pero')-.45,1.2,.3),(at('agua')-.4,.9,.2),(at('tobillo')-.4,.9,.2),(at('delegado')-.4,.9,.2),
              (at('nueve')-.4,.9,.2),(at('y',3)-.25,1.0,.2),(at('sales')-.45,1.2,.35),(at('cerrando')-.35,.9,.2),(at('como')-.35,.9,.2),
              (at('tres')-.4,.9,.2),(at('despues')-.45,1.0,.3),(at('lo')-.45,1.0,.3),(at('martes')-.2,1.1,.3),(at('apuntalo')-.05,1.2,.35),
              (at('porque')-.1,1.1,.3),(at('solo')-.35,1.4,.4)]:
    put(t,air(d),g)
put(at('gol')-.1,paper(.35),.25)
put(at('hasta')-.4,paper(.5),.25)
f0=at('cuando')+.08; f1=at('todo')+.2
for i in range(8): put(f0+(f1-f0)*i/8,pencil(.3),.28)
for i in range(9): put(f0+.1+(f1-f0)*i/9,pencil(.14),.18)
put(at('banda',2),pencil(.6),.3)
put(at('idea')-.1,pencil(.7),.32); put(at('dos')-.05,pencil(.15),.25); put(at('nombres'),pencil(.15),.25)
put(at('martes')-.15,pencil(.5),.3)
for i in range(8): put(at('lo')-.1+i*.09,paper(.2),.12)
put(at('banda',3)-.1,pencil(.4),.28)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
