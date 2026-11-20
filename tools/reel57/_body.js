// u57 · PROBLEMA · «Balón largo al más rápido» (fútbol 7, alevines) · concepto: «el saque de puerta visto desde arriba».
// Dibu Martínez con el balón en la mano (el portero que la va a pegar) → el campo de fútbol 7 cenital: una flecha larga del portero
// al más rápido y los otros cinco puntos en gris, quietos → la carrera: +2 m hoy; en cadetes el rival lo alcanza → ficha para guardar
// (el partidillo del martes, 2 reglas, ~6,8 s) → el mismo campo, ahora la jugada pasa por los siete y se encienden uno a uno →
// vuelta a Martínez (bucle) con el reto para el staff → 28 NOV → cierre de campaña de siempre con el contador real.
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));
const RED = '#e5484d', BLUE = '#2f6bff', INK = '#0d0f14';
const EM = ph('emi', '50% 30%');
const TOP = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em;font-size:40px">FÚTBOL 7 · ALEVÍN</div>', 270, 'shadow', 40);

// ── A · BALÓN LARGO / AL MÁS RÁPIDO (Martínez con el balón) ──
const a1 = tx(M('BALÓN LARGO'), 1180, 'M8 shadow', 150);
const a2 = tx(M('AL MÁS RÁPIDO'), 1340, 'M8 shadow', 120);
const a3 = tx(M('<span class="S blue">gana partidos.</span>'), 1480, 'shadow', 120);
function sA(t) {
  const b = T.los - .06, v = t < b; [a1, a2, a3].forEach(e => show(e, v)); if (!v) return;
  show(EM, true); place(EM, { is: 1.1 + .14 * seg(t, 0, b), iy: -40 * seg(t, 0, b), dark: 0, z: 1,
    grad: 'linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 45%,rgba(0,0,0,.78) 72%,rgba(0,0,0,.85) 100%)' });
  reveal(a1, 1); reveal(a2, 1); a1.style.transform = `scale(${pulse(t, T.balon - .1, .05)})`;
  show(a3, t >= T.gana - .12); reveal(a3, seg(t, T.gana - .12, T.gana + .18));
}

// ── campo de fútbol 7 cenital (motion graphics propio, no es la app) ──
const PX0 = 150, PX1 = 930, PY0 = 470, PY1 = 1530;
const PITCH = mk('div', 'position:absolute;inset:0;display:none', `
  <svg width="1080" height="1920" style="position:absolute;left:0;top:0">
    <rect x="${PX0}" y="${PY0}" width="${PX1 - PX0}" height="${PY1 - PY0}" rx="18" fill="#12261b" stroke="#3d5a48" stroke-width="5"/>
    <line x1="${PX0}" y1="${(PY0 + PY1) / 2}" x2="${PX1}" y2="${(PY0 + PY1) / 2}" stroke="#3d5a48" stroke-width="5"/>
    <circle cx="540" cy="${(PY0 + PY1) / 2}" r="90" fill="none" stroke="#3d5a48" stroke-width="5"/>
    <rect x="340" y="${PY1 - 150}" width="400" height="150" fill="none" stroke="#3d5a48" stroke-width="5"/>
    <rect x="340" y="${PY0}" width="400" height="150" fill="none" stroke="#3d5a48" stroke-width="5"/>
    <rect x="470" y="${PY1}" width="140" height="18" fill="#3d5a48"/><rect x="470" y="${PY0 - 18}" width="140" height="18" fill="#3d5a48"/>
    <path id="lng" d="M540 1440 Q 980 1000 640 640" fill="none" stroke="${BLUE}" stroke-width="12" stroke-linecap="round" stroke-dasharray="1200" stroke-dashoffset="1200"/>
    <g id="chain" fill="none" stroke="${BLUE}" stroke-width="9" stroke-linecap="round"></g>
    <g id="gap"><line x1="0" y1="0" x2="0" y2="0" stroke="#fff" stroke-width="5" stroke-dasharray="10 10"/></g>
  </svg>`, $('cards'));
