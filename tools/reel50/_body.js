// u50 v2 · SOLUCIÓN (mié 25/11 13:30) · corrección de Biel del 18/11: problema → nutrición → CTA + solución.
// Se mantiene lo que funcionaba (la pantalla de bloqueo del domingo: Pablo Laso de fondo, DOM 23:00 y la notificación del segundo) y cambia
// el resto: «no hay otro hueco» sobre la línea SÁB · DOM · LUN; ficha de papel para guardar (sábado, al recoger: tres líneas que se marcan
// cuando Mateo las dice; golpe de música en «Tres líneas»); solución en 3,5 s con la captura real de la Semana 8; vuelve la notificación
// (bucle) para el reto; cierre de la lista de espera con el contador de su día (2 d 10 h).
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
  const b = T.entre - .04, v = t < b; [WP, kDom, clk, hk2].forEach(e => show(e, v)); if (!v) return;
  place(WP, { is: 1.04 + .14 * E.io(seg(t, 0, b)), iy: 24 - 48 * seg(t, 0, b), org: '50% 30%', grad: GR });
  const sh = buzz(t, T.seg - .05); $('phs').style.transform = `translateX(${sh * .6}px)`;
  clk.innerHTML = (t >= T.martes ? '23<span style="opacity:' : '23<span style="opacity:') + (Math.floor(t * 2) % 2 ? .35 : 1) + '">:</span>' + (t >= T.martes ? '01' : '00'); clk.style.transform = `scale(${pulse(t, 0, .0) * pulse(t, T.martes, .05)})`;
  hk2.style.transform = `scale(${pulse(t, T.sem, .05) * (1 + .04 * seg(t, 0, T.seg))})`; reveal(hk2, 1); kDom.style.letterSpacing = (.24 + .1 * seg(t, 0, b)) + 'em';
  notif(t, T.seg - .1, T.que - .05, 1080);
}
// ── B · NO HAY OTRO HUECO: la línea SÁB · DOM · LUN sobre el fondo desenfocado ──
const DAYS = ['SÁB', 'DOM', 'LUN'].map((d, i) => mk('div', `position:absolute;left:${120 + i * 300}px;top:640px;width:240px;height:240px;border-radius:36px;display:none;font-family:M;text-align:center;border:3px solid ${i === 1 ? '#2f6bff' : 'rgba(255,255,255,.22)'};background:${i === 1 ? 'rgba(47,107,255,.16)' : 'rgba(13,15,20,.55)'}`,
  `<div style="margin-top:50px;font-weight:800;font-size:76px;letter-spacing:-.03em;color:#f2f1ec">${d}</div><div style="margin-top:6px;font-weight:600;font-size:34px;color:${i === 1 ? '#4f86ff' : '#9aa2b3'}">${['partido', '23:00', 'entreno'][i]}</div>`));
const LINE = mk('div', 'position:absolute;left:240px;top:758px;width:600px;height:4px;background:rgba(255,255,255,.25);display:none;transform-origin:0 50%');
const bH1 = tx(M('NO HAY'), 1040, 'M8 shadow', 170);
const bH2 = tx(M('<span class="S blue">otro hueco.</span>'), 1220, 'shadow', 170);
function sB(t) {
  const a = T.entre - .04, b = T.hazlo - .06, v = t >= a && t < b; [WB, LINE, ...DAYS, bH1, bH2].forEach(e => show(e, v)); if (!v) return;
  place(WB, { is: 1.3 - .12 * seg(t, a, b), iy: -30 + 60 * seg(t, a, b) });
  LINE.style.transform = `scaleX(${E.out(seg(t, a, a + .5))})`;
  DAYS.forEach((d, i) => { const k = [a + .05, a + .25, a + .45][i]; const q = E.out5(seg(t, k, k + .35)); d.style.opacity = q; d.style.transform = `translateY(${(1 - q) * 40}px) scale(${i === 1 ? pulse(t, T.nohay - .05, .1) : 1})`; });
  show(bH1, t >= T.nohay - .08); reveal(bH1, seg(t, T.nohay - .08, T.nohay + .22));
  show(bH2, t >= T.hueco - .08); reveal(bH2, seg(t, T.hueco - .08, T.hueco + .25));
}
// ── C · FICHA PARA GUARDAR (papel): sábado, al recoger · tres líneas ──
const FK = tx(`<div class="kick" style="color:#2f6bff">${M('GUÁRDALO')}</div>`, 300, '', 40);
const FT = tx(M('<span style="color:#0d0f14">Sábado, al recoger.</span>'), 356, 'M8', 104);
const CARD = mk('div', 'position:absolute;left:110px;top:580px;width:860px;height:640px;border-radius:28px;background:#fbfaf6;border:3px solid #d6d2c6;box-shadow:0 24px 50px rgba(0,0,0,.12);display:none;font-family:M;color:#0d0f14', `
  <div style="position:absolute;left:52px;top:44px;font-weight:700;font-size:28px;letter-spacing:.16em;color:#8a8577">DESPUÉS DEL PARTIDO · 3 LÍNEAS</div>
  ${['Qué falló', 'Qué toca el martes', 'Qué repites el jueves'].map((d, i) => `<div class="frow" style="position:absolute;left:52px;right:52px;top:${118 + i * 160}px;height:132px;border-radius:18px;background:#efede6"><b style="position:absolute;left:30px;top:30px;width:72px;height:72px;border-radius:50%;background:#d6d2c6;color:#fff;font-weight:800;font-size:40px;line-height:72px;text-align:center">${i + 1}</b><span style="position:absolute;left:130px;top:40px;font-weight:800;font-size:48px;letter-spacing:-.02em">${d}</span></div>`).join('')}`, $('cards'));
