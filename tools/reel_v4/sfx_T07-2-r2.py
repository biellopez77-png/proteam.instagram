"""Efectos suaves de T07-2-r2 «Seis en la fila»: aire en los cambios de zona, lápiz en el tiro, las marcas de gol, el rótulo, el cordón, la cuenta, los campos y «Gol = pase + tiro»; papel en la hoja del martes. Sin golpes.
python3 sfx_T07-2-r2.py T07-2-r2/sfx.wav T07-2-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('defensa')-.3,.7,.12),(at('la')-.3,.8,.14),(at('y')-.35,1.0,.2),(at('alevin')-.4,1.0,.2),(at('seis')-.35,.9,.18),(at('los')-.3,.7,.12),
              (at('atan')-.3,.7,.12),(at('cada')-.3,.7,.12),(at('siempre')-.3,.8,.14),(at('y',4)-.2,.7,.12),(at('pero')-.3,.9,.16),
              (at('lo',4)-.4,1.0,.2),(at('y',6)-.3,1.0,.18),(at('haz')-.2,1.1,.24),(at('porterias')-.3,.9,.16),(at('tu',2)-.3,.9,.16),
              (at('apuntalo')-.45,1.2,.3),(at('porque')-.15,1.4,.3)]:
    put(t,air(d),g)
put(at('manda'),pencil(.7),.25)
put(at('martes')-.1,paper(.5),.22)
for i in range(6): put(at('martes')+.15+i*.2,pencil(.18),.22)
put(at('alevin')+.3,pencil(.8),.25)
put(at('atan'),pencil(.6),.2)
for i in range(2): put(at('cada')+.2+i*.3,pencil(.25),.25)
put(at('sesion'),paper(.4),.16)
for i in range(3): put(at('cada',2)+.1+i*.25,pencil(.25),.22)
put(at('haz')+.1,pencil(.8),.2)
put(at('gol')+.3,pencil(.7),.25)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
