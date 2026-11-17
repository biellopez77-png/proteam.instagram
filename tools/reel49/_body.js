// u49 · IMPACTO (día 1 de 10) · concepto: «rótulos de retransmisión con la casilla en blanco» — tres banquillos de primer nivel, cada uno con
// el rótulo de TV que le falta el dato (— —, cursor parpadeando); los tres se apilan en «el mismo sábado» y el calendario de noviembre
// rodea el 28 a mano en azul. Cortes secos cada ~5 s. «DÍA 1 DE 10» fijo arriba (hilo del lanzamiento). Ninguna pantalla de la app.
const DAYK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.22em">DÍA 1 DE 10 · SÁB 28 NOV</div>', 262, 'shadow', 34);
const GR = 'linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.05) 26%,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 62%,rgba(0,0,0,.88) 100%)';
// rótulo de retransmisión: [dorsal/puesto | etiqueta | valor]
function rot(tag, label, y) {
  const d = mk('div', `position:absolute;left:90px;top:${y}px;width:900px;height:118px;display:none;border-radius:14px;overflow:hidden;background:rgba(13,15,20,.86);border:2px solid rgba(255,255,255,.12);box-shadow:0 18px 40px rgba(0,0,0,.5)`,
    `<div style="position:absolute;left:0;top:0;width:150px;height:100%;background:#2f6bff;color:#fff;font-family:M;font-weight:800;font-size:${tag.length > 2 ? 40 : 64}px;line-height:118px;text-align:center;letter-spacing:-.02em">${tag}</div>
     <div style="position:absolute;left:180px;top:0;height:100%;line-height:118px;font-family:M;font-weight:700;font-size:34px;letter-spacing:.12em;color:#c9cfdb">${label}</div>
     <div class="v" style="position:absolute;right:0;top:0;width:210px;height:100%;background:#151922;border-left:2px solid #262b36;color:#f2f1ec;font-family:M;font-weight:800;font-size:66px;line-height:118px;text-align:center;font-variant-numeric:tabular-nums"></div>`);
  d._v = d.querySelector('.v'); return d;
}
function rotOn(r, t, t0, val) {
  const v = t >= t0; show(r, v); if (!v) return;
  const p = E.out5(seg(t, t0, t0 + .35)); r.style.transform = `translateX(${(1 - p) * -120}px)`; r.style.opacity = p;
  if (val === null) { const on = Math.floor((t - t0) * 3) % 2 === 0; r._v.innerHTML = `<span style="color:#5d6475">—&nbsp;—</span><span style="display:inline-block;width:5px;height:60px;margin-left:8px;vertical-align:-8px;background:#2f6bff;opacity:${on ? 1 : .15}"></span>`; }
  else r._v.textContent = val;
}
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));

