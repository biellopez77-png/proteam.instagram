"""Efectos suaves de T06-2-r2 «El peto rojo»: aire en los cambios de zona, lápiz en el 0′, las flechas, la jugada, el 10′ y el subrayado; papel en la nota y la tarjeta; roce de tela al cambiar el peto. Sin golpes (el golpe es de voz).
python3 sfx_T06-2-r2.py T06-2-r2/sfx.wav T06-2-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('el',2)-.3,.7,.14),(at('y')-.3,.7,.14),(at('sin')-.3,.7,.14),(at('cadete')-.45,1.1,.25),(at('cinco')-.3,.7,.12),(at('los',2)-.35,.7,.14),
              (at('el',4)-.4,.8,.16),(at('ataca')-.4,.9,.2),(at('pero')-.35,.9,.2),(at('asi')-.4,1.1,.25),(at('entra')-.3,.8,.16),(at('y',3)-.35,.9,.2),
              (at('tu',2)-.4,.9,.2),(at('cada')-.4,.9,.2),(at('con',3)-.4,.8,.18),(at('sola'),1.3,.28),(at('apuntalo')-.45,1.2,.32),(at('para',3)-.15,1.4,.34)]:
    put(t,air(d),g)
put(at('sin'),pencil(.7),.25)
for i in range(3): put(at('los',2)+.3+i*.9,pencil(.8),.2)
put(at('ataca'),pencil(1.2),.22)
put(at('confirmas'),paper(.45),.2)
put(at('cambia')-.05,paper(.8),.22)
put(at('diez'),pencil(.7),.28); put(at('una',2),pencil(.6),.28); put(at('sola')+.4,pencil(.7),.18)
put(at('con',3)-.1,paper(.4),.16)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
