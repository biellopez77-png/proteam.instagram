// u64 · PROBLEMA · «Cinco jugadores fuera» · concepto: «la semana por asistencia» — un tablero de la semana (MAR · MIÉ · JUE · VIE · SÁB)
// en el que cada jugador es un punto. Primero la semana real del Deportivo sobre Riazor vacío (1 · 2 · 1 · 1 vuelven y el sábado a las 14:00);
// después «la tuya» en papel: 18 puntos por día que se apagan (el del examen, el que solo viene el viernes) y, en «como si vinieran todos»,
// se encienden todos a la vez (la sesión escrita para un equipo que no existe). Ficha para guardar (2 pasos, 7,5 s). Vuelta a Riazor
// para el reto al staff (bucle con el primer plano), 28 NOV y el cierre de campaña de siempre con el contador real.
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));
const RED = '#e5484d', BLUE = '#2f6bff', INK = '#0d0f14';
const RZ = ph('riazor', '50% 50%');
const TOP = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em;font-size:38px">LA SEMANA DEL DEPORTIVO</div>', 300, 'shadow', 38);

// ── A · 5 FUERA · 4 DÍAS · el último entrena una vez (Riazor vacío) ──
const a5 = tx('5 FUERA', 640, 'M8 shadow', 230);
const a4 = tx('4 DÍAS', 880, 'M8 shadow', 230);
const aU = tx(M('<span class="S blue">el último entrena una vez.</span>'), 1160, 'shadow', 104);
function sA(t) {
  const b = T.es - .04, v = t < b; [a5, a4, aU].forEach(e => show(e, v)); if (!v) return;
  show(RZ, true); RZ._img.style.objectPosition = `${38 + 24 * E.io(seg(t, 0, b))}% 50%`;
  place(RZ, { is: 1.06 + .05 * seg(t, 0, b), dark: .5, z: 1 });
  a5.style.transform = `scale(${1 + .02 * seg(t, 0, b)})`;
  a4.style.color = t >= T.cuatro - .05 ? '#fff' : '#fff'; a4.style.opacity = 1;
  a4.style.transform = `scale(${pulse(t, T.cuatro - .1, .06)})`;
  show(aU, t >= T.ult - .1); reveal(aU, seg(t, T.ult - .1, T.ult + .25));
}

// ── tablero de la semana: 5 columnas ──
const DAYS = ['MAR', 'MIÉ', 'JUE', 'VIE', 'SÁB'];
const BX = [150, 345, 540, 735, 930];
const BOARD = mk('div', 'position:absolute;inset:0;display:none', '', $('cards'));
const COLS = DAYS.map((d, i) => mk('div', `position:absolute;left:${BX[i] - 85}px;top:560px;width:170px;height:820px;border-radius:26px;border:3px solid #2a3040;background:rgba(18,22,32,.82)`, `<div style="position:absolute;left:0;right:0;top:26px;text-align:center;font-family:M;font-weight:800;font-size:44px;letter-spacing:.04em;color:#e6e8ee">${d}</div>`, BOARD));
// semana del Deportivo: puntos grandes que vuelven (1 · 2 · 1 · 1) y el partido
const RET = [[0], [1, 1], [2], [3]].flat();
const DD = [0, 1, 1, 2, 3].map((c, k) => { const n = [0, 1, 1, 2, 3].slice(0, k).filter(x => x === c).length;
  return mk('div', `position:absolute;left:${BX[c] - 42}px;top:${760 + n * 120}px;width:84px;height:84px;border-radius:50%;background:${BLUE};border:6px solid #dfe7ff;box-shadow:0 10px 26px rgba(47,107,255,.5);display:none`, '', BOARD); });
const DN = [1, 2, 1, 1].map((n, i) => mk('div', `position:absolute;left:${BX[i] - 85}px;top:1170px;width:170px;text-align:center;font-family:M;font-weight:800;font-size:120px;color:#fff;display:none`, '+' + n, BOARD));
const MATCH = mk('div', `position:absolute;left:${BX[4] - 85}px;top:740px;width:170px;text-align:center;display:none`, `<svg viewBox="0 0 100 100" width="110" height="110"><circle cx="50" cy="50" r="44" fill="#f2f1ec" stroke="${INK}" stroke-width="5"/><path d="M50 26 l20 14 -8 24 h-24 l-8 -24z" fill="${INK}"/></svg><div style="font-family:M;font-weight:800;font-size:46px;color:#fff;margin-top:24px">14:00</div>`, BOARD);
const bK = tx(M('VUELVEN DE SUS SELECCIONES'), 430, 'M7 shadow', 46);
const RTT = () => [T.es - .04, T.es + .4, T.es + .6, T.depor - .05, T.depor + .45];

