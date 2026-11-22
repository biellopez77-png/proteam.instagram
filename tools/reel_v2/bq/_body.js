// D3-C v2 · «Sin Jordan» · baloncesto infantil · hook: shock con algo conocido (Bulls 93-94) → bajada al banquillo de base
// Escenas: A foto de Jordan + hook · B marcador 57/55 · C red de pases sin el 23 + sábado/martes · D tu infantil: todo al base
// E tarea guardable con la regla del prohibido que rota · F vuelta al hook · G ProTeam · H cierre lista de espera (común)
window.GAIMG = 'base';
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));
const K = { cin1: at('cincuenta'), cin2: at('cincuenta', 2), como: at('como'), impro: at('improvisa'), sab: at('sabado'), mar: at('martes'),
  ahora: at('ahora'), pres: at('presionan'), balon: at('balon'), base1: at('base'), haz: at('haz'), primer: at('primer'), base2: at('base', 2),
  cada: at('cada'), cambia: at('cambia'), recibir: en('recibir'), los2: at('los', 2), sabe: at('sabe'), base3: at('base', 3), plan: at('planificalo'), pt: at('proteam') };
const sc = (a, b) => (t) => t >= a && t < b;
// ── fotos ──
const JO = ph('jordan', '50% 30%'), BA = ph('base', '50% 25%');
// ── A · hook ──
const aK = tx('<div class="kick" style="letter-spacing:.2em;color:#e6e8ee">BULLS · TEMPORADA 1993-94</div>', 1040, 'shadow', 40);
const aS = tx(M('SIN'), 1180, 'M8 shadow', 150);
const aJ = tx(M('JORDAN'), 1320, 'M8 shadow', 210);
const aL = tx(M('<span class="S blue">solo 2 partidos menos.</span>'), 1560, 'shadow', 104);
const aB = tx('<div class="kick" style="color:#c9cfdb;letter-spacing:.18em">ÉL SE FUE A JUGAR AL BÉISBOL</div>', 1100, 'shadow', 30);
function sA(t) {
  const v = t < K.cin1 - .1; [aK, aS, aJ, aL, aB].forEach(e => show(e, v)); if (!v) return;
  show(JO, true); place(JO, { is: 1.25 - .1 * seg(t, 0, K.cin1), iy: 30 * seg(t, 0, K.cin1), org: '50% 30%', grad: 'linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,.05) 35%,rgba(0,0,0,.75) 70%,rgba(0,0,0,.9))' });
  reveal(aS, 1); reveal(aJ, 1);
  aJ.style.transform = `scale(${pulse(t, at('jordan') - .1, .05)})`;
  show(aL, t >= at('ganaron') - .1); reveal(aL, seg(t, at('ganaron') - .1, at('ganaron') + .3));
  aB.style.opacity = E.out(seg(t, .4, .8));
}
// ── B · marcador ──
const BOARD = mk('div', 'position:absolute;left:90px;top:560px;width:900px;height:820px;border-radius:40px;background:#07080b;border:6px solid #1d2230;box-shadow:0 40px 90px rgba(0,0,0,.7),inset 0 0 0 10px #0d0f14;display:none',
  ['CON JORDAN<br><span style="color:#7d8597">1992-93</span>', 'SIN JORDAN<br><span style="color:#7d8597">1993-94</span>'].map((l, i) => `
  <div style="position:absolute;top:70px;left:${60 + i * 410}px;width:370px;text-align:center;font-family:M;font-weight:700;font-size:34px;letter-spacing:.14em;color:#e6e8ee;line-height:1.35">${l}</div>
  <div class="dig" style="position:absolute;top:250px;left:${60 + i * 410}px;width:370px;height:330px;border-radius:24px;background:#0f1219;border:3px solid #1d2230;text-align:center;font-family:M;font-weight:800;font-size:250px;line-height:330px;letter-spacing:-.04em;color:${i ? '#4f86ff' : '#f2f1ec'};font-variant-numeric:tabular-nums;text-shadow:0 0 40px ${i ? 'rgba(79,134,255,.6)' : 'rgba(242,241,236,.35)'}">00</div>
  <div style="position:absolute;top:610px;left:${60 + i * 410}px;width:370px;text-align:center;font-family:M;font-weight:700;font-size:30px;letter-spacing:.16em;color:#7d8597">VICTORIAS</div>`).join('') +
  '<div style="position:absolute;left:445px;top:250px;width:10px;height:330px;background:#1d2230;border-radius:5px"></div>', $('cards'));
