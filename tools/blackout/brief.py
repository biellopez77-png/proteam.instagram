"""Brief de Biel (12 nov): 20 Reels + 2 vídeos de marca. Titulares en inglés, voz en inglés (Kokoro «Michael», gratis).
Cada pieza: bloques del pasado (tele a pantalla completa) → móvil 3D con capturas reales → cierre.
  python3 brief.py            -> reels/rXX.json, reels/v01.json, reels/v02.json (+ versiones 16:9 _h)"""
import json, os, sys, tempfile
sys.path.insert(0, '/home/claude/tts'); import kok, soundfile as sf
os.chdir(os.path.dirname(os.path.abspath(__file__)))
VOICE = {'sid': 16, 'lang': 'en-us'}; PRESENTER = 26  # Michael narra; George hace de presentador de teletienda
_c = {}
def vd(t, sid=16):
    if not t: return 0
    k = (t, sid)
    if k not in _c:
        p = tempfile.mktemp(suffix='.wav'); kok.say(t, sid, p, 1.0, 'en-us'); a, sr = sf.read(p); os.remove(p); _c[k] = len(a) / sr
    return _c[k]
G = '0 0 10px rgba(61,255,168,.7)'
def ln(kind, text, hz):
    k = .78 if hz else 1
    if kind == 'g': return {'text': text, 'font': 'VT', 'size': int(72 * k), 'color': '#3dffa8', 'glow': G, 'cps': 30}
    if kind == 'v': return {'text': text, 'font': 'VT', 'size': int(78 * k), 'cps': 30}
    if kind == 'd': return {'text': text, 'font': 'VT', 'size': int(60 * k), 'color': '#52ff8f', 'glow': '0 0 10px rgba(80,255,140,.6)', 'cps': 34}
    if kind == 'r': return {'text': text, 'font': 'VT', 'size': int(64 * k), 'color': '#ff6b7d', 'glow': '0 0 10px rgba(255,80,100,.6)', 'cps': 34}
    if kind == 'n': return {'text': text, 'font': 'Px', 'size': int(84 * k), 'cps': 20}
    if kind == ' ': return {'text': ' ', 'size': 30}
    n = len(text); size = 150 if n <= 9 else 128 if n <= 11 else 110 if n <= 13 else 92 if n <= 16 else 78
    return {'text': text, 'size': int(size * (.8 if hz else 1)), 'cps': 16}

def words_html(big, small, hz):
    if hz:
        h = f'<div class="a" style="left:1010px;right:70px;top:360px;font-family:IT;font-weight:900;font-size:92px;letter-spacing:-.04em;color:#fff;line-height:1.02">{big}</div>'
        if small: h += f'<div class="a" style="left:1014px;right:70px;top:{360 + 104 * (1 + big.count("<br>"))}px;font-family:VT;font-size:44px;letter-spacing:.05em;color:#3dffa8;line-height:1.15">{small}</div>'
    else:
        h = f'<div class="a" style="left:60px;right:60px;top:130px;text-align:center;font-family:IT;font-weight:900;font-size:96px;letter-spacing:-.04em;color:#fff;line-height:1.02">{big}</div>'
        if small: h += f'<div class="a" style="left:40px;right:40px;bottom:120px;text-align:center;font-family:VT;font-size:48px;letter-spacing:.05em;color:#3dffa8;line-height:1.15">{small}</div>'
    return h