function sB(t) {
  const a = T.es - .04, b = T.tu - .06, v = t >= a && t < b; show(bK, v); if (!v) return;
  show(RZ, true); RZ._img.style.objectPosition = '62% 50%'; place(RZ, { is: 1.25, dark: .82, z: 1 });
  show(BOARD, true); COLS.forEach((c, i) => { const q = E.out5(seg(t, a + i * .05, a + .35 + i * .05)); c.style.opacity = q; c.style.transform = `translateY(${(1 - q) * 60}px)`; c.style.background = 'rgba(18,22,32,.82)'; c.style.borderColor = '#2a3040'; c.firstChild.style.color = '#e6e8ee'; });
  reveal(bK, seg(t, a, a + .3));
  const rt = RTT();
  DD.forEach((d, k) => { const q = E.out5(seg(t, rt[k], rt[k] + .3)); show(d, q > 0); d.style.background = BLUE; d.style.borderColor = '#dfe7ff'; d.style.transform = `translateY(${-(1 - q) * 160}px) scale(${q})`; });
  DN.forEach((d, i) => { const k = [0, 1, 3, 4][i]; const q = E.out(seg(t, rt[k] + .1, rt[k] + .35)); show(d, q > 0); d.style.opacity = q; d.style.fontSize = '84px'; d.style.top = '1230px'; d.style.color = '#fff'; });
  const mq = E.out5(seg(t, T.sab - .12, T.sab + .2)); show(MATCH, mq > 0); MATCH.style.opacity = mq; MATCH.style.transform = `scale(${(1.3 - .3 * mq) * pulse(t, T.sab - .12, .05)})`;
  COLS[4].style.borderColor = mq > 0 ? BLUE : '#2a3040';
  const fl = Math.exp(-Math.pow((t - T.sab + .1) / .07, 2)); $('grain').style.opacity = .05 + .1 * fl;
}

