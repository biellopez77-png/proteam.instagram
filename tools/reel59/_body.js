// u59 · IMPACTO · concepto: «la tira de los diez días» — la cuenta atrás convertida en la semana real del entrenador: una tira de calendario
// de once casillas (MIÉ 18 → SÁB 28) sobre Jordi Ribera (seleccionador español de balonmano) a sangre. Se encienden 5 ENTRENOS y 2 PARTIDOS,
// las sesiones se llenan de garabato («de memoria») y los partidos de una interrogación («de cabeza»); en «veintiocho» la última casilla
// crece hasta llenar la pantalla (SÁB 28 NOV · abre ProTeam); vuelve la tira sobre la foto (bucle) para el reto «¿cuántos tenéis escritos?» y
// cierre de la lista de espera. Ninguna pantalla de la app. Sin «día N de 10».
const GR = 'linear-gradient(180deg,rgba(0,0,0,.62) 0%,rgba(0,0,0,.22) 28%,rgba(0,0,0,.08) 46%,rgba(0,0,0,.55) 64%,rgba(0,0,0,.88) 100%)';
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));

const WP = ph('rib', '50% 20%');
const WB = ph('rib', '50% 25%'); WB._img.style.filter = 'blur(30px) brightness(.36) saturate(.8)';

// ── la tira: 11 casillas en dos filas (6 + 5) ──
const DAYS = [['MIÉ', 18, 'E'], ['JUE', 19], ['VIE', 20, 'E'], ['SÁB', 21, 'P'], ['DOM', 22], ['LUN', 23, 'E'], ['MAR', 24], ['MIÉ', 25, 'E'], ['JUE', 26], ['VIE', 27, 'E'], ['SÁB', 28, 'G']];
const GRID = mk('div', 'position:absolute;left:0;top:0;width:1080px;height:1920px;display:none;z-index:3', '', $('cards'));
const TW = 150, TH = 176, GAP = 14;
const tiles = DAYS.map(([d, n, k], i) => {
  const row = i < 6 ? 0 : 1, col = i < 6 ? i : i - 6, cols = row ? 5 : 6;
  const x0 = (1080 - (cols * TW + (cols - 1) * GAP)) / 2, x = x0 + col * (TW + GAP), y = row * (TH + GAP);
  const el = mk('div', `position:absolute;left:${x}px;top:${y}px;width:${TW}px;height:${TH}px;border-radius:22px;background:rgba(18,22,32,.82);border:2px solid rgba(255,255,255,.14);overflow:hidden;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)`,
    `<div style="position:absolute;left:0;right:0;top:16px;text-align:center;font-family:M;font-weight:700;font-size:24px;letter-spacing:.14em;color:#9aa2b3">${d}</div>
     <div class="n" style="position:absolute;left:0;right:0;top:46px;text-align:center;font-family:M;font-weight:800;font-size:66px;letter-spacing:-.04em;color:#f2f1ec">${n}</div>
     <div class="lb" style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font-family:M;font-weight:800;font-size:19px;letter-spacing:.1em;color:#fff;opacity:0">${k === 'E' ? 'ENTRENO' : k === 'P' || k === 'G' ? 'PARTIDO' : ''}</div>
     <svg class="scr" viewBox="0 0 150 176" style="position:absolute;inset:0;width:150px;height:176px;opacity:0"><path d="M18 60 C 40 40, 60 95, 80 62 S 120 50, 132 82 C 110 100, 70 88, 40 112 S 30 140, 128 132" fill="none" stroke="#f2f1ec" stroke-width="7" stroke-linecap="round" stroke-dasharray="460" stroke-dashoffset="460"/></svg>
     <div class="q" style="position:absolute;left:0;right:0;top:20px;text-align:center;font-family:S;font-style:italic;font-size:150px;line-height:150px;color:#0d0f14;opacity:0">?</div>`, GRID);
  el._k = k; el._scr = el.querySelector('.scr path'); el._svg = el.querySelector('.scr'); el._lb = el.querySelector('.lb'); el._n = el.querySelector('.n'); el._q = el.querySelector('.q'); el._x = x; el._y = y;
  return el;
});
const TR = tiles.filter(e => e._k === 'E'), MA = tiles.filter(e => e._k === 'P' || e._k === 'G'), G28 = tiles[10];
function grid(t, top, sc, a0) {
  show(GRID, true); GRID.style.top = top + 'px'; GRID.style.transformOrigin = '50% 0'; GRID.style.transform = `scale(${sc})`;
  tiles.forEach((el, i) => { const q = E.out5(seg(t, a0 + i * .04, a0 + .35 + i * .04)); el.style.opacity = q; el.style.transform = `translateY(${(1 - q) * 50}px)`;
    el.style.background = 'rgba(18,22,32,.82)'; el.style.borderColor = 'rgba(255,255,255,.14)'; el._lb.style.opacity = 0; el._svg.style.opacity = 0; el._q.style.opacity = 0; el._n.style.color = '#f2f1ec'; el._scr.setAttribute('stroke-dashoffset', 460); });
  G28.style.borderColor = '#4f86ff';
}
function lightE(t, t0) { TR.forEach((el, i) => { const q = E.out(seg(t, t0 + i * .1, t0 + .25 + i * .1)); if (q > 0) { el.style.background = `rgba(47,107,255,${.85 * q})`; el.style.borderColor = '#4f86ff'; el._lb.style.opacity = q; el.style.transform = `scale(${pulse(t, t0 + i * .1, .08)})`; } }); }
function lightP(t, t0) { MA.forEach((el, i) => { const q = E.out(seg(t, t0 + i * .12, t0 + .25 + i * .12)); if (q > 0) { el.style.background = `rgba(242,241,236,${.95 * q})`; el._n.style.color = q > .5 ? '#0d0f14' : '#f2f1ec'; el._lb.style.opacity = q; el._lb.style.color = '#0d0f14'; el.style.transform = `scale(${pulse(t, t0 + i * .12, .08)})`; } }); }
function scrib(t, t0) { TR.forEach((el, i) => { const q = E.io(seg(t, t0 + i * .12, t0 + .55 + i * .12)); el._svg.style.opacity = q > 0 ? 1 : 0; el._scr.setAttribute('stroke-dashoffset', 460 * (1 - q)); el._n.style.opacity = 1 - .6 * q; }); }
function quest(t, t0) { MA.forEach((el, i) => { const q = E.out5(seg(t, t0 + i * .15, t0 + .35 + i * .15)); el._q.style.opacity = q; el._q.style.transform = `scale(${1.6 - .6 * q}) rotate(${(1 - q) * -12}deg)`; el._n.style.opacity = 1 - .85 * q; }); }