// jugadores: 0 portero · 1-2 defensas · 3-4 interiores · 5 el otro de arriba · 6 el más rápido
const POS = [[540, 1440], [360, 1250], [720, 1250], [300, 1000], [780, 1000], [420, 800], [720, 820]];
const DOT = POS.map(([x, y], i) => mk('div', `position:absolute;left:${x - 38}px;top:${y - 38}px;width:76px;height:76px;border-radius:50%;background:#7d8698;border:6px solid #12261b;display:none`, '', PITCH));
const RIV = mk('div', `position:absolute;width:64px;height:64px;border-radius:50%;background:${RED};border:6px solid #12261b;display:none`, '', PITCH);
const BALL = mk('div', 'position:absolute;width:40px;height:40px;border-radius:50%;background:#f5f5f3;box-shadow:0 0 18px rgba(255,255,255,.6);display:none', '', PITCH);
const qb = (p0, c, p1, k) => [(1 - k) * (1 - k) * p0[0] + 2 * (1 - k) * k * c[0] + k * k * p1[0], (1 - k) * (1 - k) * p0[1] + 2 * (1 - k) * k * c[1] + k * k * p1[1]];
const GOAL = [640, 640];
const bK = tx(M('LOS OTROS CINCO'), 345, 'M8 shadow', 100);
const bT = tx(M('<span class="S" style="color:#c9cfdb">ni la tocan.</span>'), 1500, 'shadow', 110);
const cK = tx(M('HOY: <span style="color:#4f86ff">+2 METROS</span>'), 345, 'M8 shadow', 100);
const cC = tx(M('EN CADETES'), 345, 'M8 shadow', 100);
const cT = tx(M('<span class="S" style="color:#ff8a8d">los demás también corren.</span>'), 1500, 'shadow', 92);
const GAPL = mk('div', 'position:absolute;width:220px;text-align:center;font-family:M;font-weight:800;font-size:60px;color:#fff;display:none', '2 m', PITCH);
function basePitch(t, a) {
  show(PITCH, true); show($('sysL'), true); $('sysL').style.background = INK;
  const q = E.out5(seg(t, a, a + .3)); PITCH.style.opacity = 1; PITCH.style.transform = 'translateY(40px) scale(.86)';
  DOT.forEach((d, i) => { show(d, true); d.style.left = (POS[i][0] - 38) + 'px'; d.style.top = (POS[i][1] - 38) + 'px'; d.style.background = '#7d8698'; d.style.transform = `scale(${q})`; d.style.boxShadow = 'none'; d.style.opacity = 1; });
  show(RIV, false); show(BALL, false); show(GAPL, false); $('gap').style.display = 'none';
  $('lng').style.display = 'none'; $('chain').innerHTML = '';
}
// B · la flecha larga y los otros cinco, grises
function sB(t) {
  const a = T.los - .06, b = T.hoy - .06, v = t >= a && t < b; show(bK, v); show(bT, v); if (!v) return;
  basePitch(t, a);
  reveal(bK, seg(t, a, a + .3)); bK.style.transform = `scale(${pulse(t, T.cinco - .1, .07)})`;
  DOT[0].style.background = BLUE; DOT[6].style.background = BLUE;
  const L = $('lng'); L.style.display = 'block'; const k = E.io(seg(t, a + .1, a + .9)); L.setAttribute('stroke-dashoffset', 1200 * (1 - k));
  // el más rápido corre hacia la flecha
  const r = E.io(seg(t, a + .5, a + 1.2)); const p = [POS[6][0] + (GOAL[0] - POS[6][0]) * r, POS[6][1] + (GOAL[1] - POS[6][1]) * r];
  DOT[6].style.left = (p[0] - 38) + 'px'; DOT[6].style.top = (p[1] - 38) + 'px';
  show(BALL, true); const bp = qb([540, 1440], [980, 1000], GOAL, k); BALL.style.left = (bp[0] - 20) + 'px'; BALL.style.top = (bp[1] - 20) + 'px';
  // los otros cinco: un pulso gris en «cinco»
  [1, 2, 3, 4, 5].forEach((i, j) => { const pp = Math.exp(-Math.pow((t - T.cinco - .05 - j * .06) / .12, 2)); DOT[i].style.transform = `scale(${1 + .35 * pp})`; DOT[i].style.boxShadow = `0 0 0 ${10 * pp}px rgba(201,207,219,.35)`; });
  show(bT, t >= T.ni - .12); reveal(bT, seg(t, T.ni - .12, T.ni + .2));
  const fl = Math.exp(-Math.pow((t - T.cinco + .05) / .07, 2)); $('grain').style.opacity = .05 + .14 * fl;
}
// C · la carrera: hoy +2 m · en cadetes el rival lo alcanza
function sC(t) {
  const a = T.hoy - .06, b = T.guar - .06, v = t >= a && t < b; [cK, cC, cT].forEach(e => show(e, false)); if (!v) return;
  basePitch(t, a - 1); [1, 2, 3, 4, 5].forEach(i => { DOT[i].style.opacity = .35; });
  DOT[0].style.background = BLUE; DOT[6].style.background = BLUE; DOT[0].style.opacity = .35;
  const cad = t >= T.en - .1;
  // el más rápido corre hacia arriba; el rival detrás, a 2 m (hoy) o pegado (en cadetes)
  const run = seg(t, a, b); const y6 = 900 - 260 * E.io(run);
  DOT[6].style.left = (640 - 38) + 'px'; DOT[6].style.top = (y6 - 38) + 'px';
  show(BALL, true); BALL.style.left = (640 - 20) + 'px'; BALL.style.top = (y6 - 70 - 20) + 'px';
  const gap = cad ? 170 * (1 - E.io(seg(t, T.en - .1, T.demas + .2))) + 0 : 170 * E.out5(seg(t, a, a + .5));
  show(RIV, true); RIV.style.left = (640 - 32 + (cad ? 70 * E.io(seg(t, T.en - .1, T.demas + .2)) : 0)) + 'px'; RIV.style.top = (y6 + 60 + gap - 32) + 'px';
  const g = $('gap'); g.style.display = gap > 20 ? 'block' : 'none'; const ln = g.firstElementChild;
  ln.setAttribute('x1', 560); ln.setAttribute('x2', 560); ln.setAttribute('y1', y6 + 38); ln.setAttribute('y2', y6 + 60 + gap - 32);
  show(GAPL, gap > 60); GAPL.style.left = (330) + 'px'; GAPL.style.top = (y6 + 20 + gap / 2) + 'px'; GAPL.textContent = gap > 140 ? '2 m' : '';
  if (!cad) { show(cK, true); reveal(cK, seg(t, a, a + .3)); cK.style.transform = `scale(${pulse(t, T.dos - .1, .06)})`; }
  else { show(cC, true); reveal(cC, seg(t, T.en - .1, T.en + .2)); show(cT, t >= T.demas - .25); reveal(cT, seg(t, T.demas - .25, T.demas + .1)); }
}