// ── A · FÚTBOL (Zidane en la banda) · MIN 70 desde el fotograma 0 ──
const FA = ph('fut', '24% 40%');
const a1 = tx('MIN 70', 330, 'M8 shadow', 250);
const a2 = tx(M('<span class="S blue">¿minutos del 9?</span>'), 600, 'shadow', 130);
const ra = rot('9', 'MINUTOS JUGADOS', 1250);
const a3 = tx(M('NO LO SABES.'), 1420, 'M8 shadow', 112);
function sA(t) {
  const b = T.ult - .04, v = t < b; [FA, a1, a2, a3].forEach(e => show(e, v)); if (!v) { show(ra, false); return; }
  place(FA, { is: 1.06 + .05 * seg(t, 0, b), org: '25% 35%', grad: GR });
  a1.style.transform = `scale(${pulse(t, T.setenta, .05)})`;
  show(a2, t >= T.cuan); reveal(a2, seg(t, T.cuan, T.cuan + .3)); rotOn(ra, t, T.nueve - .2, null);
  show(a3, t >= T.nolo); reveal(a3, seg(t, T.nolo, T.nolo + .25));
}
// ── B · BALONCESTO (Pat Riley de pie; el banquillo sentado detrás) · ÚLTIMO CUARTO ──
const FB = ph('bas', '58% 40%');
const b1 = tx('ÚLTIMO CUARTO', 340, 'M8 shadow', 112);
const rb = rot('BASE', 'DESCANSOS', 1250);
const b3 = tx(M('<span class="S blue">Te das cuenta ahora.</span>'), 1400, 'shadow', 112);
function sB(t) {
  const a = T.ult - .04, b = T.desc - .04, v = t >= a && t < b; [FB, b1, b3].forEach(e => show(e, v)); if (!v) { show(rb, false); return; }
  place(FB, { is: 1.12 - .05 * seg(t, a, b), org: '55% 30%', grad: GR });
  b1.style.transform = `scale(${pulse(t, a, .05)})`;
  rotOn(rb, t, T.base + .1, seg(t, T.base + .1, T.base + .4) < 1 ? null : '0');
  if (t >= T.base + .4) rb._v.style.color = '#4f86ff';
  show(b3, t >= T.cuenta); reveal(b3, seg(t, T.cuenta, T.cuenta + .3));
}
// ── C · BALONMANO (tiempo muerto del THW Kiel) · tarjeta nítida sobre la misma foto desenfocada ──
const FCb = ph('bal', '50% 40%'); FCb._img.style.filter = 'blur(26px) brightness(.45)';
const FC = ph('bal', '46% 35%'); FC.classList.add('ol');
const c1 = tx('DESCANSO', 330, 'M8 shadow', 150);
const rc1 = rot('POR', 'GOLES ENCAJADOS', 1190), rc2 = rot('POR', 'PARADAS', 1330);
const c3 = tx(M('<span class="S blue">Nadie las ha contado.</span>'), 1470, 'shadow', 104);
function sC(t) {
  const a = T.desc - .04, b = T.tres - .04, v = t >= a && t < b; [FCb, FC, c1, c3].forEach(e => show(e, v)); if (!v) { show(rc1, false); show(rc2, false); return; }
  place(FCb, { is: 1.3, z: 1 });
  place(FC, { is: 1.04 + .05 * seg(t, a, b), org: '46% 35%', dark: .08, z: 2 }); FC.style.left = '70px'; FC.style.top = '520px'; FC.style.width = '940px'; FC.style.height = '880px';
  c1.style.transform = `scale(${pulse(t, a, .05)})`;
  const n = Math.round(14 * E.out(seg(t, T.port + .1, T.cat + .1)));
  rotOn(rc1, t, T.port, String(n)); rc1._v.style.color = t >= T.cat ? '#f2f1ec' : '#8a92a3'; rc1.style.transform += ` scale(${pulse(t, T.cat, .04)})`;
  rotOn(rc2, t, T.par, null);
  show(c3, t >= T.nadie); reveal(c3, seg(t, T.nadie, T.nadie + .3));
}
// ── D y H · TRES FRANJAS (los tres banquillos el mismo sábado; vuelven en el reto: bucle con el principio) ──
const ST = [['fut', '30% 22%'], ['bas', '55% 14%'], ['bal', '50% 12%']].map(([s, p]) => ph(s, p));
const d1 = tx(M('TRES BANQUILLOS.'), 905, 'M8 shadow', 104);
const d2 = tx(M('<span class="S blue">El mismo sábado.</span>'), 1010, 'shadow', 130);
const h0 = tx('<div class="kick" style="color:#e6e8ee">RETO PARA TU STAFF</div>', 330, 'shadow', 40);
const h1 = tx(M('Mándaselo a tu segundo:'), 420, 'M7 shadow', 64);
const h2 = tx(M('¿Cuál de los'), 860, 'M8 shadow', 120);
const h3 = tx(M('<span class="S blue">tres sois?</span>'), 990, 'shadow', 190);
function strips(t, a, b, dark) {
  ST.forEach((s, i) => {
    show(s, true); const p = E.out5(seg(t, a + i * .1, a + .45 + i * .1)); const dir = i % 2 ? 1 : -1;
    place(s, { is: 1.0 + .04 * seg(t, a, b), org: '50% 30%', dark: dark, z: 2 });
    s.style.top = (40 + i * 620) + 'px'; s.style.height = '600px'; s.style.left = (dir * (1 - p) * 1100) + 'px';
  });
}
function sD(t) {
  const a = T.tres - .04, b = T.apu - .04, v = t >= a && t < b; [d1, d2].forEach(e => show(e, v));
  const a2 = T.mand - .04, b2 = T.camp - .05, v2 = t >= a2 && t < b2; [h0, h1, h2, h3].forEach(e => show(e, v2));
  if (!v && !v2) { ST.forEach(s => show(s, false)); return; }
  if (v) { strips(t, a, b, .3 + .25 * seg(t, T.mismo - .1, T.mismo + .2)); reveal(d1, seg(t, a + .2, a + .5)); show(d2, t >= T.mismo); reveal(d2, seg(t, T.mismo, T.mismo + .3)); }
  else { strips(t, a2, b2, .62); reveal(h1, seg(t, a2 + .1, a2 + .4)); show(h2, t >= T.cual - .05); show(h3, t >= T.cual + .2); reveal(h2, seg(t, T.cual - .05, T.cual + .25)); reveal(h3, seg(t, T.cual + .2, T.cual + .5)); }
}
// ── E · CALENDARIO DE NOVIEMBRE: «Apunta otro» → se rodea el 28 a mano en azul (golpe de música) ──
const CAL = mk('div', 'position:absolute;left:85px;top:500px;width:910px;height:760px;display:none', '', $('cards'));
const DN = ['L', 'M', 'X', 'J', 'V', 'S', 'D'];
DN.forEach((d, i) => mk('div', `position:absolute;left:${i * 130}px;top:0;width:130px;text-align:center;font-family:M;font-weight:800;font-size:30px;letter-spacing:.1em;color:#8a8577`, d, CAL));
const CELL = {};
for (let d = 1; d <= 30; d++) { const k = d + 5, c = k % 7, r = Math.floor(k / 7);
  CELL[d] = mk('div', `position:absolute;left:${c * 130}px;top:${70 + r * 112}px;width:130px;height:112px;text-align:center;line-height:112px;font-family:M;font-weight:800;font-size:52px;color:${c >= 5 ? '#0d0f14' : '#4a4740'}`, String(d), CAL); }
