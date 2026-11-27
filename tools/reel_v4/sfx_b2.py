"""Efectos suaves de B2 «Una pregunta del 1 al 10»: aire en los movimientos de cámara, lápiz en el círculo del jueves, los tachones, el 7 y la cuenta, papel en las notas. Sin golpes.
python3 sfx_b2.py b2-rpe/sfx.wav b2-rpe/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('sabado')-.4,1.1,.35),(at('y')-.4,1.2,.4),(at('jueves')-.4,1.0,.3),(at('nueve')-.45,1.1,.3),(at('entreno')-.5,1.3,.4),(at('todos')-.4,1.0,.3),
              (at('el',4)-.4,1.6,.45),(at('cambias')-.45,1.2,.35),(at('cambias',2)-.4,1.0,.3),(at('lunes')-.5,1.3,.35),(at('al',2)-.2,1.6,.35),
              (at('multiplicalo')-.4,1.1,.3),(at('tres')-.45,1.2,.35),(at('apuntalo')-.45,1.6,.4),(at('porque',2),1.4,.4)]:
    put(t,air(d),g)
put(at('jueves')-.05,pencil(.6),.3); put(at('sabado'),pencil(.6),.25)
put(at('cambias')-.3,paper(.4),.25); put(at('cambias',2)-.4,paper(.4),.25)
put(at('nada')-.05,pencil(.4),.35); put(at('tampoco')-.05,pencil(.4),.35)
put(at('costado')-.05,pencil(.5),.35)
for w in ['siete','noventa','seiscientos']: put(at(w)-.05,pencil(.35),.3)
put(at('carga'),pencil(.4),.25)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
