const { chromium } = require('playwright-core');
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
// el ffmpeg de Playwright no trae decodificador de PNG; se usa el completo de npm
const FF = require('@ffmpeg-installer/ffmpeg').path;
const FPS = 25;

// pantalla -> segundos que ocupa en el montaje (ver montaje.md)
// el plan vive en plan-<set>.json; SET elige la version (v5 por defecto)
const PLAN = require('./plan-' + (process.env.SET || 'v5') + '.json');

// capas transparentes que se superponen a los planos generados
const OVER = [];

(async () => {
  const only = process.argv[2];
  const jobs = only ? PLAN.filter(p => p[0] === only) : PLAN;
  // el binario de Chromium vive en distinta ruta segun el entorno (aca chrome-linux,
  // en el sandbox de Higgsfield chrome-linux64): se busca en vez de fijarlo
  const roots = ['/opt/pw-browsers', '/ms-playwright'];
  let exe = process.env.CHROME_BIN;
  for (const r of roots) {
    if (exe || !fs.existsSync(r)) continue;
    for (const d of fs.readdirSync(r).filter(x => x.startsWith('chromium-')))
      for (const sub of ['chrome-linux/chrome', 'chrome-linux64/chrome']) {
        const c = path.join(r, d, sub);
        if (!exe && fs.existsSync(c)) exe = c;
      }
  }
  if (!exe) throw new Error('no se encontro el binario de Chromium');
  console.log('chromium', exe);
  const b = await chromium.launch({ args: ['--no-sandbox', '--font-render-hinting=none'],
    executablePath: exe });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  // NOSUBS=1 rinde el mismo plan sin subtitulos, a su propio directorio
  const OUT = process.env.NOSUBS ? 'clips-nosubs' : 'clips';
  fs.mkdirSync(OUT, { recursive: true });

  for (const [name, dur] of jobs) {
    // reanudable: un clip ya rendido no se vuelve a hacer (el sandbox tiene lease corto)
    if (fs.existsSync(OUT + '/' + name + '.mp4') && !process.env.FORCE) {
      console.log('salta', name); continue;
    }
    const tmp = fs.mkdtempSync(path.join(__dirname, '.fr-'));
    await p.goto('file://' + __dirname + '/' + name + '.html');
    await p.evaluate(async () => { await document.fonts.ready; return true; });
    if (process.env.NOSUBS) await p.evaluate(() => document.body.classList.add('nosubs'));
    await p.evaluate(d => window.buildAnim(d), dur);
    const N = Math.round(dur * FPS);
    console.log('  render', name, N, 'frames ->', tmp);
    for (let i = 0; i < N; i++) {
      await p.evaluate(([t, d]) => window.scrub(t, d), [i / FPS, dur]);
      await p.screenshot({ path: path.join(tmp, String(i).padStart(5, '0') + '.jpg'),
                           type: 'jpeg', quality: 94 });
    }
    // este entorno solo trae el ffmpeg reducido de Playwright: VP8/WebM, sin H.264
    execFileSync(FF, ['-y', '-loglevel', 'error', '-framerate', String(FPS),
      '-i', path.join(tmp, '%05d.jpg'), '-c:v', 'libx264', '-preset', 'slow',
      '-crf', '16', '-pix_fmt', 'yuv420p', OUT + '/' + name + '.mp4']);
    fs.rmSync(tmp, { recursive: true, force: true });
    console.log('clip', name, dur + 's', N + 'f');
  }
  // capas: se dejan como secuencia PNG con alpha, para superponer en el montaje
  if (!only) for (const [name, dur] of OVER) {
    const out = OUT + '/' + name;
    fs.mkdirSync(out, { recursive: true });
    await p.goto('file://' + __dirname + '/' + name + '.html');
    await p.evaluate(async () => { await document.fonts.ready; return true; });
    if (process.env.NOSUBS) await p.evaluate(() => document.body.classList.add('nosubs'));
    await p.evaluate(d => window.buildAnim(d), dur);
    const N = Math.round(dur * FPS);
    for (let i = 0; i < N; i++) {
      await p.evaluate(([t, d]) => window.scrub(t, d), [i / FPS, dur]);
      await p.screenshot({ path: path.join(out, String(i).padStart(5, '0') + '.png'), omitBackground: true });
    }
    console.log('capa', name, dur + 's', N + 'f');
  }
  await b.close();
})();
