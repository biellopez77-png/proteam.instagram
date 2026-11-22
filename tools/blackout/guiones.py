"""Guiones de Black Friday (solo las ideas de Biel): ¿Qué sistema estás usando?, Teletienda, ¿Sigues analizando como en 1995?,
Your future is calling, cuenta atrás, ¿Estás actualizado?, Métodos de 1995 (humor), Actualización disponible.
Genera reels/bXX.json para brand.py, con tiempos ajustados a la voz.   python3 guiones.py [h]   (h = también el vídeo horizontal)"""
import json, os, sys, tempfile
sys.path.insert(0, '/home/claude/tts'); import kok, soundfile as sf
os.chdir(os.path.dirname(os.path.abspath(__file__)))
_c = {}
def vd(t):
    if not t: return 0
    if t not in _c:
        p = tempfile.mktemp(suffix='.wav'); kok.say(t, 29, p, 1.0); a, sr = sf.read(p); os.remove(p); _c[t] = len(a) / sr
    return _c[t]
OF = 'Seis meses gratis para tu primer equipo. Solo hasta el veintisiete.'
G = '0 0 10px rgba(61,255,168,.7)'
def line(kind, text, hz):
    k = .8 if hz else 1
    if kind == 'g': return {'text': text, 'font': 'VT', 'size': int(72 * k), 'color': '#3dffa8', 'glow': G, 'cps': 30}
    if kind == 'v': return {'text': text, 'font': 'VT', 'size': int(80 * k), 'cps': 30}
    if kind == 'd': return {'text': text, 'font': 'VT', 'size': int(62 * k), 'color': '#52ff8f', 'glow': '0 0 10px rgba(80,255,140,.6)', 'cps': 34}
    if kind == 'n': return {'text': text, 'font': 'Px', 'size': int(92 * k), 'cps': 20}
    if kind == 'ns': return {'text': text, 'font': 'Px', 'size': int(62 * k), 'cps': 24}
    if kind == ' ': return {'text': ' ', 'size': 34}
    n = len(text); size = 150 if n <= 9 else 128 if n <= 11 else 112 if n <= 13 else 96
    return {'text': text, 'size': int(size * (.78 if hz else 1)), 'cps': 16}
def W(t0, t1, big, small, hz):
    if hz:
        h = f'<div class="a" style="left:1000px;right:80px;top:380px;font-family:IT;font-weight:900;font-size:104px;letter-spacing:-.04em;color:#fff;line-height:1">{big}</div>'
        if small: h += f'<div class="a" style="left:1004px;right:80px;top:520px;font-family:VT;font-size:50px;letter-spacing:.06em;color:#3dffa8">{small}</div>'
    else:
        h = f'<div class="a" style="left:0;right:0;top:150px;text-align:center;font-family:IT;font-weight:900;font-size:112px;letter-spacing:-.04em;color:#fff;line-height:1">{big}</div>'
        if small: h += f'<div class="a" style="left:0;right:0;top:285px;text-align:center;font-family:VT;font-size:54px;letter-spacing:.06em;color:#3dffa8">{small}</div>'
    return [round(t0, 2), round(t1, 2), h]

