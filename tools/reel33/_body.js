
// ── 1 · GANCHO: Dika Mem armando el brazo · «Brazo arriba: 4 PASES.» legible desde el fotograma 0 ──
const MEM = ph('mem', '50% 20%');
const k1 = tx(`<div class="kick" style="color:#e6e8ee">BALONMANO · JUEGO PASIVO</div>`, 980, 'shadow', 40);
const h1 = tx('Brazo arriba:', 1040, 'M8 shadow', 112);
const h2 = tx('<span class="blue">4 PASES.</span>', 1170, 'M8 shadow', 230);
const h3 = tx(M('<span class="S">y a tirar.</span>'), 1430, 'shadow', 110);
function hook(t) {
  const b = 3.0, v = t < b; [MEM, k1, h1, h2, h3].forEach(e => show(e, v)); if (!v) return;
  const k = t >= 1.5 ? 1 : 0;
  place(MEM, { is: [1.04, 1.22][k] + .04 * seg(t, 0, b), org: ['50% 30%', '55% 22%'][k], grad: 'linear-gradient(180deg,rgba(0,0,0,.4) 0%,rgba(0,0,0,0) 20%,rgba(0,0,0,.08) 40%,rgba(0,0,0,.75) 50%,rgba(0,0,0,.9) 70%,rgba(0,0,0,.94) 100%)' });
  h2.style.transform = `scale(${1 + .04 * Math.exp(-Math.pow((t - 1.5) / .15, 2))})`;
  show(h3, t >= 1.5); reveal(h3, seg(t, 1.5, 1.85));
  const out = seg(t, b - .1, b); [MEM, k1, h1, h2, h3].forEach(e => e.style.opacity = 1 - out);
}

// ── 2 · EL DATO: hasta 2022 eran 6 → 4 en el golpe; cuatro pases que se cuentan y el tiro ──
const dK = tx(`<div class="kick">${M('REGLAS IHF · DESDE EL 1/7/2022')}</div>`, 470, '', 40);
const dA = tx(M('Hasta 2022 eran'), 530, 'M8', 96);
const dA2 = tx('Desde 2022, solo', 530, 'M8', 96);
const SIX = mk('div', 'position:absolute;left:0;width:1080px;top:650px;text-align:center;font-family:M;font-weight:800;font-size:420px;line-height:1;letter-spacing:-.05em;color:#f2f1ec;display:none', '<span style="position:relative;display:inline-block">6<i class="strike" style="display:block;top:50%;height:22px;transform:scaleX(0)"></i></span>');
const FOUR = mk('div', 'position:absolute;left:0;width:1080px;top:650px;text-align:center;font-family:M;font-weight:800;font-size:420px;line-height:1;letter-spacing:-.05em;color:#4f86ff;display:none', '4');
const dB = tx(M('<span class="S blue">pases, como máximo.</span>'), 1100, '', 104);
const DOTS = [1, 2, 3, 4].map(i => mk('div', `position:absolute;left:${120 + (i - 1) * 170}px;top:1290px;width:130px;height:130px;border-radius:50%;border:4px solid #2a3040;background:#151922;font-family:M;font-weight:800;font-size:60px;color:#6d7588;line-height:122px;text-align:center;display:none`, i));
const SHOT = mk('div', 'position:absolute;left:800px;top:1290px;width:180px;height:130px;border-radius:65px;border:4px solid #2a3040;background:#151922;font-family:M;font-weight:800;font-size:44px;letter-spacing:.06em;color:#6d7588;line-height:122px;text-align:center;display:none', 'TIRO');
const dS = tx(`<div class="M5" style="font-size:36px;color:#9aa2b3">Fuente: IHF · de 6 a 4 pases tras el aviso</div>`, 1500, '', 36);
function dato(t) {
  const a = 3.0, b = 7.0, v = t >= a && t < b; [dK, dA, dA2, SIX, FOUR, dB, ...DOTS, SHOT, dS].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true); reveal(dK, seg(t, a, a + .3)); reveal(dA, seg(t, a + .05, a + .4));
  const D = T.drop, s = E.out5(seg(t, D - .55, D - .2));
  SIX.querySelector('.strike').style.transform = `scaleX(${s})`;
  const six = t < D; show(SIX, six); show(FOUR, !six); show(dA, six); show(dA2, !six);
  SIX.style.opacity = six ? E.out(seg(t, a + .1, a + .4)) : 0; SIX.style.transform = `scale(${1 - .03 * s})`;
  FOUR.style.transform = `scale(${1 + .12 * Math.exp(-Math.pow((t - D - .06) / .14, 2))})`;
  show(dB, t >= D + .15); reveal(dB, seg(t, D + .15, D + .45));
  DOTS.forEach((d, i) => { const ti = D + .7 + .38 * i, on = t >= ti; d.style.opacity = E.out(seg(t, D + .3, D + .6));
    d.style.background = on ? '#2f6bff' : '#151922'; d.style.borderColor = on ? '#4f86ff' : '#2a3040'; d.style.color = on ? '#fff' : '#6d7588';
    d.style.transform = `scale(${1 + .1 * Math.exp(-Math.pow((t - ti - .05) / .1, 2))})`; });
  const ts = D + .7 + .38 * 4, so = t >= ts; SHOT.style.opacity = E.out(seg(t, D + .3, D + .6));
  SHOT.style.background = so ? '#f2f1ec' : '#151922'; SHOT.style.color = so ? '#0d0f14' : '#6d7588'; SHOT.style.borderColor = so ? '#f2f1ec' : '#2a3040';
  SHOT.style.transform = `scale(${1 + .1 * Math.exp(-Math.pow((t - ts - .05) / .1, 2))})`;
  dS.style.opacity = E.out(seg(t, D + .2, D + .5));
  const out = seg(t, b - .12, b); [dK, dA2, dB, ...DOTS, SHOT, dS, FOUR].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 3 · LA APP: el pasivo pitado se apunta como Pérdida y el lunes está en la Cronología (capturas reales) ──
