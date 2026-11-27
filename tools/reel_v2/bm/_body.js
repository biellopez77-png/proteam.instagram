// D1-B v2 · «El papel de Lehmann» · balonmano infantil · hook: shock con algo conocido (la chuleta del Mundial 2006, subastada por 1 M€)
// Escenas: A el papel real + contador del millón + Lehmann · B Mundial 2006: el papel por dentro + 4–2 · C tu portera 12/20
// D ¿desde dónde? pista con preguntas · E la hoja de seis zonas con rayas · F los dos papeles · G ProTeam · H cierre lista de espera (común)
window.GAIMG = 'portera';
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));
const K = { vendio: at('vendio'), millon: at('millon'), euros: en('euros'), portero: at('portero'), media: at('media'), mundial: at('mundial'),
  pen: at('penaltis'), arg: at('argentina'), lehmann: at('lehmann'), miraba: at('miraba'), apuntado: at('apuntado'), alemania: at('alemania'), paso: at('paso'),
  ahora: at('ahora'), portera: at('portera'), paro: at('paro'), marcaron: at('marcaron'), desde: at('desde'), nueve: at('nueve'), ext: at('extremos'),
  contra: at('contraataque'), nadie: at('nadie'), este2: at('este', 2), hoja: at('hoja'), seis: at('seis'), raya: at('raya'), gol: en('gol'), desc: at('descanso'),
  defensa: at('defensa'), tu3: at('papel', 3), pero: at('pero'), partido: at('partido'), apuntalo: at('apuntalo'), pt: at('proteam') };
// ── objetos: el papel real (dominio público), foto de Lehmann, portera ──
const PAPER = mk('div', 'position:absolute;left:110px;top:440px;width:860px;height:1111px;display:none;box-shadow:0 40px 90px rgba(0,0,0,.7);transform-origin:50% 50%;overflow:hidden',
  '<img src="/tools/reel_v2/img/papel.jpg" style="width:100%;height:100%;display:block"><div id="hls"></div>', $('cards'));
const HLS = PAPER.querySelector('#hls');
const ROWY = [283, 362, 517, 601, 764, 856, 923];
HLS.innerHTML = ROWY.map(y => `<div class="hl" style="position:absolute;left:400px;top:${y - 38}px;width:440px;height:76px;border:6px solid #2f6bff;border-radius:16px;background:rgba(47,107,255,.12);opacity:0"></div>`).join('');
const HL = [...HLS.querySelectorAll('.hl')];
const DESK = mk('div', 'position:absolute;inset:0;display:none;background:radial-gradient(110% 70% at 50% 35%,#20242e,#07080b 75%)', '', $('cards')); $('cards').prepend(DESK);
const LE = ph('lehmann', '50% 20%'), PO = ph('portera', '55% 35%');
const POL = mk('div', 'position:absolute;left:560px;top:1180px;width:430px;height:560px;background:#fbfaf6;padding:22px 22px 90px;display:none;box-shadow:0 30px 60px rgba(0,0,0,.6)',
  '<div style="width:100%;height:100%;background:url(/tools/reel_v2/img/lehmann.jpg) 50% 18%/cover"></div><div style="position:absolute;left:0;right:0;bottom:26px;text-align:center;font-family:M;font-weight:700;font-size:30px;color:#0d0f14;letter-spacing:.04em">Jens Lehmann</div>', $('cards'));