// ── D · ficha para guardar: EL MARTES · 10′ DE PARTIDILLO · 1 · 2 (papel, ~6,8 s) ──
const CARD = mk('div', 'position:absolute;left:90px;top:540px;width:900px;height:860px;border-radius:40px;background:#fff;border:3px solid #d6d2c6;box-shadow:0 30px 70px rgba(13,15,20,.14);display:none', `
  <div style="position:absolute;left:70px;top:66px;font-family:M;font-weight:700;font-size:36px;letter-spacing:.2em;color:#6d7588">EL MARTES · 10′ DE PARTIDILLO</div>
  <div id="r1" style="position:absolute;left:70px;top:200px;right:60px"><div style="position:absolute;left:0;top:0;width:110px;height:110px;border-radius:50%;background:${BLUE};color:#fff;font-family:M;font-weight:800;font-size:64px;text-align:center;line-height:110px">1</div>
    <div style="position:absolute;left:150px;top:-4px;font-family:M;font-weight:800;font-size:76px;letter-spacing:-.04em;color:${INK};line-height:1.02">El portero<br><span class="S" style="color:${BLUE};font-size:90px">saca en corto.</span></div></div>
  <div id="r2" style="position:absolute;left:70px;top:500px;right:60px"><div style="position:absolute;left:0;top:0;width:110px;height:110px;border-radius:50%;background:${BLUE};color:#fff;font-family:M;font-weight:800;font-size:64px;text-align:center;line-height:110px">2</div>
    <div style="position:absolute;left:150px;top:-4px;font-family:M;font-weight:800;font-size:76px;letter-spacing:-.04em;color:${INK};line-height:1.02">El balón no sube<br><span class="S" style="color:${BLUE};font-size:90px">de la cintura.</span></div></div>`, $('cards'));
