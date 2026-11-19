// u68 · CONTEXTO · «Cuatro sitios» · concepto: «cuatro fichas en la mesa» — libreta, pizarra, hoja de cálculo y chat dibujados como
// fichas sobre papel, una por palabra (sin IA y sin logotipos, Biel 18/11); se juntan en un 2×2 («4 SITIOS · 1 equipo»), se iluminan
// con apuntar/buscar/avisar y se caen al suelo en «se perdiera» (SE PIERDE en rojo). Banquillos vacíos del Bernabéu y del Camp Nou para
// «nosotros también» y «para todos». En «decidimos crearlo» las cuatro fichas vuelan a un solo punto → «ProTeam.»; tres planos cortos de
// la app real (Semana, Convocatoria y la lista por jugador, rotulada «cada jugador», nunca «ficha»); «6 MESES»; «28 NOV»; cierre con la
// lista de espera y el contador real; final en bucle con las cuatro fichas del primer plano. Arriba, desde el fotograma 0: «LISTA: SE CIERRA EL 27».
const pulse = (t, t0, a = .06) => 1 + a * Math.exp(-Math.pow((t - t0 - .12) / .14, 2));
const RED = '#e5484d';
const RM = ph('rm', '50% 50%');
const CN = ph('cn', '50% 50%');
const CNB = ph('cn', '50% 50%'); CNB._img.style.filter = 'blur(26px) brightness(.32) saturate(.7)';

// ── las cuatro fichas (dibujadas, genéricas) ──
const INK = '#0d0f14';
const SV = [
  // libreta de espiral con lápiz
  `<svg viewBox="0 0 200 200"><rect x="48" y="26" width="108" height="150" rx="10" fill="#f6f1e1" stroke="${INK}" stroke-width="5" transform="rotate(-6 100 100)"/>
   <g transform="rotate(-6 100 100)">${[0,1,2,3,4,5].map(i => `<circle cx="48" cy="${44 + i * 23}" r="7" fill="none" stroke="${INK}" stroke-width="4"/>`).join('')}
   ${[0,1,2,3,4].map(i => `<line x1="66" y1="${58 + i * 22}" x2="${140 - (i % 2) * 22}" y2="${58 + i * 22}" stroke="#9aa2b3" stroke-width="4" stroke-linecap="round"/>`).join('')}
   <path d="M70 140 l18 -10 l12 12 l20 -26" fill="none" stroke="#2f6bff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
   <g transform="rotate(38 150 120)"><rect x="140" y="40" width="16" height="120" rx="3" fill="#f2c94c" stroke="${INK}" stroke-width="4"/><path d="M140 160 l8 18 l8 -18z" fill="#f6e3b4" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/></g></svg>`,
  // pizarra táctica con imanes
  `<svg viewBox="0 0 200 200"><rect x="18" y="34" width="164" height="124" rx="10" fill="#1f3b2c" stroke="${INK}" stroke-width="6"/>
   <rect x="30" y="46" width="140" height="100" fill="none" stroke="#e8efe9" stroke-width="3" opacity=".8"/><line x1="100" y1="46" x2="100" y2="146" stroke="#e8efe9" stroke-width="3" opacity=".8"/>
   <circle cx="100" cy="96" r="16" fill="none" stroke="#e8efe9" stroke-width="3" opacity=".8"/>
   ${[[56,70],[56,122],[78,96],[124,74],[130,118]].map(([x,y],i) => `<circle cx="${x}" cy="${y}" r="9" fill="${i < 3 ? '#2f6bff' : RED}" stroke="${INK}" stroke-width="3"/>`).join('')}
   <path d="M78 96 Q100 70 120 78" fill="none" stroke="#f2f1ec" stroke-width="3" stroke-dasharray="6 6"/><rect x="70" y="160" width="60" height="10" rx="4" fill="${INK}"/></svg>`,
  // hoja de cálculo genérica
  `<svg viewBox="0 0 200 200"><rect x="22" y="30" width="156" height="140" rx="10" fill="#fff" stroke="${INK}" stroke-width="5"/>
   <rect x="22" y="30" width="156" height="24" rx="10" fill="#d9dde6"/><rect x="22" y="44" width="156" height="10" fill="#d9dde6"/>
   ${[0,1,2,3,4].map(i => `<line x1="22" y1="${74 + i * 20}" x2="178" y2="${74 + i * 20}" stroke="#b9c0cc" stroke-width="2"/>`).join('')}
   ${[0,1,2].map(i => `<line x1="${62 + i * 40}" y1="54" x2="${62 + i * 40}" y2="170" stroke="#b9c0cc" stroke-width="2"/>`).join('')}
   <rect x="63" y="75" width="38" height="18" fill="#2f6bff" opacity=".85"/><rect x="103" y="115" width="38" height="18" fill="#2f6bff" opacity=".45"/>
   <rect x="143" y="95" width="34" height="18" fill="${RED}" opacity=".7"/><text x="34" y="47" font-family="M" font-weight="800" font-size="16" fill="${INK}">fx</text></svg>`,
  // chat genérico en un móvil
  `<svg viewBox="0 0 200 200"><rect x="52" y="14" width="96" height="172" rx="16" fill="#11141b" stroke="${INK}" stroke-width="5"/>
   <rect x="60" y="30" width="80" height="140" rx="8" fill="#eef0f4"/>
   <rect x="66" y="40" width="52" height="20" rx="10" fill="#fff" stroke="#c9cfdb" stroke-width="2"/><rect x="84" y="68" width="50" height="20" rx="10" fill="#2f6bff"/>
   <rect x="66" y="96" width="60" height="20" rx="10" fill="#fff" stroke="#c9cfdb" stroke-width="2"/><rect x="66" y="124" width="40" height="20" rx="10" fill="#fff" stroke="#c9cfdb" stroke-width="2"/>
   <circle cx="132" cy="44" r="10" fill="${RED}"/><text x="128" y="49" font-family="M" font-weight="800" font-size="13" fill="#fff">9</text></svg>`];
