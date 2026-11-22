"""Efectos suaves de D2 «Paró doce y fue su mejor partido»: aire en los movimientos de cámara, lápiz en el −6, la cuenta, los palotes y el tachón del veinte, papel en la hoja. Sin golpes.
python3 sfx_d2.py d2-portera/sfx.wav d2-portera/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('le')-.35,1.0,.3),(at('y')-.35,1.2,.4),(at('temporada')-.4,1.0,.3),(at('sabado')-.4,1.2,.35),(at('vestuario')-.4,1.2,.35),(at('tu')-.4,1.2,.35),
              (at('lo')-.35,1.1,.3),(at('treinta')-.45,1.2,.35),(at('doce',2)-.4,1.1,.3),(at('porcentaje')-.35,1.0,.25),(at('cada')-.35,1.2,.35),(at('lunes')-.35,1.0,.3),
              (at('el',6)-.4,1.2,.35),(at('apuntalo')-.45,1.6,.4),(at('porque')+.05,1.4,.4)]:
    put(t,air(d),g)
put(at('seis')-.05,pencil(.4),.3)
put(at('doce',2)-.05,pencil(.35),.3); put(at('treinta',2)-.05,pencil(.35),.3); put(at('ano')-.05,pencil(.5),.3)
put(at('cuenta')-.3,paper(.5),.25)
for i in range(8): put(at('tiros')+i*.17,pencil(.12),.22)
for i in range(3): put(at('goles')+i*.2,pencil(.12),.2)
put(at('ensenas')-.05,pencil(.5),.25); put(at('mentira')-.05,pencil(.6),.35)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
