"""Efectos suaves de T06-2-r3 «Primer balón: pasos»: aire en los cambios de zona, papel en las notas, lápiz en la flecha al banco, «pivote rival», las rayas y el subrayado. Sin golpes (el golpe es de voz).
python3 sfx_T06-2-r3.py T06-2-r3/sfx.wav T06-2-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('primer')-.3,.7,.14),(at('segundo')-.3,.7,.14),(at('y')-.25,.9,.2),(at('minuto',2)-.35,.7,.14),(at('juvenil')-.3,.9,.2),(at('segunda')-.3,.6,.12),
              (at('llevaba')-.35,1.0,.25),(at('asi')-.3,.7,.14),(at('problema')-.35,.9,.2),(at('y',4)-.25,.7,.14),(at('pero')-.25,.8,.16),
              (at('tu',2)-.35,1.0,.22),(at('lleno')-.2,1.0,.2),(at('y',5)-.2,.9,.2),(at('mirar')+.1,1.4,.3),(at('antes',2)-.35,1.4,.32),
              (at('entrara')-.35,1.0,.25),(at('apuntalo')-.35,1.2,.35),(at('para')-.05,1.4,.36)]:
    put(t,air(d),g)
put(at('problema')+.05,paper(.4),.2); put(at('y',4)+.0,paper(.35),.16); put(at('pero')+.3,paper(.5),.18)
put(at('sentar')-.2,pencil(.6),.18)
put(at('pivote')-.05,pencil(1.0),.3)
a,b=at('y',6),at('apunte')+.5
for i in range(5): put(a+i*(b-a)/5,pencil(.2),.3)
put(at('una',2)-.05,pencil(.5),.25); put(at('entrara')+.1,pencil(.7),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