const NAMES = ['LIBRETA', 'PIZARRA', 'EXCEL', 'WHATSAPP'];
const TL = SV.map(s => mk('div', 'position:absolute;width:400px;height:400px;border-radius:44px;background:#fbfaf6;border:4px solid #d6d2c6;display:none;box-shadow:0 22px 50px rgba(13,15,20,.16);padding:24px', s, $('cards')));
function tile(i, x, y, w, o = {}) {
  const e = TL[i]; show(e, true); e.style.left = (x - w / 2) + 'px'; e.style.top = (y - w / 2) + 'px'; e.style.width = e.style.height = w + 'px';
  e.style.padding = (w * .06) + 'px'; e.style.borderRadius = (w * .11) + 'px';
  e.style.transform = `rotate(${o.r || 0}deg) scale(${o.s || 1})`; e.style.opacity = o.op == null ? 1 : o.op;
  e.style.borderColor = o.hi ? '#2f6bff' : '#d6d2c6'; e.style.boxShadow = o.hi ? '0 0 0 12px rgba(47,107,255,.18),0 22px 50px rgba(13,15,20,.16)' : '0 22px 50px rgba(13,15,20,.16)';
  e.style.zIndex = o.z || 1;
}
const GRID = [[310, 720], [770, 720], [310, 1180], [770, 1180]];

// ── rótulo fijo arriba desde el fotograma 0 (Andrés: «lista» siempre junto a «se cierra») ──
const TOP = mk('div', 'position:absolute;left:0;right:0;top:250px;text-align:center;display:none', `<span style="display:inline-flex;align-items:center;gap:16px;background:#0d0f14;border-radius:999px;padding:16px 30px;font-family:M;font-weight:700;font-size:32px;letter-spacing:.12em;color:#f2f1ec"><span style="width:16px;height:16px;border-radius:50%;background:#2f6bff;display:inline-block"></span>LISTA: SE CIERRA EL 27</span>`);

