// u73 · PROBLEMA · datos corto · «Seis minutos con uno menos» · concepto: «dos cronómetros» — el del sábado, rojo, que corre de 0:00 a 6:00
// sobre el corro del Barça de balonmano (tres exclusiones = seis minutos con uno menos), y el del martes, en papel, clavado en 0:00
// (ni un minuto de 5 contra 6). Vuelta al corro para la pregunta al staff (bucle) y el cierre de campaña de siempre con el contador real.
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));
const RED = '#e5484d', BLUE = '#2f6bff', INK = '#0d0f14';
const BC = ph('barca', '50% 30%');
const a3 = tx('3<div style="font-size:124px;margin-top:-40px">EXCLUSIONES</div>', 620, 'M8 shadow', 330);
const aS = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">EL SÁBADO</div>', 560, 'shadow', 46);
// cronómetro
const CLK = mk('div', 'position:absolute;left:0;width:1080px;text-align:center;display:none;font-family:M;font-weight:800;letter-spacing:-.04em;font-variant-numeric:tabular-nums', '', $('txt'));
const bU = tx(M('<span class="S" style="color:#ff8a8d">con uno menos.</span>'), 1180, 'shadow', 120);
const fmt = s => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
function sA(t) {
  const b = T.martes - .06, v = t < b; [a3, aS, bU].forEach(e => show(e, false)); if (!v) return;
  show(BC, true); place(BC, { is: 1.08 + .1 * seg(t, 0, b), iy: -20 * seg(t, 0, b), org: '50% 40%', dark: t < T.seis - .1 ? .45 : .72, z: 1 });
  show(aS, true); show(a3, t < T.seis - .1); a3.style.transform = `scale(${1 + .02 * seg(t, 0, T.seis)})`;
  if (t >= T.seis - .1) {
    show(CLK, true); CLK.style.top = '640px'; CLK.style.fontSize = '330px'; CLK.style.color = RED; CLK.style.textShadow = '0 6px 40px rgba(0,0,0,.6)';
    const p = E.io(seg(t, T.seis - .1, T.menos + .1)); CLK.textContent = fmt(360 * p);
    CLK.style.transform = `scale(${pulse(t, T.menos, .05)})`;
    show(bU, t >= T.uno - .2); reveal(bU, seg(t, T.uno - .2, T.uno + .1));
  }
}
const cK = tx('<div class="kick ink" style="letter-spacing:.26em">EL MARTES</div>', 560, '', 46);
const c5 = tx(M('<span class="S blue">5 contra 6:</span>'), 1180, '', 130);
const cN = tx(M('NI UN MINUTO.'), 1340, 'M8 ink', 96);
function sC(t) {
  const a = T.martes - .06, b = T.cuan - .06, v = t >= a && t < b; [cK, c5, cN].forEach(e => show(e, v)); if (!v) return;
  show($('paper'), true); cK.style.opacity = E.out(seg(t, a, a + .2));
  show(CLK, true); CLK.style.top = '640px'; CLK.style.fontSize = '330px'; CLK.style.color = '#9aa2b3'; CLK.style.textShadow = 'none'; CLK.textContent = '0:00';
  const q = E.out5(seg(t, a, a + .3)); CLK.style.transform = `scale(${(1.15 - .15 * q) * pulse(t, T.ni - .1, .04)})`;
  show(c5, t >= T.cinco - .25); reveal(c5, seg(t, T.cinco - .25, T.cinco + .05)); show(cN, t >= T.seis2 - .1); reveal(cN, seg(t, T.seis2 - .1, T.seis2 + .2));
  const fl = Math.exp(-Math.pow((t - a) / .06, 2)); $('grain').style.opacity = .05 + .15 * fl;
}
const eK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">PREGÚNTASELO A TU STAFF</div>', 640, 'shadow', 46);
const eQ = tx(M('¿CUÁNTAS'), 720, 'M8 shadow', 200);
const eT = tx(M('<span class="S blue">lleváis este mes?</span>'), 940, 'shadow', 130);
function sE(t) {
  const a = T.cuan - .06, b = T.camp - .05, v = t >= a && t < b; [eK, eQ, eT].forEach(e => show(e, v)); if (!v) return;
  show(BC, true); place(BC, { is: 1.22 - .08 * seg(t, a, b), org: '50% 40%', dark: .62, z: 1 });
  eK.style.opacity = E.out(seg(t, a, a + .2)); reveal(eQ, seg(t, a, a + .25)); show(eT, t >= T.mes - .4); reveal(eT, seg(t, T.mes - .4, T.mes - .1));
}
function sH(t) { if (t >= T.gra - .1) show($('paper'), true); }
window.frame = t => {
  show($('sysL'), false); $('sysL').style.background = '#0d0f14'; show($('paper'), false); show(BC, false); show(CLK, false); $('grain').style.opacity = .05;
  sA(t); sC(t); sE(t); sH(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