// ── C · la tuya: 18 puntos por día (papel) → se apagan → «como si vinieran todos» se encienden todos ──
const PD = []; const NP = 18;
const OFF = [[2, 7, 11, 15], [4, 9, 13, 16, 17], [1, 6, 10, 14], [0, 3, 5, 8, 12, 15, 17], [3, 9]]; // ausencias de ejemplo por día
for (let c = 0; c < 5; c++) for (let k = 0; k < NP; k++) {
  const x = BX[c] - 45 + (k % 3) * 45, y = 690 + Math.floor(k / 3) * 100;
  PD.push(mk('div', `position:absolute;left:${x - 17}px;top:${y - 17}px;width:34px;height:34px;border-radius:50%;display:none`, '', BOARD)); PD[PD.length - 1]._c = c; PD[PD.length - 1]._k = k;
}
const cK = tx('<div class="kick ink" style="letter-spacing:.24em">TÚ NO TIENES INTERNACIONALES</div>', 330, '', 42);
const cL = tx(M('<span class="S blue" style="font-size:150px">la tuya.</span>'), 380, '', 150);
const LBL = [[0, 'examen', 'martes'], [3, 'solo hoy', 'viernes']].map(([c, w, k]) => { const d = mk('div', `position:absolute;left:${BX[c] - 130}px;top:1420px;width:260px;text-align:center;display:none`, `<span class="S" style="font-size:72px;color:${RED}">${w}</span>`, BOARD); d._k = k; d._c = c; return d; });
const cT = tx(M('COMO SI VINIERAN'), 1300, 'M8 ink', 104);
const cT2 = tx(M('<span class="S blue">todos.</span>'), 1410, '', 170);
function sC(t) {
  const a = T.tu - .06, b = T.guar - .06, v = t >= a && t < b; [cK, cL, cT, cT2].forEach(e => show(e, false)); PD.forEach(p => show(p, false)); LBL.forEach(l => show(l, false));
  if (!v) return;
  show($('paper'), true); show(BOARD, true); [...DD, ...DN, MATCH].forEach(e => show(e, false));
  const q0 = E.out5(seg(t, a, a + .35));
  COLS.forEach((c, i) => { c.style.opacity = 1; c.style.transform = `translateY(${(1 - q0) * 40}px)`; c.style.background = '#fbfaf6'; c.style.borderColor = '#d6d2c6'; c.firstChild.style.color = INK; });
  show(cK, t < T.tienes - .1); cK.style.opacity = E.out(seg(t, a, a + .25));
  show(cL, t >= T.tienes - .15 && t < T.como - .12); reveal(cL, seg(t, T.tienes - .15, T.tienes + .15));
  const all = t >= T.como - .12;
  PD.forEach((p, j) => {
    const c = p._c, k = p._k; show(p, true);
    const appear = E.out(seg(t, a + .15 + j * .004, a + .45 + j * .004));
    // las ausencias se apagan de golpe en martes (examen) y viernes (solo hoy); el resto de días, poco a poco
    const offT = c === 0 ? T.examen - .05 : c === 3 ? T.viernes - .05 : T.inter + .2 + c * .35;
    const off = OFF[c].includes(k) && t >= offT && !all;
    const on = all ? E.out5(seg(t, T.como - .12 + j * .002, T.como + .2 + j * .002)) : 0;
    p.style.background = off ? 'transparent' : (on > .5 ? BLUE : '#9aa2b3');
    p.style.border = off ? '3px dashed #c3bfb2' : 'none';
    p.style.transform = `scale(${appear * (on > 0 && on < 1 ? 1 + .3 * Math.sin(on * Math.PI) : 1)})`;
  });
  LBL.forEach(l => { const t0 = T[l._k] - .1; const on = t >= t0 && !all; show(l, on); if (on) { const q = E.out5(seg(t, t0, t0 + .25)); l.style.opacity = q; l.style.transform = `translateY(${(1 - q) * 30}px)`; } });
  COLS.forEach((c, i) => { const hl = !all && ((i === 0 && t >= T.examen - .1) || (i === 3 && t >= T.viernes - .1)); c.style.borderColor = hl ? RED : (all ? BLUE : '#d6d2c6'); });
  if (all) { show(cT, true); reveal(cT, seg(t, T.como - .12, T.como + .15)); show(cT2, t >= T.todos1 - .15); reveal(cT2, seg(t, T.todos1 - .15, T.todos1 + .15)); cT2.style.transform = `scale(${pulse(t, T.todos1 - .15, .06)})`; }
  BOARD.style.transform = all ? `translateY(${-150 * E.out(seg(t, T.como - .12, T.como + .3))}px)` : `scale(${1 + .035 * seg(t, a, T.como)}) translateY(${-14 * seg(t, a, T.como)}px)`;
  const fl = Math.exp(-Math.pow((t - T.como + .1) / .07, 2)); $('grain').style.opacity = .05 + .12 * fl;
}

// ── D · ficha para guardar: ANTES DE ESCRIBIR LA SEMANA · 1 · 2 (papel, 7,5 s) ──
const CARD = mk('div', 'position:absolute;left:90px;top:520px;width:900px;height:900px;border-radius:40px;background:#fff;border:3px solid #d6d2c6;box-shadow:0 30px 70px rgba(13,15,20,.14);display:none', `
  <div style="position:absolute;left:70px;top:70px;font-family:M;font-weight:700;font-size:36px;letter-spacing:.2em;color:#6d7588">ANTES DE ESCRIBIR LA SEMANA</div>
  <div id="r1" style="position:absolute;left:70px;top:210px;right:60px"><div style="position:absolute;left:0;top:0;width:110px;height:110px;border-radius:50%;background:${BLUE};color:#fff;font-family:M;font-weight:800;font-size:64px;text-align:center;line-height:110px">1</div>
    <div style="position:absolute;left:150px;top:-4px;font-family:M;font-weight:800;font-size:72px;letter-spacing:-.04em;color:${INK};line-height:1.02">Quién viene<br><span class="S" style="color:${BLUE};font-size:84px">cada día.</span></div></div>
  <div id="r2" style="position:absolute;left:70px;top:520px;right:60px"><div style="position:absolute;left:0;top:0;width:110px;height:110px;border-radius:50%;background:${BLUE};color:#fff;font-family:M;font-weight:800;font-size:64px;text-align:center;line-height:110px">2</div>
    <div style="position:absolute;left:150px;top:-4px;font-family:M;font-weight:800;font-size:72px;letter-spacing:-.04em;color:${INK};line-height:1.02">Lo de todos,<br><span class="S" style="color:${BLUE};font-size:84px">el día que más sois.</span></div></div>`, $('cards'));