BF = 'BLACK FRIDAY · 6 MONTHS FREE<br>FIRST TEAM · NO CARD · UNTIL 27 NOV 23:59'
def build(name, old, app, end, music, hz=False, ch=None, extra_end=None, minapp=2.4, minold=1.4):
    """old: lista de bloques dict(dev, osd, lines|js, voz, sid, dur, noise)  app: [(captura, palabra, voz, s0, s1)]  end: (grande, pequeño, voz)"""
    t = .5; dev = []; layers = []; lineas = []; CH = ch or 'CH 95'
    for i, b in enumerate(old):
        d = b.get('dev', 'tv'); dev.append([0 if i == 0 else round(t - .1, 2), d, .7]); voz = b.get('voz'); sid = b.get('sid', 16)
        at = .1; L = []
        for kind, text in b.get('lines', []):
            l = ln(kind, text, hz); l['at'] = round(at, 2); L.append(l)
            if kind != ' ': at += len(text) / l['cps'] + .15
        dur = b.get('dur') or max(at + .9, (vd(voz, sid) + .6) if voz else 0, minold)
        if voz: lineas.append([round(t + .3, 2), voz, sid])
        if b.get('osd', True) is not False and d != 'nokia':
            layers.append({'t0': round(t - .2, 2), 't1': round(t + dur + .2, 2), 'type': 'osd', 'ch': b.get('ch', CH), 'mode': b.get('osd') if isinstance(b.get('osd'), str) else 'PLAY ▶', 'blink': '●' in str(b.get('osd'))})
        if b.get('noise'): layers.append({'t0': round(t, 2), 't1': round(t + dur, 2), 'type': 'noise', 'fi': .05, 'fo': .1})
        if L: layers.append({'t0': round(t, 2), 't1': round(t + dur + .2, 2), 'type': 'text', 'valign': b.get('valign', 'flex-start'), 'align': b.get('align', 'left'),
                             'pad': b.get('pad', '170px 110px' if hz else '300px 90px'), 'gap': 16, 'lines': L})
        if b.get('js'): layers.append({'t0': round(t, 2), 't1': round(t + dur + .2, 2), 'type': 'js', 'code': b['js'], 'fi': .3})
        t += dur
    cut = round(t, 2); ta = cut; A = []; words = []
    for j, (img, word, voz, s0, s1) in enumerate(app):
        dur = max(minapp if j else minapp + .6, vd(voz) + .6 + (1.2 if j == 0 else 0))
        A.append([round(ta, 2), img, s0, s1]); w0 = ta + (1.4 if j == 0 else .1)
        if voz: lineas.append([round(w0 + .1, 2), voz, 16])
        if word: words.append([round(w0, 2), round(ta + dur, 2), words_html(word, None, hz)])
        ta += dur
    big, small, evoz = end; dur = max(4.8, vd(evoz) + 1.0)
    if evoz: lineas.append([round(ta + .2, 2), evoz, 16])
    words.append([round(ta + .1, 2), round(ta + dur, 2), words_html(big, small, hz)]); total = ta + dur
    lineas.sort(); last = 0
    for l in lineas:
        if l[0] < last + .15: l[0] = round(last + .15, 2)
        last = l[0] + vd(l[1], l[2])
    total = round(max(total, last + .8), 2)
    spec = {'w': 1920 if hz else 1080, 'h': 1080 if hz else 1920, 'd': '0', 'dur': total, 'on': True, 'vel': 1.0, 'voice': VOICE, 'cut': cut, 'trans': 1.9,
            'pose': ({'ry0': .32, 'x': -.035, 'y': 0, 'far': .36} if hz else {'ry0': -.24, 'y': -.01, 'far': .5}),
            'dev': dev, 'layers': layers, 'app': A, 'words': words,
            'audio': {'cut': cut, 'old': [music[0], music[1]], 'new': [music[2], music[3]], 'old_vol': .55, 'new_vol': .75}, 'lineas': lineas}
    json.dump(spec, open(f'reels/{name}.json', 'w'), ensure_ascii=False, indent=1)
    print(f'{name:8s} {total:5.1f}s  corte {cut}')

HT, SU, CL = 'Honky-Tonk Villain.mp3', 'Surreptitious.mp3', 'Clowns.mp3'
TH, UN, DE, SY = ('Thugs.mp3', 138.5), ('Unknown.mp3', 60), ('Deeper.mp3', 192), ('Syntheticity.mp3', 52)
NO = dict(dev='tvblack', osd=False, noise=True, dur=.8)
# escenas a medida (JS dentro de la pantalla; u = segundos desde que empieza el bloque, W/H = tamaño de la pantalla)
VHS_STACK = "[0,1,2,3,4,5].map(i => BOX(W*.5-260+(i%2)*40, H*.62-i*70-Math.min(0,u-1)*0, 520, 60, 'background:#111;border:4px solid #ddd;opacity:'+Math.min(1,Math.max(0,(u-i*.25)*3)), TX(20,6,40,'VHS · MATCH '+(i+1)))).join('') + BOX(W*.5-300,H*.62+80,600,90,'border:4px dashed #fff;opacity:'+Math.min(1,u), TX(24,14,52,'FOLDER_2003'))"
ERROR = "BOX(W*.1, H*.36, W*.8, 330, 'background:#c0c0c0;border:6px solid;border-color:#fff #404040 #404040 #fff;box-shadow:16px 16px 0 rgba(0,0,0,.45)', BOX(8,8,W*.8-28,62,'background:linear-gradient(90deg,#000080,#1084d0)', TX(18,6,46,'SYSTEM',{font:'Px'})) + TX(40,110,64,TYPE(Ly.msg,u,26),{color:'#000',glow:'none'}) + BOX(W*.4-110,250,180,60,'border:4px solid;border-color:#fff #404040 #404040 #fff', TX(52,6,46,'OK',{color:'#000',glow:'none'})))"
E = {}
E['r01'] = dict(old=[NO, dict(lines=[('g', 'BROADCAST'), (' ', ''), ('H', 'YEAR:'), ('H', '1995')]),
                     dict(lines=[('g', 'NOW SHOWING'), (' ', ''), ('H', 'YOUR'), ('H', 'ANALYSIS'), ('H', 'WORKFLOW...')], js=VHS_STACK.replace('H*.62', 'H*.78')),
                     dict(dev='tvred', osd='ERROR', js=ERROR, msg='Something went wrong.', dur=2.8),
                     dict(lines=[('H', 'MAYBE IT\'S'), ('H', 'TIME FOR AN'), ('H', 'UPGRADE.')], voz='Maybe it\'s time for an upgrade.')],
                app=[('reg-1', 'Upgrade.', None, .42, .5), ('res-0', 'Analyse.', None, .1, .35)],
                end=('Discover a new way<br>to analyse the game.', BF, 'Discover a new way to analyse the game.'), music=(HT, 0, *TH))
