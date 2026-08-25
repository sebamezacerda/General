const { chromium } = require('playwright-core');
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
// el ffmpeg de Playwright no trae decodificador de PNG; se usa el completo de npm
const FF = require('@ffmpeg-installer/ffmpeg').path;
const FPS = 25;

// pantalla -> segundos que ocupa en el montaje (ver montaje.md)
const PLAN = [
  ['plate', 3.2],
  ['v5-01', 13.6],
  ['v5-02', 15.0],
  ['v5-03', 13.7],
  ['v5-04', 15.8],
  ['v5-05', 15.4],
  ['v5-06', 14.9],
  ['v5-07', 11.3],
  ['v5-08', 15.5],
  ['v5-09', 13.6],
  ['v5-10', 14.0],
];

// capas transparentes que se superponen a los planos generados
const OVER = [];

(async () => {
  const only = process.argv[2];
  const jobs = only ? PLAN.filter(p => p[0] === only) : PLAN;
  const b = await chromium.launch({ args: ['--no-sandbox', '--font-render-hinting=none'],
    executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  // NOSUBS=1 rinde el mismo plan sin subtitulos, a su propio directorio
  const OUT = process.env.NOSUBS ? 'clips-nosubs' : 'clips';
  fs.mkdirSync(OUT, { recursive: true });

  for (const [name, dur] of jobs) {
    const tmp = fs.mkdtempSync(path.join(__dirname, '.fr-'));
    await p.goto('file://' + __dirname + '/' + name + '.html');
    await p.evaluate(async () => { await document.fonts.ready; return true; });
    if (process.env.NOSUBS) await p.evaluate(() => document.body.classList.add('nosubs'));
    await p.evaluate(d => window.buildAnim(d), dur);
    const N = Math.round(dur * FPS);
    console.log('  render', name, N, 'frames ->', tmp);
    for (let i = 0; i < N; i++) {
      await p.evaluate(([t, d]) => window.scrub(t, d), [i / FPS, dur]);
      await p.screenshot({ path: path.join(tmp, String(i).padStart(5, '0') + '.png') });
    }
    // este entorno solo trae el ffmpeg reducido de Playwright: VP8/WebM, sin H.264
    execFileSync(FF, ['-y', '-loglevel', 'error', '-framerate', String(FPS),
      '-i', path.join(tmp, '%05d.png'), '-c:v', 'libx264', '-preset', 'slow',
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
