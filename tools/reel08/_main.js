const T = window.TIMES; window.DUR = T.END;
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const lerp = (a, b, p) => a + (b - a) * p;
const E = { out: p => 1 - Math.pow(1 - p, 3), out5: p => 1 - Math.pow(1 - p, 5), in: p => p * p * p, io: p => p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2 };
const $ = id => document.getElementById(id);
const show = (el, v) => { el.style.display = v ? (el._d || 'block') : 'none'; };
const IMG = n => `/tools/reel08/img/${n}.jpg`;
const mk = (tag, css, html, parent) => { const d = document.createElement(tag); if (css) d.style.cssText = css; if (html != null) d.innerHTML = html; (parent || $('txt')).appendChild(d); return d; };
function ph(src, pos = '50% 30%') {
  const d = document.createElement('div'); d.className = 'ph';
  const i = document.createElement('img'); i.src = IMG(src); i.style.objectPosition = pos; d.appendChild(i);
  const s = document.createElement('div'); s.className = 'sh'; d.appendChild(s); d._img = i; d._sh = s;
  $('phs').appendChild(d); return d;
}
function place(el, x, y, w, h, o = {}) {
  el.style.left = x + 'px'; el.style.top = y + 'px'; el.style.width = w + 'px'; el.style.height = h + 'px';
  el.style.transform = `translate(${o.dx || 0}px,${o.dy || 0}px) rotate(${o.rot || 0}deg) scale(${o.s || 1})`;
  el.style.opacity = o.op == null ? 1 : o.op; el.style.zIndex = o.z || 1; el.style.filter = o.blur ? `blur(${o.blur}px)` : 'none';
  if (el._img) el._img.style.transform = `scale(${o.is || 1.06}) translate(${o.ix || 0}px,${o.iy || 0}px)`;
  if (el._sh) el._sh.style.background = `rgba(0,0,0,${o.dark || 0})`;
}
function tx(html, y, cls, size) {
  const d = document.createElement('div'); d.className = 'tx ' + cls; d.style.top = y + 'px'; d.style.fontSize = size + 'px'; d.innerHTML = html; $('txt').appendChild(d); return d;
}
function reveal(el, p, dir = 'up') {
  el.querySelectorAll('.mask>span').forEach((s, i, a) => { const q = E.out5(clamp(p * (1 + .25 * (a.length - 1)) - .25 * i));
    s.style.transform = dir === 'up' ? `translateY(${(1 - q) * 110}%)` : `translateX(${(q - 1) * 105}%)`; });
}
const M = s => `<span class="mask"><span>${s}</span></span>`;

// ── 1 · GANCHO: Dika Mem armando el brazo + «TU 6:0 GANA EN INFANTILES.» desde el fotograma 0 ──
const MEM = ph('mem', '50% 30%');
const tH1 = tx(M('TU 6:0'), 250, 'M8 shadow', 230);
const tH2 = tx(M('GANA EN INFANTILES.'), 500, 'M8 shadow', 84);
const tPRO = tx(M('<span class="S" style="color:#9db8ff">Ese es el</span>') + ' ' + M('<span class="S" id="pw" style="display:inline-block;color:#fff">problema.</span>'), 1360, 'shadow', 130);
function hook(t) {
  const b = T.la - .06, v = t < b; show(MEM, v); show(tH1, v); show(tH2, v); show(tPRO, v && t >= T.ese - .08); if (!v) return;
  const p = E.out5(seg(t, 0, .45)), hit = Math.exp(-Math.pow((t - T.prob - .06) / .12, 2));
  place(MEM, 0, 0, 1080, 1920, { s: 1 + (1 - p) * .08 + .03 * hit, is: 1.14 - .06 * seg(t, 0, b), iy: 18 * seg(t, 0, b), dark: .4 + .12 * seg(t, T.ese - .2, T.ese + .2), z: 1 });
  reveal(tH1, 1); reveal(tH2, 1); reveal(tPRO, seg(t, T.ese - .08, T.ese + .3));
  tH1.style.transform = `scale(${1 + .05 * (1 - p)})`; $('pw').style.transform = `scale(${1 + .14 * hit})`;
  const out = seg(t, b - .1, b); [MEM, tH1, tH2, tPRO].forEach(e => e.style.opacity = 1 - out);
}

