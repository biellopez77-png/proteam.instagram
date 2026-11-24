"""Pasa un reel explicativo del estilo papel (v3) a la estética v4 (oscuro, duotono, Plus Jakarta Sans).
python3 tools/reel_v6/reskin.py tools/reel_v4/d2-portera.html tools/reel_v6/d2-portera.html"""
import re,sys,colorsys
src,out=sys.argv[1],sys.argv[2]; s=open(src).read()
J='/tools/reel_v5/node_modules/@fontsource/plus-jakarta-sans/files/plus-jakarta-sans-latin-'
s=re.sub(r'/tools/fonts/manrope-latin-(\d+)-normal\.woff2',lambda m:J+(m.group(1) if m.group(1) in('500','700','800') else '700')+'-normal.woff2',s)
def hx(h):
    h=h.lstrip('#'); h=''.join(c*2 for c in h) if len(h)==3 else h; return tuple(int(h[i:i+2],16)/255 for i in (0,2,4))
def mapc(m):
    pre,h=m.group(1),m.group(2)
    r,g,b=hx(h); hh,l,sat=colorsys.rgb_to_hls(r,g,b)
    if sat>.35 and l>.2 and l<.85:
        deg=hh*360
        if 190<deg<260: return pre+'#6AA8FF'
        if 260<=deg<300: return pre+'#8B5CF6'
        return pre+'#B9E0FF'   # rojos, amarillos, verdes → hielo
    if l>.88: return pre+('#02050F' if 'background' in pre and ('html' in m.string[max(0,m.start()-80):m.start()] or '#st' in m.string[max(0,m.start()-80):m.start()]) else '#0C1323' if 'background' in pre or 'fill' in pre else '#F4F7FB')
    if l<.18: return pre+('#F4F7FB' if not ('background' in pre) else '#000')
    return pre+'#8f9bb8'
s=re.sub(r'((?:background|color|fill|stroke|border[^:;]*|text-shadow|box-shadow)\s*[:=]\s*"?[^;"#]*?)(#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b)',mapc,s)
# sombras de halo claras en textos → oscuras
s=re.sub(r'text-shadow:[^;}]*',lambda m:'text-shadow:0 0 12px #02050F,0 0 30px #02050F,0 0 46px #02050F' if '#0C1323' in m.group(0) or '#F4F7FB' in m.group(0) else m.group(0),s)
css='''<style>html,body,#st{background:#02050F!important}#st{background:radial-gradient(ellipse at 50% 40%,#0C1323 0%,#02050F 72%)!important}
img{filter:url(#duo)!important}#grain{opacity:.16!important;mix-blend-mode:screen}</style>
<svg width="0" height="0" style="position:absolute"><filter id="duo" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values=".33 .33 .33 0 0 .33 .33 .33 0 0 .33 .33 .33 0 0 0 0 0 1 0"/><feComponentTransfer><feFuncR type="table" tableValues="0.008 0.18 0.416 0.957"/><feFuncG type="table" tableValues="0.02 0.235 0.659 0.969"/><feFuncB type="table" tableValues="0.059 0.667 1 0.984"/></feComponentTransfer></filter></svg>'''
s=s.replace('</head>',css+'</head>',1) if '</head>' in s else s.replace('<body>','<body>'+css,1)
# filtros de imagen puestos por script: añadir duotono delante
s=re.sub(r"(\.style\.filter\s*=\s*`)(grayscale)",r"\1url(#duo) \2",s)
s=re.sub(r"rgba\(2[3-5]\d, ?2[3-5]\d, ?2[2-5]\d, ?([.\d]+)\)",r"rgba(12,19,35,\1)",s)
s=s.replace("'#121212'","'#636DFF'").replace("'#17150f'","'#F4F7FB'").replace("'#111'","'#F4F7FB'")
open(out,'w').write(s); print('ok',out)