// ── A · Libreta. Pizarra. Excel. WhatsApp. → 4 SITIOS · 1 equipo ──
const aW = NAMES.map(n => tx(M(n), 1330, 'M8 ink', 170));
const a4 = tx(M('4 SITIOS'), 1440, 'M8 ink', 170);
const a1 = tx(M('<span class="S blue">para 1 equipo.</span>'), 1620, '', 110);
const AT = () => [0, T.piz - .06, T.exc - .06, T.wa - .06, T.cua - .06];
function sA(t) {
  const b = T.si - .04, v = t < b; [...aW, a4, a1].forEach(e => show(e, false)); if (!v) return;
  show($('paper'), true);
  const at = AT(); const g = t >= at[4];
  if (!g) {
    const i = at.findIndex((x, k) => t >= x && t < at[k + 1]);
    const q = E.out5(seg(t, at[i], at[i] + .22));
    tile(i, 540, 790, 640, { s: (i === 0 ? 1 : .9 + .1 * q) * (1 + .03 * seg(t, at[i], at[i + 1])), r: (i % 2 ? 3 : -3) * (1 - q) });
    show(aW[i], true); reveal(aW[i], i === 0 ? 1 : seg(t, at[i], at[i] + .25));
  } else {
    const q = E.out5(seg(t, at[4], at[4] + .45));
    GRID.forEach(([x, y], i) => tile(i, 540 + (x - 540) * q, 790 + (y - 790) * q * .9 - 60 * q, 640 - 250 * q, { r: [-4, 3, 2, -3][i] * q }));
    show(a4, true); reveal(a4, seg(t, at[4], at[4] + .3)); a4.style.transform = `scale(${pulse(t, at[4], .05)})`;
    show(a1, t >= T.equ - .3); reveal(a1, seg(t, T.equ - .3, T.equ + .05));
  }
  const fl = Math.exp(-Math.pow((t - at[4]) / .07, 2)); $('grain').style.opacity = .05 + .12 * fl;
}
// ── B · Si entrenas… nosotros también entrenamos (banquillo vacío del Bernabéu) ──
const bK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">SI ENTRENAS,</div>', 720, 'shadow', 46);
const bN = tx(M('<span class="S blue">nosotros</span>'), 790, 'shadow', 200);
const bE = tx(M('TAMBIÉN ENTRENAMOS.'), 1030, 'M8 shadow', 88);
function sB(t) {
  const a = T.si - .04, b = T.cada - .04, v = t >= a && t < b; [bK, bN, bE].forEach(e => show(e, v)); if (!v) return;
  show(RM, true); place(RM, { is: 1.28 - .14 * E.io(seg(t, a, b)), iy: 40 - 60 * seg(t, a, b), org: '50% 70%', dark: .6, z: 2 });
  bK.style.opacity = E.out(seg(t, a, a + .25)); show(bN, t >= T.nos - .1); reveal(bN, seg(t, T.nos - .1, T.nos + .25));
  bN.style.transform = `scale(${pulse(t, T.nos - .1, .05)})`; show(bE, t >= T.entr - .15); reveal(bE, seg(t, T.entr - .15, T.entr + .2));
}
// ── C · cada semana: apuntar · buscar · avisar → SE PIERDE (las fichas se caen) ──
const cK = tx('<div class="kick ink" style="letter-spacing:.24em">CADA SEMANA</div>', 380, '', 46);
const VB = ['apuntar', 'buscar', 'avisar'].map(w => tx(M(`<span class="S" style="color:#0d0f14">${w}</span>`), 1500, '', 150));
const cP = tx(M(`<span style="color:${RED}">SE PIERDE</span>`), 1490, 'M8', 190);
const VT = () => [T.apu - .08, T.bus - .08, T.avi - .08];
const POS = [[300, 760], [780, 740], [320, 1200], [770, 1210]];
function sC(t) {
  const a = T.cada - .04, b = T.buscab - .04, v = t >= a && t < b; [cK, ...VB, cP].forEach(e => show(e, v)); if (!v) return;
  show($('paper'), true); cK.style.opacity = E.out(seg(t, a, a + .25));
  const vt = VT(); const hiI = [0, 2, 3]; const fall = T.perd - .35;
  POS.forEach(([x, y], i) => {
    let k = vt.findIndex((x0, j) => t >= x0 && t < (vt[j + 1] || fall)); const hi = k >= 0 && hiI[k] === i;
    const ft = seg(t, fall + i * .06, fall + i * .06 + .7), dy = 1300 * ft * ft, rr = [-28, 22, -16, 34][i] * ft;
    const jig = Math.sin(t * 2 + i) * 6;
    tile(i, x + [-40, 30, -20, 50][i] * ft, y + jig + dy, 380, { r: [-5, 4, 3, -4][i] + rr, s: hi ? 1.08 * pulse(t, vt[k], .04) : 1, hi, z: hi ? 3 : 1, op: 1 - seg(t, fall + .5, fall + .9) });
  });
  VB.forEach((e, k) => { const on = t >= vt[k] && t < (vt[k + 1] || fall); show(e, on); if (on) reveal(e, seg(t, vt[k], vt[k] + .2)); });
  show(cP, t >= T.perd - .1); reveal(cP, seg(t, T.perd - .1, T.perd + .2)); cP.style.transform = `scale(${pulse(t, T.perd - .1, .07)}) rotate(${-2 * seg(t, T.perd, b)}deg)`;
  if (t >= fall) { cP.style.top = (900 + 0) + 'px'; } else cP.style.top = '1490px';
  const fl = Math.exp(-Math.pow((t - T.perd) / .07, 2)); $('grain').style.opacity = .05 + .18 * fl;
}
// ── D · Buscábamos cómo arreglarlo · para nosotros y para todos (banquillo del Camp Nou) ──
const dB = tx(M('Buscábamos'), 760, 'M8 shadow', 130);
const dB2 = tx(M('<span class="S blue">cómo arreglarlo.</span>'), 920, 'shadow', 130);
const dK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">PARA NOSOTROS</div>', 700, 'shadow', 46);
const dT = tx(M('<span class="S blue">y para todos.</span>'), 790, 'shadow', 170);
const dL = tx(M('LOS ENTRENADORES QUE ESTABAN IGUAL'), 1030, 'M7 shadow', 48);
function sD(t) {
  const a = T.buscab - .04, b = T.hasta - .04, v = t >= a && t < b; [dB, dB2, dK, dT, dL].forEach(e => show(e, false)); if (!v) return;
  const p2 = t >= T.para - .05;
  if (!p2) {
    show(CNB, true); place(CNB, { is: 1.5 - .2 * seg(t, a, T.para), iy: -60 + 100 * seg(t, a, T.para), z: 1 });
    show(dB, true); reveal(dB, seg(t, a, a + .3)); show(dB2, t >= T.arr - .55); reveal(dB2, seg(t, T.arr - .55, T.arr - .2));
  } else {
    show(CN, true); place(CN, { is: 1.14 + .2 * E.io(seg(t, T.para, b)), iy: 40 - 100 * seg(t, T.para, b), org: '50% 85%', dark: .6, z: 1 });
    show(dK, true); dK.style.opacity = E.out(seg(t, T.para - .05, T.para + .2));
    show(dT, t >= T.todos - .45); reveal(dT, seg(t, T.todos - .45, T.todos - .1)); dT.style.transform = `scale(${pulse(t, T.todos - .45, .05)})`;
    show(dL, t >= T.todos + .4); reveal(dL, seg(t, T.todos + .4, T.todos + .75));
    const fl = Math.exp(-Math.pow((t - T.para) / .06, 2)); $('grain').style.opacity = .05 + .2 * fl;
  }
}
// ── E · Hasta que decidimos crearlo → las cuatro fichas a un solo punto → ProTeam. ──
const eK = tx('<div class="kick" style="color:#e6e8ee;letter-spacing:.26em">HASTA QUE</div>', 330, '', 46);
const eD = tx(M('DECIDIMOS'), 400, 'M8', 140);
const eC = tx(M('<span class="S blue">crearlo.</span>'), 540, '', 170);
const eP = tx('ProTeam.', 780, 'M8', 240);
const eA = tx(M('UNA APP PARA ENTRENADORES'), 1080, 'M7', 54);
const DOT = mk('div', 'position:absolute;left:540px;top:1240px;width:40px;height:40px;margin:-20px 0 0 -20px;border-radius:50%;background:#2f6bff;display:none', '', $('cards'));
function sE(t) {
  const a = T.hasta - .04, b = T.sem - .04, v = t >= a && t < b; [eK, eD, eC, eP, eA].forEach(e => show(e, false)); show(DOT, false); if (!v) return;
  show($('sysL'), true); const hit = t >= T.pt - .06;
  if (!hit) {
    show(eK, true); eK.style.opacity = E.out(seg(t, a, a + .25)); show(eD, t >= T.decid - .1); reveal(eD, seg(t, T.decid - .1, T.decid + .2));
    show(eC, t >= T.crear - .1); reveal(eC, seg(t, T.crear - .1, T.crear + .2));
    const q = E.in(seg(t, T.crear - .1, T.pt - .06));
    const P0 = [[250, 1050], [830, 1050], [250, 1480], [830, 1480]];
    P0.forEach(([x, y], i) => { const k = E.out(seg(t, a + i * .08, a + .4 + i * .08));
      tile(i, x + (540 - x) * q, y + (1240 - y) * q + (1 - k) * 200, 300 * (1 - .8 * q), { r: [-6, 5, 4, -5][i] * (1 - q) + 120 * q, op: k * (1 - seg(t, T.pt - .16, T.pt - .06)) }); });
    show(DOT, q > .6); DOT.style.transform = `scale(${1 + 3 * seg(t, T.pt - .3, T.pt - .06)})`;
  } else {
    show(CNB, true); place(CNB, { is: 1.4 - .12 * seg(t, T.pt, b), z: 1 });
    show(eP, true); const q = E.out5(seg(t, T.pt - .06, T.pt + .2)); eP.style.opacity = q;
    eP.style.transform = `scale(${(1.25 - .25 * q) * pulse(t, T.pt - .06, .06) * (1 + .08 * seg(t, T.pt, b))})`; eP.style.color = t >= T.pt + .3 ? '#4f86ff' : '#f2f1ec';
    show(eA, t >= T.app - .25); reveal(eA, seg(t, T.app - .25, T.app + .1));
    const fl = Math.exp(-Math.pow((t - T.pt) / .07, 2)); $('grain').style.opacity = .05 + .25 * fl;
    $('sysL').style.background = `rgba(47,107,255,${.5 * fl})`; show($('sysL'), fl > .02);
  }
}
// ── F · la app real, tres planos cortos (Semana · Convocatoria · lista por jugador) → el mismo sitio ──
const PHN = mk('div', '', '<div class="scr"><img id="pi1" src="/tools/reel68/img/semana.jpg"><img id="pi2" src="/tools/reel68/img/convocatoria.jpg"><img id="pi3" src="/tools/reel68/img/rpe.jpg"></div>', $('phones')); PHN.className = 'phone';
const FL = ['la semana', 'la convocatoria', 'cada jugador'].map(w => tx(M(`<span class="S blue">${w}</span>`), 1540, '', 120));
const fM = tx(M('EN EL MISMO SITIO.'), 1540, 'M8', 96);
function sF(t) {
  const a = T.sem - .04, b = T.llev - .04, v = t >= a && t < b; [...FL, fM].forEach(e => show(e, false)); show(PHN, v); if (!v) return;
  show($('sysL'), true); $('sysL').style.background = '#0d0f14';
  const q = E.out5(seg(t, a, a + .4)); PHN.style.left = '290px'; PHN.style.top = (410 + (1 - q) * 300) + 'px'; PHN.style.opacity = q;
  PHN.style.transform = `scale(${.98 + .04 * seg(t, a, b)})`;
  const ts = [a, T.conv - .06, T.jug - .06]; const k = t >= ts[2] ? 2 : t >= ts[1] ? 1 : 0;
  ['pi1', 'pi2', 'pi3'].forEach((id, i) => { $(id).style.display = i === k ? 'block' : 'none'; $(id).style.transform = `translateY(${-30 * seg(t, ts[i], ts[i] + 1.2)}px)`; });
  const mm = t >= T.mismo - .2;
  if (!mm) { show(FL[k], true); reveal(FL[k], seg(t, ts[k], ts[k] + .2)); }
  else { show(fM, true); reveal(fM, seg(t, T.mismo - .2, T.mismo + .1)); }
}
// ── G · 6 MESES construyéndola → ABRE EL SÁBADO 28 NOV (banquillo del Bernabéu) ──
const gK = tx('<div class="kick" style="letter-spacing:.26em;color:#e6e8ee">LLEVAMOS</div>', 640, 'shadow', 46);
const g6 = tx(M('6 MESES'), 710, 'M8 shadow', 240);
const gC = tx(M('<span class="S" style="color:#e6e8ee">construyéndola.</span>'), 990, 'shadow', 110);
const gK2 = tx('<div class="kick" style="letter-spacing:.26em;color:#e6e8ee">ABRE EL SÁBADO</div>', 640, 'shadow', 46);
const g28 = tx('28 NOV', 710, 'M8 shadow', 250);
function sG(t) {
  const a = T.llev - .04, b = T.pero - .04, v = t >= a && t < b; [gK, g6, gC, gK2, g28].forEach(e => show(e, false)); if (!v) return;
  show(RM, true); place(RM, { is: 1.12 + .14 * seg(t, a, b), iy: -30 + 50 * seg(t, a, b), org: '50% 60%', dark: .68, z: 2 });
  const z = t >= T.v28 - .3;
  if (!z) {
    show(gK, true); gK.style.opacity = E.out(seg(t, a, a + .25)); show(g6, t >= T.seis - .1); reveal(g6, seg(t, T.seis - .1, T.seis + .2));
    g6.style.transform = `scale(${pulse(t, T.seis - .1, .05)})`; show(gC, t >= T.seis + .5); reveal(gC, seg(t, T.seis + .5, T.seis + .8));
  } else {
    show(gK2, true); gK2.style.opacity = E.out(seg(t, T.v28 - .3, T.v28 - .1)); show(g28, true);
    const q = E.out5(seg(t, T.v28 - .3, T.v28 - .05)); g28.style.opacity = q; g28.style.color = '#4f86ff';
    g28.style.transform = `scale(${(1.2 - .2 * q) * (1 + .04 * seg(t, T.v28, b))})`;
  }
}
// ── H · final en bucle: las cuatro fichas del primer plano, en papel, bajo el cierre ──
function sH(t) {
  const g0 = T.gra - .1; if (t < g0) return; show($('paper'), true);
  const q = E.out5(seg(t, g0, g0 + .4));
  const dr = seg(t, g0, T.END); [0, 1, 2, 3].forEach(i => tile(i, 180 + i * 240, 1440 - 50 * q - 40 * dr * (i % 2 ? 1 : -1), 200, { r: [-4, 3, 2, -3][i] * (1 - 2 * dr), op: .5 * q }));
}

window.frame = t => {
  show($('sysL'), false); $('sysL').style.background = '#0d0f14'; show($('paper'), false); TL.forEach(e => show(e, false));
  [CN, RM, CNB].forEach(p => show(p, false)); $('grain').style.opacity = .05;
  show(TOP, t < T.pero - .04);
  sA(t); sB(t); sC(t); sD(t); sE(t); sF(t); sG(t); sH(t); webcta(t);
  $('grain').style.transform = `translate(${(Math.floor(t * 24) * 37) % 200 - 100}px,${(Math.floor(t * 24) * 53) % 200 - 100}px)`;
};
document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => setTimeout(() => { window.frame(0); window.ready = true; }, 300));
