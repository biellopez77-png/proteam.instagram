
// u12 · «Quinto periodo. Y tú, contando cruces en el acta.» (baloncesto · minibasket)
// Concepto: «El acta contra la pista». El acta de minibasket se llena de cruces y le roba la mirada al entrenador;
// la hoja de seis casillas del viernes la vacía, y el sábado la mirada vuelve a la pista (banquillo de los Heat, NBA 2012).

const SRC = '<div class="M5" style="font-size:26px;color:#aab2c3;letter-spacing:.02em">Minibasket · Fed. Extremeña de Baloncesto · normativa 2024-25</div>';

// ── 1 · GANCHO: banquillo de los Miami Heat (NBA 2012) · QUINTO PERIODO desde el fotograma 0 ──
const HEAT = ph('heat', '50% 40%');
const hK = tx(`<div class="kick" style="color:#e6e8ee">SÁBADO · MINIBASKET</div>`, 296, 'shadow', 40);
const h1 = tx('QUINTO PERIODO.', 356, 'M8 shadow', 114);
const h2 = tx(M('<span class="S blue">Y tú, contando cruces.</span>'), 500, 'shadow', 112);
const hS = tx(SRC, 1590, 'shadow', 26);
// acta (motion graphics): 12 dorsales × 6 periodos, se llena de cruces
const DOR = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
const ACTA = mk('div', 'position:absolute;left:150px;top:1010px;width:780px;height:540px;border-radius:22px;background:#fbfaf6;border:3px solid #d6d2c6;box-shadow:0 30px 70px rgba(0,0,0,.6);display:none;font-family:M;color:#0d0f14;overflow:hidden', `
  <div style="position:absolute;left:30px;top:20px;font-weight:800;font-size:26px;letter-spacing:.16em;color:#8a8577">ACTA · PERIODOS</div>
  ${[1, 2, 3, 4, 5, 6].map(p => `<div style="position:absolute;left:${200 + (p - 1) * 92}px;top:20px;width:80px;text-align:center;font-weight:800;font-size:26px;color:${p === 5 ? '#2f6bff' : '#8a8577'}">${p}º</div>`).join('')}
  ${DOR.map((d, r) => `<div style="position:absolute;left:30px;top:${64 + r * 38}px;width:720px;height:2px;background:#e8e5dc"></div>
     <div style="position:absolute;left:30px;top:${66 + r * 38}px;font-weight:700;font-size:26px;color:#5d6475">#${d}</div>`).join('')}
  <div style="position:absolute;left:${200 + 4 * 92 - 6}px;top:12px;width:92px;height:522px;border:4px solid #2f6bff;border-radius:12px"></div>`, $('cards'));
// cruces: periodos 1–4 ya marcados al azar, el 5º se va llenando
const XS = []; { let s = 7; const rnd = () => (s = (s * 9301 + 49297) % 233280) / 233280;
  DOR.forEach((d, r) => { [0, 1, 2, 3, 4].forEach(p => { if (p < 4 ? rnd() < .42 : rnd() < .5) {
    const x = mk('div', `position:absolute;left:${200 + p * 92 + 24}px;top:${62 + r * 38}px;font-family:M;font-weight:800;font-size:34px;color:${p === 4 ? '#2f6bff' : '#0d0f14'};opacity:${p < 4 ? 1 : 0}`, '×', ACTA); x._p = p; x._k = XS.filter(q => q._p === 4).length; XS.push(x); } }); }); }
function hook(t) {
  const b = T.ext - .12, v = t < b; [HEAT, hK, h1, h2, hS, ACTA].forEach(e => show(e, v)); if (!v) return;
  // 0–1,2: el entrenador de pie y el banquillo · «Y tú» corte a los asistentes con hojas · «contando» entra el acta
  const k = t >= T.yt - .05 ? 1 : 0;
  const O = [['45% 52%', 1.08], ['24% 46%', 2.0]][k];
  place(HEAT, { is: O[1] + .05 * seg(t, k ? T.yt : 0, b), org: O[0], grad: 'linear-gradient(180deg,rgba(0,0,0,.82) 0%,rgba(0,0,0,.55) 24%,rgba(0,0,0,.05) 40%,rgba(0,0,0,.1) 52%,rgba(0,0,0,.55) 70%,rgba(0,0,0,.85) 100%)' });
  h1.style.transform = `scale(${1 + .04 * Math.exp(-Math.pow((t - .5) / .25, 2))})`;
  show(h2, t >= T.yt - .08); reveal(h2, seg(t, T.yt - .08, T.yt + .25));
  const a = E.out5(seg(t, T.cont - .15, T.cont + .3)); ACTA.style.transform = `translateY(${(1 - a) * 620}px) rotate(${-2 * (1 - a) - 1.2}deg)`; ACTA.style.opacity = t < T.cont - .15 ? 0 : 1;
  XS.forEach(x => { if (x._p === 4) x.style.opacity = t > T.cont + .25 + .09 * x._k ? 1 : 0; });
  hS.style.opacity = E.out(seg(t, .2, .6));
  const out = seg(t, b - .1, b); [HEAT, hK, h1, h2, hS, ACTA].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 2 · LA NORMA: dos periodos de los cinco primeros, sin cambios ──
const nK = tx(`<div class="kick">${M('EXTREMADURA · MINIBASKET')}</div>`, 290, '', 40);
const n1 = tx(M('2 PERIODOS'), 350, 'M8', 156);
const n2 = tx(M('<span class="S blue">de los 5 primeros.</span>'), 520, '', 112);
const COLS = [1, 2, 3, 4, 5, 6].map(p => mk('div', `position:absolute;left:${90 + (p - 1) * 152}px;top:760px;width:136px;height:520px;border-radius:22px;background:#151922;border:2px solid #262b36;display:none;font-family:M;font-weight:800;text-align:center`,
  `<div style="position:absolute;left:0;right:0;top:26px;font-size:44px;color:#f2f1ec">${p}º</div><div class="cl" style="position:absolute;left:0;right:0;bottom:24px;font-size:22px;letter-spacing:.12em;color:#6d7588">${p === 6 ? 'LIBRE' : ''}</div>
   <div class="ck" style="position:absolute;left:18px;right:18px;top:190px;height:150px;border-radius:16px;background:#2f6bff;opacity:0;font-size:30px;color:#fff;line-height:150px">#7</div>`, $('cards')));
