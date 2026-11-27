"""Efectos suaves de T09-1-r3 «Tres veces antes del quince»: aire en los cambios de zona, lápiz en las rayas y en las flechas, papel al dejar la hoja en el banquillo. Sin golpes.
python3 sfx_T09-1-r3.py T09-1-r3/sfx.wav T09-1-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('hoja')-.2,.9,.15),(at('minuto')-.4,.8,.18),(at('y')-.35,.9,.2),(at('futbol')-.45,1.1,.28),(at('y',2)-.4,1.0,.22),
              (at('su')-.35,.9,.18),(at('una',2)-.35,.8,.15),(at('la',5)-.35,.8,.15),(at('y',3)-.35,.8,.15),(at('levantandote')-.15,1.3,.22),
              (at('te')-.4,1.0,.22),(at('pero')-.25,.9,.18),(at('una',4)-.35,.8,.15),(at('espalda',2)-.4,.8,.15),(at('a',4)-.35,.8,.15),
              (at('jugador')-.4,1.0,.2),(at('apuntalo')-.4,1.3,.38),(at('antes',2)+.0,1.5,.38)]:
    put(t,air(d),g)
put(at('cuarta')-.05,pencil(.55),.28)
for k in range(3): put(at('tres',2)-.05+k*.35,pencil(.45),.24)
put(at('por')-.1,paper(.6),.26)
put(at('raya')-.15,pencil(.3),.2)
for w,n in [('espalda',2),('balon',1),('salida',1)]:
    s=at(w,2 if w=='espalda' else 1)
    for k in range({'espalda':3,'balon':1,'salida':2}[w]): put(s+.2+k*.18,pencil(.14),.2)
put(at('raya',2)-.2,pencil(.55),.22)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