// ── Pista cenital de balonmano (6 m y 9 m) con seis marcas ──
const NS = 'http://www.w3.org/2000/svg';
const CT = document.createElementNS(NS, 'svg'); CT.setAttribute('viewBox', '0 0 1080 1920'); CT.style.cssText = 'position:absolute;inset:0;width:1080px;height:1920px;display:none'; $('cards').appendChild(CT);
const ln = (d, c = '#2a3040', w = 6, dash) => { const p = document.createElementNS(NS, 'path'); p.setAttribute('d', d); p.setAttribute('fill', 'none'); p.setAttribute('stroke', c); p.setAttribute('stroke-width', w); p.setAttribute('stroke-linecap', 'round'); if (dash) p.setAttribute('stroke-dasharray', dash); CT.appendChild(p); return p; };
const GY = 1480;
ln(`M40 ${GY} H1040 M40 ${GY} V860 M1040 ${GY} V860`, '#232937', 5);
const L6 = ln(`M165 ${GY} A 300 300 0 0 1 465 ${GY - 300} L 615 ${GY - 300} A 300 300 0 0 1 915 ${GY}`, '#3a4256', 7);
const L9 = ln(`M40 ${GY - 120} A 450 450 0 0 1 465 ${GY - 450} L 615 ${GY - 450} A 450 450 0 0 1 1040 ${GY - 120}`, '#3a4256', 5, '22 18');
ln(`M465 ${GY} H615`, '#8a93a6', 16);
const LAB6 = mk('div', `position:absolute;left:880px;top:${GY - 250}px;font-family:M;font-weight:800;font-size:30px;letter-spacing:.1em;color:#5d6475;display:none`, '6 m', $('cards'));
const LAB9 = mk('div', `position:absolute;left:950px;top:${GY - 420}px;font-family:M;font-weight:800;font-size:30px;letter-spacing:.1em;color:#5d6475;display:none`, '9 m', $('cards'));
const P60 = [[141, GY - 87], [297, GY - 290], [500, GY - 335], [580, GY - 335], [783, GY - 290], [939, GY - 87]];
const P33 = [[200, GY - 120], [300, GY - 470], [540, GY - 330], [540, GY - 560], [780, GY - 470], [880, GY - 120]];
const MKS = P60.map(() => { const d = mk('div', '', '', $('cards')); d.className = 'mk'; return d; });
const ATT = mk('div', '', '', $('cards')); ATT.className = 'att';
function court(t, op) {
  show(CT, true); show(LAB6, true); show(LAB9, true); CT.style.opacity = op; LAB6.style.opacity = LAB9.style.opacity = op;
}
function setMk(pos, op, grey) { MKS.forEach((m, i) => { show(m, op > 0); m.style.left = pos[i][0] + 'px'; m.style.top = pos[i][1] + 'px'; m.style.opacity = op * (m._o == null ? 1 : m._o); m.style.background = grey ? '#3a4256' : '#2f6bff'; m.style.borderColor = grey ? '#5d6475' : '#dfe7ff'; m.style.boxShadow = grey ? 'none' : ''; }); }