const dG = tx('<span style="display:inline-block;padding:18px 40px;border-radius:999px;background:' + INK + ';color:#f2f1ec;font-family:M;font-weight:800;font-size:44px;letter-spacing:.14em">GUÁRDATELO</span>', 360, '', 44);
function sD(t) {
  const a = T.guar - .06, b = T.correr - .06, v = t >= a && t < b; show(CARD, v); show(dG, v); if (!v) return;
  show($('paper'), true);
  const q = E.out5(seg(t, a, a + .45)); CARD.style.opacity = q; CARD.style.transform = `translateY(${(1 - q) * 120}px) rotate(${-1.2 * (1 - q) + .6 * Math.sin(t * .9)}deg) scale(${1 + .09 * seg(t, a, b)})`; CARD.style.marginTop = `${-60 * seg(t, a, b)}px`;
  dG.style.opacity = q; dG.style.transform = `scale(${pulse(t, a, .06)})`;
  [['r1', T.portero - .25], ['r2', T.balon2 - .25]].forEach(([id, t0]) => { const k = E.out5(seg(t, Math.min(t0, a + 1.2), Math.min(t0, a + 1.2) + .35)); $(id).style.opacity = k; $(id).style.transform = `translateX(${(1 - k) * 60}px)`; });
}

// ── E · el mismo campo: la jugada pasa por los siete ──
const eK = tx(M('CORRER YA SABE.'), 345, 'M8 shadow', 100);
const eQ = tx(M('QUE JUEGUEN'), 330, 'M8 shadow', 104);
const eT = tx(M('<span class="S blue">los siete.</span>'), 440, 'shadow', 120);
const ORD = [0, 1, 2, 4, 3, 5, 6];
function sE(t) {
  const a = T.correr - .06, b = T.preg - .06, v = t >= a && t < b; [eK, eQ, eT].forEach(e => show(e, false)); if (!v) return; show(eK, t < T.ahora - .1);
  basePitch(t, a);
  reveal(eK, seg(t, a, a + .3));
  const t0 = T.ahora - .1, step = (T.siete - t0) / 6;
  let path = '';
  ORD.forEach((i, j) => {
    const tj = t0 + j * step, on = t >= tj; const q = E.out5(seg(t, tj, tj + .25));
    DOT[i].style.background = on ? BLUE : '#7d8698'; DOT[i].style.transform = `scale(${1 + .3 * Math.sin(Math.PI * q) * (on ? 1 : 0)})`;
    if (j > 0 && on) { const p = POS[ORD[j - 1]], c = POS[i]; const k = E.out(seg(t, tj - step * .9, tj)); path += `<line x1="${p[0]}" y1="${p[1]}" x2="${p[0] + (c[0] - p[0]) * k}" y2="${p[1] + (c[1] - p[1]) * k}"/>`; }
  });
  $('chain').innerHTML = path;
  const done = t >= T.siete - .1; if (done) DOT.forEach(d => { d.style.boxShadow = `0 0 0 ${10 * E.out(seg(t, T.siete - .1, T.siete + .3))}px rgba(47,107,255,.3)`; });
  show(eQ, t >= T.ahora - .1); reveal(eQ, seg(t, T.ahora - .1, T.ahora + .2)); show(eT, t >= T.siete - .2); reveal(eT, seg(t, T.siete - .2, T.siete + .1));
  eT.style.transform = `scale(${pulse(t, T.siete - .2, .06)})`;
}

