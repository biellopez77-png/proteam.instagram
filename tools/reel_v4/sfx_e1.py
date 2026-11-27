"""Efectos suaves de E1 «Cuatro sitios» (ángulo nuevo: «el martes que no puedes ir»): aire en los movimientos, lápiz en los tachones,
la cabeza y las marcas azules, papel al pasar de foto. Sin golpes.
python3 sfx_e1.py e1-cuatro/sfx.wav e1-cuatro/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('pasas')-.45,1.2,.4),(at('cinco')-.45,1.2,.35),(at('das')-.45,1.4,.4),(at('quien')-.4,1.0,.3),(at('que',4)-.35,1.0,.3),
              (at('quien',2)-.35,1.0,.3),(at('y',3)-.35,1.1,.3),(at('martes',2)-.55,1.3,.4),(at('se')-.45,1.2,.35),(at('un',3)-.5,1.6,.4),
              (at('apuntalo')-.45,1.6,.4),(at('porque')+.05,1.6,.4)]:
    put(t,air(d),g)
put(at('no')-.05,pencil(.5),.35); put(at('pasas')-.1,paper(.45),.25)
put(at('das')-.1,pencil(1.4),.22)
for w,n in [('quien',1),('que',4),('quien',2)]: put(at(w,n)-.25,paper(.35),.2)
put(at('martes',2)+.05,pencil(.45),.3)
for w in ['temporada','semana','sesion','partido']: put(at(w)-.1,pencil(.35),.22)
for w in ['pasas','minuto']: put(at(w,2 if w=='pasas' else 1)-.15,pencil(.45),.25)
put(at('entreno',2)-.15,pencil(.45),.25); put(at('sale')-.1,pencil(.4),.3); put(at('funciona')-.1,pencil(.4),.3)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
