"""Cola del brief de Biel (12 nov): 20 Reels + 2 vídeos de marca + 10 posts, del 13 nov al 4 dic.
  python3 queue_brief.py        -> reescribe queue.json (quita bf02–bf16 y bfp1–4, añade br/bv/bp)
  python3 queue_brief.py final  -> copia a reels/ y covers/ los vídeos ya renderizados y los pone «pending»
"""
import json, os, sys, shutil, subprocess
B = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(os.path.dirname(B))
Q = os.path.join(R, 'queue.json')
MUS = {'Honky-Tonk Villain': 'Honky-Tonk Villain', 'Surreptitious': 'Surreptitious', 'Clowns': 'Clowns',
       'Thugs': 'Thugs@138.5', 'Unknown': 'Unknown@60', 'Deeper': 'Deeper@192', 'Syntheticity': 'Syntheticity@52'}
OFERTA = ('🖤 Black Friday: 6 meses gratis (en vez de 3) si creas tu primer equipo antes del 27 de noviembre a las 23:59 (hora de Madrid). '
          'Solo cuentas nuevas, sin tarjeta. Desde el 28 vuelven a ser 3 meses.')
TAGS = '#ProTeam #análisisdeportivo #entrenadores #BlackFriday'
TAGS2 = '#ProTeam #análisisdeportivo #entrenadores'
# id, fecha, archivo de render, slug, texto (en español), ¿oferta?
REELS = [
 ('r01', '11-13', 'quizas-toca-actualizar', 'Año 1995. Tu análisis: cintas VHS, carpetas y un «algo ha ido mal». 📼\nQuizás toca actualizar.', 1),
 ('r03', '11-14', 'sigues-a-la-antigua', '¿Sigues analizando a la antigua? 🗂️\nTres Excel, una libreta y una tarde entera para un solo partido. Hay otra forma.', 1),
 ('r02', '11-15', 'actualiza-tu-juego', 'Actualización disponible. ⟳\nTu equipo ya juega en 2026. ¿Y tu análisis?', 1),
 ('r16', '11-16', 'black-friday-se-acerca', 'Se acerca el Black Friday. 📡\nTu actualización te está esperando.', 1),
 ('r04', '11-17', 'senal-encontrada', 'Buscando señal… señal encontrada. 📺\nSintoniza el futuro del análisis deportivo.', 1),
 ('r06', '11-18', 'el-futuro-al-telefono', '¿Diga? ¿El futuro? ☎️\nTe está llamando. Cógelo.', 1),
 ('r09', '11-19', 'el-tiempo-del-analisis', 'El tiempo del análisis para hoy: 90 % de probabilidad de procesos anticuados y mucho trabajo a mano. 🌦️\nPrevisión: una forma mejor de analizar.', 1),
 ('v02', '11-20', 'black-friday-presentacion', 'Black Friday en ProTeam. 🖤\nDeja atrás los métodos de siempre: registro en directo, mapas de tiros, resumen por partes y control de carga, en una sola app.', 1),
 ('r10', '11-21', 'sintoniza-proteam', 'Cambia de canal. 📺\nSintoniza ProTeam.', 1),
 ('r11', '11-22', 'analizando-2-por-ciento', 'Analizando partido… 2 %. ⏳\nHay una forma más rápida.', 1),
 ('r05', '11-23', 'antes-y-despues', 'Antes: estadísticas en papel, tres hojas de cálculo y una caja de cintas.\nDespués: una app, en directo. 📱', 1),
 ('r17', '11-24', 'lo-anticuado-no-es-estrategia', 'Lo anticuado no es una estrategia. ⏩\nEl juego evoluciona. Tus herramientas también deberían.', 1),
 ('r18', '11-25', 'teletienda-proteam', 'Teletienda ProTeam 📺\nRegistro en directo: tocas el jugador y luego la acción. Marcas dónde va el tiro. Y al acabar, el resumen por partes.', 1),
 ('r19', '11-26', 'vieja-escuela-nueva-generacion', 'Vieja escuela contra nueva generación. 🆚\nEl juego ya ha cambiado.', 1),
 ('r20', '11-27', 'ultima-transmision', 'Última transmisión. 🔴\nHoy a las 23:59 se acaba la oferta de Black Friday.', 1),
 ('r08', '11-28', 'el-ano-es-1995', 'El año es 1995. 📼\nPero el juego ha cambiado. La forma de analizarlo, también.', 0),
 ('v01', '11-29', 'la-nueva-era', 'Durante años, el juego no ha parado de evolucionar. Más exigencia, más información que nunca.\nEs hora de replantear cómo lo analizamos. Esto es ProTeam. ⚡', 0),
 ('r07', '11-30', 'trabaja-mejor', 'Trabaja con más cabeza. Analiza mejor. 🧠', 0),
 ('r12', '12-01', 'una-sola-jugada', '¿Solo una jugada? Piénsalo otra vez. 🎯\nDónde empezó, dónde acabó y en qué minuto pasó.', 0),
 ('r13', '12-02', 'la-historia-detras', '¿Los datos son solo datos? 📊\nHasta que entiendes la historia que hay detrás.', 0),
 ('r14', '12-03', 'el-analista-de-siempre', 'El analista de toda la vida: papel, bolis y una montaña de cintas. 📼\nTe presentamos ProTeam.', 0),
 ('r15', '12-04', 'escucha-el-juego', '¿Y si tus datos hablaran? 👂\nMira más de cerca. Entiende lo que pasa detrás de cada jugada.', 0),
]
POSTS = [  # id, fecha, hora, n.º de imágenes, texto
 ('p02', '11-13', '20:30', 5, '¿Sigues en 1995? 💾\nSi organizar el análisis te lleva más que el propio partido, quizás toca actualizar.', 1),
 ('p03', '11-15', '20:30', 1, 'ERROR 404: análisis deportivo moderno no encontrado. 🖥️\nQuizás necesitas actualizar tu sistema.', 1),
 ('p06', '11-17', '20:30', 1, 'Actualización del sistema disponible. ⬇️\nProTeam Black Friday: es hora de actualizar.', 1),
 ('p05', '11-19', '20:30', 5, 'Vieja escuela vs. nueva escuela. 🆚\nHerramientas distintas, posibilidades distintas. ¿Cuál es tu siguiente jugada?', 1),
 ('p08', '11-21', '20:30', 6, '¿Qué hay en tu caja de herramientas de análisis? 🧰\nRegistro en directo, mapas de tiros y goles, resumen por partes (con los últimos 10 minutos) y control de carga (minutos × RPE, jugador a jugador).', 1),
 ('p04', '11-23', '20:30', 5, 'Diccionario del analista, vol. 1: el mapa de tiros. 📖\nDónde se tiró cada tiro y dónde acabó. Los patrones que en directo se escapan. (Datos de ejemplo.)', 1),
 ('p07', '11-25', '20:30', 5, 'Detrás de cada jugada hay una historia. 🎬\nMovimientos. Decisiones. Datos.', 1),
 ('p10', '11-27', '13:25', 3, 'Última transmisión. 🔴\nÚltima oportunidad para actualizar tu análisis: hoy a las 23:59.', 1),
 ('p01', '11-29', '20:30', 5, 'El juego ha cambiado. La forma de entrenar y de competir, también. ⚡\nLa forma de analizar debería cambiar con ellos. Bienvenido a la nueva era.', 0),
 ('p09', '11-26', '20:30', 1, 'El futuro no espera. 📺', 1),
]