E['r02'] = dict(old=[dict(dev='tvblack', osd=False, lines=[('d', 'BOOTING OLD ANALYSIS SYSTEM...'), ('d', 'MEMORY TEST ...... 640K OK'), ('d', 'LOADING NOTEBOOK.EXE')]),
                     dict(dev='tvblack', osd=False, lines=[('r', 'ERROR 404: TIME NOT FOUND.'), (' ', ''), ('r', 'ERROR 503: WORKFLOW OVERLOADED.'), (' ', ''), ('r', 'ERROR 001: OUTDATED METHODS'), ('r', 'DETECTED.')]),
                     dict(dev='tvblue' if False else 'tv', osd='■ HALT', js="BOX(0,0,W,H,'background:#0000aa', TX(80,H*.3,64,'A fatal exception has occurred.\\n\\nThe current analysis method\\nhas stopped responding.\\n\\nPress any key to upgrade_',{color:'#fff'}))", dur=2.6),
                     dict(osd='⟳ UPDATE', lines=[('g', 'SYSTEM UPDATE FOUND'), (' ', ''), ('H', 'UPDATE'), ('H', 'YOUR GAME.')], voz='Update your game.')],
                app=[('reg-3', 'Every shot.', None, .45, .52), ('res-0', 'Every half.', None, .1, .35), ('fF', 'Every minute.', None, 0, .15)],
                end=('Welcome to a new era<br>of sports analysis.', BF, 'Welcome to a new era of sports analysis.'), music=(SU, 0, *UN))
E['r03'] = dict(old=[NO, dict(osd='TELESHOP ●', lines=[('g', 'TELESHOP · CHANNEL 27'), (' ', ''), ('H', 'ARE YOU'), ('H', 'STILL'), ('H', 'ANALYSING'), ('H', 'THE OLD WAY?')], voz='Are you still analysing the old way?', sid=PRESENTER),
                     dict(osd='TELESHOP ●', js="DOODLE(W*.5-150, H*.42, 1.5, {mood:'panic', t}) + TX(80,H*.2,80,TYPE('TIRED OF\\nOUTDATED WORKFLOWS?',u,22),{font:'IT'})", voz='Are you tired of outdated workflows? Still wasting time with old methods?', sid=PRESENTER),
                     dict(osd='TELESHOP ●', lines=[('g', 'INTRODUCING'), (' ', ''), ('H', 'PROTEAM.'), ('v', 'A NEW WAY TO APPROACH'), ('v', 'SPORTS ANALYSIS.')], js="DOODLE(W*.62, H*.58, 1.2, {mood:'happy', t})", voz='Introducing ProTeam. A new way to approach sports analysis.', sid=PRESENTER)],
                app=[('reg-0', 'Live match.', None, .3, .4), ('reg-4', 'Goal or save.', None, .5, .56), ('cro-0', 'Full timeline.', None, 0, .15)],
                end=('BLACK FRIDAY.<br>TIME TO UPGRADE.', BF, 'Discover our Black Friday offer.'), music=(HT, 20, *TH))
E['r04'] = dict(old=[NO, dict(dev='tvblack', osd='SEARCH', lines=[('v', 'SEARCHING FOR SIGNAL...')], noise=True, dur=2.0),
                     dict(osd='CH 01', ch='CH 01', lines=[('H', 'OLD'), ('H', 'METHODS.')], dur=1.3),
                     dict(osd='CH 02', ch='CH 02', dev='tvred', lines=[('H', 'MANUAL'), ('H', 'WORKFLOWS.')], dur=1.3),
                     dict(osd='CH 03', ch='CH 03', dev='tvblack', lines=[('H', 'OUTDATED'), ('H', 'TECHNOLOGY.')], dur=1.3),
                     dict(dev='tvblack', osd='NO SIGNAL', noise=True, lines=[('v', 'NO SIGNAL')], dur=1.6),
                     dict(osd='CH 04', ch='CH 04', lines=[('g', 'SIGNAL FOUND.'), (' ', ''), ('H', 'PROTEAM'), ('H', 'CONNECTED.')], voz='Signal found. ProTeam connected.')],
                app=[('mo-home', 'Connected.', None, 0, .1), ('reg-1', 'Live.', None, .42, .5)],
                end=('Tune into the future<br>of sports analysis.', BF, 'Tune into the future of sports analysis.'), music=(CL, 100, *TH))