const dG = tx('<span style="display:inline-block;padding:18px 40px;border-radius:999px;background:' + INK + ';color:#f2f1ec;font-family:M;font-weight:800;font-size:44px;letter-spacing:.14em">GUÁRDATELO</span>', 340, '', 44);
function sD(t) {
  const a = T.guar - .06, b = T.preg - .06, v = t >= a && t < b; show(CARD, v); show(dG, v); if (!v) return;
  show($('paper'), true);
  const q = E.out5(seg(t, a, a + .45)); CARD.style.opacity = q; CARD.style.transform = `translateY(${(1 - q) * 120}px) rotate(${-1.2 * (1 - q)}deg) scale(${1 + .05 * seg(t, a, b)}) translateY(${-0 * seg(t, a, b)}px)`; CARD.style.marginTop = `${-36 * seg(t, a, b)}px`;
  dG.style.opacity = q; dG.style.transform = `scale(${pulse(t, a, .06)})`;
  [['r1', T.antes - .1], ['r2', T.necesita - .3]].forEach(([id, t0]) => { const k = E.out5(seg(t, t0, t0 + .35)); $(id).style.opacity = k; $(id).style.transform = `translateX(${(1 - k) * 60}px)`; });
}

// ── E · reto para el staff (vuelta a Riazor: bucle) ──
const eK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">RETO PARA TU STAFF</div>', 640, 'shadow', 46);
const eQ = tx(M('¿QUÉ DÍA'), 720, 'M8 shadow', 190);
const eT = tx(M('<span class="S blue">estáis todos?</span>'), 930, 'shadow', 150);
function sE(t) {
  const a = T.preg - .06, b = T.el28 - .06, v = t >= a && t < b; [eK, eQ, eT].forEach(e => show(e, v)); if (!v) return;
  show(RZ, true); RZ._img.style.objectPosition = `${38 + 10 * seg(t, a, b)}% 50%`; place(RZ, { is: 1.1 + .04 * seg(t, a, b), dark: .58, z: 1 });
  eK.style.opacity = E.out(seg(t, a, a + .25));
  show(eQ, t >= T.que2 - .3); reveal(eQ, seg(t, T.que2 - .3, T.que2)); show(eT, t >= T.entr - .1); reveal(eT, seg(t, T.entr - .1, T.entr + .2));
  eT.style.transform = `scale(${pulse(t, T.todos2 - .1, .05)})`;
}

// ── F · ABRE EL SÁBADO 28 NOV · la app de ProTeam ──
const fK = tx('<div class="kick" style="letter-spacing:.26em;color:#e6e8ee">ABRE EL SÁBADO</div>', 640, '', 46);
const f28 = tx('28 NOV', 710, 'M8', 250);
const fA = tx(M('LA APP DE <span style="color:#4f86ff">PROTEAM</span>'), 1010, 'M8', 70);
function sF(t) {
  const a = T.el28 - .06, b = T.camp - .05, v = t >= a && t < b; [fK, f28, fA].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true); $('sysL').style.background = INK;
  fK.style.opacity = E.out(seg(t, a, a + .25));
  const q = E.out5(seg(t, T.v28 - .3, T.v28 - .05)); f28.style.opacity = q; f28.style.color = '#4f86ff';
  f28.style.transform = `scale(${(1.2 - .2 * q) * (1 + .04 * seg(t, T.v28, b))})`;
  show(fA, t >= T.pt - .5); reveal(fA, seg(t, T.pt - .5, T.pt - .1));
  const fl = Math.exp(-Math.pow((t - T.v28 + .2) / .07, 2)); $('grain').style.opacity = .05 + .15 * fl;
}

// ── H · final en bucle: la semana de la tuya, en papel, bajo el cierre ──
function sH(t) {
  const g0 = T.gra - .1; if (t < g0) return; show($('paper'), true); show(BOARD, true);
  const q = E.out5(seg(t, g0, g0 + .4));
  COLS.forEach((c, i) => { c.style.opacity = .35 * q; c.style.transform = `translateY(${800 + 40 * (1 - q)}px) scale(.38)`; c.style.transformOrigin = '50% 0'; c.style.background = '#fbfaf6'; c.style.borderColor = '#d6d2c6'; c.firstChild.style.color = INK; });
}

window.frame = t => {
  show($('sysL'), false); $('sysL').style.background = '#0d0f14'; show($('paper'), false); show(BOARD, false); BOARD.style.transform = 'none';
  [RZ].forEach(p => show(p, false)); $('grain').style.opacity = .05;
  COLS.forEach(c => { c.style.transformOrigin = '50% 50%'; });
  show(TOP, t < T.tu - .06); TOP.style.opacity = 1;
  sA(t); sB(t); sC(t); sD(t); sE(t); sF(t); sH(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