const HOY = mk('div', 'position:absolute;left:0;top:0;width:96px;height:96px;margin:-48px 0 0 -48px;border-radius:50%;background:#0d0f14;display:none', '', CAL);
CAL.insertBefore(HOY, CAL.children[7]);
const RING = mk('div', 'position:absolute;left:0;top:0;width:190px;height:150px;margin:-75px 0 0 -95px;display:none',
  '<svg viewBox="0 0 190 150" width="190" height="150"><path id="ringp" d="M100 14 C150 12 182 40 178 76 C174 116 132 140 88 136 C40 132 10 104 14 70 C18 36 52 16 104 18 C120 19 134 24 146 30" fill="none" stroke="#2f6bff" stroke-width="9" stroke-linecap="round" stroke-dasharray="560" stroke-dashoffset="560"/></svg>', CAL);
const e0 = tx('<div class="kick ink" style="letter-spacing:.2em">APUNTA OTRO</div>', 330, '', 40);
const e1 = tx(M('SÁB 28 NOV'), 1290, 'M8 ink', 170);
const e2 = tx(M('<span class="S blue">abre ProTeam.</span>'), 1470, '', 132);
function sE(t) {
  const a = T.apu - .04, b = T.hoy - .04, v = t >= a + .3 && t < b; show($('paper'), v); [CAL, e0, e1, e2].forEach(e => show(e, v));
  if (t >= a && t < a + .3) show($('sysL'), true);   // el único negro (0,3 s), nunca al principio
  if (!v) { show(RING, false); show(HOY, false); return; }
  show(DAYK, false); const p = E.out5(seg(t, a + .3, a + .75)); CAL.style.transform = `translateY(${(1 - p) * 60}px)`; CAL.style.opacity = p;
  reveal(e0, seg(t, a + .3, a + .6));
  const c18 = CELL[18]; show(HOY, true); HOY.style.left = (c18.offsetLeft + 65) + 'px'; HOY.style.top = (c18.offsetTop + 56) + 'px'; c18.style.color = '#f2f1ec';
  for (let d = 19; d <= 27; d++) { const q = seg(t, a + .5 + (d - 19) * .1, a + .6 + (d - 19) * .1); CELL[d].style.opacity = 1 - .6 * q; }
  const c28 = CELL[28]; show(RING, t >= T.v28 - .1); RING.style.left = (c28.offsetLeft + 65) + 'px'; RING.style.top = (c28.offsetTop + 56) + 'px';
  $('ringp').setAttribute('stroke-dashoffset', 560 * (1 - E.out(seg(t, T.v28 - .1, T.v28 + .4))));
  c28.style.color = t >= T.v28 ? '#2f6bff' : '#0d0f14'; c28.style.transform = `scale(${t >= T.v28 ? pulse(t, T.v28, .25) * 1.1 : 1})`;
  show(e1, t >= T.v28); reveal(e1, seg(t, T.v28, T.v28 + .3)); e1.style.transform = `scale(${pulse(t, T.v28, .05)})`;
  show(e2, t >= T.abre + .3); reveal(e2, seg(t, T.abre + .3, T.abre + .6));
}
// ── G · «Hoy no te contamos más.» → 10 DÍAS ──
const g1 = tx(M('HOY NO TE'), 560, 'M8', 120), g2 = tx(M('CONTAMOS MÁS.'), 690, 'M8', 120);
const g3 = tx('<div class="kick">QUEDAN</div>', 930, '', 40);
const g4 = tx('10', 960, 'M8', 470), g5 = tx(M('<span class="S blue">días.</span>'), 1420, '', 160);
function sG(t) {
  const a = T.hoy - .04, b = T.mand - .04, v = t >= a && t < b; [g1, g2, g3, g4, g5].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true); reveal(g1, seg(t, a, a + .3)); reveal(g2, seg(t, a + .12, a + .42));
  const up = E.out5(seg(t, T.qued - .1, T.qued + .3)); [g1, g2].forEach(e => { e.style.transform = `translateY(${-200 * up}px)`; e.style.opacity = 1 - .65 * up; });
  show(g3, t >= T.qued); show(g4, t >= T.diez - .05); g4.style.transform = `scale(${pulse(t, T.diez - .05, .1)})`; g4.style.opacity = E.out(seg(t, T.diez - .05, T.diez + .1));
  show(g5, t >= T.diez + .25); reveal(g5, seg(t, T.diez + .25, T.diez + .55));
}

window.frame = t => {
  show($('sysL'), false); show($('paper'), false); show(DAYK, t < T.mand - .04 && !(t >= T.apu - .04 && t < T.hoy - .04));
  sA(t); sB(t); sC(t); sD(t); sE(t); sG(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