// ── A · hook ──
const aM = tx('0 €', 120, 'M8 shadow', 150);
const aS = tx(M('<span class="S blue">por un papel.</span>'), 285, 'shadow', 96);
const aE = tx(M('escondido en la media.'), 1790, 'M8 shadow', 70);
function sA(t) {
  const v = t < K.mundial - .1; [aM, aS, aE].forEach(e => show(e, v)); show(POL, v); if (!v) return;
  show(DESK, true); show(PAPER, true);
  const tuck = E.io(seg(t, K.media - .2, K.media + .45));
  PAPER.style.transform = `rotate(${-4 + 2 * tuck}deg) scale(${(1.02 - .03 * seg(t, 0, K.media)) * (1 - .62 * tuck)}) translate(${-60 * tuck}px,${300 * tuck}px)`;
  const q = E.out(seg(t, K.vendio - .1, K.euros)); const n = Math.round(1e6 * q); aM.textContent = t < K.vendio - .1 ? 'ESTE PAPEL' : n.toLocaleString('es-ES').replace(/ /g, '.') + ' €';
  if (n >= 1e6) aM.textContent = '1.000.000 €'; aM.style.transform = `scale(${pulse(t, K.euros - .1, .07)})`; aM.style.color = n >= 1e6 ? '#fff' : '#c9cfdb';
  show(aS, t >= K.euros - .2); reveal(aS, seg(t, K.euros - .2, K.euros + .15));
  const pp = E.out5(seg(t, K.portero - .1, K.portero + .3)); POL.style.opacity = pp; POL.style.transform = `translateY(${(1 - pp) * 140}px) rotate(${6 - 2 * pp}deg)`;
  show(aE, t >= at('escondido') - .1); reveal(aE, seg(t, at('escondido') - .1, at('escondido') + .2));
}
// ── B · Mundial 2006 ──
const bK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.2em">MUNDIAL 2006 · CUARTOS</div>', 1200, 'shadow', 40);
const bT = tx(M('ALEMANIA – ARGENTINA'), 1265, 'M8 shadow', 84);
const bP = tx(M('<span class="S blue">penaltis.</span>'), 1370, 'shadow', 150);
const TRAD = mk('div', 'position:absolute;left:120px;top:1470px;width:840px;display:none;font-family:M;font-weight:700;font-size:50px;color:#f2f1ec;text-align:center;line-height:1.4',
  '<span style="color:#7d8597">links</span> = izquierda &nbsp;·&nbsp; <span style="color:#7d8597">rechts</span> = derecha', $('cards'));
const STAMP = mk('div', 'position:absolute;left:140px;top:1500px;width:800px;height:200px;border:12px solid #2f6bff;border-radius:26px;display:none;font-family:M;font-weight:800;font-size:86px;color:#4f86ff;text-align:center;line-height:176px;white-space:nowrap;letter-spacing:-.03em;background:rgba(13,15,20,.85)', 'ALEMANIA PASA', $('cards'));
const bS = tx('<div class="kick" style="color:#c9cfdb;letter-spacing:.16em">4–2 EN LA TANDA</div>', 1730, 'shadow', 36);
function sB(t) {
  const a = K.mundial - .1, b = K.ahora - .1, v = t >= a && t < b; [bK, bT, bP, bS].forEach(e => show(e, false)); show(TRAD, false); show(STAMP, false); if (!v) return;
  const inPaper = t >= K.miraba - .15;
  if (!inPaper) { show(LE, true); place(LE, { is: 1.12 + .06 * seg(t, a, b), org: '50% 20%', grad: 'linear-gradient(180deg,rgba(0,0,0,.15) 35%,rgba(0,0,0,.9) 80%)' });
    show(bK, true); show(bT, true); show(bP, t >= K.pen - .1); bK.style.opacity = E.out(seg(t, a, a + .25)); reveal(bT, seg(t, K.arg - .3, K.arg + .1)); reveal(bP, seg(t, K.pen - .1, K.pen + .2)); return; }
  show(DESK, true); show(PAPER, true);
  const z = E.io(seg(t, K.miraba - .15, K.miraba + .35)); PAPER.style.top = (440 - 300 * z) + 'px'; PAPER.style.transform = `rotate(${-2 + 2 * z}deg) scale(${.9 + .22 * z})`;
  HL.forEach((h, i) => { const k = K.apuntado + i * .32; const q = E.out(seg(t, k, k + .2)); h.style.opacity = q * (t > K.alemania - .1 ? .35 : 1); h.style.transform = `scale(${1.15 - .15 * q})`; });
  show(TRAD, t >= K.apuntado + .4 && t < K.alemania - .1); TRAD.style.top = '1440px'; TRAD.style.opacity = E.out(seg(t, K.apuntado + .4, K.apuntado + .7));
  show(STAMP, t >= K.alemania - .1); const sq = E.out5(seg(t, K.alemania - .1, K.alemania + .15)); STAMP.style.opacity = sq; STAMP.style.top = '1420px'; STAMP.style.transform = `rotate(-7deg) scale(${1.6 - .6 * sq})`;
  show(bS, t >= K.paso); bS.style.top = '1740px'; bS.style.opacity = E.out(seg(t, K.paso, K.paso + .3));
}
// ── C · tu portera ──
const cK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.22em">AHORA, TU PORTERA</div>', 220, 'shadow', 44);
const STATS = mk('div', 'position:absolute;left:90px;top:1180px;width:900px;height:420px;display:none;font-family:M',
  ['PARADAS', 'GOLES'].map((l, i) => `<div style="position:absolute;left:${i * 470}px;top:0;width:430px;height:420px;border-radius:34px;background:${i ? '#2f6bff' : 'rgba(13,15,20,.88)'};border:3px solid ${i ? '#2f6bff' : '#262b36'};text-align:center">
   <div class="n" style="font-weight:800;font-size:230px;letter-spacing:-.05em;color:#fff;line-height:300px;font-variant-numeric:tabular-nums">0</div>
   <div style="font-weight:700;font-size:38px;letter-spacing:.16em;color:${i ? '#dfe7ff' : '#7d8597'}">${l}</div></div>`).join(''), $('cards'));