// ── 2 · LA MURALLA: foto real de una defensa → pista; nadie sale al atacante ──
const WALL = ph('muralla', '50% 55%');
const tMU = tx(M('LA MURALLA AGUANTA.'), 300, 'M8', 96);
const tNA = tx(M('<span class="S blue" style="position:relative;display:inline-block">nadie<span class="uline" id="ul" style="bottom:-4px;height:8px"></span></span>') + ' ' + M('<span class="S" style="color:#f2f1ec">aprende el 1×1.</span>'), 450, '', 110);
function wall(t) {
  const a = T.la - .06, b = T.eu - .06, v = t >= a && t < b; show(WALL, v && t < T.agu + .3); show(tMU, v); show(tNA, v && t >= T.nadie - .1);
  if (!v) return; show($('sysL'), true);
  const ph1 = seg(t, T.agu - .05, T.agu + .3);
  if (t < T.agu + .3) place(WALL, 0, 0, 1080, 1920, { s: 1 + .04 * seg(t, a, T.agu) + .1 * ph1, is: 1.3, dark: .45 + .4 * ph1, op: 1 - E.io(ph1), z: 3 });
  court(t, E.out(ph1));
  MKS.forEach((m, i) => { const s0 = T.agu - .05 + i * .07; const q = E.out5(seg(t, s0, s0 + .2)); m._o = q; m.style.transform = `scale(${1.6 - .6 * q})`; });
  setMk(P60, 1);
  const ap = seg(t, T.nadie - .05, T.uno1 + .25); show(ATT, ap > 0); ATT.style.left = lerp(80, 1000, E.io(ap)) + 'px'; ATT.style.top = (GY - 470) + 'px';
  MKS.forEach((m, i) => { const near = Math.exp(-Math.pow((parseFloat(ATT.style.left) - P60[i][0]) / 90, 2)) * (ap > 0 && ap < 1 ? 1 : 0); m.style.boxShadow = `0 0 0 ${near * 14}px rgba(47,107,255,.25)`; });
  reveal(tMU, seg(t, a, a + .35)); reveal(tNA, seg(t, T.nadie - .1, T.nadie + .25));
  $('ul').style.transform = `scaleX(${E.out(seg(t, T.apr, T.apr + .35))})`;
  const out = seg(t, b - .1, b); tMU.style.opacity = tNA.style.opacity = 1 - out; ATT.style.opacity = 1 - out;
}

// ── 3 · LA NORMA: «infantil: defensa en 2 líneas» → las marcas pasan a 3:3 ──
const tIN = tx(`<div class="kick">${M('EN EUSKADI, UN INFANTIL')}</div>` + M('DEFIENDE EN') + ' ' + M('<span class="blue">2 LÍNEAS</span>'), 290, 'M8', 100);
const tSRC = mk('div', 'position:absolute;left:0;width:1080px;top:1545px;text-align:center;font-family:M;font-weight:500;font-size:34px;color:#8a93a6;display:none', 'Juegos Escolares de Euskadi · normativa 2025');
function norma(t) {
  const a = T.eu - .06, b = T.esta - .06, v = t >= a && t < b; show(tIN, v); show(tSRC, v && t >= T.inf - .2); if (!v) return;
  show($('sysL'), true); court(t, 1);
  const mv = E.io(seg(t, T.dos - .1, T.dos + .45));
  MKS.forEach((m, i) => { m._o = 1; m.style.transform = `scale(${1 + .25 * Math.sin(Math.PI * seg(t, T.dos - .1 + i * .03, T.dos + .4))})`; });
  setMk(P60.map((p, i) => [lerp(p[0], P33[i][0], mv), lerp(p[1], P33[i][1], mv)]), 1);
  reveal(tIN, seg(t, a, a + .4)); tSRC.style.opacity = E.out(seg(t, T.inf - .2, T.inf + .2));
  const ring = seg(t, T.lin, T.elin + .3); L9.setAttribute('stroke', ring > 0 ? '#2f6bff' : '#3a4256');
  const out = seg(t, b - .1, b); tIN.style.opacity = tSRC.style.opacity = 1 - out; CT.style.opacity = 1 - out; MKS.forEach(m => m.style.opacity = 1 - out); LAB6.style.opacity = LAB9.style.opacity = 1 - out;
}

// ── 4 · ESTA SEMANA: Karabatić + ficha guardable ──
const KAR = ph('karabatic', '50% 25%');
const FI = mk('div', 'position:absolute;left:100px;top:620px;width:880px;height:620px;background:#fbfaf6;border-radius:30px;box-shadow:0 40px 90px rgba(0,0,0,.45);display:none;overflow:hidden', '', $('cards'));
mk('div', 'position:absolute;left:60px;top:50px;font-family:M;font-weight:800;font-size:34px;letter-spacing:.14em;color:#8a877e', 'ESTA SEMANA', FI);
mk('div', 'position:absolute;right:60px;top:42px;padding:8px 20px;border-radius:999px;background:#2f6bff;font-family:M;font-weight:800;font-size:26px;letter-spacing:.08em;color:#fff', 'GUÁRDALO', FI);
mk('div', 'position:absolute;left:60px;right:60px;top:118px;height:3px;background:#e4e0d4', '', FI);
const FR = [['10′ de 1×1', 'sin ayudas, cada entreno'], ['Después, 2 líneas', '3:3 o 5:1 antes que 6:0']].map(([h, s], i) => { const r = mk('div', `position:absolute;left:60px;right:60px;top:${160 + i * 220}px;height:200px;border-bottom:${i < 1 ? '2px solid #ece8de' : 'none'}`, '', FI);
  mk('div', 'position:absolute;left:0;top:30px;font-family:M;font-weight:800;font-size:96px;color:#2f6bff;line-height:1', String(i + 1), r);
  mk('div', 'position:absolute;left:100px;top:34px;font-family:M;font-weight:800;font-size:86px;letter-spacing:-.035em;color:#0d0f14;line-height:1', h, r);
  mk('div', 'position:absolute;left:102px;top:132px;font-family:M;font-weight:500;font-size:38px;color:#6d6a62', s, r); return r; });
