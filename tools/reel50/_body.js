// u50 · IMPACTO · concepto: «la pantalla de bloqueo del domingo» — el Reel es el móvil del entrenador a las 23:00: reloj grande de pantalla
// de bloqueo sobre la foto de un entrenador de primer nivel (Pablo Laso) como fondo; entra la notificación del segundo («¿Qué hacemos el martes?»,
// sin logos de terceros), el móvil vibra; en «veintiocho» el widget de fecha salta a SÁB 28 NOV con golpe de música; contador de días; vuelve la
// notificación (bucle con el principio) para el reto de enviarlo; cierre de la lista de espera. Ninguna pantalla de la app. Sin «día N de 10».
const GR = 'linear-gradient(180deg,rgba(0,0,0,.62) 0%,rgba(0,0,0,.25) 30%,rgba(0,0,0,.05) 48%,rgba(0,0,0,.5) 68%,rgba(0,0,0,.85) 100%)';
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));
const buzz = (t, t0) => { const k = seg(t, t0, t0 + .45); return k > 0 && k < 1 ? Math.sin(k * 60) * 9 * (1 - k) : 0; };

// fondo de pantalla de bloqueo: Laso nítido + versión desenfocada para los bloques de fecha
const WP = ph('laso', '50% 22%');
const WB = ph('laso', '50% 30%'); WB._img.style.filter = 'blur(30px) brightness(.38) saturate(.8)';

// reloj de pantalla de bloqueo
const kDom = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.24em">DOMINGO</div>', 300, 'shadow', 40);
const clk = tx('23:00', 350, 'M8 shadow', 300);
const hk2 = tx(M('<span class="S blue">la semana, sin preparar.</span>'), 1400, 'shadow', 112);

// notificación genérica (motion graphics, sin marca de ninguna app de mensajería)
const NT = mk('div', 'position:absolute;left:70px;top:1010px;width:940px;height:236px;display:none;border-radius:44px;background:rgba(32,36,46,.72);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:2px solid rgba(255,255,255,.14);box-shadow:0 26px 60px rgba(0,0,0,.55)',
  `<div style="position:absolute;left:34px;top:40px;width:108px;height:108px;border-radius:50%;background:#2f6bff;color:#fff;font-family:M;font-weight:800;font-size:46px;line-height:108px;text-align:center">2º</div>
   <div style="position:absolute;left:170px;top:38px;font-family:M;font-weight:800;font-size:38px;color:#f2f1ec">Tu segundo</div>
   <div style="position:absolute;right:38px;top:44px;font-family:M;font-weight:500;font-size:30px;color:#9aa2b3">ahora</div>
   <div class="nb" style="position:absolute;left:170px;top:100px;width:730px;font-family:M;font-weight:500;font-size:48px;color:#f2f1ec;white-space:nowrap"></div>`);
NT._b = NT.querySelector('.nb');
const MSG = '¿Qué hacemos el martes?';
function notif(t, t0, tType, y) {
  const v = t >= t0; show(NT, v); if (!v) return;
  const p = E.out5(seg(t, t0, t0 + .4)); NT.style.top = (y - (1 - p) * 160) + 'px'; NT.style.opacity = p;
  NT.style.transform = `translateX(${buzz(t, t0 + .05)}px) scale(${.96 + .04 * p})`;
  const n = Math.floor(MSG.length * clamp((t - tType) / .55)); NT._b.textContent = tType <= t0 ? MSG : (n > 0 ? MSG.slice(0, n) : 'Escribiendo…');
  NT._b.style.color = n > 0 || tType <= t0 ? '#f2f1ec' : '#7d8597';
}