const DIG = [...BOARD.querySelectorAll('.dig')];
const bD = tx(M('<span class="S blue">−2</span>'), 1430, 'shadow', 200);
function sB(t) {
  const a = K.cin1 - .1, b = K.como - .05, v = t >= a && t < b; show(BOARD, v); show(bD, v); if (!v) return;
  show(JO, true); place(JO, { is: 1.4, iy: -60, org: '50% 30%', dark: .82 });
  const p = E.out5(seg(t, a, a + .35)); BOARD.style.opacity = p; BOARD.style.transform = `translateY(${(1 - p) * 80}px) scale(${.96 + .04 * p})`;
  [[K.cin1, 57], [K.cin2, 55]].forEach(([k, n], i) => { const q = E.out(seg(t, k - .05, k + .55)); DIG[i].textContent = String(Math.round(n * q)).padStart(2, '0');
    DIG[i].style.transform = `scale(${pulse(t, k + .45, .07)})`; DIG[i].style.opacity = t >= k - .05 ? 1 : .25; });
  show(bD, t >= K.cin2 + .7); reveal(bD, seg(t, K.cin2 + .7, K.cin2 + 1));
}
// ── pista (vista cenital, media pista) ──
const COURT = mk('div', 'position:absolute;inset:0;display:none;background:radial-gradient(120% 80% at 50% 40%,#1a2438,#0b0f18 70%)',
  `<svg viewBox="0 0 1080 1920" style="position:absolute;inset:0;width:100%;height:100%">
   <g fill="none" stroke="rgba(230,232,238,.28)" stroke-width="6">
    <rect x="60" y="150" width="960" height="1620" rx="8"/><line x1="60" y1="960" x2="1020" y2="960"/><circle cx="540" cy="960" r="150"/>
    <rect x="370" y="150" width="340" height="430"/><circle cx="540" cy="580" r="150"/><path d="M130 150 V330 A440 440 0 0 0 950 330 V150"/>
    <rect x="370" y="1340" width="340" height="430"/><circle cx="540" cy="1340" r="150"/><path d="M130 1770 V1590 A440 440 0 0 1 950 1590 V1770"/>
   </g><line x1="470" y1="190" x2="610" y2="190" stroke="#e6e8ee" stroke-width="8"/><circle cx="540" cy="225" r="30" fill="none" stroke="#ff7a3d" stroke-width="7"/>
   <g id="links"></g></svg><div style="position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(180deg,rgba(7,9,14,.95) 55%,rgba(7,9,14,0))"></div>`, $('cards'));
