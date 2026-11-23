"""Efectos suaves de T01-4-r1 «Seis de diez»: aire en los movimientos de cámara, lápiz en las casillas y las rayas, papel en la ficha y en la hoja. Sin golpes.
python3 sfx_T01-4-r1.py T01-4-r1/sfx.wav T01-4-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('eso')-.35,.9,.25),(at('ocho')-.35,.9,.25),(at('y')-.35,.9,.25),(at('un',2)-.45,1.3,.38),(at('un',3)-.35,.9,.25),
              (at('con')-.45,1.4,.4),(at('quince')-.35,.9,.25),(at('lo')-.45,1.3,.35),(at('es',2)-.35,.9,.2),(at('recuerdas')-.45,1.3,.35),
              (at('la')-.35,1.0,.28),(at('hoy')-.5,1.4,.38),(at('padre')-.35,.9,.25),(at('cinco')-.4,.9,.25),(at('tu')-.5,1.5,.4),
              (at('una',2)-.35,.9,.25),(at('en',4)-.35,.9,.25),(at('apuntalo')-.4,1.4,.4),(at('porque'),1.6,.4)]:
    put(t,air(d),g)
put(at('estudio')-.25,paper(.5),.25); put(at('seis',2)-.2,paper(.6),.3)
put(at('vestuario')-.05,air(.8,300,2600),.3)
for i in range(4): put(at('saber')-.2+i*.28,pencil(.3),.2)
for i in range(4): put(at('banda')+.2+i*.55,pencil(.5),.2)
for i in range(6): put(at('seis',2)+i*.12,pencil(.4),.22)
for w in ['perdidas','centros','tiros','balon','portero']: put(at(w)-.15,pencil(.35),.2)
put(at('banda',2)-.15,pencil(.35),.2)
c0=at('raya')-.05; c1=at('en',4)-.35
for k in range(7): put(c0+(c1-c0)*k/7,pencil(),.4)
o0=at('en',4)-.05; o1=at('cuentas')-.35
for k in range(12): put(o0+(o1-o0)*k/12,pencil(.12),.3)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
