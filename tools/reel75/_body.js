// u75 · PROBLEMA · «Un entreno y un avión» (balonmano, Barça) · concepto: «dos partidos y un lunes a ciegas».
// El Barça de balonmano saludando (Palau, foto real) con JUE 24-32 · SÁB 20:00 desde el fotograma 0 → TÚ NO VUELAS: dos siluetas
// propias (motion graphics, no es la app), 50′ y 5′, y una sola barra «LUNES: MISMA SESIÓN» bajo las dos → ficha para guardar
// en papel (al acabar: del 1 al 10 · jugó poco: más · jugó todo: menos; ~10 s) → vuelta a la foto (bucle) con el reto →
// ABRE EL SÁBADO 28 NOV → cierre de campaña de siempre con el contador real.
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));
const RED = '#e5484d', BLUE = '#2f6bff', INK = '#0d0f14';
const BA = ph('barca', '50% 50%');
const TOP = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em;font-size:38px">BARÇA · KIELCE · IRUN</div>', 250, 'shadow', 38);

// ── A · JUE 24-32 · SÁB 20:00 (el Barça saludando) ──
const a1 = tx(M('JUE <span style="color:#4f86ff">24-32</span>'), 360, 'M8 shadow', 150);
const a2 = tx(M('SÁB <span style="color:#fff">20:00</span>'), 545, 'M8 shadow', 150);
const a3 = tx(M('<span class="S">un entreno y un avión.</span>'), 1560, 'shadow', 104);
function sA(t) {
  const b = T.tu - .06, v = t < b; [a1, a2, a3].forEach(e => show(e, false)); if (!v) return;
  show(BA, true); place(BA, { is: 1.06 + .12 * seg(t, 0, b), iy: 30 * seg(t, 0, b), z: 1,
    grad: 'linear-gradient(180deg,rgba(0,0,0,.82) 0%,rgba(0,0,0,.55) 30%,rgba(0,0,0,0) 45%,rgba(0,0,0,0) 62%,rgba(0,0,0,.8) 82%,rgba(0,0,0,.9) 100%)' });
  show(a1, true); reveal(a1, 1); a1.style.transform = `scale(${pulse(t, T.polonia - .3, .04)})`;
  show(a2, t >= T.hoy - .15); reveal(a2, seg(t, T.hoy - .15, T.hoy + .15)); a2.style.transform = `scale(${pulse(t, T.hoy + .3, .05)})`;
  show(a3, t >= T.medio - .12); reveal(a3, seg(t, T.medio - .12, T.medio + .2)); a3.style.transform = `scale(${pulse(t, T.avion - .1, .05)})`;
}

// ── B · TÚ NO VUELAS → dos jugadores, 50′ y 5′, y el lunes la misma sesión (motion graphics propio) ──
const fig = (x, col) => mk('div', `position:absolute;left:${x - 130}px;top:760px;width:260px;height:520px;display:none`, `
  <svg width="260" height="520" viewBox="0 0 260 520"><circle cx="130" cy="90" r="78" fill="${col}"/>
  <path d="M30 520 L30 300 Q30 190 130 190 Q230 190 230 300 L230 520 Z" fill="${col}"/></svg>`, $('cards'));
const F1 = fig(330, BLUE), F2 = fig(750, '#7d8698');
const L1 = mk('div', 'position:absolute;left:200px;top:640px;width:260px;text-align:center;font-family:M;font-weight:800;font-size:110px;letter-spacing:-.04em;color:#fff;display:none', '50′', $('cards'));
const L2 = mk('div', 'position:absolute;left:620px;top:640px;width:260px;text-align:center;font-family:M;font-weight:800;font-size:110px;letter-spacing:-.04em;color:#c9cfdb;display:none', '5′', $('cards'));
const BAR = mk('div', `position:absolute;left:150px;top:1330px;width:780px;height:150px;border-radius:28px;background:#1b2b55;border:3px solid ${BLUE};display:none;overflow:hidden`,
  `<div style="position:absolute;inset:0;text-align:center;line-height:144px;font-family:M;font-weight:800;font-size:58px;letter-spacing:.06em;color:#fff">LUNES: MISMA SESIÓN</div>`, $('cards'));
const bK = tx(M('TÚ NO VUELAS.'), 330, 'M8 shadow', 120);
const bT = tx(M('<span class="S" style="color:#c9cfdb">sin saber cómo acabaron.</span>'), 1560, 'shadow', 88);
function sB(t) {
  const a = T.tu - .06, b = T.guar - .06, v = t >= a && t < b; [bK, bT].forEach(e => show(e, v)); [F1, F2, L1, L2, BAR].forEach(e => show(e, false)); if (!v) return;
  show($('sysL'), true); $('sysL').style.background = INK;
  reveal(bK, seg(t, a, a + .25)); bK.style.transform = `scale(${pulse(t, a, .07)})`;
  const fl = Math.exp(-Math.pow((t - a - .02) / .07, 2)); $('grain').style.opacity = .05 + .14 * fl;
  const pa = a + .35, q = E.out5(seg(t, pa, pa + .45)), dr = Math.sin(t * 1.3) * 22;
  [F1, F2].forEach((f, i) => { show(f, t >= pa); f.style.opacity = q; f.style.transform = `translateY(${(1 - q) * 80 + dr * (i ? -1 : 1)}px)`; });
  const pl = T.pegado - .2, ql = E.out5(seg(t, pl, pl + .35));
  [L1, L2].forEach((l, i) => { show(l, t >= pl); l.style.opacity = ql; l.style.transform = `scale(${(1.25 - .25 * ql) * pulse(t, pl + i * .12, .05)})`; });
  const pb = T.escribes - .15, qb = E.io(seg(t, pb, pb + .6));
  show(BAR, t >= pb); BAR.style.clipPath = `inset(0 ${100 * (1 - qb)}% 0 0 round 28px)`; BAR.style.transform = `translateY(${-30 * seg(t, pb, b)}px) scale(${pulse(t, T.domingo - .1, .03) * (1 + .06 * seg(t, pb, b))})`;
  [L1, L2].forEach((l, i) => { l.style.marginTop = `${(i ? -1 : 1) * dr}px`; });
  if (t >= T.domingo) { const k = seg(t, T.domingo, T.domingo + .4); F2.style.filter = `brightness(${1 + .25 * k})`; }
  show(bT, t >= T.sin - .15); reveal(bT, seg(t, T.sin - .15, T.sin + .2));
}