const ROWS = [...CARD.querySelectorAll('.frow')];
const FS = tx(M('<span class="S blue">Tres líneas.</span>'), 1330, '', 150);
function sC(t) {
  const a = T.hazlo - .06, b = T.ysi - .08, v = t >= a && t < b; [FK, FT, CARD, FS].forEach(e => show(e, v)); if (!v) return;
  show($('paper'), true); reveal(FK, seg(t, a, a + .3)); reveal(FT, seg(t, T.sab - .1, T.sab + .25));
  const p = E.out5(seg(t, a, a + .45)); CARD.style.opacity = p; CARD.style.transform = `translateY(${(1 - p) * 120}px) scale(${(1 + .03 * seg(t, a, b)) * pulse(t, T.lineas - .05, .04)})`;
  [T.falla, T.toca, T.rep].forEach((k, i) => { const r = ROWS[i], m = E.out5(seg(t, k - .05, k + .25));
    r.style.background = m > .02 ? `rgb(${239 - 192 * m},${237 - 130 * m},${230 + 25 * m})` : '#efede6';
    r.querySelector('span').style.color = m > .5 ? '#fff' : '#0d0f14'; r.querySelector('b').style.background = m > .5 ? '#fff' : '#d6d2c6'; r.querySelector('b').style.color = m > .5 ? '#2f6bff' : '#fff';
    r.style.transform = `scale(${1 + .04 * Math.exp(-Math.pow((t - k - .15) / .15, 2))})`; });
  show(FS, t >= T.tres - .05); reveal(FS, seg(t, T.tres - .05, T.tres + .3)); FS.style.transform = `scale(${pulse(t, T.lineas - .05, .07)})`;
  const out = seg(t, b - .12, b); [FK, FT, FS].forEach(e => e.style.opacity = 1 - out); CARD.style.opacity = Math.min(p, 1 - out);
}
// ── D · SOLUCIÓN (≈ 3,5 s de captura real): la Semana 8 en la app de ProTeam ──
const PW = 600, PX = 240, SW = PW - 26, SH = Math.round(SW * 2410 / 1112), PH = SH + 26;
const PHN = mk('div', `position:absolute;left:${PX}px;top:640px;width:${PW}px;height:${PH}px;border-radius:62px;background:#0b0d12;border:3px solid #2a3040;padding:10px;display:none;box-shadow:0 40px 90px rgba(0,0,0,.6);transform-origin:50% 0`, '<div id="scr" style="position:relative;width:100%;height:100%;border-radius:50px;overflow:hidden;background:#f6f6f4"></div>', $('phones'));
const SCI = mk('img', 'position:absolute;left:0;top:0;width:100%;height:100%', null, $('scr')); SCI.src = IMG('semana');
const HL = mk('div', 'position:absolute;border:5px solid #2f6bff;border-radius:22px;display:none;z-index:6;box-shadow:0 0 0 8px rgba(47,107,255,.16)', '', $('scr'));
const dK = tx(`<div class="kick">${M('PLANIFICACIÓN · CAPTURA REAL')}</div>`, 290, '', 40);
const dQ = tx(M('¿La quieres'), 340, 'M8', 120);
const dQ2 = tx(M('<span class="S blue">montada?</span>'), 470, '', 130);
const dA = tx(M('Tu semana,'), 340, 'M8', 120);
const dA2 = tx(M('<span class="S blue">montada.</span>'), 470, '', 130);
function sD(t) {
  const a = T.ysi - .08, b = T.mand - .04, v = t >= a && t < b; [PHN, dK, dQ, dQ2, dA, dA2, HL].forEach(e => show(e, false)); if (!v) return;
  show($('sysL'), true); show(dK, t >= T.app - .1); reveal(dK, seg(t, T.app - .1, T.app + .25));
  if (t < T.app - .1) { show(dQ, true); show(dQ2, t >= T.montada - .1); reveal(dQ, seg(t, a, a + .3)); reveal(dQ2, seg(t, T.montada - .1, T.montada + .25)); }
  else { show(dA, true); show(dA2, true); reveal(dA, seg(t, T.app - .1, T.app + .2)); reveal(dA2, seg(t, T.app + .05, T.app + .35)); }
  const p = E.out5(seg(t, T.app - .25, T.app + .3)); show(PHN, t >= T.app - .25);
  const s = 1 + .28 * E.io(seg(t, T.planif - .1, T.planif + .5));
  PHN.style.transform = `translateY(${(1 - p) * 1100}px) scale(${s})`;
  show(HL, t >= T.planif + .2); HL.style.left = .03 * SW + 'px'; HL.style.top = .158 * SH + 'px'; HL.style.width = .94 * SW + 'px'; HL.style.height = .285 * SH + 'px';
  HL.style.opacity = E.out(seg(t, T.planif + .2, T.planif + .45)) * (1 - seg(t, T.sesion + .2, T.sesion + .4));
  const out = seg(t, b - .12, b); PHN.style.opacity = 1 - out; [dK, dA, dA2].forEach(e => e.style.opacity = 1 - out);
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
