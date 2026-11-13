// Renderiza las publicaciones y Stories del kit «El 27 se encienden los focos».
//   node kit/posts.js RAW_DIR OUT_DIR
const { chromium } = require('playwright');
const path = require('path');
const RAW = path.resolve(process.argv[2]), OUT = path.resolve(process.argv[3]);
const L = '<b>pro-team.app</b><br>Lista de espera · 27.11 · 23:59';
const F = (n) => 'file://' + path.join(RAW, n);
const POSTS = [
  { id: 'p1-focos', w: 1080, h: 1350, photo: F('img0.png'), pos: '50% 60%', chip: 'LISTA DE ESPERA ABIERTA', chipBlue: true,
    kick: 'Fútbol · Baloncesto · Balonmano', hl: 'El 27 se encienden<br>los <em>focos.</em>', hs: 118, sub: 'Algo llega para los entrenadores que lo dan todo cada semana.', cta: 'Crea tu cuenta', url: L, txtTop: 190 },
  { id: 'p2-banquillo', w: 1080, h: 1350, photo: F('img1.png'), pos: '50% 70%', chip: 'FALTA POCO',
    kick: 'ProTeam · lista de espera', hl: 'Tu banquillo,<br>en tu <em>bolsillo.</em>', hs: 118, sub: 'Registro en directo, planificación y resumen del partido en una sola app.', cta: 'Entra en la lista', url: L, txtTop: 190 },
  { id: 'p3-cada-accion', w: 1080, h: 1350, photo: F('img2.png'), pos: '50% 80%', chip: '27.11 · 23:59',
    kick: 'Balonmano · Baloncesto · Fútbol', hl: 'Cada acción,<br><em>registrada.</em>', hs: 118, sub: 'Ataque, defensa, exclusiones y tiempos muertos, mientras juegas.', cta: 'Crea tu cuenta', url: L, txtTop: 190 },
  { id: 'p4-en-directo', w: 1080, h: 1350, photo: F('img3-res.png'), pos: '50% 50%', chip: 'APP REAL',
    shade: 'linear-gradient(90deg,rgba(13,15,20,.92) 0%,rgba(13,15,20,.6) 45%,rgba(13,15,20,0) 70%),linear-gradient(180deg,rgba(13,15,20,0) 70%,rgba(13,15,20,.9) 100%)',
    kick: 'Resumen del partido', hl: 'El partido,<br><em>en directo.</em>', hs: 100, sub: 'Marcador por parte, eficacia y lanzamientos al momento.', subW: 520, cta: 'Entra en la lista', url: L, txtTop: 300 },
  { id: 'p5-pizarra', w: 1080, h: 1350, photo: F('img4.png'), pos: '50% 80%', chip: 'LISTA DE ESPERA',
    kick: 'Planificación', hl: 'La pizarra<br>se queda <em>corta.</em>', hs: 118, sub: 'Planifica la temporada, la semana y cada sesión desde el móvil.', cta: 'Crea tu cuenta', url: L, txtTop: 190 },
  // carrusel
  { id: 'c1-1', w: 1080, h: 1350, photo: F('img7.png'), pos: '50% 50%', chip: '1 / 3',
    shade: 'linear-gradient(180deg,rgba(13,15,20,.75) 0%,rgba(13,15,20,0) 40%,rgba(13,15,20,0) 70%,rgba(13,15,20,.85) 100%)',
    kick: 'Libreta · cronómetro · memoria', hl: '¿Así analizas<br><em>tus partidos?</em>', hs: 112, sub: '', cta: '', url: '<b>Desliza →</b>', txtTop: 190 },
  { id: 'c1-2', w: 1080, h: 1350, photo: F('img3-reg.png'), pos: '50% 50%', chip: '2 / 3',
    shade: 'linear-gradient(90deg,rgba(13,15,20,.92) 0%,rgba(13,15,20,.6) 45%,rgba(13,15,20,0) 70%),linear-gradient(180deg,rgba(13,15,20,0) 70%,rgba(13,15,20,.9) 100%)',
    kick: 'Registro en directo', hl: 'Así,<br><em>en directo.</em>', hs: 104, sub: 'Cada acción con uno o dos toques, desde la banda.', subW: 520, cta: '', url: '<b>Desliza →</b>', txtTop: 300 },
  { id: 'c1-3', w: 1080, h: 1350, photo: F('img0.png'), pos: '50% 60%', chip: '3 / 3', chipBlue: true,
    shade: 'linear-gradient(180deg,rgba(13,15,20,.94) 0%,rgba(13,15,20,.7) 45%,rgba(13,15,20,.2) 70%,rgba(13,15,20,.92) 100%)',
    kick: 'Lista de espera', hl: '6 meses gratis<br>para la <em>lista.</em>', hs: 118, sub: 'Crea tu cuenta antes del 27.11 a las 23:59 y entra en la lista de espera.', cta: 'Crea tu cuenta', url: L, txtTop: 190 },
  // stories
  { id: 's1-focos', w: 1080, h: 1920, photo: F('img5.png'), pos: '50% 50%', chip: 'LISTA DE ESPERA', chipBlue: true,
    shade: 'linear-gradient(180deg,rgba(13,15,20,.55) 0%,rgba(13,15,20,0) 30%,rgba(13,15,20,0) 45%,rgba(13,15,20,.9) 80%,rgba(13,15,20,.95) 100%)',
    kick: '27.11 · 23:59', hl: 'Se encienden<br>los <em>focos.</em>', hs: 132, sub: 'Crea tu cuenta y entra en la lista de espera.', cta: 'pro-team.app', url: '', txtBottom: 470 },
  { id: 's2-tunel', w: 1080, h: 1920, photo: F('img6.png'), pos: '50% 50%', chip: '27.11 · 23:59',
    shade: 'linear-gradient(180deg,rgba(13,15,20,.7) 0%,rgba(13,15,20,0) 30%,rgba(13,15,20,0) 50%,rgba(13,15,20,.9) 80%,rgba(13,15,20,.95) 100%)',
    kick: 'Lista de espera', hl: 'Crea tu cuenta.<br><em>Sal al campo.</em>', hs: 120, sub: '6 meses gratis para quien esté en la lista antes del 27.11 a las 23:59.', cta: 'pro-team.app', url: '', txtBottom: 470 },
];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'post.html'));
  for (const s of POSTS) {
    await p.setViewportSize({ width: s.w, height: s.h });
    await p.evaluate((s) => window.build(s), s);
    if (s.subW) await p.evaluate((w) => { document.getElementById('sub').style.maxWidth = w + 'px'; }, s.subW);
    await p.waitForTimeout(150);
    await p.locator('#c').screenshot({ path: path.join(OUT, s.id + '.jpg'), type: 'jpeg', quality: 92 });
    console.log('ok', s.id);
  }
  await b.close();
})();