const nC = tx(`<div style="display:inline-block;border:3px solid #4f86ff;border-radius:999px;padding:14px 34px" class="M8"><span style="font-size:40px;letter-spacing:.08em">SIN CAMBIOS DEL 1º AL 5º</span></div>`, 1340, '', 40);
const nS = tx(SRC, 1470, '', 26);
function norma(t) {
  const a = T.ext - .12, b = T.guar - .12, v = t >= a && t < b; [nK, n1, n2, nC, nS, ...COLS].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true); reveal(nK, seg(t, a, a + .3));
  show(n1, t >= T.mini - .12); reveal(n1, seg(t, T.mini - .12, T.mini + .2));
  n1.style.transform = `scale(${1 + .05 * Math.exp(-Math.pow((t - T.dos - .1) / .16, 2))})`;
  show(n2, t >= T.cinco - .12); reveal(n2, seg(t, T.cinco - .12, T.cinco + .22));
  COLS.forEach((c, i) => { const p = E.out5(seg(t, a + .08 * i, a + .08 * i + .45)); c.style.opacity = p; c.style.transform = `translateY(${(1 - p) * 120}px)`;
    // «minibasket»: columnas en marcha; «dos»: el #7 ocupa dos periodos; «cinco»: los cinco primeros en azul, el 6º libre
    const on5 = i < 5 ? E.out(seg(t, T.cinco - .05 + .05 * i, T.cinco + .25 + .05 * i)) : 0;
    c.style.borderColor = on5 > .5 ? '#2f6bff' : '#262b36'; c.style.background = on5 > .5 ? '#16213d' : '#151922';
    const ck = c.querySelector('.ck'); ck.style.opacity = (i === 1 || i === 3) ? E.out(seg(t, T.dos + .15 * (i === 3), T.dos + .3 + .15 * (i === 3))) : 0;
    if (i === 5) c.querySelector('.cl').style.color = t >= T.cinco + .3 ? '#aab2c3' : '#6d7588'; });
  nC.style.opacity = E.out(seg(t, T.cinco + .35, T.cinco + .65)); nS.style.opacity = E.out(seg(t, a + .2, a + .5));
  const out = seg(t, b - .12, b); [nK, n1, n2, nC, nS, ...COLS].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 3 · FICHA PARA GUARDAR (papel): el viernes, seis casillas ──
