"""10 posts y carruseles del brief (1080×1350). Diapositivas «viejas» = pantalla de tubo (screen.html + crt); «nuevas» = móvil 3D.
  python3 posts_brief.py  -> ../../feed/pXX-N.jpg"""
import os, json
from PIL import Image
from playwright.sync_api import sync_playwright
from photo import serve
import brand
OUT = '../../feed'; os.makedirs(OUT, exist_ok=True)
G = '0 0 10px rgba(61,255,168,.7)'
COND = '6 MONTHS FREE · FIRST TEAM · NEW ACCOUNTS<br>NO CARD · UNTIL 27 NOV 2026, 23:59 (MADRID)'
def L(text, size=110, font='IT', color=None):
    d = {'text': text, 'size': size, 'font': font, 'at': 0, 'cps': 999}
    if color: d.update(color=color, glow='0 0 10px ' + color + 'aa')
    return d
def old(dev, lines, mode='PLAY ▶', ch='CH 95', js=None, osd=True):
    lay = []
    if osd: lay.append({'t0': 0, 't1': 99, 'type': 'osd', 'ch': ch, 'mode': mode})
    if lines: lay.append({'t0': 0, 't1': 99, 'type': 'text', 'valign': 'flex-start', 'pad': '265px 90px', 'gap': 14, 'lines': lines})
    if js: lay.append({'t0': 0, 't1': 99, 'type': 'js', 'code': js})
    return {'w': 1080, 'h': 1350, 'd': '0', 'dur': 10, 'cut': 99, 'dev': [[0, dev]], 'layers': lay, 'app': []}
def new(img, big, small=None, s=.1, ry=-.3):
    w = f'<div class="a" style="left:60px;right:60px;top:70px;text-align:center;font-family:IT;font-weight:900;font-size:84px;letter-spacing:-.04em;color:#fff;line-height:1.02">{big}</div>'
    if small: w += f'<div class="a" style="left:40px;right:40px;bottom:46px;text-align:center;font-family:VT;font-size:42px;letter-spacing:.05em;color:#3dffa8;line-height:1.15">{small}</div>'
    return {'w': 1080, 'h': 1350, 'd': '0', 'dur': 30, 'cut': 0, 'trans': 1.0, 'dev': [[0, 'tv']], 'layers': [], 'pose': {'ry0': ry, 'y': -.013, 'far': .42},
            'app': [[0, img, s, s]], 'words': [[0, 99, w]]}