E['r05'] = dict(old=[dict(osd='BEFORE', js="BOX(0,0,W,H,'',TX(80,300,90,'BEFORE',{font:'IT'}) + TX(80,430,62,TYPE('- PAPER STATS\\n- 3 SPREADSHEETS\\n- VHS TAPES\\n- MEMORY',u,26)) + DOODLE(W*.55,H*.55,1.3,{mood:'panic',t}))", voz='Before: paper stats, three spreadsheets and a box of tapes.', dur=None),
                     dict(osd='VHS ▶▶', js="BOX(0,0,W,H,'',TX(80,H*.4,96,TYPE('SAME GAME.\\nDIFFERENT\\nWORKFLOW.',u,18),{font:'IT'}))", voz='Same game. Different workflow.')],
                app=[('reg-1', 'After.', 'After: one app, live.', .42, .5), ('res-0', 'Same game.', None, .1, .35), ('fF', 'Different workflow.', None, 0, .15)],
                end=('Upgrade your<br>analysis.', BF, 'Upgrade your analysis.'), music=(SU, 20, *DE))
E['r06'] = dict(old=[dict(dev='nokia', lines=[('n', 'INCOMING'), ('n', 'CALL...'), (' ', ''), ('n', '☎ THE FUTURE')], valign='center', align='center', dur=2.4),
                     dict(osd='☎ RING', js="DOODLE(W*.5-160, H*.38, 1.6, {mood:'ok', arms:'phone', t})", voz='Hello? The future? You\'re calling us?'),
                     dict(osd='☎ CALL', lines=[('g', 'MESSAGE FROM THE FUTURE:'), (' ', ''), ('H', 'YOUR'), ('H', 'ANALYSIS'), ('H', 'NEEDS AN'), ('H', 'UPGRADE.')], voz='Your analysis needs an upgrade.', sid=26)],
                app=[('mo-home', 'Answer.', None, 0, .1), ('res-0', 'The future.', None, .1, .35)],
                end=('Answer the call.', BF, 'Answer the call.'), music=(HT, 35, *SY))
E['r07'] = dict(old=[dict(osd='POV', js="TX(80,320,84,TYPE('POV: YOU\\'RE A\\nSPORTS ANALYST.',u,22),{font:'IT'}) + DOODLE(W*.5-140,H*.48,1.4,{mood:'ok',t,glasses:true}) + BOX(W*.5-210,H*.48+300,420,220,'border:6px solid #fff;border-radius:10px')", dur=3.0),
                     dict(osd='POV', js="['FINDING THAT ONE PLAY.','ORGANISING ENDLESS VIDEOS.','REVIEWING THE SAME SEQUENCE.','ANOTHER MATCH REPORT.'].map((s,i)=>TX(80,560+i*120,58,TYPE(s,u-i*.9,30))).join('') + DOODLE(W*.5-140,H*.55,1.3,{mood:u>3?'panic':'ok',t})", dur=4.4),
                     dict(osd='❚❚ FREEZE', dev='tvblack', js="DOODLE(W*.5-140,H*.4,1.4,{mood:'frozen',t:0}) + TX(80,330,96,'WE NEED\\nAN UPDATE.',{font:'IT'})", dur=2.4)],
                app=[('cro-0', 'Every play.', None, 0, .2), ('res-1', 'Every player.', None, .2, .45), ('mo-week', 'Every week.', None, .05, .2)],
                end=('Work smarter.<br>Analyse better.', 'PROTEAM · PRO-TEAM.APP', 'Work smarter. Analyse better.'), music=(SU, 40, *SY))
E['r08'] = dict(old=[NO, dict(lines=[('g', 'BROADCAST · 1995'), (' ', ''), ('H', 'THE YEAR'), ('H', 'IS 1995.')], voz='The year is nineteen ninety-five.'),
                     dict(dev='tvblack', osd='◀◀ ERR', noise=False, lines=[('H', 'BUT THE'), ('H', 'GAME HAS'), ('H', 'CHANGED.')], voz='But the game has changed.'),
                     dict(osd='⟳', lines=[('H', 'SO SHOULD'), ('H', 'THE WAY WE'), ('H', 'ANALYSE IT.')], voz='So should the way we analyse it.')],
                app=[('mo-plan', 'Plan.', None, .02, .12), ('reg-1', 'Record.', None, .42, .5), ('res-0', 'Analyse.', None, .1, .35), ('fF', 'Control.', None, 0, .15)],
                end=('PROTEAM.<br>The new era of<br>sports analysis.', 'DISCOVER PROTEAM · PRO-TEAM.APP', 'ProTeam. The new era of sports analysis.'), music=(HT, 0, *TH))