def build(ch, old, app, end, music, hz=False, name=None, dlabel=None):
    """old: [(device, osd_mode or None, [(kind, text)], voz)], app: [(captura, palabra, voz, s0, s1)], end: (grande, pequeño, voz)"""
    t = .5; dev = []; layers = []; lineas = []; CH = dlabel or f'CH {ch:02d}'
    for i, (d, mode, lines, voz) in enumerate(old):
        dev.append([0 if i == 0 else round(t - .1, 2), d, .8])
        at = .1; L = []
        for kind, text in lines:
            if kind == '__bar': continue
            l = line(kind, text, hz); l['at'] = round(at, 2); L.append(l)
            if kind != ' ': at += len(text) / l['cps'] + .18
        typed = at
        dur = max(typed + 1.0, vd(voz) + .7) if voz else typed + .45
        if voz: lineas.append([round(t + .3, 2), voz])
        if d != 'nokia' and mode is not False:
            layers.append({'t0': round(t - .2, 2), 't1': round(t + dur + .2, 2), 'type': 'osd', 'ch': CH, 'mode': mode or 'PLAY ▶', 'blink': bool(mode and ('●' in mode or '⟳' in mode))})
        if d == 'nokia': layers.append({'t0': round(t - .2, 2), 't1': round(t + dur + .2, 2), 'type': 'nokia', 'hora': '23:59'})
        layers.append({'t0': round(t, 2), 't1': round(t + dur + .2, 2), 'type': 'text', 'valign': 'flex-start' if d != 'nokia' else 'center',
                       'align': 'center' if d == 'nokia' else 'left', 'pad': ('170px 110px' if hz else '300px 90px'), 'gap': 16,
                       'lines': [x for x in L if x['text'] != '__bar']})
        if any(x[0] == '__bar' for x in lines):
            layers.append({'t0': round(t, 2), 't1': round(t + dur + .2, 2), 'type': 'bar', 'at': .8, 'len': max(1.2, dur - 1.2), 'bottom': 200 if hz else 330})
        t += dur
    cut = round(t, 2); trans = 1.9; ta = cut; A = []; words = []
    for j, (img, word, voz, s0, s1) in enumerate(app):
        dur = max(2.3 if j else 3.0, vd(voz) + .6 + (1.2 if j == 0 else 0))
        A.append([round(ta, 2), img, s0, s1])
        w0 = ta + (1.4 if j == 0 else .1)
        if voz: lineas.append([round(w0 + .1, 2), voz])
        words.append(W(w0, ta + dur, word, None, hz)); ta += dur
    big, small, evoz = end; dur = max(4.6, vd(evoz) + .9)
    if evoz: lineas.append([round(ta + .2, 2), evoz])
    words.append(W(ta + .1, ta + dur, big, small, hz)); total = round(ta + dur, 2)
    # sin solapes de voz: si una frase empieza antes de que acabe la anterior, se retrasa
    lineas.sort(); last = 0
    for l in lineas:
        if l[0] < last + .15: l[0] = round(last + .15, 2)
        last = l[0] + vd(l[1])
    total = max(total, round(last + .8, 2))
    spec = {'w': 1920 if hz else 1080, 'h': 1080 if hz else 1920, 'd': str(ch), 'dur': total, 'on': True, 'vel': 1.0, 'cut': cut, 'trans': trans,
            'pose': ({'ry0': .32, 'x': -.035, 'y': 0, 'far': .36} if hz else {'ry0': -.24, 'y': -.014, 'far': .47}),
            'dev': dev, 'layers': layers, 'app': A, 'words': words,
            'audio': {'cut': cut, 'old': [music[0], music[1]], 'new': [music[2], music[3]], 'old_vol': .5, 'new_vol': .75}, 'lineas': lineas}
    json.dump(spec, open(f'reels/{name or "b%02d" % ch}.json', 'w'), ensure_ascii=False, indent=1)
    print(name or f'b{ch:02d}', f'{total:.1f}s', 'corte', cut)

