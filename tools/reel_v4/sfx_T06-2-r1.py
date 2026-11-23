"""Efectos suaves de T06-2-r1 «Dieciséis en la lista»: aire en los cambios de zona, lápiz en la raya del 17, el círculo, la interrogación,
la frase de la tarjeta y las flechas; papel en las notas; goma al borrar. Sin golpes.
python3 sfx_T06-2-r1.py T06-2-r1/sfx.wav T06-2-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('diecisiete')-.3,.7,.14),(at('nadie')-.3,.9,.2),(at('juvenil')-.3,.9,.2),(at('segunda')-.25,.6,.12),(at('primera')-.3,1.0,.22),
              (at('sabado')-.3,.7,.14),(at('al')-.35,.9,.2),(at('despues')-.3,.9,.2),(at('tu')-.35,.9,.2),(at('el',3)-.2,.7,.14),(at('y',3)-.2,.8,.16),
              (at('alta')+.1,1.4,.3),(at('dile')-.35,1.4,.32),(at('el',4)-.3,.8,.18),(at('dos',2)-.3,1.2,.28),(at('apuntalo')-.35,1.2,.35),(at('para',2)-.05,1.4,.36)]:
    put(t,air(d),g)
put(at('viene')-.1,pencil(.55),.28)
put(at('segunda')+.05,pencil(.7),.2)
put(at('preguntaba')-.15,pencil(.35),.22)
put(at('dejo')-.1,paper(.9),.14)
put(at('tu')+.1,paper(.4),.2); put(at('el',3)+.1,paper(.35),.16)
put(at('dile')+.15,pencil(1.6),.28)
put(at('una',2)-.05,pencil(.5),.25); put(at('entrena'),pencil(.6),.18)
put(at('dos',2)+.4,pencil(.9),.18); put(at('despues',2)+.3,pencil(.6),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