const LINKS = COURT.querySelector('#links');
// atacantes (azules) y defensores (huecos)
const mkDot = (n, col, hollow) => mk('div', `position:absolute;width:120px;height:120px;margin:-60px 0 0 -60px;border-radius:50%;display:none;font-family:M;font-weight:800;font-size:52px;line-height:${hollow ? 108 : 120}px;text-align:center;color:${hollow ? '#e6e8ee' : '#fff'};${hollow ? 'border:6px solid rgba(230,232,238,.55);background:rgba(13,15,20,.4)' : `background:${col};box-shadow:0 10px 30px rgba(0,0,0,.45)`}`, n, $('cards'));
const ATT = [['1', 540, 1290], ['2', 230, 1120], ['3', 850, 1120], ['4', 300, 800], ['5', 780, 760]].map(([n, x, y]) => { const d = mkDot(n, '#2f6bff'); d._x = x; d._y = y; return d; });
const DEF = [[540, 1180], [300, 1040], [780, 1040], [400, 850], [690, 820]].map(([x, y]) => { const d = mkDot('', '', true); d._x = x; d._y = y; return d; });
const BULLS = [['23', 540, 1250], ['33', 230, 1080], ['10', 850, 1080], ['7', 330, 760], ['54', 760, 720]].map(([n, x, y]) => { const d = mkDot(n, '#c8102e'); d._x = x; d._y = y; return d; });
const BALL = mk('div', 'position:absolute;width:56px;height:56px;margin:-28px 0 0 -28px;border-radius:50%;background:#ff7a3d;box-shadow:0 0 0 6px rgba(255,122,61,.25),0 8px 20px rgba(0,0,0,.5);display:none', '', $('cards'));
const BAN = mk('div', 'position:absolute;width:170px;height:170px;margin:-85px 0 0 -85px;display:none',
  '<svg viewBox="0 0 170 170" style="width:100%;height:100%"><circle cx="85" cy="85" r="76" fill="none" stroke="#f2f1ec" stroke-width="10"/><line x1="32" y1="138" x2="138" y2="32" stroke="#f2f1ec" stroke-width="10" stroke-linecap="round"/></svg>', $('cards'));