// ── F · reto para el staff (vuelta a Martínez: bucle con el primer plano) ──
const fK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">RETO PARA TU STAFF</div>', 1090, 'shadow', 46);
const fQ = tx(M('¿CUÁNTOS GOLES'), 1170, 'M8 shadow', 112);
const fT = tx(M('<span class="S blue">de balón largo al mismo?</span>'), 1330, 'shadow', 104);
function sF(t) {
  const a = T.preg - .06, b = T.el28 - .06, v = t >= a && t < b; [fK, fQ, fT].forEach(e => show(e, v)); if (!v) return;
  show(EM, true); place(EM, { is: 1.12 + .05 * seg(t, a, b), iy: -10, z: 1,
    grad: 'linear-gradient(180deg,rgba(0,0,0,.4) 0%,rgba(0,0,0,0) 25%,rgba(0,0,0,.25) 48%,rgba(0,0,0,.82) 70%,rgba(0,0,0,.88) 100%)' });
  fK.style.opacity = E.out(seg(t, a, a + .25));
  show(fQ, t >= T.cuantos - .3); reveal(fQ, seg(t, T.cuantos - .3, T.cuantos)); show(fT, t >= T.largo2 - .4); reveal(fT, seg(t, T.largo2 - .4, T.largo2 - .1));
  fT.style.transform = `scale(${pulse(t, T.mismo - .1, .05)})`;
}

// ── G · ABRE EL SÁBADO 28 NOV · la app de ProTeam ──
const gK = tx('<div class="kick" style="letter-spacing:.26em;color:#e6e8ee">ABRE EL SÁBADO</div>', 640, '', 46);
const g28 = tx('28 NOV', 710, 'M8', 250);
const gA = tx(M('LA APP DE <span style="color:#4f86ff">PROTEAM</span>'), 1010, 'M8', 70);
function sG(t) {
  const a = T.el28 - .06, b = T.camp - .05, v = t >= a && t < b; [gK, g28, gA].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true); $('sysL').style.background = INK;
  gK.style.opacity = E.out(seg(t, a, a + .25));
  const q = E.out5(seg(t, T.v28 - .3, T.v28 - .05)); g28.style.opacity = q; g28.style.color = '#4f86ff';
  g28.style.transform = `scale(${(1.2 - .2 * q) * (1 + .04 * seg(t, T.v28, b))})`;
  show(gA, t >= T.pt - .5); reveal(gA, seg(t, T.pt - .5, T.pt - .1));
  const fl = Math.exp(-Math.pow((t - T.v28 + .2) / .07, 2)); $('grain').style.opacity = .05 + .15 * fl;
}

// ── H · final en bucle: los siete puntos en azul, tenues, bajo el cierre ──
function sH(t) {
  const g0 = T.gra - .1; if (t < g0) return; show($('paper'), true); show(PITCH, true);
  const q = E.out5(seg(t, g0, g0 + .4));
  PITCH.style.opacity = .3 * q; PITCH.style.transform = `translateY(${640 + 40 * (1 - q)}px) scale(.42)`; PITCH.style.transformOrigin = '50% 50%';
  DOT.forEach((d, i) => { show(d, true); d.style.left = (POS[i][0] - 38) + 'px'; d.style.top = (POS[i][1] - 38) + 'px'; d.style.background = BLUE; d.style.transform = 'none'; d.style.opacity = 1; });
  show(RIV, false); show(BALL, false); show(GAPL, false); $('gap').style.display = 'none'; $('lng').style.display = 'none';
}

window.frame = t => {
  show($('sysL'), false); $('sysL').style.background = '#0d0f14'; show($('paper'), false); show(PITCH, false); PITCH.style.transform = 'none'; PITCH.style.opacity = 1;
  show(EM, false); $('grain').style.opacity = .05;
  show(TOP, t < T.guar - .06 || (t >= T.correr - .06 && t < T.preg - .06)); TOP.style.opacity = 1; TOP.style.top = (t < T.los - .06 ? 1100 : 270) + 'px';
  sA(t); sB(t); sC(t); sD(t); sE(t); sF(t); sG(t); sH(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
