// ── 1 · GANCHO: Tony Parker pasando el bloqueo de Booker (NBA) · «EN OCTUBRE LO DEFENDÍAN» desde el fotograma 0 ──
const PNR = ph('pnr', '40% 30%');
const MON = mk('div', 'position:absolute;left:375px;top:858px;width:330px;height:84px;border-radius:42px;border:3px solid #4f86ff;background:rgba(13,15,20,.78);overflow:hidden;display:none;font-family:M;font-weight:800;font-size:44px;letter-spacing:.14em;color:#fff;text-align:center', '<div id="monI" style="position:absolute;left:0;right:0;top:0;line-height:78px"><div style="height:78px">OCTUBRE</div><div style="height:78px;color:#9db8ff">NOVIEMBRE</div></div>');
const h1 = tx('2×2 CONTRA EL BLOQUEO', 978, 'M8 shadow', 80);   // v2 (Andrés, 17/11): la escena de los apuntes en el fotograma 0, no un titular
const h2 = tx('<span class="blue">10′ · L · X · V</span>', 1082, 'M8 shadow', 132);
const hH = tx(M('<span class="S">Hoy no.</span>'), 1250, 'shadow', 170);
const hA = tx(M('No apuntaste la semana.'), 1460, 'M8 shadow', 78);
const ULH = mk('div', 'position:absolute;left:150px;top:1555px;width:780px;height:10px;background:#2f6bff;border-radius:3px;transform-origin:0 50%;display:none');
function hook(t) {
  const b = T.tres - .1, v = t < b; [PNR, MON, h1, h2, hH, hA, ULH].forEach(e => show(e, v)); if (!v) return;
  // plano general → cerrado sobre Parker atrapado en el bloqueo (Hoy no) → un poco más (No apuntaste)
  const k = t >= T.apu - .05 ? 2 : t >= T.hoy - .05 ? 1 : 0;
  const O = [['40% 30%', 1.02], ['38% 18%', 1.28], ['38% 18%', 1.28]][k];
  const gray = E.out(seg(t, T.hoy - .05, T.hoy + .35));
  place(PNR, { is: O[1] + .04 * seg(t, 0, b) + (k ? .08 * E.io(seg(t, T.hoy, b)) : 0), org: O[0], grad: 'linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,.05) 38%,rgba(0,0,0,.72) 50%,rgba(0,0,0,.9) 70%,rgba(0,0,0,.94) 100%)' });
  PNR._img.style.filter = `grayscale(${gray * .85}) contrast(${1 + .1 * gray})`;
  $('monI').style.transform = `translateY(${-78 * E.out5(seg(t, T.hoy - .1, T.hoy + .2))}px)`;
  h2.style.transform = `scale(${1 + .05 * Math.exp(-Math.pow((t - T.bloq) / .18, 2))})`;
  h2.style.opacity = 1 - .45 * gray; h1.style.opacity = 1 - .45 * gray;
  show(hH, t >= T.hoy - .08); reveal(hH, seg(t, T.hoy - .08, T.hoy + .2));
  show(hA, t >= T.apu - .05); reveal(hA, seg(t, T.apu - .05, T.apu + .3));
  show(ULH, t >= T.apu + .2); ULH.style.transform = `scaleX(${E.out5(seg(t, T.apu + .2, T.eapu))})`;
  const out = seg(t, b - .1, b); [PNR, MON, h1, h2, hH, hA, ULH].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 2 · ESCENA + GIRO: tres tiras de sesión (L · X · V); el 2×2 de 10′ no sabe dónde va; se dan la vuelta y quedan en blanco ──
const SX = [120, 410, 700], SW2 = 260, SY = 690, SH2 = 780;
const STR = ['L', 'X', 'V'].map((d, i) => {
  const w = mk('div', `position:absolute;left:${SX[i]}px;top:${SY}px;width:${SW2}px;height:${SH2}px;perspective:1600px;display:none`, '', $('cards'));
  w.innerHTML = `<div class="fl" style="position:absolute;inset:0;transform-style:preserve-3d">
    <div class="fr" style="position:absolute;inset:0;border-radius:26px;background:#151922;border:2px solid #262b36;backface-visibility:hidden;overflow:hidden">
      <div style="position:absolute;left:0;right:0;top:26px;text-align:center;font-family:M;font-weight:800;font-size:64px;color:#f2f1ec">${d}</div>
      <div style="position:absolute;left:22px;right:22px;top:128px;height:2px;background:#262b36"></div>
      <div class="sg" style="position:absolute;left:22px;right:22px;top:160px;height:150px;border-radius:16px;background:#1c212c;font-family:M;font-weight:700;font-size:28px;letter-spacing:.1em;color:#6d7588;line-height:150px;text-align:center">CALENT.</div>
      <div class="sg2" style="position:absolute;left:22px;right:22px;top:590px;height:150px;border-radius:16px;background:#1c212c;font-family:M;font-weight:700;font-size:28px;letter-spacing:.1em;color:#6d7588;line-height:150px;text-align:center">PARTIDO</div>
      <div class="bk" style="position:absolute;left:22px;right:22px;top:340px;height:190px;border-radius:18px;background:#1b2b55;border:3px solid #2f6bff;font-family:M;font-weight:800;color:#fff;text-align:center">
        <div style="position:absolute;left:0;right:0;top:34px;font-size:64px;letter-spacing:-.03em">2×2</div><div style="position:absolute;left:0;right:0;top:112px;font-size:40px;color:#9db8ff">10′</div></div>
    </div>
    <div style="position:absolute;inset:0;border-radius:26px;background:#f2f1ec;border:2px solid #d6d2c6;backface-visibility:hidden;transform:rotateY(180deg)">
      <div style="position:absolute;left:0;right:0;top:26px;text-align:center;font-family:M;font-weight:800;font-size:64px;color:#c9c4b6">${d}</div>
      ${[0, 1, 2, 3, 4, 5].map(j => `<div style="position:absolute;left:30px;right:30px;top:${190 + j * 110}px;height:3px;background:#e1ddd1"></div>`).join('')}
    </div></div>`;
  w._f = w.querySelector('.fl'); w._b = w.querySelector('.bk'); w._s1 = w.querySelector('.sg'); w._s2 = w.querySelector('.sg2'); return w; });
const eK = tx(`<div class="kick">${M('TRES ENTRENOS · UN 2×2 · 10′')}</div>`, 290, '', 40);
const eQ1 = tx(M('¿Al principio'), 380, 'M8', 108);
const eQ2 = tx(M('<span class="S blue">o al final?</span>'), 500, '', 120);
const gA = tx(M('Lo que funcionó'), 300, 'M8', 100);
const gB = tx(M('y no está escrito…'), 420, 'M8', 100);
const gC = tx(M('<span class="S blue">no vuelve.</span>'), 1560, '', 170);
function escena(t) {
  const a = T.tres - .1, b = T.app - .1, v = t >= a && t < b; [...STR, eK, eQ1, eQ2, gA, gB, gC].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true);
  const g0 = T.lo - .1;   // empieza el giro
  STR.forEach((w, i) => {
    const p = E.out5(seg(t, a + .12 * i, a + .12 * i + .45)); w.style.opacity = p; w.style.transform = `translateY(${(1 - p) * 140}px)`;
    // 2×2 se enciende en «dos contra dos»; en «¿al principio o al final?» salta arriba/abajo
    const on = E.out(seg(t, T.dos, T.dos + .3)); w._b.style.opacity = .25 + .75 * on;
    let y = 340;
    if (t >= T.pri - .05) { const ph = (t - T.pri) * 2.6 + i * .9; y = 340 + 210 * Math.sin(ph * Math.PI) * clamp((T.epri + .4 - t) / .3, 0, 1) ; }
    w._b.style.top = y + 'px';
    w._b.style.transform = `scale(${1 + .06 * Math.exp(-Math.pow((t - T.diez - .05 * i) / .15, 2))})`;
    // vuelta: cada tira se gira y queda en blanco (lo que no está escrito)
    const f = E.io(seg(t, g0 + .35 + .28 * i, g0 + .35 + .28 * i + .6)); w._f.style.transform = `rotateY(${180 * f}deg)`;
  });
  const sc = t < g0;
  show(eK, sc); reveal(eK, seg(t, a, a + .35));
  show(eQ1, sc && t >= T.pri - .1); show(eQ2, sc && t >= T.final - .1); reveal(eQ1, seg(t, T.pri - .1, T.pri + .25)); reveal(eQ2, seg(t, T.final - .1, T.final + .25));
  show(gA, !sc); show(gB, !sc && t >= T.lo + .9); reveal(gA, seg(t, g0, g0 + .3)); reveal(gB, seg(t, T.lo + .9, T.lo + 1.2));
  show(gC, t >= T.vuelve - .06); reveal(gC, seg(t, T.vuelve - .06, T.vuelve + .22));
  gC.style.transform = `scale(${1 + .06 * Math.exp(-Math.pow((t - T.vuelve - .1) / .16, 2))})`;
  const out = seg(t, b - .12, b); [...STR, eK, eQ1, eQ2, gA, gB, gC].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 3 · LA APP POR DENTRO: Planificación real → PLANTILLAS SEMANALES → «Aplicar a esta semana» recuadrado ──
const PW = 580, PX = 250, PY = 600, SW = PW - 26, SH = Math.round(SW * 2410 / 1112), PH = SH + 26;
const PHN = mk('div', `position:absolute;left:${PX}px;top:${PY}px;width:${PW}px;height:${PH}px;border-radius:62px;background:#0b0d12;border:3px solid #2a3040;padding:10px;display:none;box-shadow:0 40px 90px rgba(0,0,0,.6);transform-origin:0 0;will-change:transform`, '<div id="scr" style="position:relative;width:100%;height:100%;border-radius:50px;overflow:hidden;background:#f6f6f4"></div>', $('phones'));
const SCI = mk('img', 'position:absolute;left:0;top:0;width:100%;height:100%', null, $('scr')); SCI.src = IMG('plan');
const HL1 = mk('div', 'position:absolute;border:5px solid #2f6bff;border-radius:16px;display:none;z-index:6;box-shadow:0 0 0 8px rgba(47,107,255,.16)', '', $('scr'));
const HL2 = mk('div', 'position:absolute;border:6px solid #2f6bff;border-radius:16px;display:none;z-index:6;box-shadow:0 0 0 10px rgba(47,107,255,.2)', '', $('scr'));
const BAND = mk('div', 'position:absolute;left:0;top:0;width:1080px;height:560px;background:linear-gradient(#0d0f14 84%,rgba(13,15,20,0));display:none');
const aK = tx(`<div class="kick">${M('PLANIFICACIÓN · CAPTURA REAL')}</div>`, 280, '', 40);
const A1 = tx('<span style="color:#4f86ff">1</span>&nbsp; Plantillas semanales', 340, 'M8', 84);
const A2 = tx('<span style="color:#4f86ff">2</span>&nbsp; <span class="S blue" style="font-size:96px">Aplicar a esta semana</span>', 334, 'M8', 84);
const K = { a: [1, .5, .5, 1160], p: [1.75, .5, .58, 1000], b: [2.25, .3, .55, 1000] };
function cam(t) {
  const A = T.app - .1, s1 = T.app + .35, s2 = T.plant - .05;
  let P, Q, q;
  if (t < s1) { P = K.a; Q = K.p; q = E.out5(seg(t, A + .2, s1 + .3)); }
  else if (t < s2) { P = K.p; Q = K.p; q = 0; }
  else { P = K.p; Q = K.b; q = E.io(seg(t, s2, s2 + .5)); }
  const L = i => P[i] + (Q[i] - P[i]) * q, s = L(0), lx = 13 + L(1) * SW, ly = 13 + L(2) * SH;
  return [540 - PX - s * lx, L(3) - PY - s * ly, s];
}
function box(el, x0, y0, x1, y1) { el.style.left = x0 * SW + 'px'; el.style.top = y0 * SH + 'px'; el.style.width = (x1 - x0) * SW + 'px'; el.style.height = (y1 - y0) * SH + 'px'; }
function app(t) {
  const a = T.app - .1, b = T.guarda - .1, v = t >= a && t < b;
  [PHN, BAND, aK, A1, A2, HL1, HL2].forEach(e => show(e, false)); if (!v) return;
  show($('sysL'), true); [PHN, BAND, aK].forEach(e => show(e, true)); reveal(aK, seg(t, a, a + .35));
  const p = E.out5(seg(t, a, a + .45)), out = seg(t, b - .14, b), [x, y, s] = cam(t);
  PHN.style.transform = `translate(${x}px,${y + (1 - p) * 900}px) scale(${s})`; PHN.style.opacity = 1 - out;
  if (t < T.plant) { show(A1, true); const q = E.out5(seg(t, T.app + .2, T.app + .5)); A1.style.opacity = q; A1.style.transform = `translateY(${(1 - q) * 26}px)`;
    show(HL1, t >= T.app + .7); box(HL1, .032, .583, .965, .695); HL1.style.opacity = E.out(seg(t, T.app + .7, T.app + .95)); }
  else { show(A2, true); const q = E.out5(seg(t, T.plant, T.plant + .3)); A2.style.opacity = q; A2.style.transform = `translateY(${(1 - q) * 26}px)`;
    show(HL2, true); box(HL2, .03, .521, .487, .577); HL2.style.opacity = E.out(seg(t, T.plant, T.plant + .2));
    HL2.style.transform = `scale(${1 + .04 * Math.exp(-Math.pow((t - T.aplic - .1) / .15, 2))})`; }
  [BAND, aK, A1, A2].forEach(e => e.style.opacity = Math.min(+e.style.opacity || 1, 1 - out));
}

// ── 4 · FICHA PARA GUARDAR (papel): el domingo, tres apuntes ──
const FK = tx(`<div class="kick ink" style="color:#2f6bff">${M('GUÁRDALO · CADA DOMINGO')}</div>`, 290, '', 40);
const FT = tx(M('3 apuntes de la semana.'), 344, 'M8 ink', 92);
const ITEMS = [['Qué hiciste', '2×2 defensa del bloqueo'], ['Cuánto', '10′ · lunes, miércoles, viernes'], ['En qué orden', 'al principio, tras calentar']];
const CARD = mk('div', 'position:absolute;left:110px;top:540px;width:860px;height:900px;border-radius:28px;background:#fbfaf6;border:3px solid #d6d2c6;box-shadow:0 24px 50px rgba(0,0,0,.12);display:none;font-family:M;color:#0d0f14', `
  <div style="position:absolute;left:52px;top:44px;font-weight:700;font-size:28px;letter-spacing:.16em;color:#8a8577">SEMANA DEL __ · LO QUE FUNCIONÓ</div>
  ${ITEMS.map(([h, e], i) => `<div class="fi" style="position:absolute;left:44px;right:44px;top:${120 + i * 250}px;height:220px;border-radius:20px;background:#efede6">
    <b style="position:absolute;left:30px;top:30px;width:76px;height:76px;border-radius:50%;background:#d9d5c8;color:#fff;font-weight:800;font-size:44px;line-height:76px;text-align:center">${i + 1}</b>
    <div style="position:absolute;left:136px;top:30px;font-weight:800;font-size:58px;letter-spacing:-.03em">${h}</div>
    <div class="fe S" style="position:absolute;left:136px;top:116px;font-size:58px;color:#2f6bff;opacity:0">${e}</div></div>`).join('')}`, $('cards'));
const FIS = [...CARD.querySelectorAll('.fi')];
function ficha(t) {
  const a = T.guarda - .1, b = T.seg - .1, v = t >= a && t < b; [FK, FT, CARD].forEach(e => show(e, v)); if (!v) return;
  show($('paper'), true); reveal(FK, seg(t, a, a + .3)); reveal(FT, seg(t, T.dom - .1, T.dom + .3));
  const p = E.out5(seg(t, a, a + .45)); CARD.style.transform = `translateY(${(1 - p) * 120}px) scale(${1 + .03 * seg(t, a, b)})`; CARD.style.opacity = p;
  [T.q1, T.q2, T.q3].forEach((tt, i) => { const m = E.out5(seg(t, tt - .05, tt + .25)), f = FIS[i];
    f.style.background = m > .02 ? `rgb(${239 - 12 * m},${237 - 4 * m},${230 + 22 * m})` : '#efede6';
    f.querySelector('b').style.background = m > .5 ? '#2f6bff' : '#d9d5c8'; f.querySelector('.fe').style.opacity = m;
    f.style.transform = `scale(${1 + .03 * Math.exp(-Math.pow((t - tt - .12) / .15, 2))})`; });
  const out = seg(t, b - .12, b); [FK, FT, CARD].forEach(e => e.style.opacity = Math.min(e === CARD ? p : 1, 1 - out));
}

// ── 5 · RETO PARA EL STAFF sobre la foto del principio (bucle) + campaña ──
const PNR2 = ph('pnr', '40% 30%');
const rK = tx(`<div class="kick" style="color:#e6e8ee">${M('RETO PARA TU STAFF')}</div>`, 880, 'shadow', 40);
const r1 = tx(M('¿Qué semana de <span class="blue">octubre</span>'), 940, 'M8 shadow', 86);
const r2 = tx(M('<span class="S" style="color:#9db8ff">repetiríais mañana?</span>'), 1050, 'shadow', 116);
const rC = tx(`<div class="M7" style="font-size:44px;color:#fff">Comenta tu deporte, categoría y días</div>`, 1236, 'shadow', 44);
function reto(t) {
  const a = T.seg - .1, v = t >= a && t < T.camp - .05; [PNR2, rK, r1, r2, rC].forEach(e => show(e, v)); if (!v) return;
  place(PNR2, { is: 1.1 + .05 * seg(t, a, T.END), org: '40% 20%', grad: 'linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.05) 22%,rgba(0,0,0,.1) 36%,rgba(0,0,0,.78) 46%,rgba(0,0,0,.92) 64%,rgba(0,0,0,.95) 100%)', z: 3 });
  PNR2.style.opacity = E.out(seg(t, a, a + .16));
  reveal(rK, seg(t, a + .05, a + .35)); show(r1, t >= T.que - .1); show(r2, t >= T.oct2 + .2);
  reveal(r1, seg(t, T.que - .1, T.que + .25)); reveal(r2, seg(t, T.oct2 + .2, T.oct2 + .55));
  const fo = 1 - seg(t, T.camp - .17, T.camp - .05); rC.style.opacity = Math.min(seg(t, T.seg + .25, T.seg + .6), fo); [rK, r1, r2].forEach(e => e.style.opacity = fo); PNR2.style.opacity = Math.min(+PNR2.style.opacity, fo);
}

// ── 6 · CIERRE (v2, 17/11): la entrada en la lista de espera con el contador (la misma animación de u28 v3 y u09) ──
// el contador sale de lo que falta de verdad cuando se publica (mar 17/11 22:30 → vie 27/11 23:59:59 = 10 d 1 h 29 min 59 s)
let rs = 11; const rnd = () => (rs = (rs * 16807) % 2147483647) / 2147483647;
const W = { web: T.camp - .05 }; W.tap = W.web + 1.15; W.ok = W.tap + .22; W.gal = T.gra - .1;
const PT = Array.from({ length: 22 }, () => { const o = document.createElement('div'); const a = rnd() * Math.PI * 2, r = 160 + rnd() * 260;
  o.style.cssText = `position:absolute;left:0;top:0;width:${10 + rnd() * 10}px;height:${10 + rnd() * 10}px;border-radius:50%;background:${rnd() < .7 ? '#2f6bff' : '#f2f1ec'};display:none;margin-left:${470 + 70}px;margin-top:0px`;
  o._dx = Math.cos(a) * r; o._dy = Math.sin(a) * r * .7; $('web').appendChild(o); return o; });
const GA = ph('pnr', '40% 30%');
const tHE = tx('<span class="mask"><span>HASTA EL</span></span>', 1130, 'M8 shadow', 70);
const t28 = tx('<span class="mask"><span>27 NOV</span></span>', 1220, 'M8 shadow', 230);
const t3M = tx('<span class="mask"><span class="S blue">3 meses gratis.</span></span>', 800, 'shadow', 180);
function webcta(t) {
  // 9 · web oscura
  const wv = t >= W.web && t < W.gal; show($('web'), wv);
  if (wv) {
    const p = E.out5(seg(t, W.web, W.web + .4));
    $('wp').style.top = (470 + (1 - p) * 120) + 'px'; $('wp').style.opacity = p;
    [...$('wp').children].forEach((c, i) => { const q = E.out(seg(t, W.web + i * .04, W.web + .28 + i * .04)); c.style.opacity = q; c.style.transform = `translateY(${(1 - q) * 40}px)`; });
    const pg = (t * 1.4) % 1; $('ping').style.transform = `scale(${1 + pg * 1.6})`; $('ping').style.opacity = 1 - pg;
    const total0 = ((10 * 24 + 1) * 60 + 29) * 60 + 59 - Math.floor(t - W.web);
    const acc = E.in(seg(t, W.web + .3, W.gal - .08)); const rem = Math.max(0, Math.round(total0 * (1 - acc)));
    const dd = Math.floor(rem / 86400), hh = Math.floor(rem % 86400 / 3600), mm = Math.floor(rem % 3600 / 60), ss = rem % 60;
    [[ 'cd1', dd], ['cd2', hh], ['cd3', mm], ['cd4', ss]].forEach(([id, v]) => { const el = $(id); const nv = String(v).padStart(2, '0'); if (el.textContent !== nv) { el._ch = t; el.textContent = nv; } el.style.color = rem === 0 ? '#4f86ff' : '#f2f1ec';
      const q = E.out(seg(t, el._ch || -9, (el._ch || -9) + .18)); el.style.transform = `translateY(${(1 - q) * -22}px)`; el.style.opacity = .35 + .65 * q; });
    PT.forEach((o, i) => { const q = seg(t, W.ok + .15, W.ok + .85); o.style.display = q > 0 && q < 1 ? 'block' : 'none'; if (q > 0 && q < 1) { const e = E.out(q); o.style.transform = `translate(${o._dx * e}px,${o._dy * e + 120 * q * q}px) scale(${1 - q})`; o.style.opacity = 1 - q; } });
    const z = seg(t, W.gal - .12, W.gal); $('wp').querySelector('.cd').style.transform = `scale(${1 + .05 * Math.sin(z * Math.PI)})`;
    // cursor
    const fl = $('fld'), bt = $('btn'), wp = $('wp'); const top = parseFloat(wp.style.top);
    const fy = top + fl.offsetTop + 75, by = top + bt.offsetTop + 80;
    const P = [[W.web + .08, 980, 1800], [W.web + .22, 760, fy + 10], [W.web + .5, 740, fy + 14], [W.tap - .12, 560, by + 12], [W.tap - .02, 562, by + 14], [W.gal, 562, by + 14]];
    let x = P[0][1], y = P[0][2];
    for (let i = 0; i < P.length - 1; i++) if (t >= P[i][0]) { const k = E.io(seg(t, P[i][0], P[i + 1][0])); x = P[i][1] + (P[i + 1][1] - P[i][1]) * k; y = P[i][2] + (P[i + 1][2] - P[i][2]) * k; }
    const cu = $('cur'); show(cu, t > W.web + .08 && t < W.ok + .2); cu.style.left = x + 'px'; cu.style.top = y + 'px';
    const click = Math.max(Math.exp(-Math.pow((t - (W.web + .24)) / .06, 2)), Math.exp(-Math.pow((t - W.tap) / .06, 2)));
    cu.style.transform = `scale(${1 - .2 * click})`; cu.style.opacity = 1 - seg(t, W.ok, W.ok + .2);
    // campo
    const focus = t > W.web + .24;
    fl.style.borderColor = focus ? '#2f6bff' : '#262b36'; fl.style.boxShadow = focus ? `0 0 0 ${(8 + 3 * Math.sin(t * 6)) * E.out(seg(t, W.web + .24, W.web + .37))}px rgba(47,107,255,.22)` : 'none';
    const em = 'entrenador@miclub.es'; const tp = seg(t, W.web + .26, W.web + .5); const ne = Math.floor(em.length * clamp(tp + .06 * Math.sin(tp * 19)));
    $('fldt').innerHTML = ne ? em.slice(0, ne) : (focus ? '' : '<span class="ph2">Tu email</span>');
    $('fc').style.opacity = focus && t < W.tap ? (Math.floor(t * 4) % 2 ? 1 : .15) : 0;
    if (t > W.tap) { fl.style.borderColor = '#262b36'; fl.style.boxShadow = 'none'; }
    // botón
    const press = Math.exp(-Math.pow((t - W.tap) / .08, 2)); const hov = E.out(seg(t, W.tap - .35, W.tap - .1));
    const doneP = E.out5(seg(t, W.ok, W.ok + .45));
    bt.style.transform = `scale(${1 - .05 * press + .025 * hov * (t < W.tap ? 1 : 0)})`; bt.style.boxShadow = `0 0 ${60 * hov * (t < W.ok ? 1 : 0) + 50 * Math.exp(-Math.pow((t - W.ok - .3) / .25, 2))}px rgba(47,107,255,.6)`;
    bt.style.width = (940 - (940 - 560) * doneP) + 'px'; bt.style.borderRadius = (28 + 52 * doneP) + 'px';
    PT.forEach(o => { o.style.left = '0px'; o.style.top = (top + bt.offsetTop + 70) + 'px'; });
    const rip = $('rip'); const rp = seg(t, W.tap, W.tap + .5); show(rip, rp > 0 && rp < 1);
    rip.style.left = (560 - 70 - 20) + 'px'; rip.style.top = '60px'; rip.style.transform = `scale(${1 + rp * 40})`; rip.style.opacity = .9 * (1 - rp);
    const busy = t >= W.tap + .1 && t < W.ok;
    $('btt').style.display = t < W.tap + .1 ? 'inline' : 'none'; $('spin').style.display = busy ? 'block' : 'none'; $('spin').style.transform = `rotate(${t * 900}deg)`;
    $('ok').style.display = t >= W.ok ? 'flex' : 'none';
    $('okr').setAttribute('stroke-dashoffset', 239 * (1 - E.out(seg(t, W.ok + .05, W.ok + .4))));
    $('okp').setAttribute('stroke-dashoffset', 60 * (1 - E.out(seg(t, W.ok + .25, W.ok + .55))));
    bt.style.background = '#2f6bff';
  }

  const g0 = W.gal, v = t >= g0; show(GA, v); if (v) place(GA, { is: 1.16 - .06 * seg(t, g0, T.END), org: '40% 20%', dark: .66, z: 3 });
  show(tHE, v); show(t28, t >= g0 + .1); show(t3M, v); reveal(tHE, seg(t, g0, g0 + .3)); reveal(t28, seg(t, g0 + .1, g0 + .45));
  reveal(t3M, seg(t, T.gra - .05, T.gra + .3)); t3M.style.transform = `scale(${1 + .05 * seg(t, T.gra, T.END)})`;
  if (v) show($('web'), false);
}

window.frame = t => {
  show($('sysL'), false); show($('paper'), false);
  hook(t); escena(t); app(t); ficha(t); reto(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
</script></body></html>