const posD = (d, dx = 0, dy = 0, s = 1, o = 1) => { d.style.left = (d._x + dx) + 'px'; d.style.top = (d._y + dy) + 'px'; d.style.transform = `scale(${s})`; d.style.opacity = o; };
const line = (a, b, col, w, dash, p = 1) => { const x1 = a._x, y1 = a._y, x2 = x1 + (b._x - x1) * p, y2 = y1 + (b._y - y1) * p;
  return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${col}" stroke-width="${w}" stroke-linecap="round" ${dash ? 'stroke-dasharray="4 26"' : ''}/>`; };
const ballAlong = (path, t, t0, dt) => { const n = path.length - 1, u = clamp((t - t0) / dt) * n, i = Math.min(n - 1, Math.floor(u)), f = E.io(u - i);
  const a = path[i], b = path[i + 1]; BALL.style.left = (a._x + (b._x - a._x) * f) + 'px'; BALL.style.top = (a._y + (b._y - a._y) * f) + 'px'; };
// ── C · sin el 23: red de pases · sábado / martes ──
const cQ = tx(M('¿Cómo gana un equipo'), 150, 'M8 shadow', 78), cQ2 = tx(M('<span class="S blue">sin su mejor jugador?</span>'), 245, 'shadow', 96);
const CAL = ['SÁBADO', 'MARTES'].map((d, i) => mk('div', `position:absolute;left:${120 + i * 450}px;top:1370px;width:390px;height:400px;border-radius:30px;background:#f2f1ec;display:none;box-shadow:0 30px 60px rgba(0,0,0,.55);overflow:hidden`,
  `<div style="height:110px;background:${i ? '#2f6bff' : '#0d0f14'};color:#fff;font-family:M;font-weight:800;font-size:46px;line-height:110px;text-align:center;letter-spacing:.08em">${d}</div>
   <div style="font-family:M;font-weight:800;font-size:52px;color:#0d0f14;text-align:center;margin-top:90px;letter-spacing:-.03em">${i ? 'se entrena' : 'se improvisa'}</div>
   ${i ? '' : '<div class="strike" style="top:58%;left:6%;right:6%"></div>'}`, $('cards')));
function sC(t) {
  const a = K.como - .05, b = K.ahora - .05, v = t >= a && t < b; show(COURT, v); [cQ, cQ2].forEach(e => show(e, v)); BULLS.forEach(d => show(d, v)); CAL.forEach(c => show(c, v)); if (!v) { return; }
  const p = E.out5(seg(t, a, a + .35)); COURT.style.opacity = p;
  BULLS.forEach((d, i) => posD(d, 0, -120, i === 0 ? 1 + .3 * seg(t, a + .3, a + 1) : E.out5(seg(t, a + .05 * i, a + .3 + .05 * i)), i === 0 ? 1 - seg(t, a + .3, a + 1) : 1));
  // tras quitar al 23, los otros cuatro se pasan el balón entre ellos
  const R = BULLS.slice(1); const sh = seg(t, a + .9, a + 1.6);
  LINKS.innerHTML = [[0, 1], [1, 3], [3, 2], [2, 0], [0, 3], [1, 2]].map(([i, j], k) => line({ _x: R[i]._x, _y: R[i]._y - 120 }, { _x: R[j]._x, _y: R[j]._y - 120 }, '#4f86ff', 8, true, E.out(seg(sh, k * .12, k * .12 + .4)))).join('');
  show(BALL, t >= a + 1); if (t >= a + 1) { const P = [R[0], R[1], R[3], R[2], R[0]].map(d => ({ _x: d._x, _y: d._y - 120 })); ballAlong(P, t, a + 1, K.impro - a - 1.1); }
  show(cQ, true); reveal(cQ, seg(t, a, a + .3)); show(cQ2, true); reveal(cQ2, seg(t, a + .25, a + .6));
  CAL.forEach((c, i) => { const k = i ? K.mar : K.impro; const q = E.out5(seg(t, k - .1, k + .3)); c.style.opacity = q; c.style.transform = `translateY(${(1 - q) * 120}px) rotate(${(i ? 3 : -4) * q}deg) scale(${i ? pulse(t, K.mar, .06) : 1})`; });
  const st = CAL[0].querySelector('.strike'); st.style.transform = `scaleX(${E.out(seg(t, K.sab + .1, K.sab + .45))})`;
}
// ── D · tu infantil: todo acaba en el base ──
const dK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.22em">AHORA</div>', 1240, 'shadow', 44);
const dT = tx(M('TU INFANTIL.'), 1310, 'M8 shadow', 150);
const dP = tx(M('Os presionan…'), 120, 'M8 shadow', 84), dP2 = tx(M('<span class="S blue">y siempre al base.</span>'), 215, 'shadow', 100);
function sD(t) {
  const a = K.ahora - .05, b = K.haz - .05, v = t >= a && t < b; [dK, dT, dP, dP2].forEach(e => show(e, false)); if (!v) return;
  const onCourt = t >= K.pres - .15;
  if (!onCourt) { show(BA, true); place(BA, { is: 1.18 - .06 * seg(t, a, K.pres), org: '50% 25%', grad: 'linear-gradient(180deg,rgba(0,0,0,.1) 40%,rgba(0,0,0,.85))' });
    show(dK, true); show(dT, true); dK.style.opacity = E.out(seg(t, a, a + .25)); reveal(dT, seg(t, at('infantil') - .1, at('infantil') + .25)); return; }
  show(COURT, true); COURT.style.opacity = 1; ATT.forEach(d => { show(d, true); posD(d); }); DEF.forEach((d, i) => { show(d, true); const q = E.out5(seg(t, K.pres - .1 + i * .05, K.pres + .3 + i * .05)); posD(d, 0, (1 - q) * -200, 1, q); });
  show(dP, true); reveal(dP, seg(t, K.pres - .1, K.pres + .2)); show(dP2, t >= K.balon - .1); reveal(dP2, seg(t, K.balon - .1, K.balon + .2));
  // todas las líneas de pase convergen en el 1, que brilla
  const q = seg(t, K.balon, K.base1 + .2); LINKS.innerHTML = ATT.slice(1).map((d, i) => line(d, ATT[0], '#f2f1ec', 7, true, E.out(seg(q, i * .15, i * .15 + .5)))).join('');
  ATT[0].style.boxShadow = `0 0 ${60 * seg(t, K.base1 - .2, K.base1 + .1)}px rgba(79,134,255,.9),0 10px 30px rgba(0,0,0,.45)`; posD(ATT[0], 0, 0, pulse(t, K.base1 - .1, .12));
  show(BALL, true); ballAlong([ATT[2], ATT[0], ATT[3], ATT[0], ATT[4], ATT[0]], t, K.balon - .2, Math.max(.6, K.base1 + .4 - K.balon));
}
// ── E · la tarea (ficha guardable) y el prohibido que rota ──
const CARD = mk('div', 'position:absolute;left:70px;top:150px;width:940px;height:500px;border-radius:34px;background:#f2f1ec;display:none;box-shadow:0 30px 70px rgba(0,0,0,.55);font-family:M;color:#0d0f14',
  `<div style="position:absolute;left:50px;top:40px;font-weight:700;font-size:30px;letter-spacing:.16em;color:#2f6bff">TAREA DEL MARTES · 10′</div>
   <div style="position:absolute;left:50px;top:90px;font-weight:800;font-size:76px;letter-spacing:-.04em">5 × 5 con presión</div>
   ${['El 1.er pase no puede ir al base', 'Cada 2′ cambia el prohibido', 'Todos aprenden a sacar el balón'].map((s, i) => `<div class="row" style="position:absolute;left:50px;top:${215 + i * 85}px;font-weight:700;font-size:40px;letter-spacing:-.01em;opacity:0"><span style="display:inline-block;width:46px;height:46px;border-radius:12px;background:#2f6bff;color:#fff;text-align:center;line-height:46px;font-size:30px;margin-right:20px;vertical-align:4px">${i + 1}</span>${s}</div>`).join('')}`, $('cards'));
const ROWS = [...CARD.querySelectorAll('.row')];
const CLK = mk('div', 'position:absolute;left:810px;top:1640px;width:200px;height:200px;display:none',
  '<svg viewBox="0 0 200 200" style="width:100%;height:100%"><circle cx="100" cy="100" r="88" fill="#0d0f14" stroke="#262b36" stroke-width="10"/><circle id="clkr" cx="100" cy="100" r="88" fill="none" stroke="#4f86ff" stroke-width="10" stroke-dasharray="553" transform="rotate(-90 100 100)"/><text x="100" y="118" text-anchor="middle" font-family="M" font-weight="800" font-size="52" fill="#f2f1ec">2′</text></svg>', $('cards'));
function sE(t) {
  const a = K.haz - .05, b = K.los2 - .05, v = t >= a && t < b; show(CARD, v); show(BAN, v); show(CLK, v); if (!v) return;
  show(COURT, true); ATT.forEach(d => { show(d, true); posD(d, 0, 110); }); DEF.forEach(d => { show(d, true); posD(d, 0, 110); });
  const p = E.out5(seg(t, a, a + .4)); CARD.style.opacity = p; CARD.style.transform = `translateY(${(1 - p) * -80}px) rotate(${-1.5 + 1.5 * p}deg)`;
  [K.primer, K.cada, K.recibir - .3].forEach((k, i) => { const q = E.out(seg(t, k - .1, k + .25)); ROWS[i].style.opacity = q; ROWS[i].style.transform = `translateX(${(1 - q) * 30}px)`; });
  // el prohibido: primero el 1; desde «cambia», salta al 3, al 5, al 2
  const seq = [0, 2, 4, 1]; const st = t < K.cambia ? 0 : 1 + Math.min(2, Math.floor((t - K.cambia) / .75)); const who = ATT[seq[st]];
  const bq = E.out5(seg(t, K.base2 - .2, K.base2 + .15)); BAN.style.opacity = bq; BAN.style.left = who._x + 'px'; BAN.style.top = (who._y + 110) + 'px';
  BAN.style.transform = `scale(${(1.4 - .4 * bq) * pulse(t, st ? K.cambia + (st - 1) * .75 : K.base2, .1)})`;
  // el balón busca a otro: 2 → 4 → 5 (nunca al prohibido)
  const tgt = ATT.filter((_, i) => i !== seq[st]); const sh = t >= K.base2;
  LINKS.innerHTML = sh ? line({ _x: ATT[1]._x, _y: ATT[1]._y + 110 }, { _x: tgt[1]._x, _y: tgt[1]._y + 110 }, '#4f86ff', 8, true, E.out(seg(t, K.base2, K.base2 + .4))) : '';
  show(BALL, true); const A0 = { _x: ATT[1]._x, _y: ATT[1]._y + 110 }, B0 = { _x: tgt[1]._x, _y: tgt[1]._y + 110 }; ballAlong([A0, B0], t, K.base2 + .1, .5);
  const ck = seg(t, K.cada, K.recibir + .4); CLK.querySelector('#clkr').setAttribute('stroke-dashoffset', 553 * ck); CLK.style.opacity = E.out(seg(t, K.cada - .1, K.cada + .2));
}
// ── F · vuelta al hook ──
const fA = tx(M('Los Bulls sabían jugar'), 520, 'M8 shadow', 84), fA2 = tx(M('sin Jordan.'), 615, 'M8 shadow', 84);
const fB = tx(M('¿Tu equipo sabe jugar'), 1240, 'M8 shadow', 90), fB2 = tx(M('<span class="S blue">sin su base?</span>'), 1345, 'shadow', 150);
function sF(t) {
  const a = K.los2 - .05, b = K.plan - .05, v = t >= a && t < b; [fA, fA2, fB, fB2].forEach(e => show(e, v)); if (!v) return;
  const two = t >= K.sabe - .5;
  show(JO, true); place(JO, { is: 1.12 + .05 * seg(t, a, b), org: '50% 30%', dark: two ? .78 : .5, z: 1 });
  if (two) { show(BA, true); place(BA, { is: 1.1, org: '50% 25%', dark: .55, z: 2 }); const w = E.io(seg(t, K.sabe - .5, K.sabe - .1)); BA.style.clipPath = `inset(${100 - 55 * w}% 0 0 0)`; } else BA.style.clipPath = 'none';
  reveal(fA, seg(t, a, a + .3)); reveal(fA2, seg(t, at('jordan', 3) - .15, at('jordan', 3) + .15));
  show(fB, two); show(fB2, two); reveal(fB, seg(t, K.sabe - .3, K.sabe)); reveal(fB2, seg(t, K.base3 - .15, K.base3 + .2)); fB2.style.transform = `scale(${pulse(t, K.base3, .06)})`;
}
// ── G · ProTeam ──
const gK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.22em">PLANIFÍCALO CON</div>', 820, 'shadow', 44);
const gP = tx('<span class="S" style="font-size:.6em">la app de</span> ProTeam.', 890, 'M8 shadow', 128);
function sG(t) {
  const a = K.plan - .05, b = T.camp - .05, v = t >= a && t < b; show(gK, v); show(gP, v); if (!v) return;
  show(COURT, true); COURT.style.opacity = .55; LINKS.innerHTML = '';
  gK.style.opacity = E.out(seg(t, a, a + .25)); const q = E.out5(seg(t, K.pt - .15, K.pt + .2)); gP.style.opacity = q; gP.style.transform = `scale(${(1.12 - .12 * q) * pulse(t, K.pt - .1, .05)})`;
}
window.frame = t => {
  show($('sysL'), false); show($('paper'), false); [JO, BA].forEach(p => { show(p, false); p.style.clipPath = 'none'; }); show(COURT, false); [...ATT, ...DEF, ...BULLS].forEach(d => show(d, false)); show(BALL, false);
  LINKS.innerHTML = ''; $('grain').style.opacity = .05;
  sA(t); sB(t); sC(t); sD(t); sE(t); sF(t); sG(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
