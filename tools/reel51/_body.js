
// u51 · CONTEXTO · concepto: «el reloj que no se para» — el marcador del estadio acaba a las 13:00, pero el reloj del entrenador sigue
// corriendo (13:10, 13:11…) sobre el banquillo vacío del Camp Nou. Las tres preguntas del después del partido saltan como avisos encima
// del banquillo; corte a papel donde «OFICINA» se tacha en azul y, en «banquillo», corte seco al banquillo vacío del Bernabéu.
// Golpe de música en «nació»: «ProTeam.» a pantalla completa; tres deportes; ancla «hecha en el banquillo»; vuelve el reloj (bucle) para
// el reto «¿quién sigue con el partido?» y cierre de la lista de espera con el contador. Ninguna pantalla de la app. Sin nombre de nadie.
const GR = 'linear-gradient(180deg,rgba(0,0,0,.66) 0%,rgba(0,0,0,.25) 30%,rgba(0,0,0,.1) 48%,rgba(0,0,0,.5) 66%,rgba(0,0,0,.88) 100%)';
const GT = 'linear-gradient(180deg,rgba(0,0,0,.94) 0%,rgba(0,0,0,.8) 12%,rgba(0,0,0,.3) 30%,rgba(0,0,0,.1) 48%,rgba(0,0,0,.5) 66%,rgba(0,0,0,.88) 100%)';
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));

const CN = ph('cn', '50% 50%');
const RM = ph('rm', '50% 50%');
const CNB = ph('cn', '50% 50%'); CNB._img.style.filter = 'blur(26px) brightness(.32) saturate(.7)';

// ── el reloj (marcador LED) ──
const CLK = mk('div', 'position:absolute;left:140px;top:560px;width:800px;height:300px;border-radius:34px;background:rgba(8,10,14,.86);border:3px solid rgba(255,255,255,.12);display:none;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)',
  `<div style="position:absolute;left:0;right:0;top:26px;text-align:center;font-family:M;font-weight:700;font-size:30px;letter-spacing:.3em;color:#7d8597" class="lab">FINAL</div>
   <div class="d" style="position:absolute;left:0;right:0;top:66px;text-align:center;font-family:M;font-weight:800;font-size:200px;line-height:200px;letter-spacing:-.02em;color:#f2f1ec;font-variant-numeric:tabular-nums">13:00</div>`, $('cards'));
CLK._dg = CLK.querySelector('.d'); CLK._l = CLK.querySelector('.lab');
function clock(t, base, run, y, sc = 1) {
  show(CLK, true); CLK.style.top = y + 'px'; CLK.style.transform = `scale(${sc})`;
  // base: minuto mostrado; run: segundos de reloj que corren deprisa (cada 0,5 s de vídeo = 1 minuto)
  const mm = base + Math.floor(run); CLK._dg.textContent = `13:${String(mm).padStart(2, '0')}`;
}
// ── A · SÁBADO 13:10 (0 → «Y el entrenador sigue con él») ──
const aK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">SÁBADO</div>', 470, 'shadow', 44);
const aS = tx(M('<span class="S blue">acabó hace 10 minutos.</span>'), 900, 'shadow', 92);
function sA(t) {
  const b = T.ent - .04, v = t < b; [aK, aS].forEach(e => show(e, v)); if (!v) return;
  show(CN, true); place(CN, { is: 1.3 + .1 * E.io(seg(t, 0, b)), iy: 60 - 30 * seg(t, 0, b), org: '50% 85%', grad: GT });
  // 13:10 desde el fotograma 0; en «acabó» el rótulo cambia a FINAL 13:00 y vuelve a correr hasta 13:10
  let mm = 10, lab = 'AHORA';
  if (t >= T.acabo - .05 && t < T.min - .05) { mm = 0; lab = 'FINAL'; }
  else if (t >= T.min - .05) { mm = Math.min(10, Math.floor(10 * seg(t, T.min - .05, T.min + .7))); lab = 'FINAL + ' + mm + ' MIN'; }
  clock(t, mm, 0, 560, pulse(t, 0, 0) * pulse(t, T.acabo - .05, .05) * pulse(t, T.min + .6, .05));
  CLK._l.textContent = lab; CLK._l.style.color = mm === 0 ? '#4f86ff' : '#9aa2b3'; CLK.style.borderColor = mm === 0 ? '#2f6bff' : 'rgba(255,255,255,.12)';
  aK.style.opacity = 1 - E.out(seg(t, T.acabo - .1, T.acabo + .1));
  show(aS, t >= T.min - .05); reveal(aS, seg(t, T.min - .05, T.min + .3));
}
// ── B · el entrenador sigue con él: tres avisos sobre el banquillo (¿minutos? ¿qué falló? ¿martes?) ──
const bK = tx('<div class="kick" style="color:#e6e8ee">EL ENTRENADOR</div>', 300, 'shadow', 44);
const bH = tx(M('<span class="S blue">sigue con él.</span>'), 350, 'shadow', 150);
const NOTES = [['¿MINUTOS?', 'quién jugó cuánto'], ['¿QUÉ FALLÓ?', 'en el segundo tiempo'], ['¿MARTES?', 'la sesión, sin hacer']].map(([h, s], i) =>
  mk('div', `position:absolute;left:120px;width:840px;height:170px;border-radius:30px;background:rgba(18,22,32,.9);border:2px solid rgba(255,255,255,.14);display:none;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)`,
    `<div style="position:absolute;left:40px;top:34px;width:22px;height:22px;border-radius:50%;background:#2f6bff"></div>
     <div style="position:absolute;left:86px;top:20px;font-family:M;font-weight:800;font-size:66px;letter-spacing:-.03em;color:#f2f1ec">${h}</div>
     <div style="position:absolute;left:88px;top:104px;font-family:M;font-weight:500;font-size:36px;color:#9aa2b3">${s}</div>`, $('cards')));
