
// u72 · CONTEXTO · Reel de datos corto (versión corta de u52) · concepto: «tres franjas, un lunes» — tres franjas verticales a sangre
// (Unai Simón con España, Kawhi Leonard en las Finales de la NBA, Tobias Reichmann en la Bundesliga de balonmano). Cada franja se
// enciende con su número (11 · 5 · 7) en la palabra exacta; en «lunes» (golpe de música) las tres se juntan, se apagan y cae una sola
// hoja de lunes con tres casillas (SEMANA · CONVOCATORIA · MINUTOS) que se marcan; «ProTeam.» para los tres; cierre de la lista con contador.
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));
const SPS = [['fut', '50% 30%', '11', 'FÚTBOL'], ['bal', '45% 30%', '5', 'BALONCESTO'], ['bm', '42% 40%', '7', 'BALONMANO']];
const ST = SPS.map(([n, pos]) => ph(n, pos));
const NUM = SPS.map(([, , n], i) => tx(n, 0, 'M8 shadow', 300));
const LAB = SPS.map(([, , , l], i) => tx(`<div class="kick" style="color:#e6e8ee;font-size:30px;letter-spacing:.16em">${l}</div>`, 0, 'shadow', 30));
const KEYS = () => [T.once, T.cinco, T.siete];
function strips(t, merge, dim) {
  // merge 0 → tres franjas de 360 px; 1 → juntas en el centro (ancho 0) y apagadas
  ST.forEach((el, i) => { show(el, true); place(el, { is: 1.12 + .05 * seg(t, 0, 6), org: '50% 40%', dark: dim[i], z: 1 });
    const w = 360 * (1 - merge) + 2 * merge, x = i * 360 * (1 - merge) + 539 * merge;
    el.style.width = w + 'px'; el.style.left = x + 'px'; el.style.borderRight = i < 2 ? '4px solid #000' : 'none'; });
}
// ── A · 11 · 5 · 7 (fotograma 0: las tres franjas y el 11 ya puesto) ──
const aK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.24em">EN JUEGO</div>', 300, 'shadow', 40);
function sA(t) {
  const b = T.tres - .04, v = t < b; show(aK, v); NUM.forEach(e => show(e, false)); LAB.forEach(e => show(e, false)); if (!v) return;
  const K = KEYS(); const dim = K.map((k, i) => (i === 0 || t >= k - .05) ? .25 : .72);
  strips(t, 0, dim);
  K.forEach((k, i) => { const on = i === 0 || t >= k - .05; show(NUM[i], on); show(LAB[i], on);
    const q = i === 0 ? 1 : E.out5(seg(t, k - .05, k + .2));
    NUM[i].style.width = '360px'; NUM[i].style.left = (i * 360) + 'px'; NUM[i].style.top = '820px';
    NUM[i].style.opacity = q; NUM[i].style.transform = `scale(${(1.3 - .3 * q) * pulse(t, k - .05, .07)})`; NUM[i].style.color = i === 1 ? '#4f86ff' : '#fff';
    LAB[i].style.width = '360px'; LAB[i].style.left = (i * 360) + 'px'; LAB[i].style.top = '1160px'; LAB[i].style.opacity = q; });
}
// ── B · TRES DEPORTES · EL MISMO LUNES (golpe en «lunes») ──
const bK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.24em">TRES DEPORTES</div>', 640, 'shadow', 44);
const bM = tx(M('EL MISMO'), 700, 'M8 shadow', 120);
const bL = tx(M('<span class="S blue">lunes.</span>'), 830, 'shadow', 260);
const SHEET = mk('div', 'position:absolute;left:150px;width:780px;height:640px;top:1120px;border-radius:34px;background:#f2f1ec;display:none;box-shadow:0 30px 70px rgba(0,0,0,.55)',
  ['SEMANA', 'CONVOCATORIA', 'MINUTOS'].map((w, i) => `<div style="position:absolute;left:60px;top:${70 + i * 190}px;width:660px;height:150px">
    <div class="bx" style="position:absolute;left:0;top:30px;width:90px;height:90px;border-radius:20px;border:5px solid #0d0f14"></div>
    <svg class="ck" viewBox="0 0 90 90" style="position:absolute;left:0;top:30px;width:90px;height:90px"><path d="M18 47l17 17 37-40" fill="none" stroke="#2f6bff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="90" stroke-dashoffset="90"/></svg>
    <div style="position:absolute;left:130px;top:38px;font-family:M;font-weight:800;font-size:64px;letter-spacing:-.03em;color:#0d0f14">${w}</div></div>`).join(''), $('cards'));
