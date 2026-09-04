// Render determinista: scrub(t) pinta el frame exacto. Se le pasan los nombres
// a renderizar por argv, para repartir el plan entre varios procesos en paralelo.
const { chromium } = require('playwright-core');
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const FPS = 25;
// el sandbox trae ffmpeg completo; en local viene por npm
let FF = 'ffmpeg';
try { FF = require('@ffmpeg-installer/ffmpeg').path; } catch (e) {}
const PLAN = require('./plan-' + process.env.SET + '.json');
(async () => {
  const pedidos = process.argv.slice(2);
  const jobs = pedidos.length ? PLAN.filter(p => pedidos.includes(p[0])) : PLAN;
  // el binario de Chromium vive en distinta ruta segun el entorno
  const roots = ['/ms-playwright', '/opt/pw-browsers'];
  let exe = process.env.CHROME_BIN;
  for (const r of roots) {
    if (exe || !fs.existsSync(r)) continue;
    for (const d of fs.readdirSync(r).filter(x => x.startsWith('chromium-')))
      for (const s of ['chrome-linux/chrome', 'chrome-linux64/chrome']) {
        const c = path.join(r, d, s);
        if (!exe && fs.existsSync(c)) exe = c;
      }
  }
  const b = await chromium.launch({ args: ['--no-sandbox', '--font-render-hinting=none'],
    executablePath: exe });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  fs.mkdirSync('clips', { recursive: true });
  for (const [name, dur] of jobs) {
    // reanudable: un clip ya rendido no se vuelve a hacer (el sandbox tiene lease corto)
    if (fs.existsSync('clips/' + name + '.mp4') && !process.env.FORCE) { console.log('salta', name); continue; }
    const tmp = fs.mkdtempSync(path.join(__dirname, '.fr-'));
    await p.goto('file://' + __dirname + '/' + name + '.html');
    await p.evaluate(async () => { await document.fonts.ready; return true; });
    await p.evaluate(d => window.buildAnim(d), dur);
    const N = Math.round(dur * FPS);
    for (let i = 0; i < N; i++) {
      await p.evaluate(([t, d]) => window.scrub(t, d), [i / FPS, dur]);
      await p.screenshot({ path: path.join(tmp, String(i).padStart(5, '0') + '.jpg'),
                           type: 'jpeg', quality: 94 });
    }
    execFileSync(FF, ['-y', '-loglevel', 'error', '-framerate', String(FPS),
      '-i', path.join(tmp, '%05d.jpg'), '-c:v', 'libx264', '-preset', 'slow',
      '-crf', '16', '-pix_fmt', 'yuv420p', 'clips/' + name + '.mp4']);
    fs.rmSync(tmp, { recursive: true, force: true });
    console.log('clip', name, dur + 's', N + 'f');
  }
  await b.close();
})();