const NT = () => [T.quien - .05, T.falla - .05, T.martes - .3];
function sB(t) {
  const a = T.ent - .04, b = T.ese - .04, v = t >= a && t < b; [bK, bH].forEach(e => show(e, v)); NOTES.forEach(n => show(n, v)); if (!v) return;
  show(CN, true); place(CN, { is: 1.22 + .1 * seg(t, a, b), iy: -20 + 40 * seg(t, a, b), org: '50% 85%', dark: .58 });
  // el reloj sigue corriendo arriba, pequeño: 13:10 → 13:14
  clock(t, 10, 4 * seg(t, a, b), 1480, .62); CLK._l.textContent = 'SIGUE'; CLK._l.style.color = '#4f86ff'; CLK.style.borderColor = 'rgba(255,255,255,.12)';
  bK.style.opacity = E.out(seg(t, a, a + .25)); reveal(bH, seg(t, a + .1, a + .45));
  NT().forEach((t0, i) => { const q = E.out5(seg(t, t0, t0 + .3)); const n = NOTES[i]; show(n, q > 0); n.style.top = (700 + i * 200) + 'px';
    n.style.opacity = q; n.style.transform = `translateX(${(1 - q) * (i % 2 ? -120 : 120)}px) scale(${pulse(t, t0, .05)})`; n.style.borderColor = t >= t0 && t < (NT()[i + 1] || b) ? '#4f86ff' : 'rgba(255,255,255,.14)'; });
}
// ── C · papel: NO EN UNA OFICINA (se tacha) → corte seco al banquillo del Bernabéu: «en el banquillo.» ──
const cK = tx('<div class="kick ink" style="letter-spacing:.24em">ESE PROBLEMA</div>', 640, '', 44);
const cO = tx('<span style="position:relative;display:inline-block">' + M('OFICINA') + '<span class="strike" id="stk"></span></span>', 800, 'M8 ink', 180);
const cN = tx(M('NO LO VIMOS DESDE UNA'), 720, 'M7 ink', 58);
const cB0 = tx('<div class="kick" style="color:#e6e8ee">LO VIVIMOS</div>', 1300, 'shadow', 44);
const cB = tx(M('<span class="S blue">en el banquillo.</span>'), 1350, 'shadow', 150);
function sC(t) {
  const a = T.ese - .04, b = T.busc - .04, v = t >= a && t < b; [cK, cO, cB0, cB, cN].forEach(e => show(e, v)); if (!v) { show($('paper'), false); return; }
  const ban = t >= T.banq - .06;   // corte seco en «banquillo»
  show($('paper'), !ban); [cK, cO, cN].forEach(e => show(e, !ban));
  if (!ban) {
    cK.style.opacity = E.out(seg(t, a, a + .25)); reveal(cN, seg(t, a + .5, a + .85)); show(cN, t >= a + .5); reveal(cO, seg(t, T.ofi - .15, T.ofi + .2)); show(cO, t >= T.ofi - .15);
    cO.style.transform = `scale(${1 + .03 * seg(t, T.ofi, T.banq)})`;
    const s = $('stk'); if (s) s.style.transform = `scaleX(${E.out(seg(t, T.lo - .05, T.lo + .35))})`;
  } else {
    show(RM, true); place(RM, { is: 1.14 - .08 * E.io(seg(t, T.banq - .06, b)), iy: 30 - 50 * seg(t, T.banq, b), dark: .64, z: 2 });
    cB0.style.opacity = 1; reveal(cB, seg(t, T.banq - .06, T.banq + .25));
    const fl = Math.exp(-Math.pow((t - T.banq) / .06, 2)); $('grain').style.opacity = .05 + .2 * fl;
  }
  if (!ban) { show(cB0, false); show(cB, false); }
}
// ── D · «Buscábamos cómo resolverlo» → golpe en «nació»: ProTeam. · tres deportes ──
const dK = tx(M('Buscábamos'), 760, 'M8', 120);
const dK2 = tx(M('<span class="S blue">cómo resolverlo.</span>'), 900, '', 120);
const dA = tx('<div class="kick" style="letter-spacing:.3em;color:#e6e8ee">Y ASÍ NACIÓ</div>', 640, '', 46);
const dP = tx('ProTeam.', 700, 'M8', 230);
const SP = ['FÚTBOL', 'BALONCESTO', 'BALONMANO'].map((w, i) => tx(w, 1120 + i * 100, 'M7', 70));
function sD(t) {
  const a = T.busc - .04, b = T.hecha - .04, v = t >= a && t < b; [dK, dK2, dA, dP, ...SP].forEach(e => show(e, v)); if (!v) return;
  const hit = t >= T.nacio - .05;
  show(CNB, !hit); if (!hit) place(CNB, { is: 1.5 - .3 * seg(t, a, b), iy: -60 + 120 * seg(t, a, b), z: 1 });
  // tras el golpe: el Camp Nou nítido y muy oscuro, con un empuje que se nota (sin tramos quietos)
  if (hit) { show(CN, true); place(CN, { is: 1.12 + .26 * E.io(seg(t, T.nacio, b)), iy: 40 - 120 * seg(t, T.nacio, b), org: '50% 85%', dark: .8, z: 1 }); }
  const na = t >= T.nac - .05; show(dK, !na); reveal(dK, seg(t, a, a + .3)); show(dK2, !na && t >= T.busc + .7); reveal(dK2, seg(t, T.busc + .7, T.busc + 1.0));
  dK.style.transform = dK2.style.transform = `scale(${1 + .04 * seg(t, a, T.nacio)})`;
  show(dA, t >= T.nac - .05); dA.style.opacity = E.out(seg(t, T.nac - .05, T.nac + .2)); dA.style.top = '640px';
  show(dP, hit); const q = E.out5(seg(t, T.nacio - .05, T.nacio + .2)); dP.style.opacity = q;
  dP.style.transform = `scale(${(1.25 - .25 * q) * pulse(t, T.nacio - .05, .06) * (1 + .1 * seg(t, T.nacio, b))})`;
  dP.style.color = t >= T.pt - .05 ? '#4f86ff' : '#f2f1ec';
  [T.fut, T.bal, T.bm].forEach((k, i) => { const r = E.out(seg(t, k - .05, k + .25)); show(SP[i], t >= k - .05); SP[i].style.opacity = r; SP[i].style.transform = `translateY(${(1 - r) * 30}px)`; SP[i].style.color = '#c9cfdb'; });
  const fl = Math.exp(-Math.pow((t - T.nacio) / .07, 2)); $('grain').style.opacity = .05 + .25 * fl;
  // destello azul en el golpe
  $('sysL').style.background = `rgba(47,107,255,${.5 * fl})`; show($('sysL'), fl > .02);
}
// ── E · ancla: HECHA EN EL BANQUILLO · no en una oficina (tachado) ──
const eK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">HECHA EN EL</div>', 700, 'shadow', 50);
const eB = tx(M('BANQUILLO'), 760, 'M8 shadow', 170);
const eN = tx('<span style="position:relative;display:inline-block">' + M('<span class="S" style="color:#c9cfdb">no en una oficina.</span>') + '<span class="strike" id="stk2" style="height:9px"></span></span>', 1000, 'shadow', 96);
function sE(t) {
  const a = T.hecha - .04, b = T.preg - .04, v = t >= a && t < b; [eK, eB, eN].forEach(e => show(e, v)); if (!v) return;
  show(RM, true); place(RM, { is: 1.3 - .16 * E.io(seg(t, a, b)), iy: -40 + 60 * seg(t, a, b), org: '50% 70%', dark: .72, z: 2 });
  eK.style.opacity = E.out(seg(t, a, a + .25)); reveal(eB, seg(t, T.banq2 - .2, T.banq2 + .15)); show(eB, t >= T.banq2 - .2);
  eB.style.transform = `scale(${pulse(t, T.banq2 - .2, .05)})`;
  show(eN, t >= T.noofi - .05); reveal(eN, seg(t, T.noofi - .05, T.noofi + .3));
  const s = $('stk2'); if (s) s.style.transform = `scaleX(${E.out(seg(t, T.ofi2, T.ofi2 + .35))})`;
}
// ── F · vuelve el reloj sobre el Camp Nou (bucle): RETO · ¿quién sigue con el partido? ──
const fK = tx('<div class="kick" style="color:#e6e8ee">RETO PARA TU STAFF</div>', 300, 'shadow', 44);
const fQ = tx(M('¿Quién sigue'), 1040, 'M8 shadow', 128);
const fQ2 = tx(M('<span class="S blue">con el partido?</span>'), 1190, 'shadow', 140);
function sF(t) {
  const a = T.preg - .04, b = T.abre - .04, v = t >= a && t < b; [fK, fQ, fQ2].forEach(e => show(e, v)); if (!v) return;
  show(CN, true); place(CN, { is: 1.3 + .08 * seg(t, a, b), iy: 60 - 30 * seg(t, a, b), org: '50% 85%', grad: GT });
  clock(t, 10, 6 * seg(t, a, b), 600, .8); CLK._l.textContent = 'AHORA'; CLK._l.style.color = '#9aa2b3'; CLK.style.borderColor = 'rgba(255,255,255,.12)';
  fK.style.opacity = E.out(seg(t, a, a + .3));
  show(fQ, t >= T.quien2 - .1); reveal(fQ, seg(t, T.quien2 - .1, T.quien2 + .25)); show(fQ2, t >= T.sigue2 + .1); reveal(fQ2, seg(t, T.sigue2 + .1, T.sigue2 + .4));
}
// ── G · ABRE EL SÁBADO 28 ──
const gK = tx('<div class="kick" style="letter-spacing:.26em;color:#e6e8ee">ABRE EL SÁBADO</div>', 640, '', 46);
const g1 = tx('28 NOV', 700, 'M8', 250);
function sG(t) {
  const a = T.abre - .04, b = T.camp - .05, v = t >= a && t < b; [gK, g1].forEach(e => show(e, v)); if (!v) return;
  show(CNB, true); place(CNB, { is: 1.4 - .1 * seg(t, a, b), z: 1 });
  gK.style.opacity = E.out(seg(t, a, a + .25)); show(g1, t >= T.v28 - .05); const q = E.out5(seg(t, T.v28 - .05, T.v28 + .2));
  g1.style.opacity = q; g1.style.transform = `scale(${(1.2 - .2 * q) * (1 + .04 * seg(t, T.v28, b))})`; g1.style.color = '#4f86ff';
}

window.frame = t => {
  show($('sysL'), false); $('sysL').style.background = '#0d0f14'; show($('paper'), false); show(CLK, false); NOTES.forEach(n => show(n, false));
  [CN, RM, CNB].forEach(p => show(p, false)); $('grain').style.opacity = .05;
  sA(t); sB(t); sC(t); sD(t); sE(t); sF(t); sG(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