WIN = lambda title, body, btn='OK': f"BOX(W*.07,H*.3,W*.86,H*.4,'background:#c0c0c0;border:6px solid;border-color:#fff #404040 #404040 #fff;box-shadow:16px 16px 0 rgba(0,0,0,.45)', BOX(8,8,W*.86-28,64,'background:linear-gradient(90deg,#000080,#1084d0)', TX(18,6,44,'{title}',{{font:'Px'}})) + TX(40,110,68,'{body}',{{color:'#000',glow:'none'}}) + BOX(W*.43-110,H*.4-110,200,64,'border:4px solid;border-color:#fff #404040 #404040 #fff', TX(40,8,44,'{btn}',{{color:'#000',glow:'none'}})))"
TELE = lambda pag, title, body: f"BOX(0,0,W,H,'background:#000', TX(50,150,50,'P{pag}  PROTEAM TXT  NOV 26',{{color:'#0ff'}}) + BOX(50,230,W-100,110,'background:#00f', TX(20,8,86,'{title}',{{color:'#ff0'}})) + TX(60,420,92,'{body}',{{color:'#fff',w:W-120}}))"
PAPER = lambda title, body: f"BOX(0,0,W,H,'background:#ece6d6', TX(70,190,46,'PROTEAM MAGAZINE · VOL. 1995',{{color:'#7a6f5a',glow:'none'}}) + BOX(70,260,W-140,6,'background:#1d1d1d') + TX(70,300,96,'{title}',{{font:'IT',color:'#1d1d1d',glow:'none',w:W-140}}) + TX(70,H*.56,64,'{body}',{{color:'#2b2b2b',glow:'none',w:W-140}}))"
COURT = "'<svg class=\"a\" style=\"left:80px;top:'+(H*.3)+'px\" width=\"'+(W-160)+'\" height=\"'+(H*.5)+'\" viewBox=\"0 0 800 700\"><g fill=\"none\" stroke=\"#fff\" stroke-width=\"5\"><rect x=\"20\" y=\"20\" width=\"760\" height=\"660\"/><path d=\"M20 350 H780\"/><circle cx=\"400\" cy=\"350\" r=\"80\"/></g>'+(Ly.k>0?'<g stroke=\"#ffd34d\" stroke-width=\"8\" fill=\"none\"><path d=\"M180 600 Q300 420 520 260\"/><path d=\"M560 600 L600 300\" stroke-dasharray=\"20 14\"/></g>':'')+(Ly.k>1?'<g fill=\"#3dffa8\" font-family=\"VT\" font-size=\"44\"><text x=\"430\" y=\"230\">DECISION: SHOOT</text></g>':'')+(Ly.k>2?'<g fill=\"#ffd34d\" font-family=\"VT\" font-size=\"44\"><text x=\"60\" y=\"80\">6.2 s · 4 PASSES · 1 SHOT</text></g>':'')+'<g fill=\"#fff\">'+[[180,600],[560,600],[400,480],[300,250],[520,260]].map(([x,y])=>'<circle cx=\"'+x+'\" cy=\"'+y+'\" r=\"16\"/>').join('')+'</g></svg>'"
def court(k, title): return old('tv', [L(title, 92)], js=COURT.replace('Ly.k', str(k)))
P = {
 'p01': [old('tv', [L('THE GAME', 150), L('HAS', 150), L('CHANGED.', 150)]), old('tvblack', [L('THE WAY', 120), L('WE TRAIN', 120), L('HAS CHANGED.', 104)], mode='VHS ▶'),
         old('tvblack', None, js=TELE(200, 'COMPETITION', 'THE WAY WE COMPETE\\nHAS CHANGED.'), osd=False), old('tvred', [L('THE WAY WE', 110), L('ANALYSE', 110), L('SHOULD CHANGE', 92), L('TOO.', 110)], mode='⟳'),
         new('mo-home', 'PROTEAM.<br>Welcome to the new era.', 'PRO-TEAM.APP', s=0)],
 'p02': [old('tv', [L('ARE YOU', 150), L('STILL IN', 150), L('1995?', 150)]), old('tvblack', [L('C:\\> STILL WORKING', 84, 'VT', '#52ff8f'), L('WITH OUTDATED', 84, 'VT', '#52ff8f'), L('WORKFLOWS?', 84, 'VT', '#52ff8f'), L('Y/N_', 84, 'VT', '#52ff8f')], osd=False),
         old('nokia', [L('STILL SPENDING', 64, 'Px'), L('TOO MUCH TIME', 64, 'Px'), L('ORGANISING YOUR', 64, 'Px'), L('ANALYSIS?', 64, 'Px')], osd=False),
         old('tv', None, js=WIN('ANALYSIS.EXE', 'Still using tools that\\ndon’t evolve with\\nyour team?', 'NO'), osd=False), new('reg-1', 'Maybe it\'s time<br>for an upgrade.', 'PRO-TEAM.APP', s=.45)],
 'p03': [old('tv', None, js="BOX(0,0,W,H,'background:#0000aa', TX(80,H*.24,150,'ERROR 404',{font:'IT'}) + TX(80,H*.42,78,'MODERN SPORTS\\nANALYSIS NOT FOUND.',{font:'IT'}) + TX(80,H*.7,54,'Maybe you need to update\\nyour system._'))", osd=False)],
 'p04': [old('tv', None, js=PAPER('THE ANALYST\\nDICTIONARY.', 'Vol. 1: the shot map.'), osd=False), old('tv', None, js=PAPER('WHAT IS A\\nSHOT MAP?', 'Entry n.º 1'), osd=False),
         old('tv', None, js=PAPER('SHOT MAP', '(n.) A map of where every\\nshot was taken from, and\\nwhere it ended up. It shows\\npatterns you miss live.'), osd=False),
         new('reg-3', 'Example: where<br>each shot went.', 'EXAMPLE DATA · PROTEAM', s=.48), old('tv', [L('UNDERSTAND', 120), L('THE GAME', 120), L('BEYOND WHAT', 110), L('YOU SEE.', 120)])],
 'p05': [old('tv', None, js="BOX(0,0,W/2,H,'background:#1f3cff') + BOX(W/2,0,W/2,H,'background:#f2f3f5') + TX(50,H*.4,92,'OLD\\nSCHOOL',{font:'IT'}) + TX(W/2+50,H*.4,92,'NEW\\nSCHOOL',{font:'IT',color:'#111',glow:'none'}) + TX(W/2-50,H*.44,80,'VS',{font:'IT',color:'#ffd34d'})", osd=False),
         old('tvblack', [L('TRADITIONAL', 110), L('WORKFLOWS.', 110)], js="[0,1,2,3].map(i=>BOX(W*.2+i*30,H*.62-i*70,W*.6,60,'background:#111;border:4px solid #ddd',TX(20,6,40,'VHS · MATCH '+(i+1)))).join('')"),
         new('mo-week', 'Modern<br>workflows.', 'PRO-TEAM.APP', s=.08), old('tv', [L('DIFFERENT', 120), L('TOOLS.', 120), L('DIFFERENT', 120), L('POSSIBILITIES.', 92)]),
         old('tvred', [L('WHAT\'S', 150), L('YOUR NEXT', 130), L('MOVE?', 150)], mode='?')],
 'p06': [old('tv', None, js=WIN('SYSTEM UPDATE', 'SYSTEM UPDATE AVAILABLE.\\nPROTEAM BLACK FRIDAY.\\nTIME TO UPGRADE.', 'INSTALL') + " + TX(60,H*.78,40,'6 MONTHS FREE · FIRST TEAM · NEW ACCOUNTS\\nNO CARD · UNTIL 27 NOV 2026, 23:59 (MADRID)',{color:'#3dffa8'})", osd=False)],
 'p07': [court(0, 'BEHIND EVERY PLAY,<br>THERE\'S A STORY.'), court(1, 'MOVEMENTS.'), court(2, 'DECISIONS.'), court(3, 'DATA.'), old('tv', [L('ANALYSIS', 140), L('CHANGES', 140), L('EVERYTHING.', 124)])],
 'p08': [old('tv', [L('WHAT\'S IN', 130), L('YOUR', 130), L('ANALYSIS', 130), L('TOOLKIT?', 130)]), new('reg-1', 'Live match<br>recording.', 'TAP THE PLAYER · TAP THE ACTION', s=.45),
         new('reg-3', 'Shot and<br>goal maps.', 'WHERE EVERY SHOT GOES', s=.48), new('res-0', 'Summary<br>by halves.', 'PLUS THE LAST 10 MINUTES', s=.12), new('fF', 'Load control.', 'MINUTES × RPE, PLAYER BY PLAYER', s=.02),
         old('tv', [L('BUILD YOUR', 120), L('WORKFLOW', 120), L('WITH', 120), L('PROTEAM.', 120)])],
 'p10': [old('tvred', [L('FINAL', 160), L('TRANS-', 160), L('MISSION.', 160)], mode='REC ●', ch='CH 00'), old('tvred', [L('LAST CHANCE', 110), L('TO UPGRADE', 110), L('YOUR', 110), L('ANALYSIS.', 110)], mode='REC ●', ch='CH 00'),
         old('tvred', [L('PROTEAM', 120), L('BLACK FRIDAY.', 104), L(' ', 30), L('ENDS 27 NOV 2026, 23:59', 56, 'VT', '#3dffa8'), L('6 MONTHS FREE · FIRST TEAM', 56, 'VT'), L('NEW ACCOUNTS · NO CARD', 56, 'VT'), L('PRO-TEAM.APP', 64, 'VT')], mode='REC ●', ch='CH 00')],
}
port = serve()
with sync_playwright() as p:
    for k, slides in P.items():
        for n, sp in enumerate(slides, start=1):
            b, pgs = brand.pages(p, port, sp)
            Image.fromarray(brand.frame(pgs, sp, 6.0, n)).save(f'{OUT}/{k}-{n}.jpg', quality=93); b.close()
        print(k, len(slides))
