const { chromium } = require('playwright-core');
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
// el ffmpeg de Playwright no trae decodificador de PNG; se usa el completo de npm
const FF = require('@ffmpeg-installer/ffmpeg').path;
const FPS = 25;

// pantalla -> segundos que ocupa en el montaje (ver montaje.md)
const PLAN = [
  ['plate', 4.0], ['04-dependencias', 13.3], ['04-pregunta', 13.2],
  ['06-criterios', 7.85], ['06-permisos', 7.85],
  ['07-registro', 5.9], ['07-patron', 5.95],
  ['08-insight', 12.7],
  ['09-mcp', 9.3], ['09-skill', 9.3],
  ['10-bandeja', 7.0], ['10-caso', 6.9],
  ['11-valor', 15.06], ['12-plataforma', 10.75],
];

// capas transparentes que se superponen a los planos generados
const OVER = [
  ['ov-01-sistemas', 8.75], ['ov-02-areas', 8.00], ['ov-03-brasil', 7.60],
  ['ov-05-capa', 6.60], ['ov-12-cierre', 7.00],
];

(async () => {
  const only = process.argv[2];
  const jobs = only ? PLAN.filter(p => p[0] === only) : PLAN;
  const b = await chromium.launch({ args: ['--no-sandbox', '--font-render-hinting=none'],
    executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  fs.mkdirSync('clips', { recursive: true });

  for (const [name, dur] of jobs) {
    const tmp = fs.mkdtempSync(path.join(__dirname, '.fr-'));
    await p.goto('file://' + __dirname + '/' + name + '.html');
    await p.evaluate// capas transparentes que se superponen a los planos generados
const OVER = [
  ['ov-01-sistemas', 8.75], ['ov-02-areas', 8.00], ['ov-03-brasil', 7.60],
  ['ov-05-capa', 6.60], ['ov-12-cierre', 7.00],
];

(async () => { await document.fonts.ready; return true; });
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
      '-crf', '16', '-pix_fmt', 'yuv420p', 'clips/' + name + '.mp4']);
    fs.rmSync(tmp, { recursive: true, force: true });
    console.log('clip', name, dur + 's', N + 'f');
  }
  // capas: se dejan como secuencia PNG con alpha, para superponer en el montaje
  if (!only) for (const [name, dur] of OVER) {
    const out = 'clips/' + name;
    fs.mkdirSync(out, { recursive: true });
    await p.goto('file://' + __dirname + '/' + name + '.html');
    await p.evaluate(async () => { await document.fonts.ready; return true; });
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