// ── C · ficha para guardar (papel, ~10 s): AL ACABAR EL PARTIDO · 1 · 2 · 3 ──
const row = (id, n, top, a, b) => `<div id="${id}" style="position:absolute;left:70px;top:${top}px;right:50px;opacity:0"><div style="position:absolute;left:0;top:0;width:104px;height:104px;border-radius:50%;background:${BLUE};color:#fff;font-family:M;font-weight:800;font-size:60px;text-align:center;line-height:104px">${n}</div>
    <div style="position:absolute;left:140px;top:-2px;font-family:M;font-weight:800;font-size:70px;letter-spacing:-.04em;color:${INK};line-height:1.04">${a}<br><span class="S" style="color:${BLUE};font-size:84px">${b}</span></div></div>`;
const CARD = mk('div', 'position:absolute;left:90px;top:520px;width:900px;height:980px;border-radius:40px;background:#fff;border:3px solid #d6d2c6;box-shadow:0 30px 70px rgba(13,15,20,.14);display:none', `
  <div style="position:absolute;left:70px;top:64px;font-family:M;font-weight:700;font-size:36px;letter-spacing:.2em;color:#6d7588">AL ACABAR EL PARTIDO</div>
  ${row('r1', 1, 180, 'Del 1 al 10:', '¿cuánto costó?')}${row('r2', 2, 460, 'Jugó poco:', 'más.')}${row('r3', 3, 720, 'Jugó todo:', 'menos.')}`, $('cards'));
const cG = tx('<span style="display:inline-block;padding:18px 40px;border-radius:999px;background:' + INK + ';color:#f2f1ec;font-family:M;font-weight:800;font-size:44px;letter-spacing:.14em">GUÁRDATELO</span>', 350, '', 44);
function sC(t) {
  const a = T.guar - .06, b = T.preg - .06, v = t >= a && t < b; show(CARD, v); show(cG, v); if (!v) return;
  show($('paper'), true);
  const q = E.out5(seg(t, a, a + .45)); CARD.style.opacity = q;
  const sc = 1 + .10 * seg(t, a, b), ty = (1 - q) * 120 - 60 * seg(t, a, b);
  CARD.style.transform = `translateY(${ty}px) rotate(${-1.2 * (1 - q) + 1.6 * Math.sin(t * .9)}deg) scale(${sc})`;
  cG.style.opacity = q; cG.style.transform = `translateY(${ty - 490 * (sc - 1)}px) scale(${pulse(t, a, .06)})`;
  [['r1', T.acabar - .3], ['r2', T.poco - .3], ['r3', T.todo - .3]].forEach(([id, t0]) => { const k = E.out5(seg(t, t0, t0 + .35)); $(id).style.opacity = k; $(id).style.transform = `translateX(${(1 - k) * 60}px) scale(${pulse(t, t0 + .1, .04)})`; });
}

// ── D · reto para el staff (vuelta a la foto del principio: bucle) ──
const dK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">RETO PARA TU STAFF</div>', 1080, 'shadow', 46);
const dQ = tx(M('¿QUIÉN ACABÓ'), 1160, 'M8 shadow', 120);
const dT = tx(M('<span class="S blue">más cargado?</span>'), 1320, 'shadow', 120);
const dS = tx(M('SIN MIRAR.'), 1500, 'M8 shadow', 64);
function sD(t) {
  const a = T.preg - .06, b = T.el28 - .06, v = t >= a && t < b; [dK, dQ, dT, dS].forEach(e => show(e, v)); if (!v) return;
  show(BA, true); place(BA, { is: 1.14 + .05 * seg(t, a, b), iy: -20, z: 1,
    grad: 'linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 25%,rgba(0,0,0,.25) 46%,rgba(0,0,0,.85) 66%,rgba(0,0,0,.9) 100%)' });
  dK.style.opacity = E.out(seg(t, a, a + .25));
  show(dQ, t >= T.quien - .3); reveal(dQ, seg(t, T.quien - .3, T.quien)); show(dT, t >= T.cargado - .35); reveal(dT, seg(t, T.cargado - .35, T.cargado - .05));
  dT.style.transform = `scale(${pulse(t, T.cargado - .1, .05)})`;
  show(dS, t >= T.sinmirar - .15); reveal(dS, seg(t, T.sinmirar - .15, T.sinmirar + .15));
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
  show(gA, t >= T.pt - .9); reveal(gA, seg(t, T.pt - .9, T.pt - .5));
  const fl = Math.exp(-Math.pow((t - T.v28 + .2) / .07, 2)); $('grain').style.opacity = .05 + .15 * fl;
}
function sH(t) { if (t >= T.gra - .1) show($('paper'), true); }

window.frame = t => {
  show($('sysL'), false); $('sysL').style.background = '#0d0f14'; show($('paper'), false);
  show(BA, false); $('grain').style.opacity = .05;
  show(TOP, t < T.tu - .06 || (t >= T.preg - .06 && t < T.el28 - .06)); TOP.style.opacity = 1;
  sA(t); sB(t); sC(t); sD(t); sG(t); sH(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