WEATHER = "BOX(0,0,W,H,'background:linear-gradient(#0b2a8a,#0a1a55)', TX(60,150,64,'SPORTS ANALYSIS\\nWEATHER REPORT',{font:'IT'}) + BOX(80,H*.32,W-160,H*.36,'border:4px solid #7fb3ff;border-radius:40px 120px 60px 140px;background:rgba(80,140,255,.15)', TX(60,60,120,'☁ ⛈',{a:Math.min(1,u)}) + TX(60,230,56,TYPE('90% CHANCE OF\\nOUTDATED WORKFLOWS',u-.6,30)) ) + TX(80,H*.72,52,TYPE('HIGH LEVELS OF MANUAL WORK\\nLOW VISIBILITY ON PERFORMANCE',u-2.2,32),{color:'#ffd34d'}) + TX(80,H-260,34,'FICTIONAL FORECAST. HUMOUR, NOT DATA.',{color:'#9fb7ff'})"
E['r09'] = dict(old=[NO, dict(osd='LIVE ●', js=WEATHER, voz='Today\'s sports analysis forecast: ninety percent chance of outdated workflows, high levels of manual work, and low visibility on performance.'),
                     dict(osd='LIVE ●', lines=[('g', 'TOMORROW:'), (' ', ''), ('H', '☀ FORECAST:'), ('H', 'A BETTER'), ('H', 'WAY TO'), ('H', 'ANALYSE.')], voz='Forecast: a better way to analyse.')],
                app=[('res-0', 'Clear skies.', None, .1, .35), ('fF', 'Full visibility.', None, 0, .15)],
                end=('Get ready<br>for the future.', BF, 'Get ready for the future.'), music=(CL, 0, *UN))
E['r10'] = dict(old=[dict(osd='CH 01', ch='CH 01', lines=[('H', 'OLD'), ('H', 'METHODS.')], dur=1.2), dict(osd='CH 02', ch='CH 02', dev='tvred', lines=[('H', 'MANUAL'), ('H', 'ANALYSIS.')], dur=1.2),
                     dict(osd='CH 03', ch='CH 03', dev='tvblack', lines=[('H', 'OUTDATED'), ('H', 'TECHNOLOGY.')], dur=1.2), dict(osd='CH 04', ch='CH 04', lines=[('g', 'CH 04'), ('H', 'PROTEAM.')], dur=1.6)],
                app=[('mo-home', 'Finally,<br>the right channel.', None, 0, .1), ('reg-1', None, None, .42, .5)],
                end=('Tune into PROTEAM.', BF, 'Tune into ProTeam.'), music=(CL, 100, *TH))
LOADING = "TX(80,300,80,'ANALYSING MATCH...',{font:'IT'}) + BOX(80,420,W-160,70,'border:5px solid #fff', BOX(6,6,(W-180)*0.02,48,'background:#fff')) + TX(80,520,72,'2%') + TX(80,640,64,['MON','TUE','WED','THU','FRI','SAT','SUN','MON...'][Math.min(7,Math.floor(u*2))]+'  '+['09:00','13:00','18:00','23:59','03:12'][Math.floor(u*3)%5]) + DOODLE(W*.5-140,H*.5,1.4,{mood:u>2?'panic':'ok',t})"
E['r11'] = dict(old=[dict(dev='tvblack', osd=False, js=LOADING, voz='Analysing match. Two percent.', dur=4.6),
                     dict(dev='tvblack', osd=False, js=LOADING.replace("u>2?'panic':'ok'", "'frozen'"), dur=1.8),
                     dict(lines=[('H', 'THERE\'S A'), ('H', 'BETTER WAY.')], voz='There\'s a better way.')],
                app=[('reg-1', 'Live.', None, .42, .5), ('cro-0', 'Done.', None, 0, .2)],
                end=('Upgrade your<br>workflow.', BF, 'Upgrade your workflow.'), music=(SU, 30, *TH))