const SN = [...STATS.querySelectorAll('.n')];
function sC(t) {
  const a = K.ahora - .1, b = K.desde - .1, v = t >= a && t < b; show(cK, v); show(STATS, v); if (!v) return;
  show(PO, true); place(PO, { is: 1.15 + .07 * seg(t, a, b), org: '55% 35%', grad: 'linear-gradient(180deg,rgba(0,0,0,.5),rgba(0,0,0,.1) 30%,rgba(0,0,0,.2) 55%,rgba(0,0,0,.85))' });
  cK.style.opacity = E.out(seg(t, a, a + .3));
  [[K.paro, 12], [K.marcaron, 20]].forEach(([k, n], i) => { const q = E.out(seg(t, k - .05, k + .5)); SN[i].textContent = Math.round(n * q); SN[i].parentNode.style.opacity = E.out(seg(t, k - .1, k + .15));
    SN[i].parentNode.style.transform = `translateY(${(1 - E.out5(seg(t, k - .1, k + .2))) * 60}px) scale(${pulse(t, k + .4, .06)})`; });
}
// ── pista de balonmano (cenital, portería arriba) ──
const HB = mk('div', 'position:absolute;inset:0;display:none;background:radial-gradient(120% 80% at 50% 30%,#1d2a46,#0b0f18 72%)',
  `<svg viewBox="0 0 1080 1920" style="position:absolute;inset:0;width:100%;height:100%"><g fill="none" stroke="rgba(230,232,238,.32)" stroke-width="7">
   <line x1="40" y1="300" x2="1040" y2="300"/><path d="M180 300 A170 170 0 0 0 350 470 L730 470 A170 170 0 0 0 900 300"/>
   <path d="M60 300 A260 260 0 0 0 320 640 L760 640 A260 260 0 0 0 1020 300" stroke-dasharray="26 22"/><line x1="40" y1="1700" x2="1040" y2="1700"/></g>
   <rect x="440" y="270" width="200" height="30" fill="#e6e8ee"/><g id="hbl"></g></svg>`, $('cards'));