const tES = tx(M('<span class="S" style="color:#fff">lo que haría yo el martes:</span>'), 380, 'shadow', 92);
function week(t) {
  const a = T.esta - .06, b = T.el6 - .06, v = t >= a && t < b; show(KAR, v); show(FI, v); show(tES, v); if (!v) return;
  place(KAR, 0, 0, 1080, 1920, { s: 1 + .05 * (1 - E.out5(seg(t, a, a + .4))), is: 1.1 + .05 * seg(t, a, b), dark: .58, z: 1 });
  const p = E.out5(seg(t, a + .05, a + .5)); FI.style.transform = `translateY(${(1 - p) * 700}px) rotate(${(1 - p) * 4}deg) scale(${1 + .02 * seg(t, a, b)})`;
  reveal(tES, seg(t, a, a + .35));
  FR.forEach((r, i) => { const s0 = [T.diez, T.sin + .35][i] - .1; const q = E.out5(seg(t, s0, s0 + .3)); r.style.opacity = .12 + .88 * q; r.style.transform = `translateX(${(1 - q) * -24}px)`; });
  const out = seg(t, b - .1, b); FI.style.opacity = tES.style.opacity = KAR.style.opacity = 1 - out;
}

// ── 5 · CIERRE: las seis vuelven a la línea y se apagan; «6:0 puede esperar a cadetes» ──
const tSX = tx(M('6:0'), 230, 'M8', 300);
const tCA = tx(M('<span class="S blue">puede esperar a cadetes.</span>'), 590, '', 104);
function wait(t) {
  const a = T.el6 - .06, b = T.com - .06, v = t >= a && t < b; show(tSX, v); show(tCA, v && t >= T.el6 + .4); if (!v) return;
  show($('sysL'), true); court(t, E.out(seg(t, a, a + .25)));
  const back = E.io(seg(t, a, a + .5)), grey = t >= T.cad;
  MKS.forEach((m, i) => { m._o = 1; m.style.transform = `scale(${1 - .15 * seg(t, T.cad, T.cad + .3)})`; });
  setMk(P60.map((p, i) => [lerp(P33[i][0], p[0], back), lerp(P33[i][1], p[1], back)]), 1, grey);
  reveal(tSX, seg(t, a, a + .35)); reveal(tCA, seg(t, T.el6 + .4, T.el6 + .75));
  tSX.style.color = grey ? '#5d6475' : '#fff';
  const out = seg(t, b - .1, b); tSX.style.opacity = tCA.style.opacity = CT.style.opacity = 1 - out; MKS.forEach(m => m.style.opacity = 1 - out); LAB6.style.opacity = LAB9.style.opacity = 1 - out;
}

// ── 6 · LA APP: captura real de Semana ──
const PHN = mk('div', 'position:absolute;left:310px;top:540px;width:460px;height:940px;border-radius:60px;background:#0b0d12;border:3px solid #2a3040;padding:14px;display:none;box-shadow:0 40px 90px rgba(0,0,0,.6)',
  '<div style="position:relative;width:100%;height:100%;border-radius:46px;overflow:hidden;background:#f6f6f4"><div id="sA" style="position:absolute;left:0;top:0;width:100%"><img src="/tools/reel08/img/semana.jpg" style="width:100%;display:block"><div id="hl1" style="position:absolute;left:2%;top:7.2%;width:96%;height:16.4%;border:5px solid #2f6bff;border-radius:18px;opacity:0;box-shadow:0 0 0 999px rgba(13,15,20,.0)"></div><div id="hl2" style="position:absolute;left:2%;top:25.6%;width:96%;height:11.4%;border:5px solid #2f6bff;border-radius:18px;opacity:0"></div></div></div>', $('phones'));