const CK = [...SHEET.querySelectorAll('.ck path')];
function sB(t) {
  const a = T.tres - .04, b = T.por - .04, v = t >= a && t < b; [bK, bM, bL].forEach(e => show(e, v)); show(SHEET, v); if (!v) return;
  const mg = E.io(seg(t, T.lunes - .1, T.lunes + .35));
  strips(t, mg, [.6, .6, .6].map(d => d + .3 * mg));
  // tras el golpe, fondo: la franja de baloncesto abierta a pantalla completa, muy oscura y en movimiento
  if (mg >= 1) { ST.forEach((el, i) => show(el, i === 1)); place(ST[1], { is: 1.3 + .12 * seg(t, T.lunes, b), iy: -30 * seg(t, T.lunes, b), org: '50% 30%', dark: .8, z: 1 }); }
  bK.style.opacity = E.out(seg(t, a, a + .25)); show(bM, t >= T.mismo - .1); reveal(bM, seg(t, T.mismo - .1, T.mismo + .2));
  const up = E.io(seg(t, T.semana - .45, T.semana - .1));
  [bK, bM, bL].forEach((e, i) => e.style.top = ([640, 700, 830][i] - 380 * up) + 'px');
  show(bL, t >= T.lunes - .05); reveal(bL, seg(t, T.lunes - .05, T.lunes + .25)); bL.style.transform = `scale(${pulse(t, T.lunes - .05, .07)})`;
  const sp = E.out5(seg(t, T.semana - .12, T.semana + .25)); SHEET.style.opacity = sp; SHEET.style.top = (1120 - 300 * sp + 40 * (1 - sp)) + 'px';
  SHEET.style.transform = `rotate(${-2 + 2 * sp}deg)`;
  [T.semana, T.conv, T.min].forEach((k, i) => CK[i].setAttribute('stroke-dashoffset', 90 * (1 - E.out(seg(t, k - .05, k + .25)))));
  const fl = Math.exp(-Math.pow((t - T.lunes) / .07, 2)); $('grain').style.opacity = .05 + .25 * fl;
}
// ── C · ProTeam. para los tres · abre el sábado 28 ──
const cK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.24em">POR ESO</div>', 600, 'shadow', 44);
const cP = tx('ProTeam.', 660, 'M8 shadow', 220);
const cT = tx(M('<span class="S blue">para los tres.</span>'), 920, 'shadow', 130);
const cD = tx('<div class="kick" style="color:#c9cfdb;letter-spacing:.22em">ABRE EL SÁB 28 NOV</div>', 1500, 'shadow', 40);
function sC(t) {
  const a = T.por - .04, b = T.camp - .05, v = t >= a && t < b; [cK, cP, cT, cD].forEach(e => show(e, v)); if (!v) return;
  // vuelven las tres franjas (bucle con el principio), oscurecidas
  const op = E.io(seg(t, a, a + .4)); strips(t, 1 - op, [.62, .62, .62]);
  cK.style.opacity = E.out(seg(t, a, a + .25)); const q = E.out5(seg(t, T.pt - .1, T.pt + .2)); show(cP, t >= T.pt - .1); cP.style.opacity = q;
  cP.style.transform = `scale(${(1.15 - .15 * q) * pulse(t, T.pt - .1, .05)})`;
  show(cT, t >= T.tres2 - .15); reveal(cT, seg(t, T.tres2 - .15, T.tres2 + .15));
  cD.style.opacity = E.out(seg(t, T.tres2, T.tres2 + .3));
}

window.frame = t => {
  show($('sysL'), false); show($('paper'), false); show(SHEET, false); ST.forEach(p => show(p, false)); $('grain').style.opacity = .05;
  sA(t); sB(t); sC(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