const HBL = HB.querySelector('#hbl');
const chip = (h, x, y) => { const d = mk('div', `position:absolute;left:${x}px;top:${y}px;transform:translate(-50%,-50%);display:none;padding:22px 36px;border-radius:999px;background:#2f6bff;color:#fff;font-family:M;font-weight:800;font-size:52px;white-space:nowrap;box-shadow:0 16px 40px rgba(0,0,0,.5)`, h, $('cards')); return d; };
const CH = [[K.nueve, chip('¿9 metros?', 540, 820)], [K.ext, chip('¿Extremos?', 250, 470)], [K.ext + .15, chip('¿Extremos?', 830, 470)], [K.contra, chip('¿Contraataque?', 540, 1500)]];
const dQ = tx(M('¿Desde dónde?'), 1080, 'M8 shadow', 120);
const dN = tx(M('<span class="S blue">Nadie lo apuntó.</span>'), 1150, 'shadow', 140);
function sD(t) {
  const a = K.desde - .1, b = K.este2 - .1, v = t >= a && t < b; show(HB, v); show(dQ, v); show(dN, v); CH.forEach(([, c]) => show(c, v)); if (!v) return;
  HB.style.opacity = E.out(seg(t, a, a + .3)); const nd = t >= K.nadie - .1;
  show(dQ, !nd || t < K.nadie + .2); reveal(dQ, seg(t, a, a + .3)); dQ.style.opacity = 1 - seg(t, K.nadie - .1, K.nadie + .1);
  CH.forEach(([k, c]) => { const q = E.out5(seg(t, k - .1, k + .2)); c.style.opacity = q * (nd ? 1 - .75 * seg(t, K.nadie - .1, K.nadie + .2) : 1); c.style.transform = `translate(-50%,-50%) scale(${(.6 + .4 * q) * pulse(t, k - .1, .08)})`;
    c.style.background = nd ? '#262b36' : '#2f6bff'; });
  HBL.innerHTML = t >= K.contra - .1 ? `<path d="M540 1840 C 520 1500 560 900 540 360" fill="none" stroke="#4f86ff" stroke-width="12" stroke-linecap="round" stroke-dasharray="1600" stroke-dashoffset="${1600 * (1 - E.out(seg(t, K.contra - .1, K.contra + .5)))}"/>` : '';
  show(dN, nd); reveal(dN, seg(t, K.nadie - .1, K.nadie + .25)); dN.style.transform = `scale(${pulse(t, K.nadie, .05)})`;
}
// ── E · la hoja de seis zonas ──
const Z = [['EXTREMO IZQ', 150, 400, 6], ['LATERAL IZQ', 290, 720, 3], ['CENTRAL', 540, 800, 2], ['LATERAL DER', 790, 720, 3], ['EXTREMO DER', 930, 400, 1], ['6 METROS', 540, 520, 5]];
const SHEET = mk('div', 'position:absolute;left:60px;top:470px;width:960px;height:1180px;border-radius:12px;display:none;background:#f4efe1;box-shadow:0 40px 90px rgba(0,0,0,.65);overflow:hidden',
  `<div style="position:absolute;left:50px;top:40px;font-family:M;font-weight:800;font-size:46px;color:#0d0f14;letter-spacing:-.02em">Sábado · goles recibidos</div>
   <div style="position:absolute;right:50px;top:50px;font-family:M;font-weight:700;font-size:26px;color:#8a8473;letter-spacing:.14em">EJEMPLO</div>
   <svg viewBox="0 0 1080 1100" style="position:absolute;left:-60px;top:120px;width:1080px;height:1100px"><g fill="none" stroke="#3a3a3a" stroke-width="5">
   <line x1="80" y1="190" x2="1000" y2="190"/><path d="M200 190 A160 160 0 0 0 360 350 L720 350 A160 160 0 0 0 880 190"/>
   <path d="M90 190 A250 250 0 0 0 340 590 L740 590 A250 250 0 0 0 990 190" stroke-dasharray="20 18"/>
   <line x1="250" y1="190" x2="250" y2="500" stroke-dasharray="6 14"/><line x1="830" y1="190" x2="830" y2="500" stroke-dasharray="6 14"/>
   <line x1="420" y1="350" x2="400" y2="900" stroke-dasharray="6 14"/><line x1="660" y1="350" x2="680" y2="900" stroke-dasharray="6 14"/></g>
   <rect x="460" y="170" width="160" height="22" fill="#3a3a3a"/>
   <rect id="zhl" x="60" y="200" width="190" height="300" rx="18" fill="rgba(47,107,255,.18)" stroke="#2f6bff" stroke-width="6" opacity="0"/>
   ${Z.map(([n, x, y]) => `<text x="${x}" y="${y - 70}" text-anchor="middle" font-family="M" font-weight="700" font-size="30" fill="#6f6a5c" letter-spacing="2">${n}</text><g class="tal" data-x="${x}" data-y="${y}"></g>`).join('')}</svg>`, $('cards'));
const TAL = [...SHEET.querySelectorAll('.tal')];
const eT = tx(M('una raya por gol'), 1700, 'M8 shadow', 72);
const eD = tx(M('<span class="S blue">en el descanso, ya lo sabes.</span>'), 1700, 'shadow', 80);
function marks(n, x, y, p) { let s = ''; for (let i = 0; i < n; i++) { const q = clamp(p * n - i); if (q <= 0) break; const g = Math.floor(i / 5), j = i % 5;
  const x0 = x - 70 + g * 95 + j * 16; s += j < 4 || true ? (j === 4 ? `<line x1="${x0 - 74}" y1="${y + 50}" x2="${x0 - 74 + 80 * q}" y2="${y + 50 - 70 * q}" stroke="#1f4fd6" stroke-width="7" stroke-linecap="round"/>`
    : `<line x1="${x0}" y1="${y - 10}" x2="${x0 + 3}" y2="${y - 10 + 70 * q}" stroke="#1f4fd6" stroke-width="7" stroke-linecap="round"/>`) : ''; } return s; }