const tCO = tx(`<div class="kick">${M('COMENTA')}</div>` + M('CATEGORÍA + DÍAS'), 262, 'M8', 100);
const tWK = tx(M('<span class="S blue">te preparo la semana</span>'), 1505, '', 96);
const tAPP = tx(M('<span class="S" style="color:#f2f1ec">en la app de</span>') + ' ' + M('<span class="S blue">ProTeam.</span>'), 1505, '', 96);
function app(t) {
  const a = T.com - .06, b = T.lista - .06, v = t >= a && t < b; show(PHN, v); show(tCO, v); show(tWK, v && t >= T.te - .1 && t < T.app - .2); show(tAPP, v && t >= T.app - .2); if (!v) return;
  show($('sysL'), true);
  const p = E.out5(seg(t, a, a + .45)), cam = seg(t, a, b), out = seg(t, b - .12, b);
  const z = E.io(seg(t, T.te - .1, T.te + .5));
  PHN.style.transform = `translateY(${(1 - p) * 600 - 30 * cam + 120 * z}px) scale(${1 + .03 * cam + .22 * z})`; PHN.style.opacity = 1 - out;
  $('sA').style.transform = `translateY(${-6 * seg(t, a, T.te)}px)`;
  $('hl1').style.opacity = E.out(seg(t, T.sem - .1, T.sem + .2)); $('hl2').style.opacity = E.out(seg(t, T.app - .1, T.app + .2));
  reveal(tCO, seg(t, a, a + .4)); reveal(tWK, seg(t, T.te - .1, T.te + .25)); reveal(tAPP, seg(t, T.app - .2, T.app + .15));
  tCO.style.opacity = tWK.style.opacity = tAPP.style.opacity = 1 - out;
}

// ── 8 · RETO: vuelta a Dika Mem (bucle) + pregunta para el segundo ──
const MEM2 = ph('mem', '50% 30%');
const tPR = tx(`<div class="kick" style="color:#e6e8ee">${M('PREGÚNTALE A TU SEGUNDO')}</div>`, 330, 'shadow', 40);
const tQ1 = tx(M('¿Cuántos 1×1'), 430, 'M8 shadow', 120);
const tQ2 = tx(M('<span class="S" style="color:#9db8ff">defendieron el sábado?</span>'), 590, 'shadow', 104);
const ROW = [0, 1, 2, 3, 4, 5].map(i => { const d = mk('div', `position:absolute;left:${265 + i * 110}px;top:1340px;width:66px;height:66px;border-radius:50%;background:#2f6bff;border:5px solid #dfe7ff;display:none`, '', $('txt')); return d; });
function reto(t) {
  const a = T.preg - .06, v = t >= a; show(MEM2, v); show(tPR, v); show(tQ1, v && t >= T.cuan - .1); show(tQ2, v && t >= T.defe - .1); ROW.forEach(r => show(r, v && t >= T.uno3 - .1)); if (!v) return;
  const p = E.out5(seg(t, a, a + .45));
  place(MEM2, 0, 0, 1080, 1920, { s: 1 + (1 - p) * .06, is: 1.2 - .08 * seg(t, a, T.END), iy: 18, dark: .62, z: 2 });
  reveal(tPR, seg(t, a, a + .35)); reveal(tQ1, seg(t, T.cuan - .1, T.cuan + .25)); reveal(tQ2, seg(t, T.defe - .1, T.defe + .25));
  ROW.forEach((r, i) => { const q = E.out5(seg(t, T.uno3 - .1 + i * .05, T.uno3 + .15 + i * .05)); const st = i === 3 ? E.out5(seg(t, T.sab, T.sab + .4)) : 0;
    r.style.opacity = q; r.style.transform = `translateY(${(1 - q) * 40 - 150 * st}px) scale(${1 + .2 * st})`; });
  const fo = seg(t, T.END - .5, T.END); $('st').style.opacity = 1 - .0 * fo;
}