def credit(spec):
    a = spec['audio']; n = lambda p: MUS[os.path.splitext(os.path.basename(p))[0]]
    return f'Música: «{n(a["old"][0])}» y «{n(a["new"][0])}», de Tanner Helland (CC BY 4.0).'


def cap(text, bf, extra):
    return '\n\n'.join(x for x in [text, OFERTA if bf else None, '👉 pro-team.app (enlace en la bio)', extra, TAGS if bf else TAGS2] if x)


def rid(k): return ('bv' if k[0] == 'v' else 'br') + k[1:]


def build():
    q = json.load(open(Q))
    old = {f'bf{n:02d}' for n in range(2, 17)} | {'bfp1', 'bfp2', 'bfp3', 'bfp4'}
    new = {rid(k) for k, *_ in REELS} | {'b' + k for k, *_ in POSTS}
    q = [i for i in q if i['id'] not in old and i['id'] not in new]
    for k, d, slug, text, bf in REELS:
        spec = json.load(open(f'{B}/reels/{k}.json'))
        q.append({'id': rid(k), 'when': f'2026-{d}T13:30:00+01:00', 'kind': 'reel', 'files': [f'reels/{rid(k)}-{slug}.mp4'],
                  'cover': f'covers/{rid(k)}-{slug}.jpg', 'status': 'borrador', 'campana': 'blackout',
                  'caption': cap(text, bf, credit(spec)),
                  'note': f'Brief 12 nov · {k} · tele a pantalla completa → móvil 3D; voz en inglés (Kokoro), subtítulos en pantalla; en «borrador» hasta que acabe el render'})
    for k, d, h, n, text, bf in POSTS:
        files = [f'feed/{k}-{j}.jpg' for j in range(1, n + 1)]
        q.append({'id': 'b' + k, 'when': f'2026-{d}T{h}:00+01:00', 'kind': 'carousel' if n > 1 else 'image', 'files': files,
                  'status': 'pending', 'campana': 'blackout', 'caption': cap(text, bf, None), 'note': f'Brief 12 nov · post {k}'})
    q.sort(key=lambda i: i['when'])
    json.dump(q, open(Q, 'w'), ensure_ascii=False, indent=1)
    print(len(q), 'entradas')


def final():
    q = json.load(open(Q)); by = {i['id']: i for i in q}
    for k, *_ in REELS:
        log = f'{B}/reels/{k}.log'
        if not (os.path.exists(log) and open(log).read().rstrip().split('\n')[-1].startswith('ok')): continue
        i = by[rid(k)]
        if i['status'] != 'borrador': continue
        spec = json.load(open(f'{B}/reels/{k}.json'))
        shutil.copy(f'{B}/reels/{k}.mp4', os.path.join(R, i['files'][0]))
        t = max(.5, spec.get('cut', 3) - .4)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', f'{B}/reels/{k}.mp4', '-frames:v', '1', '-q:v', '3', os.path.join(R, i['cover'])], check=True)
        i['status'] = 'pending'; i['note'] = i['note'].replace('; en «borrador» hasta que acabe el render', '')
        print('listo', i['id'])
    json.dump(q, open(Q, 'w'), ensure_ascii=False, indent=1)


final() if sys.argv[1:] == ['final'] else build()
