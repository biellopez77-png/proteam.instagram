"""Efectos suaves de T02-2-r1 «Nadie llega»: aire en los cambios de zona, papel en la foto, la libreta y la ficha, lápiz/rotulador en las flechas, ACTITUD, el subrayado, el boli y las 56 h. Sin golpes.
python3 sfx_T02-2-r1.py T02-2-r1/sfx.wav T02-2-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
def aft(w,t0):
    for x in W:
        if x[0]==w and x[1]>=t0: return x[1]
for t,d,g in [(at('y')-.35,1.1,.3),(at('ni')-.3,.9,.2),(at('es')-.35,1.1,.3),(at('cuatro')-.3,1.0,.25),(at('repites')-.4,1.2,.3),(at('piensas')-.3,.9,.2),
              (at('lo',3)-.35,1.1,.3),(at('lo',4)-.3,1.0,.3),(at('veinte')-.3,.9,.2),(at('en',2)-.25,.9,.2),(aft('del',26.5)-.3,1.1,.3),(aft('y',29.6)-.35,1.1,.3),
              (at('cambia')-.4,1.2,.3),(aft('el',36.1)-.25,.9,.2),(aft('el',40)-.2,.9,.2),(aft('y',42)-.2,.9,.2),(at('corto')-.15,1.1,.3),
              (at('apuntalo')-.15,1.2,.35),(at('porque')-.05,1.3,.3)]:
    put(t,air(d),g)
put(at('es')-.1,paper(.4),.22); put(at('lo',4)+.1,paper(.5),.25); put(aft('y',29.6),paper(.4),.2)
for w in ['repites','paras','explicas']:
    s=at(w)-.1
    for i in range(3): put(s+i*.13,pencil(.3),.22)
s=at('actitud')-.1
for i in range(5): put(s+i*.12,pencil(.14),.22)
put(at('no')-.05,pencil(.5),.2); put(at('cuatro')-.05,pencil(.6),.2); put(at('veinte')-.05,pencil(.7),.3)
s=at('mayusculas')-.05
for i in range(6): put(s+i*.13,pencil(.14),.25)
put(aft('del',26.5)+.3,pencil(1.2),.22); put(at('cincuenta')-.1,pencil(.7),.25)
put(at('orden')-.15,air(.8,300,2600),.3)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