const FK = tx(`<div class="kick ink" style="color:#2f6bff">${M('GUÁRDALO · EL VIERNES')}</div>`, 286, '', 40);
const FT = tx(M('6 casillas.'), 338, 'M8 ink', 104);
const ORD = [13, 14, 15, 4, 5, 6, 7, 8, 9, 10, 11, 12];   // primero, los que menos juegan
const SLOT = [[], [], [], [], []]; ORD.forEach((d, i) => { SLOT[i % 5].push([d, i, 0]); SLOT[(i + 2) % 5].push([d, i, 1]); });
const BX = [1, 2, 3, 4, 5, 6].map(p => { const c = (p - 1) % 3, r = Math.floor((p - 1) / 3);
  const d = mk('div', `position:absolute;left:${80 + c * 312}px;top:${500 + r * 330}px;width:296px;height:310px;border-radius:22px;background:#fbfaf6;border:3px solid #d6d2c6;display:none;font-family:M;color:#0d0f14`,
    `<div style="position:absolute;left:24px;top:16px;font-weight:800;font-size:40px">${p}º</div>${p === 6 ? '<div class="S" style="position:absolute;left:0;right:0;top:120px;text-align:center;font-size:72px;color:#2f6bff;opacity:0" id="lib">libre</div>' : ''}`, $('cards'));
  if (p < 6) d._ch = SLOT[p - 1].map(([n, i, w], j) => { const blue = i < 3;
    const e = mk('div', `position:absolute;left:${22 + (j % 3) * 88}px;top:${84 + Math.floor(j / 3) * 96}px;width:78px;height:78px;border-radius:16px;font-weight:800;font-size:30px;line-height:78px;text-align:center;opacity:0;${blue ? 'background:#2f6bff;color:#fff' : 'background:#e4e0d4;color:#0d0f14'}`, '#' + n, d);
    e._t = blue ? T.pri + .2 + .1 * (2 * i + w) : T.pri + .85 + .03 * (i * 2 + w); return e; });
  return d; });
const STEPS = mk('div', 'position:absolute;left:80px;top:1190px;width:920px;height:380px;border-radius:24px;background:#fbfaf6;border:3px solid #d6d2c6;display:none;font-family:M;color:#0d0f14', [
  ['Primero, los que menos juegan', 'pri'], ['Dos periodos cada uno, del 1º al 5º', 'menos'], ['El 6º, libre', 'menos']].map(([s, k], i) =>
  `<div class="st" style="position:absolute;left:36px;top:${36 + i * 112}px;font-weight:800;font-size:46px;letter-spacing:-.02em;opacity:.25"><b style="display:inline-block;width:62px;height:62px;border-radius:50%;background:#2f6bff;color:#fff;font-size:34px;line-height:62px;text-align:center;margin-right:22px">${i + 1}</b>${s}</div>`).join(''), $('cards'));