// ── A · DOM 23:00 (0 → «Este puede ser…») ──
function sA(t) {
  const b = T.ult - .04, v = t < b; [WP, kDom, clk, hk2].forEach(e => show(e, v)); if (!v) return;
  place(WP, { is: 1.04 + .14 * E.io(seg(t, 0, b)), iy: 24 - 48 * seg(t, 0, b), org: '50% 30%', grad: GR });
  const sh = buzz(t, T.seg - .05); $('phs').style.transform = `translateX(${sh * .6}px)`;
  clk.innerHTML = (t >= T.martes ? '23<span style="opacity:' : '23<span style="opacity:') + (Math.floor(t * 2) % 2 ? .35 : 1) + '">:</span>' + (t >= T.martes ? '01' : '00'); clk.style.transform = `scale(${pulse(t, 0, .0) * pulse(t, T.martes, .05)})`;
  hk2.style.transform = `scale(${pulse(t, T.sem, .05) * (1 + .04 * seg(t, 0, T.seg))})`; reveal(hk2, 1); kDom.style.letterSpacing = (.24 + .1 * seg(t, 0, b)) + 'em';
  notif(t, T.seg - .1, T.que - .05, 1080);
}
// ── B · ¿EL ÚLTIMO DOMINGO ASÍ? ──
const b1 = tx(M('¿EL ÚLTIMO'), 1180, 'M8 shadow', 150);
const b2 = tx(M('<span class="S blue">domingo así?</span>'), 1340, 'shadow', 170);
function sB(t) {
  const a = T.ult - .04, b = T.sab - .04, v = t >= a && t < b; [b1, b2].forEach(e => show(e, v)); if (!v) return;
  show(WP, true); place(WP, { is: 1.22 + .06 * seg(t, a, b), org: '50% 22%', dark: .5 });
  show(kDom, true); show(clk, true); clk.textContent = '23:01'; clk.style.transform = 'scale(.62)'; clk.style.top = '250px'; kDom.style.top = '220px';
  kDom.style.opacity = clk.style.opacity = .55;
  reveal(b1, seg(t, a + .05, a + .35)); show(b2, t >= T.ultimo - .1); reveal(b2, seg(t, T.ultimo - .1, T.ultimo + .25));
}
// ── C · el widget de fecha salta a SÁB 28 NOV (golpe en «veintiocho») ──
const c0 = tx('<div class="kick" style="letter-spacing:.24em">EL SÁBADO</div>', 520, '', 40);
const c1 = tx('SÁB 28', 570, 'M8 shadow', 270), c1b = tx('NOV', 860, 'M8', 150);
const c2 = tx(M('<span class="S blue">abre ProTeam.</span>'), 1060, 'shadow', 140);
const SP = ['FÚTBOL', 'BALONCESTO', 'BALONMANO'].map((w, i) => tx(w, 1330 + i * 92, 'M7', 62));
function sC(t) {
  const a = T.sab - .04, b = T.qued - .14, v = t >= a && t < b; [WB, c0, c1, c1b, c2, ...SP].forEach(e => show(e, v)); if (!v) return;
  place(WB, { is: 1.42 - .2 * seg(t, a, b), iy: -40 + 80 * seg(t, a, b), z: 1 });
  show(c0, t < T.v28 + .05); c0.style.opacity = E.out(seg(t, a, a + .3));
  show(c1, t >= T.v28 - .02); show(c1b, t >= T.v28 + .08);
  c1.style.transform = `scale(${pulse(t, T.v28 - .02, .09) * (1 + .05 * seg(t, T.v28, b))})`; c1b.style.transform = `scale(${1 + .05 * seg(t, T.v28, b)})`; c1.style.opacity = E.out(seg(t, T.v28 - .02, T.v28 + .12));
  c1b.style.opacity = E.out(seg(t, T.v28 + .08, T.v28 + .3)); c1b.style.color = '#4f86ff';
  show(c2, t >= T.abre + .2); reveal(c2, seg(t, T.abre + .2, T.abre + .5));
  [T.fut, T.bal, T.bm].forEach((k, i) => { const q = E.out(seg(t, k - .05, k + .25)); show(SP[i], t >= k - .05); SP[i].style.opacity = q; SP[i].style.transform = `translateY(${(1 - q) * 30}px)`; SP[i].style.color = i === 1 ? '#f2f1ec' : '#c9cfdb'; });
  const fl = Math.exp(-Math.pow((t - T.v28) / .07, 2)); $('grain').style.opacity = .05 + .25 * fl;
}
// ── D · QUEDAN 10 DÍAS ──
const d3 = tx('<div class="kick">QUEDAN</div>', 640, '', 40);
const d4 = tx('10', 670, 'M8', 470), d5 = tx(M('<span class="S blue">días.</span>'), 1130, '', 160);
function sD(t) {
  const a = T.qued - .14, b = T.mand - .04, v = t >= a && t < b; [d3, d4, d5].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true);
  show(d4, t >= T.diez - .05); d4.style.transform = `scale(${pulse(t, T.diez - .05, .1)})`; d4.style.opacity = E.out(seg(t, T.diez - .05, T.diez + .1));
  show(d5, t >= T.diez + .25); reveal(d5, seg(t, T.diez + .25, T.diez + .55));
}
// ── E · vuelve la notificación (bucle con el principio): MÁNDASELO al de los domingos ──
const e0 = tx('<div class="kick" style="color:#e6e8ee">RETO PARA TU STAFF</div>', 1170, 'shadow', 40);
const e1 = tx(M('MÁNDASELO'), 1210, 'M8 shadow', 150);
const e2 = tx(M('<span class="S blue">al de los domingos</span>'), 1375, 'shadow', 110);
const e3 = tx(M('<span class="S blue">a las once.</span>'), 1480, 'shadow', 110);
function sE(t) {
  const a = T.mand - .04, b = T.camp - .05, v = t >= a && t < b; [e0, e1, e2, e3].forEach(e => show(e, v)); if (!v) return;
  show(WP, true); place(WP, { is: 1.08 + .04 * seg(t, a, b), org: '50% 30%', grad: GR, dark: .2 }); WP._sh.style.background = GR;
  reveal(e1, seg(t, a + .05, a + .35)); show(e2, t >= T.mand + .9); reveal(e2, seg(t, T.mand + .9, T.mand + 1.2));
  show(e3, t >= T.once2 - .05); reveal(e3, seg(t, T.once2 - .05, T.once2 + .25));
  notif(t, a + .15, a, 860);
}

window.frame = t => {
  show($('sysL'), false); show($('paper'), false); show(NT, false); $('grain').style.opacity = .05;
  kDom.style.opacity = clk.style.opacity = 1; clk.style.top = '350px'; kDom.style.top = '300px'; $('phs').style.transform = '';
  sA(t); sB(t); sC(t); sD(t); sE(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