PLAY = "(()=>{const p=Math.min(1,u/2);return BOX(60,H*.22,W-120,H*.5,'border:5px solid #fff;border-radius:16px', '<svg class=\"a\" style=\"inset:0\" viewBox=\"0 0 800 900\"><g fill=\"none\" stroke=\"#fff\" stroke-width=\"5\"><rect x=\"40\" y=\"40\" width=\"720\" height=\"820\"/><path d=\"M40 450 H760\"/><circle cx=\"400\" cy=\"450\" r=\"90\"/></g>'+(u>2.4?'<g stroke=\"#ffd34d\" stroke-width=\"8\" fill=\"none\"><path d=\"M200 700 Q300 500 520 360\" stroke-dasharray=\"900\" stroke-dashoffset=\"'+(900-900*Math.min(1,(u-2.4)/1))+'\"/><circle cx=\"520\" cy=\"360\" r=\"'+(40*Math.min(1,(u-3)/.4))+'\"/><path d=\"M560 700 L600 420\" stroke-dasharray=\"300\" stroke-dashoffset=\"'+(300-300*Math.min(1,(u-3.2)/.8))+'\"/></g>':'')+'<g fill=\"#fff\">'+[[200,700],[560,700],[400,560],[300,300],[520,360]].map(([x,y])=>'<circle cx=\"'+x+'\" cy=\"'+(y-30*p)+'\" r=\"18\"/>').join('')+'</g></svg>') + TX(70,H*.75,90,u<2.2?TYPE('JUST ONE PLAY?',u,18):TYPE('THINK AGAIN.',u-2.2,18),{font:'IT'}) + (u>3.6?TX(70,H*.86,50,'xG 0.31 · 4 PASSES · 6.2 s',{color:'#ffd34d'}):'')})()"
E['r12'] = dict(old=[dict(osd='▶ PLAY', js=PLAY, voz='Just one play? Think again.', dur=5.2)],
                app=[('reg-2', 'Where.', 'Where it started.', .4, .5), ('reg-3', 'How.', 'Where it ended.', .45, .52), ('cro-0', 'When.', 'And when it happened.', 0, .2)],
                end=('See beyond<br>the game.', 'PROTEAM · PRO-TEAM.APP', 'See beyond the game.'), music=(SU, 0, *DE))
DATA = "(()=>{const v=Math.floor(Math.min(1,u/1.2)*67);return TX(W*.5-240,H*.25,260,v+'%',{font:'IT'}) + TX(80,H*.55,80,TYPE('DATA IS\\nJUST DATA?',u-1.2,16),{font:'IT'}) + (u>2.6?'<svg class=\"a\" style=\"left:80px;top:'+(H*.72)+'px\" width=\"'+(W-160)+'\" height=\"300\"><polyline fill=\"none\" stroke=\"#3dffa8\" stroke-width=\"8\" points=\"'+[0,1,2,3,4,5,6,7,8].map(i=>(i*(W-160)/8)+','+(250-[40,80,60,140,120,200,170,230,210][i]*Math.min(1,(u-2.6)/1.2))).join(' ')+'\"/></svg>':'')})()"
E['r13'] = dict(old=[dict(dev='tvblack', osd=False, js=DATA, voz='Data is just data?', dur=4.6),
                     dict(osd='▶', lines=[('H', 'UNTIL YOU'), ('H', 'UNDERSTAND'), ('H', 'THE STORY.')], voz='Until you understand the story.')],
                app=[('res-0', 'The story.', None, .1, .35), ('res-1', 'The players.', None, .2, .45), ('reg-3', 'The shots.', None, .45, .52)],
                end=('Discover the story<br>behind the game.', 'PROTEAM · PRO-TEAM.APP', 'Discover the story behind the game.'), music=(SU, 20, *SY))
OLDSCHOOL = "TX(80,320,84,'THE OLD SCHOOL\\nANALYST.',{font:'IT'}) + DOODLE(W*.5-150,H*.42,1.5,{mood:u>2.5?'panic':'ok',t,glasses:true}) + Array.from({length:Math.min(14,Math.floor(u*4))},(_, i)=>BOX(80+(i*97)%(W-300), H*.86-Math.floor(i/5)*90-((i*53)%40), 200, 70, 'background:'+(i%3?'#eee':'#111')+';border:4px solid #fff;transform:rotate('+((i*37)%20-10)+'deg)', TX(14,8,36,i%3?'PAPER':'VHS',{color:i%3?'#000':'#fff',glow:'none'}))).join('')"
E['r14'] = dict(old=[dict(osd='▶', js=OLDSCHOOL, voz='The old school analyst. Paper, pens, and a mountain of tapes.', dur=None)],
                app=[('mo-home', 'Let\'s talk about<br>an upgrade.', None, 0, .1), ('res-1', None, None, .2, .45)],
                end=('Meet PROTEAM.', 'PRO-TEAM.APP', 'Meet ProTeam.'), music=(HT, 25, *UN))
TALK = "TX(80,320,84,TYPE('WHAT IF YOUR\\nDATA COULD TALK?',u,20),{font:'IT'}) + ['EFFICIENCY 67%','SHOTS 39','SAVES 50%','LAST 10 MIN 5-3'].map((s,i)=>TX(80+Math.sin(t*2+i)*10,H*.5+i*110,64,s,{a:Math.min(1,Math.max(0,u-1.5-i*.3)),color:'#3dffa8'})).join('')"
E['r15'] = dict(old=[dict(osd='▶', js=TALK, voz='What if your data could talk? Look closer. Understand more. Discover what happens behind every play.', dur=None)],
                app=[('res-0', 'Look closer.', None, .1, .35), ('reg-3', 'Understand more.', None, .45, .52)],
                end=('Listen to the game.', 'PROTEAM · PRO-TEAM.APP', 'Listen to the game.'), music=(SU, 0, *DE))