const STS = [...STEPS.querySelectorAll('.st')];
function ficha(t) {
  const a = T.guar - .12, b = T.sab + .35, v = t >= a && t < b; [FK, FT, STEPS, ...BX].forEach(e => show(e, v)); if (!v) return;
  show($('paper'), true); reveal(FK, seg(t, a, a + .3)); show(FT, t >= T.seis - .12); reveal(FT, seg(t, T.seis - .12, T.seis + .2));
  BX.forEach((d, i) => { const p = E.out5(seg(t, T.vie + .05 * i, T.vie + .05 * i + .4)); d.style.opacity = p; d.style.transform = `translateY(${(1 - p) * 90}px)`;
    (d._ch || []).forEach(e => { const q = E.out5(seg(t, e._t, e._t + .2)); e.style.opacity = q; e.style.transform = `scale(${.6 + .4 * q})`; }); });
  const lib = $('lib'); if (lib) lib.style.opacity = E.out(seg(t, T.pri + 1.3, T.pri + 1.6));
  const sp = E.out5(seg(t, T.seis, T.seis + .4)); STEPS.style.opacity = sp; STEPS.style.transform = `translateY(${(1 - sp) * 80}px)`;
  [T.pri, T.pri + .85, T.pri + 1.3].forEach((tt, i) => { STS[i].style.opacity = .25 + .75 * E.out(seg(t, tt - .1, tt + .2)); });
  const out = seg(t, b - .12, b); [FK, FT, STEPS, ...BX].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 4 · CIERRE: el sábado miras el partido, no el acta (vuelve la foto, el entrenador mira la pista) ──
const HEAT2 = ph('heat', '50% 40%');
const cK = tx(`<div class="kick" style="color:#e6e8ee">${M('Y EL SÁBADO')}</div>`, 296, 'shadow', 40);
const c1 = tx(M('MIRAS EL PARTIDO.'), 350, 'M8 shadow', 112);
const c2 = tx(M('<span class="S blue">No el acta.</span>'), 1330, 'shadow', 190);
const MINI = mk('div', 'position:absolute;left:390px;top:1120px;width:300px;height:200px;border-radius:16px;background:#fbfaf6;border:3px solid #d6d2c6;display:none;overflow:hidden', `${[0, 1, 2, 3, 4].map(r => `<div style="position:absolute;left:20px;right:20px;top:${30 + r * 34}px;height:3px;background:#e1ddd1"></div>`).join('')}<div class="strike" style="top:46%;transform:scaleX(0)"></div>`, $('cards'));
function cierre(t) {
  const a = T.sab + .35, b = T.com - .12, v = t >= a && t < b; [HEAT2, cK, c1, c2, MINI].forEach(e => show(e, v)); if (!v) return;
  place(HEAT2, { is: 1.55 + .08 * seg(t, a, b), org: '38% 62%', grad: 'linear-gradient(180deg,rgba(0,0,0,.8) 0%,rgba(0,0,0,.4) 24%,rgba(0,0,0,0) 40%,rgba(0,0,0,.1) 52%,rgba(0,0,0,.6) 66%,rgba(0,0,0,.88) 100%)', z: 3 });
  HEAT2.style.opacity = E.out(seg(t, a, a + .16));
  reveal(cK, seg(t, a, a + .25)); show(c1, t >= T.partido - .3); reveal(c1, seg(t, T.partido - .3, T.partido + .05));
  const m = E.out5(seg(t, T.noel - .1, T.noel + .25)); MINI.style.opacity = m; MINI.style.transform = `translateY(${(1 - m) * 60}px) rotate(-4deg)`;
  MINI.querySelector('.strike').style.transform = `scaleX(${E.out5(seg(t, T.acta2 - .05, T.acta2 + .2))})`;
  show(c2, t >= T.acta2 - .08); reveal(c2, seg(t, T.acta2 - .08, T.acta2 + .2));
  c2.style.transform = `scale(${1 + .06 * Math.exp(-Math.pow((t - T.acta2 - .1) / .16, 2))})`;
}

// ── 5 · CTA (sin pausa) sobre los asistentes con hojas + campaña ──
const HEAT3 = ph('heat', '50% 40%');
const kK = tx(`<div class="kick" style="color:#e6e8ee">${M('COMENTA')}</div>`, 296, 'shadow', 40);
const k1 = tx(M('Tu deporte, categoría y días'), 350, 'M8 shadow', 72);
const k2 = tx(M('<span class="S" style="color:#9db8ff">y te preparo la semana.</span>'), 446, 'shadow', 96);
const k3 = tx(`<div class="M7" style="font-size:40px;color:#e6e8ee">en la app de ProTeam</div>`, 580, 'shadow', 40);
const kL = tx(`<div class="kick" style="color:#e6e8ee">LISTA DE ESPERA · HASTA EL 27 NOV</div>`, 1300, 'shadow', 36);
const kG = tx('<span class="S blue">3 meses gratis.</span>', 1352, 'shadow', 150);
function cta(t) {
  const a = T.com - .12, b = T.preg - .12, v = t >= a && t < b; [HEAT3, kK, k1, k2, k3, kL, kG].forEach(e => show(e, v)); if (!v) return;
  const k = t >= T.lis - .1 ? 1 : 0, O = [['64% 34%', 2.1], ['16% 52%', 1.9]][k];
  place(HEAT3, { is: O[1] + .05 * seg(t, k ? T.lis : a, b), org: O[0], grad: 'linear-gradient(180deg,rgba(0,0,0,.85) 0%,rgba(0,0,0,.6) 30%,rgba(0,0,0,.2) 44%,rgba(0,0,0,.35) 56%,rgba(0,0,0,.85) 72%,rgba(0,0,0,.92) 100%)', z: 3 });
  HEAT3.style.opacity = 1;
  reveal(kK, seg(t, a, a + .3)); reveal(k1, seg(t, T.com, T.com + .3));
  show(k2, t >= T.prep - .1); reveal(k2, seg(t, T.prep - .1, T.prep + .25));
  k3.style.opacity = E.out(seg(t, T.app - .15, T.app + .15));
  show(kL, t >= T.lis - .1); kL.style.opacity = E.out(seg(t, T.lis - .1, T.lis + .2));
  show(kG, t >= T.tres - .1); kG.style.opacity = E.out(seg(t, T.tres - .1, T.tres + .2)); kG.style.transform = `scale(${1 + .05 * Math.exp(-Math.pow((t - T.tres - .15) / .16, 2))})`;
}

// ── 6 · RETO PARA EL STAFF sobre el plano del principio (bucle) ──
const HEAT4 = ph('heat', '50% 40%');
const rK = tx(`<div class="kick" style="color:#e6e8ee">${M('RETO PARA TU STAFF')}</div>`, 296, 'shadow', 40);
const r1 = tx(M('¿Quién llevaba el <span class="blue">acta</span>'), 352, 'M8 shadow', 88);
const r2 = tx(M('<span class="S" style="color:#9db8ff">en el quinto periodo?</span>'), 462, 'shadow', 108);
const rL = tx(`<div class="kick" style="color:#c9cfdb">LISTA DE ESPERA · HASTA EL 27 NOV</div><div class="S blue" style="font-size:64px;margin-top:6px">3 meses gratis.</div>`, 1460, 'shadow', 34);
function reto(t) {
  const a = T.preg - .12, v = t >= a; [HEAT4, rK, r1, r2, rL].forEach(e => show(e, v)); if (!v) return;
  place(HEAT4, { is: 1.08 + .05 * seg(t, a, T.END), org: '45% 52%', grad: 'linear-gradient(180deg,rgba(0,0,0,.82) 0%,rgba(0,0,0,.55) 24%,rgba(0,0,0,.05) 40%,rgba(0,0,0,.1) 52%,rgba(0,0,0,.55) 70%,rgba(0,0,0,.85) 100%)', z: 4 });
  HEAT4.style.opacity = E.out(seg(t, a, a + .16));
  reveal(rK, seg(t, a + .05, a + .35)); show(r1, t >= T.qui - .12); reveal(r1, seg(t, T.qui - .12, T.qui + .22));
  show(r2, t >= T.acta3 + .15); reveal(r2, seg(t, T.acta3 + .15, T.acta3 + .45)); rL.style.opacity = E.out(seg(t, a + .2, a + .5));
}

window.frame = t => {
  show($('sysL'), false); show($('paper'), false);
  hook(t); norma(t); ficha(t); cierre(t); cta(t); reto(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
</script></body></html>