const PW = 580, PX = 250, PY = 560, SW = PW - 26, SH = Math.round(SW * 2410 / 1112), PH = SH + 26;
const PHN = mk('div', `position:absolute;left:${PX}px;top:${PY}px;width:${PW}px;height:${PH}px;border-radius:62px;background:#0b0d12;border:3px solid #2a3040;padding:10px;display:none;box-shadow:0 40px 90px rgba(0,0,0,.6);transform-origin:0 0;will-change:transform`, '<div id="scr" style="position:relative;width:100%;height:100%;border-radius:50px;overflow:hidden;background:#f6f6f4"></div>', $('phones'));
const SC1 = mk('img', 'position:absolute;left:0;top:0;width:100%;height:100%', null, $('scr')); SC1.src = IMG('accion');
const SC2 = mk('img', 'position:absolute;left:0;top:0;width:100%;height:100%;display:none', null, $('scr')); SC2.src = IMG('crono');
const HL = mk('div', 'position:absolute;border:6px solid #2f6bff;border-radius:16px;display:none;z-index:6;box-shadow:0 0 0 10px rgba(47,107,255,.2)', '', $('scr'));
const BAND = mk('div', 'position:absolute;left:0;top:0;width:1080px;height:540px;background:linear-gradient(#0d0f14 84%,rgba(13,15,20,0));display:none');
const aK = tx(`<div class="kick">${M('EN LA APP DE PROTEAM · CAPTURA REAL')}</div>`, 280, '', 40);
const A1 = tx('<span class="M8">Pasivo pitado</span> <span class="S blue" style="font-size:104px">= pérdida.</span>', 336, 'M8', 92);
const A2 = tx('<span class="M8">El lunes,</span> <span class="S blue" style="font-size:100px">en la cronología.</span>', 340, 'M8', 84);
const K = { a: [1, .5, .62, 1180], p: [1.55, .5, .775, 1120], c: [1.6, .5, .855, 1100] };
function box(el, x0, y0, x1, y1) { el.style.left = x0 * SW + 'px'; el.style.top = y0 * SH + 'px'; el.style.width = (x1 - x0) * SW + 'px'; el.style.height = (y1 - y0) * SH + 'px'; }
function app(t) {
  const a = 7.0, m = 8.75, b = 10.3, v = t >= a && t < b;
  [PHN, BAND, aK, A1, A2, HL].forEach(e => show(e, false)); if (!v) return;
  show($('sysL'), true); [PHN, BAND, aK].forEach(e => show(e, true)); reveal(aK, seg(t, a, a + .3));
  const p = E.out5(seg(t, a, a + .4)), out = seg(t, b - .12, b);
  let P, q, Q;
  if (t < m) { P = K.a; Q = K.p; q = E.out5(seg(t, a + .05, a + .45)); } else { P = K.c; Q = K.c; q = 0; }
  const L = i => P[i] + (Q[i] - P[i]) * q, s = L(0), lx = 13 + L(1) * SW, ly = 13 + L(2) * SH;
  const x = 540 - PX - s * lx, y = L(3) - PY - s * ly;
  PHN.style.transform = `translate(${x}px,${y + (1 - p) * 900}px) scale(${s})`; PHN.style.opacity = 1 - out;
  const first = t < m; show(SC1, first); show(SC2, !first);
  if (first) { show(A1, true); const r = E.out5(seg(t, a + .15, a + .45)); A1.style.opacity = r; A1.style.transform = `translateY(${(1 - r) * 26}px)`;
    show(HL, t >= a + .28); box(HL, .06, .728, .94, .818); HL.style.opacity = E.out(seg(t, a + .28, a + .45));
    HL.style.transform = `scale(${1 + .04 * Math.exp(-Math.pow((t - a - .4) / .15, 2))})`; }
  else { show(A2, true); const r = E.out5(seg(t, m, m + .3)); A2.style.opacity = r; A2.style.transform = `translateY(${(1 - r) * 26}px)`;
    show(HL, t >= m + .05); box(HL, .02, .833, .98, .876); HL.style.opacity = E.out(seg(t, m + .05, m + .2)); HL.style.transform = 'none'; }
  [BAND, aK, A1, A2].forEach(e => e.style.opacity = Math.min(+e.style.opacity || 1, 1 - out));
}

