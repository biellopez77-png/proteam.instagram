"""Guiones de los Reels retro (CH 14 → CH 00). Cada bloque = (escena, voz, duración mínima).
La duración de cada bloque se ajusta a lo que dura la voz, así nunca se solapan.
  python3 episodios.py  -> reels/e{CH}.json (para sonido.py y retro_video.py)"""
import json, sys, os, tempfile
sys.path.insert(0, '/home/claude/tts'); import kok, soundfile as sf
VEL = 1.0
_cache = {}
def dur(txt):
    if txt not in _cache:
        p = tempfile.mktemp(suffix='.wav'); kok.say(txt, 29, p, VEL); a, sr = sf.read(p); os.remove(p); _cache[txt] = len(a) / sr
    return _cache[txt]

OFERTA = 'Seis meses gratis para tu primer equipo. Solo hasta el veintisiete.'
def cierre(voz=OFERTA): return ({'type': 'cierre'}, voz, 5.5)
ST = ({'type': 'static'}, None, .6)
OFF = ({'type': 'off'}, None, .5)

E = {
 14: [ST,
      ({'type': 'win95', 'dialog': 'Error 404:<br>planificación<br>no encontrada.', 'dialogAt': 1.2}, '¿Sigues planificando la temporada en un Excel de dos mil tres?', 3.2),
      ({'type': 'blue', 'lines': [[0, 'UN EXCEL'], [.5, 'NO ES'], [.9, 'UN PLAN.', 190, 900]]}, 'Un Excel no es un plan. Es un archivo que nadie abre.', 3),
      OFF,
      ({'type': 'future', 'sub': 'La semana, planificada.', 'shots': [[0, 'mo-plan', 'Planifica el microciclo.', .05], [2.4, 'mo-week', 'Volumen y días de trabajo.', .1]]},
       'En ProTim planificas el microciclo y ves el volumen y los días de trabajo de cada semana.', 4.6),
      cierre()],
 13: [ST,
      ({'type': 'nokia', 'counter': [1, 47, 22, 'AUDIOS<br>NUEVOS'], 'lines': [[1.4, '«¿A QUÉ HORA<br>ES EL SÁBADO?»', 560, 60], [2.4, '«¿Y DÓNDE<br>JUGAMOS?»', 800, 60]]}, 'Cuarenta y siete audios de guasap. Y aún no sabes quién viene el sábado.', 3.5),
      ({'type': 'blue', 'lines': [[0, '47 AUDIOS', 150], [.5, 'NO SON UNA', 120, 790], [.9, 'CONVOCATORIA.', 112, 920]]}, 'Eso no es una convocatoria. Es ruido.', 2.6),
      OFF,
      ({'type': 'future', 'sub': 'Convoca en un toque.', 'shots': [[0, 'fA', 'Convocados y titulares.', .1], [2.2, 'grid-0', 'La lista, de un vistazo.', .3]]},
       'En ProTim haces la convocatoria: convocados y titulares, en una sola pantalla.', 4.2),
      cierre()],
 12: [ST,
      ({'type': 'teletext', 'pag': 101, 'title': 'RESULTADOS', 'lines': [[.2, 'RIBES ....... 26', '#fff'], [.6, 'RIVAL ....... 17', '#fff'], [1.2, '¿GOLEADORES? ....... ???', '#ff0'], [1.8, '¿MINUTOS? ..... NI IDEA', '#f0f']], 'blink': 'SIGUE EN LA LIBRETA'},
       'Has ganado de nueve. ¿Quién marcó? ¿Cuántos minutos jugó cada uno? Ni idea.', 3.6),
      ({'type': 'blue', 'lines': [[0, 'TU LIBRETA'], [.5, 'NO VIO EL'], [.9, 'PARTIDO.', 190, 900]]}, 'Tu libreta no vio el partido.', 2.2),
      OFF,
      ({'type': 'future', 'sub': 'El partido, en directo.', 'shots': [[0, 'reg-1', 'Jugador y acción.', .45], [1.6, 'reg-3', 'Dónde va el tiro.', .5], [3.0, 'reg-4', '¿Gol o parada?', .55], [4.4, 'cro-0', 'La crónica, hecha.', .1]]},
       'ProTim registra el partido en directo: jugador, acción, dónde va el tiro y si es gol o parada. Al acabar, la crónica ya está hecha.', 6),
      cierre()],
 11: [ST,
      ({'type': 'vhs', 'mode': '◀◀ REBOBINANDO', 'lines': [[.3, '¿CUÁNDO SE', 120, 620], [.8, 'ROMPIÓ EL', 120, 760], [1.3, 'PARTIDO?', 150, 900]]}, '¿Cuándo se rompió el partido? Rebobinas la cinta y sigues sin saberlo.', 3.6),
      ({'type': 'blue', 'lines': [[0, 'NI IDEA.', 220, 760]]}, 'Ni idea.', 1.4),
      OFF,
      ({'type': 'future', 'sub': 'Lo ves en un segundo.', 'shots': [[0, 'res-0', 'Marcador por partes.', .18], [2.6, 'res-0', 'Eficacia y paradas.', .55]]},
       'En ProTim tienes el marcador por partes, los últimos diez minutos y la eficacia, frente al rival.', 5),
      cierre()],
 10: [ST,  # montaje sin voz, al ritmo
      ({'type': 'nokia', 'lines': [[0, 'DEJA DE', 360, 110], [.3, 'ENTRENAR', 520, 110]]}, None, 1.0),
      ({'type': 'teletext', 'pag': 199, 'title': 'COMO EN', 'lines': [[0, 'LOS 90.', '#ff0']], 'size': 200}, None, 1.0),
      ({'type': 'win95', 'dialog': 'Fin del<br>siglo XX.', 'dialogAt': 0}, None, .9),
      ({'type': 'vhs', 'mode': '▶▶ AVANZANDO', 'lines': [[0, '2026.', 260, 700]]}, None, 1.0),
      OFF,
      ({'type': 'future', 'title': 'Planifica.', 'tsize': 150, 'shots': [[0, 'mo-plan', None, .05]]}, None, .9),
      ({'type': 'future', 'title': 'Convoca.', 'tsize': 150, 'shots': [[0, 'fA', None, .1]]}, None, .9),
      ({'type': 'future', 'title': 'Registra.', 'tsize': 150, 'shots': [[0, 'reg-1', None, .45]]}, None, .9),
      ({'type': 'future', 'title': 'Analiza.', 'tsize': 150, 'shots': [[0, 'res-0', None, .2]]}, None, .9),
      ({'type': 'future', 'title': 'Controla.', 'tsize': 150, 'shots': [[0, 'fF', None, .02]]}, None, .9),
      ({'type': 'future', 'title': 'ProTeam.', 'sub': 'Bienvenido a 2026.', 'tsize': 150, 'shots': [[0, 'mo-home', None, 0]]}, None, 1.4),
      cierre()],
 9: [ST,
      ({'type': 'lcd', 'top': 'CASIO · CARGA', 'lines': [[.2, '52 x 8'], [1.4, '= ?']], 'sub': '¿Cuánto ha jugado?<br>¿Seguro?', 'subAt': 2.2},
       '¿Cuánto ha jugado? ¿Y a qué esfuerzo? Cincuenta y dos por ocho. Saca la calculadora.', 3.8),
      ({'type': 'blue', 'lines': [[0, 'LA CARGA'], [.5, 'NO SE'], [.9, 'ADIVINA.', 190, 900]]}, 'La carga no se adivina.', 2),
      OFF,
      ({'type': 'future', 'sub': 'Minutos × RPE.', 'shots': [[0, 'fF', 'RPE y carga del partido.', .02], [2.6, 'fF', 'Jugador a jugador.', .3]]},
       'ProTim calcula la carga de cada jugador: minutos por esfuerzo, igual que en los entrenos.', 4.8),
      cierre()],
 8: [ST,
      ({'type': 'lcd', 'top': 'CRONO · 1995', 'lines': [[.2, '00:30.27'], [1.2, 'LAP 3']], 'sub': 'Tus tests físicos,<br>en un papel.', 'subAt': 1.8},
       'Tus tests físicos: un cronómetro de mil novecientos noventa y cinco y un papel que se pierde.', 3.8),
      ({'type': 'blue', 'lines': [[0, 'EL PAPEL'], [.5, 'SE MOJA.', 190, 790]]}, 'El papel se moja. Y se pierde.', 2),
      OFF,
      ({'type': 'future', 'sub': 'Preparación física.', 'shots': [[0, 'mo-tests', 'Tests programados.', .05], [2.4, 'mo-routines', 'Rutinas y ejercicios.', .05]]},
       'En ProTim programas los tests físicos y las rutinas de preparación física del equipo.', 4.6),
      cierre()],
 7: [ST,
      ({'type': 'teletext', 'pag': 300, 'title': 'PROGRAMACIÓN', 'band': '#a00', 'lines': [[.2, 'LUN ... ¿?', '#fff'], [.5, 'MAR ... LO DE SIEMPRE', '#fff'], [.8, 'JUE ... YA VEREMOS', '#0ff'], [1.1, 'SÁB ... PARTIDO (¿HORA?)', '#ff0']]},
       'Lunes, lo de siempre. Jueves, ya veremos. Así no se planifica una semana.', 3.6),
      ({'type': 'blue', 'lines': [[0, 'LA SEMANA'], [.5, 'NO SE'], [.9, 'PLANIFICA'], [1.3, 'SOLA.', 190, 1040]]}, 'La semana no se planifica sola.', 2.4),
      OFF,
      ({'type': 'future', 'sub': 'Todo, en el calendario.', 'shots': [[0, 'mo-week', 'Tu semana.', .1], [2.2, 'mo-cal', 'El mes entero.', .15]]},
       'En ProTim planificas la semana y la ves en el calendario del equipo, mes a mes.', 4.4),
      cierre()],
 6: [ST,  # sin voz: 1998 contra hoy
      ({'type': 'split', 'left': ['3 EXCELS', 'UNA LIBRETA', '47 AUDIOS', 'EL DOMINGO, PERDIDO'], 'right': ['1 APP', 'LA SEMANA, HECHA', 'CONVOCATORIA, LISTA', 'EL DOMINGO, TUYO']}, None, 4.2),
      ({'type': 'blue', 'lines': [[0, 'TU DOMINGO'], [.5, 'NO ES DEL'], [.9, 'EXCEL.', 190, 900]]}, None, 2),
      OFF,
      ({'type': 'future', 'sub': 'Recupera tu domingo.', 'shots': [[0, 'mo-home', 'Tu día, en orden.', 0]]}, None, 2.6),
      cierre(None)],
 5: [ST,
      ({'type': 'nokia', 'lines': [[0, 'GRUPO<br>«INFANTIL A»', 340, 72], [.8, 'GRUPO<br>«PADRES INF A»', 600, 60], [1.4, 'GRUPO<br>«STAFF»', 840, 60]]}, '¿Cuántos grupos de guasap tiene tu equipo? ¿Tres? ¿Cuatro?', 3.2),
      ({'type': 'blue', 'lines': [[0, 'TU EQUIPO'], [.5, 'NO CABE EN'], [.9, 'UN GRUPO.', 170, 900]]}, 'Tu equipo no cabe en un grupo de guasap.', 2.4),
      OFF,
      ({'type': 'future', 'sub': 'Tu día, en orden.', 'shots': [[0, 'mo-home', 'Qué toca hoy.', 0], [2.2, 'mo-cal', 'Y lo que viene.', .15]]},
       'En ProTim abres la app y ves qué toca hoy, lo que tienes pendiente y lo que viene.', 4.4),
      cierre()],
 4: [ST,
      ({'type': 'vhs', 'mode': '▶▶ AVANZANDO', 'lines': [[.2, 'DIC', 130, 560], [.6, 'ENE', 130, 700], [1.0, 'FEB', 130, 840], [1.4, 'MAR', 130, 980], [1.8, 'ABR', 130, 1120], [2.2, 'MAY', 130, 1260]]},
       'Diciembre, enero, febrero, marzo, abril, mayo.', 3.4),
      ({'type': 'blue', 'lines': [[0, '6 MESES.', 190, 600], [.6, 'UNA', 150, 820], [.9, 'TEMPORADA.', 150, 960]]}, 'Seis meses. Casi una temporada entera.', 2.6),
      OFF,
      ({'type': 'future', 'sub': 'Toda la temporada.', 'shots': [[0, 'mo-plan', 'De diciembre a mayo.', .05]]},
       'Si creas tu primer equipo antes del veintisiete, la tienes en ProTim. Gratis.', 4),
      cierre('Seis meses gratis. Solo hasta el veintisiete.')],
 3: [ST,
      ({'type': 'vhs', 'mode': '◀◀ REBOBINA', 'lines': [[.2, '◀◀', 260, 600], [.6, 'EXCEL.', 120, 900], [.9, 'LIBRETA.', 120, 1030], [1.2, 'AUDIOS.', 120, 1160]]}, 'Puedes rebobinar. Excel, libreta, audios.', 3),
      ({'type': 'vhs', 'mode': '▶▶ O AVANZA', 'bg': TVBLUE if False else '#1f3cff', 'lines': [[.2, '▶▶', 260, 600], [.6, 'O AVANZAR.', 130, 900]]}, 'O avanzar.', 1.6),
      OFF,
      ({'type': 'future', 'title': 'ProTeam.', 'sub': 'Avanza.', 'shots': [[0, 'mo-week', None, .1], [1.0, 'reg-1', None, .45], [2.0, 'res-0', None, .2]]}, 'Quedan tres días.', 3),
      cierre()],
 2: [ST,
      ({'type': 'teletext', 'pag': 888, 'title': 'PREGUNTAS', 'size': 60, 'lines': [[.3, '¿TARJETA? ......... NO', '#fff'], [1.6, '¿DEPORTES? FÚTBOL,', '#0ff'], [1.6, '  BALONCESTO, BALONMANO', '#0ff'], [3.6, '¿QUIÉN? TU PRIMER EQUIPO', '#ff0'], [3.6, '  (CUENTA NUEVA)', '#ff0'], [5.6, '¿HASTA? VIE 27 · 23:59', '#f0f']]},
       '¿Hace falta tarjeta? No. ¿Deportes? Fútbol, baloncesto y balonmano. ¿Para quién? Para el primer equipo de una cuenta nueva. ¿Hasta cuándo? El viernes veintisiete, a medianoche.', 8),
      ({'type': 'blue', 'lines': [[0, 'SIN TARJETA.'], [.6, 'SIN', 150, 790], [.9, 'EXCUSAS.', 150, 930]]}, 'Sin tarjeta. Sin excusas.', 2.2),
      cierre()],
 1: [ST,
      ({'type': 'blue', 'mode': 'REC ●', 'lines': [[0, 'MAÑANA', 170, 560], [.5, 'SE CORTA', 150, 720], [.9, 'LA SEÑAL.', 150, 860]]}, 'Mañana a medianoche se corta la señal.', 2.8),
      ({'type': 'vhs', 'mode': '■ STOP', 'lines': [[.2, 'Y CON ELLA,', 110, 640], [.7, 'LOS 6 MESES', 130, 790], [1.1, 'GRATIS.', 160, 940]]}, 'Y con ella, los seis meses gratis.', 2.6),
      OFF,
      ({'type': 'future', 'sub': 'Hoy todavía puedes.', 'shots': [[0, 'mo-home', 'Crea tu primer equipo.', 0]]}, 'Hoy todavía puedes. Crea tu primer equipo en ProTim.', 3.4),
      cierre('Seis meses gratis. Hasta mañana a medianoche.')],
 0: [ST,
      ({'type': 'blue', 'mode': 'REC ●', 'lines': [[0, 'HOY', 220, 520], [.4, 'SE CORTA', 150, 740], [.8, 'LA SEÑAL.', 150, 880]]}, 'Hoy, a medianoche, se corta la señal.', 2.8),
      ({'type': 'vhs', 'mode': '● ÚLTIMAS HORAS', 'lines': [[.2, 'MAÑANA', 130, 640], [.6, '6 MESES', 150, 790], [1.0, 'SERÁN 3.', 150, 940]]}, 'Mañana, los seis meses vuelven a ser tres.', 2.8),
      OFF,
      ({'type': 'future', 'sub': 'Es ahora.', 'shots': [[0, 'mo-week', 'Tu temporada, en orden.', .1], [1.6, 'reg-1', None, .45]]}, 'Si aún no has creado tu equipo, es ahora.', 3),
      cierre('Seis meses gratis. Hasta las doce de esta noche.')],
}

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    for ch, blocks in E.items():
        t = 0; scenes = []; lineas = []; est = []; apag = []
        for sc, voz, mn in blocks:
            d = max(mn, (dur(voz) + .55) if voz else 0)
            s = dict(sc); s['t0'] = round(t, 2); scenes.append(s)
            if voz: lineas.append([round(t + .2, 2), voz])
            if sc['type'] == 'static': est.append([t, t + mn])
            elif sc['type'] in ('blue', 'nokia', 'win95', 'teletext', 'lcd', 'vhs'): est.append([t, t + .08])
            if sc['type'] == 'off': apag.append(t)
            t += d
        fut = next((s['t0'] for s in scenes if s['type'] == 'future'), None)
        spec = dict(retro='ep', d=str(ch), dur=round(t, 2), voz_sid=29, vel=VEL, clunks=[], dark_at=99, estatica=est, apagado=apag,
                    zumbido=[.6, apag[0] if apag else t], musica=dict(bpm=112 if ch in (10, 6) else 104, vol=.7 if ch in (10, 6) else .4, desde=fut if fut is not None else 0, duck=.5),
                    lineas=lineas, ep={'scenes': scenes})
        json.dump(spec, open(f'reels/e{ch:02d}.json', 'w'), ensure_ascii=False, indent=1)
        print(f'CH {ch:02d}: {t:.1f} s, {len(lineas)} frases')
