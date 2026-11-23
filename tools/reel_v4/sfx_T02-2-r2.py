"""Efectos suaves de T02-2-r2 «Dos relojes»: aire en los cambios de zona, lápiz en el hilo, las 56 h, la cadena, el subrayado y la línea azul, papel en la etiqueta, la libreta y la ficha. Sin golpes.
python3 sfx_T02-2-r2.py T02-2-r2/sfx.wav T02-2-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
def aft(w,t0):
    for x in W:
        if x[0]==w and x[1]>=t0: return x[1]
CUT1=at('la')-.12; CUT2=at('asi',2)-.15
for t,d,g in [(at('relojes')+.2,1.0,.25),(at('entre')-.3,1.1,.3),(at('y',2)-.3,.9,.2),(at('el')-.25,.9,.2),(at('el',2)-.2,.9,.2),
              (at('en')-.35,1.2,.3),(at('porque')-.3,.9,.2),(at('y',4)-.25,.9,.2),(at('pero')-.3,1.1,.3),(at('asi')-.3,1.0,.25),
              (at('recuperar')-.3,.9,.2),(at('una')-.35,1.1,.3),(CUT1-.1,1.0,.25),(at('domingo')-.25,.9,.2),(at('ahora')-.4,1.2,.3),
              (at('en',3)-.3,1.0,.25),(CUT2-.1,1.1,.3),(at('antes')-.25,.9,.2),(at('despues',2)-.25,.9,.2),(aft('el',41)-.2,.9,.2),
              (at('corto',2)-.15,1.1,.3),(at('apuntalo')-.15,1.2,.35),(at('porque',2)-.05,1.3,.3)]:
    put(t,air(d),g)
put(at('error')-.25,paper(.45),.22); put(at('en',3)-.2,paper(.45),.2); put(CUT1+.1,paper(.5),.22); put(at('tercer')-.15,paper(.4),.18)
put(at('entre')-.05,pencil(1.0),.2); put(at('cincuenta')-.05,pencil(.8),.25); put(at('una')-.05,pencil(1.2),.22)
put(at('coche')-.2,pencil(.6),.25); put(at('coche')+.25,pencil(.5),.22); put(at('cuenta')-.1,pencil(.7),.22)
put(at('alargas')-.1,air(.9,300,2600),.22); put(at('duro')-.25,paper(.4),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