// ── 4 · RETO PARA EL STAFF: la selección española en corro + campaña ──
const ESP = ph('espana', '50% 50%');
const rK = tx(`<div class="kick" style="color:#e6e8ee">${M('RETO PARA TU STAFF')}</div>`, 880, 'shadow', 40);
const r1 = tx(M('¿Cuántos balones perdisteis'), 940, 'M8 shadow', 74);
const r2 = tx(M('<span class="S" style="color:#9db8ff">por pasivo el sábado?</span>'), 1036, 'shadow', 108);
const rC = tx(`<div class="M7" style="font-size:44px;color:#fff">Comenta tu deporte, categoría y días</div>`, 1236, 'shadow', 44);
const rL = tx(`<div class="kick" style="color:#e6e8ee">LISTA DE ESPERA · HASTA EL 27 NOV</div>`, 1346, 'shadow', 36);
const rG = tx('<span class="S blue">3 meses gratis.</span>', 1396, 'shadow', 110);
function reto(t) {
  const a = 10.3, v = t >= a; [ESP, rK, r1, r2, rC, rL, rG].forEach(e => show(e, v)); if (!v) return;
  place(ESP, { is: 1.0 + .06 * seg(t, a, T.END), org: '42% 30%', grad: 'linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 20%,rgba(0,0,0,.1) 36%,rgba(0,0,0,.78) 46%,rgba(0,0,0,.92) 64%,rgba(0,0,0,.95) 100%)', z: 3 });
  ESP._img.style.objectPosition = '42% 50%';
  reveal(rK, seg(t, a, a + .3)); reveal(r1, seg(t, a + .15, a + .5)); reveal(r2, seg(t, a + .5, a + .85));
  const c = seg(t, a + .9, a + 1.2); rC.style.opacity = c; rL.style.opacity = c; rG.style.opacity = E.out(seg(t, a + 1.0, a + 1.4));
}

window.frame = t => {
  show($('sysL'), false); show($('paper'), false);
  hook(t); dato(t); app(t); reto(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
</script></body></html>
