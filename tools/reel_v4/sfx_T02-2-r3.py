"""Efectos suaves de T02-2-r3 «Viernes, noventa minutos»: aire en los cambios de zona, lápiz en las flechas, la línea de 2 días y la de 72 h, papel en el sello, la etiqueta, las fichas y el bloque que se mueve. Sin golpes.
python3 sfx_T02-2-r3.py T02-2-r3/sfx.wav T02-2-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
CUT1=at('problema')-.33; CUT2=at('ordenalo')-.2
for t,d,g in [(at('a')-.3,1.1,.28),(at('todavia')-.25,.9,.2),(at('el')-.3,1.0,.28),(at('tu')-.3,1.1,.28),(at('el',3)-.25,.9,.2),
              (at('pusiste')-.25,.8,.18),(at('salio',2)-.25,.8,.18),(at('miercoles')-.35,.8,.2),(at('viernes',2)-.3,.8,.2),
              (at('y',3)-.3,1.1,.28),(at('y',4)-.25,.8,.18),(CUT1-.1,1.0,.22),(at('en')-.25,.9,.2),(at('en',2)-.3,1.0,.25),
              (CUT2-.1,1.1,.28),(at('martes',3)-.25,.8,.18),(at('miercoles',2)-.25,.8,.18),(at('viernes',3)-.25,.8,.18),
              (at('corto')-.1,1.1,.28),(at('app')-.3,1.2,.3),(at('noventa',2)-.3,1.3,.3)]:
    put(t,air(d),g)
put(at('salio')-.2,paper(.45),.25); put(at('fuerte')-.3,paper(.45),.22); put(at('en')-.4,paper(.45),.2); put(at('en',2)-.1,paper(.4),.18)
put(at('ordenalo')+.1,paper(.6),.2)
put(at('a')+.35,pencil(.6),.18); put(at('todavia')+.05,pencil(.6),.18); put(at('repitiendo')+.3,pencil(.6),.18)
put(at('dos',2)-.1,pencil(.6),.22); put(at('corregir')-.1,pencil(1.6),.25); put(at('miercoles')-.05,pencil(.5),.2); put(at('viernes',2)-.05,pencil(.5),.2)
put(at('setenta')-.15,pencil(.7),.22)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