function sE(t) {
  const a = K.este2 - .1, b = K.tu3 - .15, v = t >= a && t < b; show(SHEET, v); show(eT, false); show(eD, false); if (!v) return;
  show(DESK, true); const p = E.out5(seg(t, K.este2 - .1, K.este2 + .4)); SHEET.style.opacity = Math.max(.0001, p); SHEET.style.transform = `translateY(${(1 - p) * 300}px) rotate(${-3 + 2 * p}deg)`;
  // las seis zonas aparecen con «seis zonas»; las rayas, desde «raya»
  SHEET.querySelector('svg').style.opacity = E.out(seg(t, K.seis - .1, K.seis + .4));
  TAL.forEach((g, i) => { const [, x, y, n] = Z[i]; const st = K.raya - .1 + i * .28; g.innerHTML = marks(n, x, y, E.out(seg(t, st, st + .9))); });
  show(eT, t >= K.raya - .1 && t < K.desc - .15); reveal(eT, seg(t, K.raya - .1, K.raya + .2));
  const zh = SHEET.querySelector('#zhl'); zh.setAttribute('opacity', E.out(seg(t, K.desc, K.desc + .3)));
  show(eD, t >= K.desc - .15); reveal(eD, seg(t, K.desc - .15, K.desc + .2));
}
// ── F · los dos papeles ──
const fA = tx(M('Tu papel no vale un millón.'), 190, 'M8 shadow', 76);
const fB = tx(M('Pero el sábado'), 1560, 'M8 shadow', 90), fB2 = tx(M('<span class="S blue">vale un partido.</span>'), 1665, 'shadow', 140);
function sF(t) {
  const a = K.tu3 - .15, b = K.apuntalo - .1, v = t >= a && t < b; [fA, fB, fB2].forEach(e => show(e, v)); if (!v) return;
  show(DESK, true); show(PAPER, true); show(SHEET, true); SHEET.querySelector('svg').style.opacity = 1;
  TAL.forEach((g, i) => { const [, x, y, n] = Z[i]; g.innerHTML = marks(n, x, y, 1); }); SHEET.querySelector('#zhl').setAttribute('opacity', 1); SHEET.style.opacity = 1;
  const m = E.io(seg(t, a, a + .5));
  PAPER.style.top = '440px'; PAPER.style.transform = `translate(${-250 * m}px,${-20 * m}px) rotate(${-7 * m}deg) scale(${1 - .48 * m})`; PAPER.style.opacity = 1 - .35 * seg(t, K.pero - .1, K.pero + .3);
  SHEET.style.transform = `translate(${230 * m}px,${-40 * m}px) rotate(${5 * m}deg) scale(${1 - .45 * m})`;
  const big = E.io(seg(t, K.pero - .1, K.pero + .4)); SHEET.style.transform += ` scale(${1 + .45 * big})`;
  reveal(fA, seg(t, a, a + .3)); fA.style.opacity = 1 - .5 * big; show(fB, t >= K.pero - .1); show(fB2, t >= K.partido - .4); reveal(fB, seg(t, K.pero - .1, K.pero + .2)); reveal(fB2, seg(t, K.partido - .4, K.partido));
}
// ── G · ProTeam ──
const gK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.22em">APÚNTALO EN</div>', 820, 'shadow', 44);
const gP = tx('<span class="S" style="font-size:.6em">la app de</span> ProTeam.', 890, 'M8 shadow', 128);
function sG(t) {
  const a = K.apuntalo - .1, b = T.camp - .05, v = t >= a && t < b; show(gK, v); show(gP, v); if (!v) return;
  show(HB, true); HB.style.opacity = .5; HBL.innerHTML = '';
  gK.style.opacity = E.out(seg(t, a, a + .25)); const q = E.out5(seg(t, K.pt - .15, K.pt + .2)); gP.style.opacity = q; gP.style.transform = `scale(${(1.12 - .12 * q) * pulse(t, K.pt - .1, .05)})`;
}
window.frame = t => {
  show($('sysL'), false); show($('paper'), false); [LE, PO].forEach(p => show(p, false)); [DESK, PAPER, HB, SHEET, POL].forEach(e => show(e, false)); PAPER.style.opacity = 1; $('grain').style.opacity = .05;
  sA(t); sB(t); sC(t); sD(t); sE(t); sF(t); sG(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