// ── A · 10 DÍAS (0 → «Cinco sesiones…») ──
const aK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.24em">BALONMANO</div>', 250, 'shadow', 40);
const aH = tx('10 DÍAS', 300, 'M8 shadow', 250);
const aS1 = tx(M('<span class="S blue">5 entrenos · 2 partidos</span>'), 580, 'shadow', 104);
function sA(t) {
  const b = T.ses - .04, v = t < b; [WP, aK, aH].forEach(e => show(e, v)); if (!v) { show(aS1, false); return; }
  place(WP, { is: 1.05 + .12 * E.io(seg(t, 0, b)), iy: 20 - 40 * seg(t, 0, b), org: '50% 25%', grad: GR });
  aH.style.transform = `scale(${pulse(t, 0, 0) * pulse(t, T.dias - .1, .05) * (1 + .03 * seg(t, 0, b))})`;
  grid(t, 1240 - 40 * seg(t, 0, b), 1, .7);
  // «tres días por semana»: un foco recorre la tira casilla a casilla (sin imagen quieta antes de que se enciendan)
  if (t >= T.si && t < T.cinco - .05) { const k = Math.min(10, Math.floor(11 * seg(t, T.si, T.cinco - .1))); tiles.forEach((el, i) => { const on = i === k; el.style.borderColor = on ? '#f2f1ec' : 'rgba(255,255,255,.14)'; if (on) el.style.transform = 'scale(1.07)'; }); }
  lightE(t, T.cinco - .05); lightP(t, T.dos - .05);
  show(aS1, t >= T.cinco - .05); reveal(aS1, seg(t, T.cinco - .05, T.cinco + .3));
}
// ── B · DE MEMORIA / DE CABEZA ──
const bK = tx('<div class="kick" style="color:#e6e8ee">5 SESIONES</div>', 300, 'shadow', 40);
const bM = tx(M('<span class="S blue">de memoria.</span>'), 350, 'shadow', 190);
const bK2 = tx('<div class="kick" style="color:#e6e8ee">2 PARTIDOS</div>', 1520, 'shadow', 40);
const bC = tx(M('<span class="S blue">de cabeza.</span>'), 1570, 'shadow', 190);
function sB(t) {
  const a = T.ses - .04, b = T.sab - .04, v = t >= a && t < b, v2 = t >= a && t < T.v28 - .3; [bK, bM].forEach(e => show(e, v)); [bK2, bC].forEach(e => show(e, v2));
  if (v2 && !v) { show(bK2, true); bK2.style.opacity = 1; show(bC, true); reveal(bC, 1); }
  if (!v) return;
  show(WP, true); place(WP, { is: 1.2 + .2 * seg(t, a, b), iy: -30 * seg(t, a, b), org: '50% 22%', dark: .62 });
  const k = E.io(seg(t, a, a + .5)); grid(t, 1200 - 480 * k - 50 * seg(t, a + .5, b), 1 + .04 * seg(t, a + .5, b), -9);
  lightE(t, -9); lightP(t, -9); scrib(t, T.memoria - .5); quest(t, T.cabeza - .1);
  show(bK, true); bK.style.opacity = E.out(seg(t, a, a + .3)); reveal(bM, seg(t, T.memoria - .15, T.memoria + .2)); show(bM, t >= T.memoria - .15);
  show(bK2, t >= T.par - .05); bK2.style.opacity = E.out(seg(t, T.par - .05, T.par + .25)); show(bC, t >= T.cabeza - .1); reveal(bC, seg(t, T.cabeza - .1, T.cabeza + .25));
}
// ── C · la casilla del 28 crece: SÁB 28 NOV · abre ProTeam (golpe en «veintiocho») ──
const BIG = mk('div', 'position:absolute;display:none;z-index:4;border-radius:22px;background:#2f6bff', '', $('cards'));
const c0 = tx('<div class="kick" style="letter-spacing:.24em;color:#e6e8ee">EL SÁBADO</div>', 520, '', 40);
const c1 = tx('SÁB 28', 570, 'M8 shadow', 270), c1b = tx('NOV', 860, 'M8', 150);
const c2 = tx(M('<span class="S" style="color:#fff">abre ProTeam.</span>'), 1060, 'shadow', 140);
const SP = ['FÚTBOL', 'BALONCESTO', 'BALONMANO'].map((w, i) => tx(w, 1330 + i * 92, 'M7', 62));
function sC(t) {
  const a = T.sab - .04, b = T.mand - .04, v = t >= a && t < b; [c0, c1, c1b, c2, ...SP].forEach(e => show(e, v)); show(BIG, v); if (!v) return;
  const cp = t >= T.para - .04;   // corte seco en «para entrenadores…»: vuelve Ribera nítido y oscurecido, con zoom de salida
  show(WB, !cp); show(WP, cp); if (!cp) place(WB, { is: 1.6 - .4 * seg(t, a, b), iy: -80 + 160 * seg(t, a, b), z: 1 });
  else place(WP, { is: 1.32 - .24 * E.io(seg(t, T.para - .04, b)), iy: -60 + 120 * seg(t, T.para - .04, b), org: '50% 25%', dark: .72, z: 1 });
  // antes del golpe: la tira sigue, la casilla del 28 parpadea; en «veintiocho» crece hasta llenar la pantalla
  const g = E.io(seg(t, T.v28 - .3, T.v28 + .05));
  if (t < T.v28 + .05) { grid(t, 720, 1, -9); lightE(t, -9); lightP(t, -9); scrib(t, -9); quest(t, -9); GRID.style.opacity = 1 - g; G28._q.style.opacity = 0; G28._n.style.opacity = 1; G28.style.background = '#2f6bff'; G28._n.style.color = '#fff'; G28._lb.style.color = '#fff'; }
  else show(GRID, false);
  const x0 = G28._x, y0 = 720 + G28._y; BIG.style.left = (x0 * (1 - g)) + 'px'; BIG.style.top = (y0 * (1 - g)) + 'px';
  BIG.style.width = (TW + (1080 - TW) * g) + 'px'; BIG.style.height = (TH + (1920 - TH) * g) + 'px'; BIG.style.borderRadius = (22 * (1 - g)) + 'px';
  const fade = seg(t, T.v28 + .4, T.v28 + 1.0); show(BIG, !cp && t >= T.v28 - .3); BIG.style.background = `rgba(47,107,255,${1 - .78 * fade})`;
  if (fade >= 1) { const sx = -30 + 160 * seg(t, T.v28 + 1.0, b), sy = 30 + 40 * seg(t, T.v28 + 1.0, b); BIG.style.background = `radial-gradient(520px 760px at ${sx}% ${sy}%, rgba(79,134,255,.42), rgba(47,107,255,.22) 60%, rgba(47,107,255,.18))`; }
  show(c0, t < T.v28 - .25); c0.style.opacity = E.out(seg(t, a, a + .3));
  show(c1, t >= T.v28 - .02); show(c1b, t >= T.v28 + .08);
  c1.style.transform = `translateY(${-40 * seg(t, T.v28, b)}px) scale(${pulse(t, T.v28 - .02, .09) * (1 + .1 * seg(t, T.v28, b))})`; c1b.style.transform = `translateY(${-30 * seg(t, T.v28, b)}px) scale(${1 + .1 * seg(t, T.v28, b)})`; c1.style.opacity = E.out(seg(t, T.v28 - .02, T.v28 + .12));
  c1b.style.opacity = E.out(seg(t, T.v28 + .08, T.v28 + .3)); c1b.style.color = fade > .5 ? '#4f86ff' : '#0d0f14';
  show(c2, t >= T.abre + .2); reveal(c2, seg(t, T.abre + .2, T.abre + .5)); c2.querySelector('.S').style.color = fade > .5 ? '#4f86ff' : '#fff';
  [T.fut, T.bal, T.bm2].forEach((k, i) => { const q = E.out(seg(t, k - .05, k + .25)); show(SP[i], t >= k - .05); SP[i].style.opacity = q; SP[i].style.transform = `translateY(${(1 - q) * 30}px)`; SP[i].style.color = i === 2 ? '#f2f1ec' : '#c9cfdb'; });
  const fl = Math.exp(-Math.pow((t - T.v28) / .07, 2)); $('grain').style.opacity = .05 + .25 * fl;
}
// ── D · vuelve la foto y la tira (bucle): RETO · ¿cuántos tenéis escritos? __/5 ──
const d0 = tx('<div class="kick" style="color:#e6e8ee">RETO PARA TU STAFF</div>', 300, 'shadow', 40);
const d1 = tx(M('MÁNDASELO'), 345, 'M8 shadow', 150);
const d2 = tx(M('<span class="S blue">a tu segundo.</span>'), 505, 'shadow', 120);
const d3 = tx(M('¿Cuántos tenéis'), 1520, 'M8 shadow', 96);
const d4 = tx(M('<span class="S blue">ya escritos?</span>'), 1630, 'shadow', 120);
const d5 = tx('', 1000, 'M8 shadow', 210);
function sD(t) {
  const a = T.mand - .04, b = T.camp - .05, v = t >= a && t < b; [d0, d1, d2, d3, d4, d5].forEach(e => show(e, v)); if (!v) return;
  show(WP, true); place(WP, { is: 1.06 + .05 * seg(t, a, b), org: '50% 25%', dark: .55 });
  grid(t, 760, .92, a - .2); lightE(t, a); TR.forEach(el => { el._n.style.opacity = 1; });
  d0.style.opacity = E.out(seg(t, a, a + .3)); reveal(d1, seg(t, a + .05, a + .35)); show(d2, t >= T.mand + .7); reveal(d2, seg(t, T.mand + .7, T.mand + 1.0));
  show(d3, t >= T.cuan - .05); reveal(d3, seg(t, T.cuan - .05, T.cuan + .3)); show(d4, t >= T.escritos - .3); reveal(d4, seg(t, T.escritos - .3, T.escritos + .05));
  GRID.style.opacity = 1 - .75 * E.out(seg(t, T.cinco2 - .1, T.cinco2 + .3));
  show(d5, t >= T.cinco2 - .1); d5.innerHTML = `<span style="color:#4f86ff">${Math.floor(t * 2.5) % 2 ? '_' : '?'}</span> / 5`;
  d5.style.opacity = E.out(seg(t, T.cinco2 - .1, T.cinco2 + .2)); d5.style.transform = `scale(${pulse(t, T.cinco2 - .1, .08)})`;
}

window.frame = t => {
  show($('sysL'), false); show($('paper'), false); show(GRID, false); show(BIG, false); GRID.style.opacity = 1; $('grain').style.opacity = .05;
  tiles.forEach(el => { el._n.style.opacity = 1; el._lb.style.color = '#fff'; });
  sA(t); sB(t); sC(t); sD(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