COUNT = "TX(80,220,60,'TRANSMISSION STARTING...',{color:'#ffd34d'}) + TX(70,H*.35,230,(()=>{const s=Math.max(0,10-Math.floor(u*2.2));return '00:0'+(s>9?'':'')+Math.min(9,s)})(),{font:'VT'})"
E['r16'] = dict(old=[dict(dev='tvblack', osd='P100 TXT', js="BOX(0,0,W,H,'background:#000', TX(60,140,58,'P100  PROTEAM TXT  27 NOV',{color:'#0ff'}) + BOX(60,230,W-120,110,'background:#00f', TX(20,10,90,'BLACK FRIDAY',{color:'#ff0'})) + TX(70,400,64,TYPE('TRANSMISSION STARTING...',u,26),{color:'#fff'}) + TX(70,H*.42,240,'00:0'+Math.max(0,9-Math.floor(Math.max(0,u-1.2)*3)),{color:'#ff0'}))", dur=4.6),
                     dict(osd='⟳', lines=[('H', 'BLACK FRIDAY'), ('H', 'IS COMING.'), (' ', ''), ('v', 'YOUR UPGRADE IS WAITING.')], voz='Black Friday is coming. Your upgrade is waiting.')],
                app=[('mo-week', 'Stay tuned.', None, .05, .2)],
                end=('Stay tuned.', BF, 'Stay tuned.'), music=(CL, 60, *TH))
E['r17'] = dict(old=[NO, dict(lines=[('H', 'OUTDATED'), ('H', 'IS NOT A'), ('H', 'STRATEGY.')], voz='Outdated is not a strategy.'),
                     dict(dev='tvblack', osd='ERR', js=VHS_STACK, dur=2.4),
                     dict(osd='⟳', lines=[('H', 'THE GAME'), ('H', 'EVOLVES.'), ('H', 'YOUR TOOLS'), ('H', 'SHOULD TOO.')], voz='The game evolves. Your tools should too.')],
                app=[('reg-1', 'Evolve.', None, .42, .5), ('res-0', None, None, .1, .35)],
                end=('Move forward.', BF, 'Move forward.'), music=(SU, 40, *DE))
E['r18'] = dict(old=[NO, dict(osd='SPECIAL ●', lines=[('g', 'TONIGHT\'S'), ('H', 'SPECIAL'), ('H', 'FEATURE:'), (' ', ''), ('v', 'LIVE MATCH RECORDING')], voz='Tonight\'s special feature: live match recording.', sid=PRESENTER)],
                app=[('reg-1', 'Tap the player.<br>Tap the action.', 'Tap the player, then the action.', .42, .5), ('reg-3', 'Mark where<br>the shot goes.', 'Mark where the shot goes.', .45, .52),
                     ('res-0', 'Get the summary<br>by halves.', 'Get the summary by halves, the moment the match ends.', .1, .35)],
                end=('Discover more<br>about PROTEAM.', BF, 'Discover more about ProTeam.'), music=(HT, 10, *UN))
TWO = "BOX(30,H*.12,W-60,120,'',TX(0,0,72,'THE OLD SCHOOL VS\\nTHE NEW GENERATION.',{font:'IT'})) + BOX(30,H*.34,W*.46,H*.4,'background:#1f3cff;border-radius:30px/50px;box-shadow:0 0 40px #1f3cff', TX(30,40,48,TYPE('PAPER\\nVHS\\nEXCEL 97\\nMEMORY',u,10))) + BOX(W*.52,H*.34,W*.46,H*.4,'background:#f4f5f7;border-radius:30px;overflow:hidden', '<img src=\"../app/res-0.jpg\" style=\"width:100%;margin-top:-20%\">') + TX(W*.5-40,H*.5,90,'VS',{font:'IT',color:'#ffd34d'})"
E['r19'] = dict(old=[dict(dev='tvblack', osd=False, js=TWO, voz='The old school versus the new generation.', dur=None)],
                app=[('res-0', 'The game has<br>moved on.', 'The game has moved on.', .1, .35), ('fF', None, None, 0, .15)],
                end=('Join the new<br>generation.', BF, 'Join the new generation.'), music=(CL, 30, *TH))
