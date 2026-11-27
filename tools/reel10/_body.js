
// ── 1 · GANCHO: banquillo de la selección (zona de cambios) · «ENTRA A DEFENDER. SALE A ATACAR.» legible desde el fotograma 0 ──
const BQ = ph('banquillo', '47% 50%');
const k1 = tx(`<div class="kick" style="color:#e6e8ee">BALONMANO · INFANTILES</div>`, 1120, 'shadow', 40);
const h1 = tx('ENTRA A DEFENDER.', 1180, 'M8 shadow', 104);
const h2 = tx('SALE A ATACAR.', 1300, 'M8 shadow', 104);
const h3 = tx(M('<span class="S blue">Tiene 12 años.</span>'), 1420, 'shadow', 150);
function hook(t) {
  const b = T.gan - .1, v = t < b; [BQ, k1, h1, h2, h3].forEach(e => show(e, v)); if (!v) return;
  const punch = .05 * E.out5(seg(t, T.sal - .05, T.sal + .25));
  place(BQ, { is: 1.08 + .05 * seg(t, 0, b) + punch, org: '40% 45%', grad: 'linear-gradient(180deg,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,.35) 52%,rgba(0,0,0,.82) 66%,rgba(0,0,0,.9) 100%)' });
  h2.style.opacity = .55 + .45 * E.out(seg(t, T.sal - .1, T.sal + .15));
  h1.style.opacity = 1 - .45 * E.out(seg(t, T.sal - .1, T.sal + .15));
  show(h3, t >= T.doc - .05); reveal(h3, seg(t, T.doc - .05, T.doc + .3));
  h3.style.transform = `scale(${1 + .05 * Math.exp(-Math.pow((t - T.doc - .2) / .15, 2))})`;
  const out = seg(t, b - .1, b); [BQ, k1, h1, h2, h3].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 2 y 4 · LA PISTA DESDE ARRIBA: mitad de defensa y mitad de ataque; la ficha 12 se queda en su mitad… y en el partidillo cruza ──
const CX = 190, CY = 640, CW = 700, CH = 1000;
const COURT = mk('div', `position:absolute;left:${CX}px;top:${CY}px;width:${CW}px;height:${CH}px;border:5px solid #3a4152;border-radius:18px;background:#121620;display:none;overflow:hidden`,
  `<div id="hA" style="position:absolute;left:0;top:0;width:100%;height:50%;background:#121620"></div>
   <div id="hD" style="position:absolute;left:0;top:50%;width:100%;height:50%;background:#121620"></div>
   <div id="hatch" style="position:absolute;left:0;top:0;width:100%;height:50%;opacity:0;background:repeating-linear-gradient(45deg,rgba(255,255,255,.07) 0 14px,rgba(0,0,0,0) 14px 30px)"></div>
   <div style="position:absolute;left:0;right:0;top:50%;height:5px;margin-top:-2px;background:#3a4152"></div>
   <div style="position:absolute;left:50%;top:-230px;width:460px;height:460px;margin-left:-230px;border:5px solid #3a4152;border-radius:50%"></div>
   <div style="position:absolute;left:50%;bottom:-230px;width:460px;height:460px;margin-left:-230px;border:5px solid #3a4152;border-radius:50%"></div>
   <div id="lA" style="position:absolute;left:0;right:0;top:150px;text-align:center;font-family:M;font-weight:800;font-size:44px;letter-spacing:.16em;color:#6d7588">ATAQUE</div>
   <div id="lD" style="position:absolute;left:0;right:0;bottom:150px;text-align:center;font-family:M;font-weight:800;font-size:44px;letter-spacing:.16em;color:#6d7588">DEFENSA</div>
   <div id="zA" style="position:absolute;left:0;right:0;top:215px;text-align:center;font-family:M;font-weight:800;font-size:96px;color:#8a92a3;opacity:0">0 min</div>`, $('cards'));
const CHIP = mk('div', `position:absolute;left:${CX + CW - 330}px;top:${CY + CH - 300}px;width:250px;height:84px;border-radius:42px;background:#2f6bff;color:#fff;font-family:M;font-weight:800;font-size:40px;line-height:84px;text-align:center;display:none;box-shadow:0 12px 30px rgba(47,107,255,.45)`, '+1 defensa', $('cards'));
const FICHA = mk('div', `position:absolute;left:0;top:0;width:150px;height:150px;margin:-75px 0 0 -75px;border-radius:50%;background:#f2f1ec;border:8px solid #4f86ff;color:#0d0f14;font-family:M;font-weight:800;font-size:76px;line-height:134px;text-align:center;display:none;box-shadow:0 14px 34px rgba(0,0,0,.5)`, '12', $('cards'));
const TRAIL = mk('div', 'position:absolute;left:540px;width:8px;margin-left:-4px;border-radius:4px;background:repeating-linear-gradient(180deg,#4f86ff 0 18px,rgba(0,0,0,0) 18px 34px);display:none', '', $('cards'));
const cA = tx(M('Tú ganas una defensa.'), 300, 'M8', 84);
const cB = tx(M('Él se queda sin'), 410, 'M8', 84);
const cC = tx(M('<span class="S blue">medio balonmano.</span>'), 500, '', 112);
function court(t, on) { [COURT, FICHA].forEach(e => show(e, on)); }
function conse(t) {
  const a = T.gan - .1, b = T.eus - .1, v = t >= a && t < b; [cA, cB, cC, CHIP].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true); court(t, true);
  const p = E.out5(seg(t, a, a + .4)); COURT.style.opacity = p; COURT.style.transform = `translateY(${(1 - p) * 120}px) scale(${.96 + .04 * p})`;
  FICHA.style.left = '540px'; FICHA.style.top = (CY + CH * .75 + (1 - p) * 120) + 'px'; FICHA.style.opacity = E.out(seg(t, a + .15, a + .4));
  FICHA.style.transform = `scale(${1 + .1 * Math.exp(-Math.pow((t - T.gan - .3) / .15, 2))})`;
  reveal(cA, seg(t, a, a + .3));
  const d = E.out(seg(t, T.gan + .2, T.gan + .5)); $('hD').style.background = `rgba(47,107,255,${.28 * d})`; $('lD').style.color = d > .5 ? '#9db8ff' : '#6d7588';
  CHIP.style.opacity = d; CHIP.style.transform = `translateY(${(1 - d) * 30}px) scale(${.9 + .1 * d})`;
  show(cB, t >= T.med - .1); reveal(cB, seg(t, T.med - .1, T.med + .2)); show(cC, t >= T.med + .5); reveal(cC, seg(t, T.med + .5, T.med + .85));
  const g = E.out(seg(t, T.med + .5, T.med + .9)); $('hatch').style.opacity = g; $('hA').style.background = `rgba(0,0,0,${.35 * g})`; $('zA').style.opacity = g; $('lA').style.opacity = 1 - .5 * g;
  const out = seg(t, b - .12, b); [COURT, FICHA, cA, cB, cC, CHIP].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 3 · LA NORMA (papel): balonmano base en España, hasta juvenil · NO PERMITIDO ──
const DOC = mk('div', 'position:absolute;left:110px;top:560px;width:860px;height:760px;background:#fbfaf6;border:3px solid #d6d2c6;border-radius:22px;box-shadow:0 30px 60px rgba(0,0,0,.18);display:none',
  `<div style="position:absolute;left:60px;top:60px;font-family:M;font-weight:700;font-size:30px;letter-spacing:.14em;color:#6d6a60">BALONMANO BASE · ESPAÑA</div>
   <div style="position:absolute;left:60px;top:108px;font-family:M;font-weight:700;font-size:30px;letter-spacing:.14em;color:#6d6a60">HASTA JUVENIL</div>
   <div style="position:absolute;left:60px;right:60px;top:170px;height:3px;background:#e1ddd1"></div>
   <div style="position:absolute;left:60px;top:220px;font-family:M;font-weight:800;font-size:80px;letter-spacing:-.04em;line-height:1.02;color:#0d0f14">Cambio<br>ataque-defensa</div>
   ${[0, 1, 2].map(r => `<div style="position:absolute;left:60px;width:${[640, 700, 520][r]}px;top:${440 + r * 46}px;height:14px;border-radius:7px;background:#e4e0d4"></div>`).join('')}
   <div id="stamp" style="position:absolute;left:150px;top:560px;padding:14px 34px;border:8px solid #2f6bff;border-radius:16px;color:#2f6bff;font-family:M;font-weight:800;font-size:72px;letter-spacing:.04em;transform:rotate(-6deg);opacity:0">NO PERMITIDO</div>`, $('cards'));
const nK = tx(`<div class="kick ink" style="color:#0d0f14">${M('LA NORMA')}</div>`, 400, '', 40);
const nN = tx(`<div class="M5" style="font-size:34px;color:#6d6a60">Balonmano base · hasta juvenil</div>`, 1400, '', 34);
function norma(t) {
  const a = T.eus - .1, b = T.sem - .1, v = t >= a && t < b; [DOC, nK, nN].forEach(e => show(e, v)); if (!v) return;
  show($('paper'), true);
  const p = E.out5(seg(t, a, a + .4)); DOC.style.opacity = p; DOC.style.transform = `translateY(${(1 - p) * 140}px) rotate(${(1 - p) * 3}deg) scale(${1 + .03 * seg(t, a, b)})`;
  reveal(nK, seg(t, a + .05, a + .35)); nN.style.opacity = E.out(seg(t, a + .4, a + .7));
  const sT = T.per + .55, s = E.out5(seg(t, sT, sT + .2)), st = $('stamp');
  st.style.opacity = s; st.style.transform = `rotate(-6deg) scale(${1.6 - .6 * s})`;
  DOC.style.transform += ` translate(${Math.exp(-Math.pow((t - sT - .2) / .06, 2)) * 6}px,0)`;
  const out = seg(t, b - .12, b); [DOC, nK, nN].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 4 · FICHA PARA GUARDAR: esta semana, en el partidillo, quien defiende ataca la siguiente (la ficha 12 cruza) ──
const fK = tx(`<div class="kick">${M('ESTA SEMANA · EN EL PARTIDILLO')}</div>`, 300, '', 40);
const f1 = tx(M('Quien defiende,'), 360, 'M8', 92);
const f2 = tx(M('<span class="S blue">ataca la siguiente.</span>'), 466, '', 120);
const fN = mk('div', `position:absolute;left:${CX}px;top:${CY + CH + 40}px;width:${CW}px;text-align:center;font-family:M;font-weight:700;font-size:40px;color:#c9cfdb;display:none`, 'Nadie sale al recuperar.');
function ficha(t) {
  const a = T.sem - .1, b = T.ald - .1, v = t >= a && t < b; [fK, f1, f2, fN, TRAIL].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true); court(t, true); show(CHIP, false);
  $('hatch').style.opacity = 0; $('hA').style.background = '#121620'; $('zA').style.opacity = 0; $('lA').style.opacity = 1;
  const p = E.out5(seg(t, a, a + .35)); COURT.style.opacity = p; COURT.style.transform = `translateY(${(1 - p) * 60}px)`;
  reveal(fK, seg(t, a, a + .3)); show(f1, t >= T.qui - .1); reveal(f1, seg(t, T.qui - .1, T.qui + .2)); show(f2, t >= T.ata - .1); reveal(f2, seg(t, T.ata - .1, T.ata + .25));
  const d = E.out(seg(t, T.qui - .05, T.qui + .3)); $('hD').style.background = `rgba(47,107,255,${.28 * d})`; $('lD').style.color = d > .5 ? '#9db8ff' : '#6d7588';
  const c = E.io(seg(t, T.ata - .05, T.ata + .65)); const y0 = CY + CH * .75, y1 = CY + CH * .25;
  FICHA.style.left = '540px'; FICHA.style.top = (y0 + (y1 - y0) * c) + 'px'; FICHA.style.opacity = p;
  FICHA.style.transform = `scale(${1 + .12 * Math.sin(c * Math.PI)})`;
  TRAIL.style.top = (y0 + (y1 - y0) * c) + 'px'; TRAIL.style.height = ((y0 - y1) * c) + 'px'; TRAIL.style.opacity = c > 0 ? .9 : 0;
  const u = E.out(seg(t, T.ata + .45, T.ata + .8)); $('hA').style.background = `rgba(47,107,255,${.28 * u})`; $('lA').style.color = u > .5 ? '#9db8ff' : '#6d7588';
  fN.style.opacity = E.out(seg(t, T.ata + .7, T.ata + 1));
  const out = seg(t, b - .12, b); [COURT, FICHA, TRAIL, fK, f1, f2, fN].forEach(e => e.style.opacity = Math.min(+(e.style.opacity || 1), 1 - out));
}

// ── 5 · SENTENCIA: a los doce, nadie es especialista (atacante y defensora en el mismo balón) ──
const CT = ph('contacto', '62% 40%');
const sA = tx(M('A LOS 12,'), 1180, 'M8 shadow', 150);
const sB = tx(M('<span class="S blue">nadie es especialista.</span>'), 1350, 'shadow', 112);
function sent(t) {
  const a = T.ald - .1, b = T.seg - .1, v = t >= a && t < b; [CT, sA, sB].forEach(e => show(e, v)); if (!v) return;
  place(CT, { is: 1.06 + .06 * seg(t, a, b), org: '55% 40%', grad: 'linear-gradient(180deg,rgba(0,0,0,.15) 0%,rgba(0,0,0,0) 40%,rgba(0,0,0,.6) 58%,rgba(0,0,0,.88) 74%,rgba(0,0,0,.9) 100%)', z: 3 });
  CT.style.opacity = E.out(seg(t, a, a + .14));
  reveal(sA, seg(t, a + .05, a + .35)); show(sB, t >= T.esp - .1); reveal(sB, seg(t, T.esp - .1, T.esp + .25));
  sB.style.transform = `scale(${1 + .04 * Math.exp(-Math.pow((t - T.esp - .5) / .15, 2))})`;
}

// ── 6 · RETO PARA EL STAFF sobre el banquillo del principio (bucle) ──
const BQ2 = ph('banquillo', '47% 50%');
const rK = tx(`<div class="kick" style="color:#e6e8ee">${M('RETO PARA TU STAFF')}</div>`, 1120, 'shadow', 40);
const r1 = tx(M('¿Quién no ha atacado'), 1180, 'M8 shadow', 96);
const r2 = tx(M('<span class="S" style="color:#9db8ff">en todo el año?</span>'), 1300, 'shadow', 120);
function reto(t) {
  const a = T.seg - .1, b = T.com - .1, v = t >= a && t < b; [BQ2, rK, r1, r2].forEach(e => show(e, v)); if (!v) return;
  place(BQ2, { is: 1.2 + .05 * seg(t, a, b), org: '35% 40%', grad: 'linear-gradient(180deg,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,.4) 52%,rgba(0,0,0,.85) 66%,rgba(0,0,0,.9) 100%)', z: 4 });
  BQ2.style.opacity = E.out(seg(t, a, a + .14));
  reveal(rK, seg(t, a + .05, a + .35)); show(r1, t >= T.que - .1); reveal(r1, seg(t, T.que - .1, T.que + .25)); show(r2, t >= T.que + .6); reveal(r2, seg(t, T.que + .6, T.que + .9));
}

// ── 7 · COMENTA: te preparo la semana en la app de ProTeam (captura real de Semana) ──
const PW = 560, SW = PW - 26, SH = Math.round(SW * 2410 / 1112);
const PHN = mk('div', `position:absolute;left:${540 - PW / 2}px;top:760px;width:${PW}px;height:${SH + 26}px;border-radius:62px;background:#0b0d12;border:3px solid #2a3040;padding:10px;display:none;box-shadow:0 40px 90px rgba(0,0,0,.6);transform-origin:50% 0;will-change:transform`, '<div style="position:relative;width:100%;height:100%;border-radius:50px;overflow:hidden;background:#f6f6f4"><img src="/tools/reel10/img/semana.jpg" style="position:absolute;left:0;top:0;width:100%;height:100%"></div>', $('phones'));
const BAND = mk('div', 'position:absolute;left:0;top:0;width:1080px;height:700px;background:linear-gradient(#0d0f14 86%,rgba(13,15,20,0));display:none');
const mK = tx(`<div class="kick">${M('COMENTA')}</div>`, 300, '', 40);
const m1 = tx(M('Tu categoría y tus días'), 360, 'M8', 84);
const m2 = tx(M('<span class="S blue">y te preparo la semana.</span>'), 466, '', 104);
const m3 = tx(`<div class="M7" style="font-size:36px;color:#9aa2b3">en la app de ProTeam · captura real</div>`, 600, '', 36);
function appc(t) {
  const a = T.com - .1, b = T.camp - .05, v = t >= a && t < b; [PHN, BAND, mK, m1, m2, m3].forEach(e => show(e, v)); if (!v) return;
  show($('sysL'), true);
  const p = E.out5(seg(t, a + .05, a + .5)); PHN.style.transform = `translateY(${(1 - p) * 900}px) scale(${1.05 + .06 * seg(t, a, b)})`;
  reveal(mK, seg(t, a, a + .3)); reveal(m1, seg(t, T.com + .05, T.com + .35)); show(m2, t >= T.pre - .1); reveal(m2, seg(t, T.pre - .1, T.pre + .25));
  m3.style.opacity = E.out(seg(t, T.pre + .8, T.pre + 1.1));
  const out = seg(t, b - .12, b); [PHN, mK, m1, m2, m3].forEach(e => e.style.opacity = 1 - out);
}

