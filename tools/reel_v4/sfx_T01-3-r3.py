"""Efectos suaves de T01-3-r3 «Primera posesión»: aire en los movimientos de cámara, roce de papel en las hojas, rotulador en la pizarra y la libreta. Sin golpes.
python3 sfx_T01-3-r3.py T01-3-r3/sfx.wav T01-3-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('perdida')-.4,1.0,.3),(at('contra')-.35,1.2,.35),(at('dibujado')-.35,1.0,.3),(at('rebobina')-.35,1.3,.4),(at('parece')-.35,1.0,.3),
              (at('cinco')-.5,1.0,.3),(at('hoja')-.45,1.0,.3),(at('base')-.45,1.0,.3),(at('uno')-.35,.9,.25),(at('cuando')-.35,1.1,.3),(at('y',3)-.4,1.2,.35),
              (at('sales')-.4,1.0,.3),(at('y',4)-.35,1.2,.4),(at('en',2)-.5,1.4,.35),(at('elige')-.4,1.0,.3),(at('respuesta',2)-.45,1.0,.3),
              (at('primera',2)-.35,1.2,.35),(at('apuntalo')-.4,1.4,.4),(at('porque'),1.6,.4)]:
    put(t,air(d),g)
put(at('segun')-.2,paper(.5),.25); put(at('hoja')-.35,paper(.45),.25)
for i in range(5): put(at('empiezas')+.05+i*.13,pencil(.2),.22)
for w in ['uno','dos','tres']: put(at(w)-.15,pencil(.6),.28)
put(at('trampa',2)-.1,pencil(.4),.25)
for i in range(8): put(at('sales')+i*.18,pencil(.3),.2)
put(at('elige')-.05,pencil(.7),.3); put(at('balon')-.2,pencil(.6),.3)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