E['r20'] = dict(old=[dict(dev='tvred', osd='REC ●', lines=[('g', 'CH 00'), (' ', ''), ('H', 'FINAL'), ('H', 'TRANSMISSION.')], voz='Final transmission.'),
                     dict(dev='tvred', osd='CH ▲▼', js="DOODLE(W*.5-150,H*.4,1.5,{mood:'panic',arms:'phone',t}) + TX(80,320,72,'CHANNEL '+String(Math.floor(u*6)%99).padStart(2,'0'),{color:'#fff'})", dur=2.4),
                     dict(dev='tvred', osd='REC ●', lines=[('H', 'YOUR BLACK'), ('H', 'FRIDAY'), ('H', 'UPGRADE IS'), ('H', 'ALMOST OVER.')], voz='Your Black Friday upgrade is almost over.')],
                app=[('mo-home', '6 months free.', 'Six months free for your first team. New accounts, no card, until the twenty-seventh at midnight.', 0, .1)],
                end=('Don\'t miss your<br>chance to upgrade.', BF, 'Don\'t miss your chance to upgrade.'), music=(HT, 40, *TH))
# vídeos de marca (75–85 s y 60–80 s)
E['v01'] = dict(old=[NO, dict(lines=[('g', 'BROADCAST'), (' ', ''), ('H', 'ONCE UPON'), ('H', 'A TIME...')], js=VHS_STACK.replace('H*.62', 'H*.82'), voz='For years, the game has been evolving.'),
                     dict(osd='▶', js=OLDSCHOOL, voz='New challenges. New demands. More information than ever before.', dur=None),
                     dict(osd='◀◀', lines=[('H', 'BUT SOME'), ('H', 'THINGS STAY'), ('H', 'THE SAME.')], voz='But some things stay the same.'),
                     dict(dev='tvred', osd='ERROR', js=ERROR, msg='The old way is no longer enough.', dur=3.6),
                     dict(dev='tvblack', osd='NO SIGNAL', noise=True, lines=[('v', 'NO SIGNAL')], dur=1.8)],
                app=[('mo-plan', 'New tools.', 'It\'s time to rethink the way we analyse the game.', .02, .12), ('mo-week', 'New perspectives.', None, .05, .2),
                     ('reg-1', 'New possibilities.', 'ProTeam brings technology and sports analysis together to help professionals understand the game in new ways.', .42, .5),
                     ('reg-3', None, None, .45, .52), ('res-0', None, None, .1, .35), ('res-1', None, None, .2, .45), ('fF', 'The game never<br>stops evolving.', None, 0, .15), ('mo-tests', None, None, 0, .12)],
                end=('PROTEAM.<br>The new era of<br>sports analysis.', 'DISCOVER PROTEAM · PRO-TEAM.APP', 'ProTeam. The new era of sports analysis.'), music=(HT, 0, *TH))
E['v02'] = dict(old=[NO, dict(osd='TELESHOP ●', lines=[('g', 'TELESHOP · BLACK FRIDAY 2026'), (' ', ''), ('H', 'WELCOME TO'), ('H', 'THE OLD'), ('H', 'SCHOOL OF'), ('H', 'SPORTS ANALYSIS.')], voz='Are you still analysing the old way?', sid=PRESENTER),
                     dict(osd='TELESHOP ●', js=OLDSCHOOL, voz='Still wasting time? Still using outdated workflows? Still doing things the hard way?', sid=PRESENTER, dur=None),
                     dict(dev='tvblack', osd='❚❚', lines=[('H', 'WAIT...'), ('H', 'THERE\'S AN'), ('H', 'UPDATE.')], voz=None, dur=2.6),
                     dict(osd='⟳ UPDATE', lines=[('g', 'INSTALLING PROTEAM'), (' ', ''), ('v', '██████████ 100%')], dur=1.6)],
                app=[('mo-home', 'Introducing<br>PROTEAM.', 'Introducing ProTeam. A smarter way to approach sports analysis.', 0, .1), ('reg-1', 'Live match<br>recording.', None, .42, .5),
                     ('reg-3', 'Shot maps.', None, .45, .52), ('res-0', 'Summary<br>by halves.', None, .1, .35), ('fF', 'Load control.', None, 0, .15),
                     ('mo-week', 'BLACK FRIDAY 2026.<br>Time to upgrade.', 'This Black Friday, it\'s time to leave the old methods behind. Six months free for your first team. New accounts, no card, until November twenty-seventh at midnight.', .05, .2)],
                end=('Your team has evolved.<br>Your analysis should too.', BF, 'Discover the Black Friday offer.'), music=(HT, 20, *TH))

if __name__ == '__main__':
    for k, e in E.items():
        # el mensaje del cuadro de error va dentro del bloque
        for b in e['old']:
            if 'msg' in b: b['js'] = b['js'].replace('Ly.msg', json.dumps(b['msg']))
        kw = dict(minapp=5.2, minold=4.0) if k in ('v01', 'v02') else {}
        build(k, e['old'], e['app'], e['end'], e['music'], **kw)
        if k in ('v01', 'v02'): build(k + '_h', e['old'], e['app'], e['end'], e['music'], hz=True, **kw)