HT, SU, CL = 'Honky-Tonk Villain.mp3', 'Surreptitious.mp3', 'Clowns.mp3'
TH, UN, DE, SY = ('Thugs.mp3', 138.5), ('Unknown.mp3', 60), ('Deeper.mp3', 192), ('Syntheticity.mp3', 52)
END = ('6 meses gratis.', 'SOLO HASTA EL 27 · PRO-TEAM.APP', OF)
E = {
 14: dict(old=[('tvblack', False, [('d', 'C:\\> VER'), (' ', ''), ('d', 'SISTEMA DE ANÁLISIS:'), ('d', 'LIBRETA 1.0 (1995)')], '¿Qué sistema estás usando?'),
               ('tvblack', False, [('d', 'C:\\> ANALIZAR PARTIDO'), (' ', ''), ('d', 'ERROR 1995:'), ('d', 'MEMORIA INSUFICIENTE'), ('d', '¿REINTENTAR? S/N')], 'Si tu análisis depende de tu memoria, tienes un problema de sistema.'),
               ('tv', '⟳ UPDATE', [('g', 'SISTEMA RECOMENDADO'), (' ', ''), ('H', 'PROTEAM'), ('H', '2026.')], 'Sistema recomendado: ProTim.')],
          app=[('reg-1', 'Registra.', 'Registra el partido en directo.', .42, .5), ('reg-3', 'Cada tiro.', 'Dónde va cada tiro.', .45, .52), ('res-0', 'Analiza.', 'Y el resumen por partes, al acabar.', .1, .4)],
          end=END, music=(SU, 0, *UN)),
 13: dict(old=[('tv', 'TELETIENDA', [('g', 'TELETIENDA PROTEAM'), (' ', ''), ('H', '¿ANALIZA'), ('H', 'SUS PARTIDOS'), ('H', 'CON UNA'), ('H', 'LIBRETA?')], '¿Analiza usted sus partidos con una libreta?'),
               ('nokia', None, [('n', 'LLAME YA'), (' ', ''), ('ns', '900 1995 1995'), ('ns', '(ES BROMA)')], '¡Llame ya! Es broma.'),
               ('tv', 'TELETIENDA', [('H', '¡NO SUFRA'), ('H', 'MÁS!')], 'No sufra más.')],
          app=[('reg-0', 'En directo.', 'Con ProTim, el partido se registra en directo.', .3, .4), ('reg-4', '¿Gol o parada?', 'Gol o parada, con un toque.', .5, .56), ('cro-0', 'Crónica hecha.', 'Y al acabar, la crónica ya está hecha.', 0, .15)],
          end=('6 meses gratis.', 'SOLO HASTA EL 27 · PRO-TEAM.APP', 'Y ahora, seis meses gratis para su primer equipo. Solo hasta el veintisiete.'), music=(HT, 20, *TH)),
 12: dict(old=[('tvblack', '◀◀ REW', [('v', '◀◀ REBOBINANDO'), (' ', ''), ('H', 'MINUTO 23.'), ('H', '¿DÓNDE'), ('H', 'ESTABA?')], 'Rebobinando la cinta para encontrar el minuto veintitrés.'),
               ('tv', 'PLAY ▶', [('g', 'PREGUNTA'), (' ', ''), ('H', '¿SIGUES'), ('H', 'ANALIZANDO'), ('H', 'COMO EN'), ('H', '1995?')], '¿Sigues analizando como en mil novecientos noventa y cinco?')],
          app=[('cro-0', 'Cronología.', 'En ProTim, cada acción queda en la cronología.', 0, .2), ('res-0', 'Últimos 10 min.', 'Ves los parciales y los últimos diez minutos.', .1, .35), ('res-1', 'Por jugador.', 'Y los números de cada jugador.', .2, .45)],
          end=END, music=(SU, 20, *DE)),
 11: dict(old=[('nokia', None, [('n', 'LLAMADA'), ('n', 'ENTRANTE'), (' ', ''), ('ns', '☎ TU FUTURO')], 'Llamada entrante.'),
               ('nokia', None, [('ns', 'TU FUTURO'), ('ns', 'TE ESTÁ LLAMANDO'), (' ', ''), ('n', '¿DESCOLGAR?')], 'Es tu futuro. ¿Lo coges?'),
               ('tv', 'CONECTANDO', [('g', 'LLAMADA ACEPTADA'), (' ', ''), ('H', 'YOUR'), ('H', 'FUTURE'), ('H', 'IS CALLING.')], None)],
          app=[('mo-home', 'Tu día.', 'ProTim. Abres la app y ves tu día.', 0, .1), ('mo-plan', 'Tu semana.', 'Tu semana, planificada.', .02, .12), ('res-0', 'Tus partidos.', 'Y tus partidos, analizados.', .1, .4)],
          end=END, music=(HT, 35, *SY)),
 10: dict(old=[('tv', None, [('g', 'CH 01'), ('H', 'LIBRETA.')], None), ('tvblack', None, [('d', 'CH 02'), ('H', 'EXCEL 97.')], None), ('tv', None, [('g', 'CH 03'), ('H', 'VHS.')], None),
               ('nokia', None, [('n', 'CH 04'), ('n', 'SMS.')], None), ('tvblack', None, [('d', 'CH 05'), ('H', 'FAX.')], None), ('tv', None, [('g', 'CH 06'), ('H', 'CALCULADORA.')], None),
               ('tvred', None, [('g', 'CH 07'), ('H', 'MEMORIA.')], None), ('tv', '⟳ UPDATE', [('g', 'CH 10'), ('H', 'PROTEAM.')], None)],
          app=[('mo-plan', 'Planifica.', None, .02, .1), ('reg-1', 'Registra.', None, .42, .5), ('res-0', 'Analiza.', None, .1, .3), ('fF', 'Controla.', None, 0, .12)],
          end=('Quedan 10 días.', '6 MESES GRATIS · PRO-TEAM.APP', None), music=(CL, 100, *TH)),
 9: dict(old=[('tv', 'TEST 1/2', [('H', '¿APUNTAS'), ('H', 'LOS GOLES'), ('H', 'EN UN PAPEL?'), (' ', ''), ('v', '[SÍ]    NO')], 'Test. ¿Apuntas los goles en un papel?'),
              ('tv', 'TEST 2/2', [('H', '¿CALCULAS'), ('H', 'LA CARGA'), ('H', 'A OJO?'), (' ', ''), ('v', '[SÍ]    NO')], '¿Calculas la carga a ojo?'),
              ('tvred', 'RESULTADO', [('H', 'VERSIÓN'), ('H', '1995'), ('H', 'DETECTADA.')], 'Versión mil novecientos noventa y cinco detectada.')],
         app=[('reg-2', 'Cada tiro.', 'ProTim registra cada tiro y desde dónde.', .4, .5), ('fF', 'Cada carga.', 'Y calcula la carga: minutos por esfuerzo.', 0, .15)],
         end=END, music=(CL, 0, *UN)),
 8: dict(old=[('tv', 'MÉTODOS DE 1995', [('g', 'N.º 1'), (' ', ''), ('H', 'LA LIBRETA'), ('H', 'DE'), ('H', 'ESTADÍSTICAS.')], 'Métodos de mil novecientos noventa y cinco. Número uno: la libreta de estadísticas.'),
              ('tv', 'MÉTODOS DE 1995', [('g', 'VENTAJAS'), ('v', '- NO NECESITA BATERÍA'), (' ', ''), ('g', 'INCONVENIENTES'), ('v', '- TODO LO DEMÁS')], 'Ventajas: no necesita batería. Inconvenientes: todo lo demás.')],
         app=[('res-1', 'Por jugador.', 'En ProTim, los números de cada jugador.', .2, .45), ('res-0', 'Por partes.', 'Y el partido, por partes.', .1, .35)],
         end=END, music=(HT, 0, *SY)),
 7: dict(old=[('tv', 'TELETIENDA', [('H', '¿QUIERE'), ('H', 'SABER CUÁNDO'), ('H', 'SE ROMPIÓ SU'), ('H', 'PARTIDO?')], '¿Quiere saber cuándo se rompió su partido?'),
              ('tv', 'TELETIENDA', [('H', '¡Y NO'), ('H', 'SOLO ESO!')], '¡Y no solo eso!')],
         app=[('res-0', 'Por partes.', 'Marcador por partes y últimos diez minutos.', .1, .35), ('reg-3', 'Cada tiro.', 'Dónde va cada tiro.', .45, .52), ('res-1', 'Por jugador.', 'Y los números de cada jugador.', .2, .45)],
         end=END, music=(CL, 30, *DE)),
 6: dict(old=[('tv', 'MÉTODOS DE 1995', [('g', 'N.º 2'), (' ', ''), ('H', 'EL EXCEL'), ('H', 'DEL LUNES.')], 'Métodos de mil novecientos noventa y cinco. Número dos: el Excel del lunes.'),
              ('tvblack', False, [('d', 'C:\\> DIR'), (' ', ''), ('d', 'PLANIFICACION_FINAL.XLS'), ('d', 'PLANIFICACION_FINAL2.XLS'), ('d', 'PLANIFICACION_BUENA.XLS'), ('d', 'PLANIFICACION_ESTA_SI.XLS')], 'Final. Final dos. Buena. Esta sí.')],
         app=[('mo-plan', 'Planifica.', 'En ProTim planificas el microciclo.', .02, .12), ('mo-week', 'Una versión.', 'Una sola semana. Una sola versión.', .05, .2)],
         end=END, music=(SU, 40, *SY)),
 5: dict(old=[('tvblack', False, [('v', 'CARGANDO'), ('v', 'TEMPORADA 26/27'), ('__bar', '')], 'Cargando temporada.'),
              ('tvred', 'ERROR', [('H', 'ERROR:'), (' ', ''), ('v', 'TEMPORADA NO'), ('v', 'PLANIFICADA')], 'Error: temporada no planificada.')],
         app=[('mo-cal', 'Mes a mes.', 'Con ProTim, la temporada mes a mes.', .05, .2), ('mo-week', 'Semana a semana.', 'Y semana a semana.', .05, .2)],
         end=('Quedan 5 días.', '6 MESES GRATIS · PRO-TEAM.APP', OF), music=(SU, 30, *TH)),
 4: dict(old=[('tv', '▶▶ FF', [('g', 'INSTALANDO PROTEAM'), (' ', ''), ('H', 'DIC ENE FEB'), ('H', 'MAR ABR MAY')], 'Diciembre, enero, febrero, marzo, abril y mayo.'),
              ('tv', '▶▶ FF', [('H', '6 MESES.'), ('H', 'UNA'), ('H', 'TEMPORADA.')], 'Seis meses. Casi una temporada entera.')],
         app=[('mo-plan', 'Toda la temporada.', 'Si creas tu primer equipo antes del veintisiete, la tienes en ProTim. Gratis.', .02, .15)],
         end=('6 meses gratis.', 'SOLO HASTA EL 27 · PRO-TEAM.APP', 'Seis meses gratis. Solo hasta el veintisiete.'), music=(HT, 10, *UN)),
 3: dict(old=[('tv', 'MÉTODOS DE 1995', [('g', 'N.º 3'), (' ', ''), ('H', 'LA CARGA'), ('H', 'A OJO.')], 'Métodos de mil novecientos noventa y cinco. Número tres: la carga a ojo.'),
              ('tv', 'MÉTODOS DE 1995', [('v', '«ESTE ESTÁ'), ('v', 'CANSADO, SE'), ('v', 'LE NOTA EN LA CARA.»')], 'Este está cansado, se le nota en la cara.')],
         app=[('fF', 'Minutos × RPE.', 'En ProTim, minutos por esfuerzo, jugador a jugador.', 0, .15), ('mo-tests', 'Tests físicos.', 'Y los tests físicos, programados.', 0, .12)],
         end=('Quedan 3 días.', '6 MESES GRATIS · PRO-TEAM.APP', OF), music=(CL, 60, *UN)),
 2: dict(old=[('tv', 'TELETIENDA', [('H', '¡ÚLTIMAS'), ('H', 'UNIDADES!'), (' ', ''), ('g', '(ES SOFTWARE, NO SE AGOTA)')], '¡Últimas unidades! Bueno, es software, no se agota.'),
              ('tv', 'TELETIENDA', [('H', '6 MESES'), ('H', 'GRATIS.'), (' ', ''), ('v', 'SIN TARJETA'), ('v', 'SIN LETRA PEQUEÑA')], 'Pero los seis meses gratis, sí. Y sin tarjeta.')],
         app=[('mo-home', 'Hasta el viernes.', 'Solo hasta el viernes veintisiete.', 0, .1), ('reg-1', 'Sin tarjeta.', None, .42, .5)],
         end=('Quedan 2 días.', '6 MESES GRATIS · PRO-TEAM.APP', 'Crea tu primer equipo en ProTim.'), music=(HT, 25, *TH)),
 1: dict(old=[('tvred', 'AVISO', [('g', 'EMISIÓN FINAL'), (' ', ''), ('H', 'MAÑANA'), ('H', '23:59.')], 'Aviso: mañana a las doce de la noche se corta la señal.'),
              ('tvred', 'AVISO', [('H', 'Y CON ELLA,'), ('H', 'LOS 6 MESES'), ('H', 'GRATIS.')], 'Y con ella, los seis meses gratis.')],
         app=[('mo-week', 'Hoy todavía.', 'Hoy todavía puedes crear tu primer equipo en ProTim.', .05, .2)],
         end=('Mañana se corta.', '6 MESES GRATIS · PRO-TEAM.APP', 'Seis meses gratis. Hasta mañana a medianoche.'), music=(SU, 0, *DE)),
 0: dict(old=[('tvred', 'REC ●', [('H', 'HOY'), ('H', 'SE CORTA'), ('H', 'LA SEÑAL.')], 'Hoy, a medianoche, se corta la señal.'),
              ('nokia', None, [('n', '3 LLAMADAS'), ('n', 'PERDIDAS'), (' ', ''), ('ns', 'TU FUTURO')], 'Tienes tres llamadas perdidas de tu futuro.')],
         app=[('mo-home', 'Contesta.', 'Contesta. Crea tu primer equipo en ProTim.', 0, .1), ('res-0', 'Hoy.', None, .1, .3)],
         end=('Hasta las 23:59.', '6 MESES GRATIS · PRO-TEAM.APP', 'Seis meses gratis. Hasta las doce de esta noche.'), music=(HT, 40, *TH)),
}
if __name__ == '__main__':
    for ch, e in E.items(): build(ch, e['old'], e['app'], e['end'], e['music'])
    # vídeo horizontal de presentación de Black Friday
    build(15, [('tv', 'EMISIÓN ESPECIAL', [('g', 'BLACK FRIDAY · PROTEAM'), (' ', ''), ('H', 'TU ANÁLISIS'), ('H', 'SIGUE EN 1995.')], 'Emisión especial. Tu análisis sigue en mil novecientos noventa y cinco.'),
               ('tvblack', False, [('d', 'C:\\> ANALISIS.EXE'), (' ', ''), ('d', 'LIBRETA.DOC ...... OBSOLETO'), ('d', 'EXCEL_97.XLS ..... OBSOLETO'), ('d', 'VHS_PARTIDO ...... OBSOLETO')], 'Libreta, Excel y una cinta de vídeo. Todo obsoleto.'),
               ('nokia', None, [('n', 'LLAMADA ENTRANTE'), (' ', ''), ('ns', '☎ TU FUTURO')], 'Y tu futuro te está llamando.'),
               ('tv', '⟳ UPDATE', [('H', 'ACTUALIZACIÓN'), ('H', 'DISPONIBLE.'), ('v', 'PROTEAM 2026 · ¿INSTALAR? [SÍ]'), ('__bar', '')], 'Actualización disponible.')],
          [('mo-plan', 'Planifica.', 'ProTim. Planifica la temporada.', .02, .12), ('reg-1', 'Registra.', 'Registra el partido en directo.', .42, .5),
           ('res-0', 'Analiza.', 'Analiza cada parcial.', .1, .35), ('fF', 'Controla.', 'Y controla la carga de cada jugador.', 0, .15)],
          ('Black Friday.', '6 MESES GRATIS · HASTA EL 27 · PRO-TEAM.APP', 'Black Friday: seis meses gratis para tu primer equipo. Solo hasta el viernes veintisiete.'),
          (HT, 0, *TH), hz=True, name='h-blackfriday', dlabel='CH 27')
