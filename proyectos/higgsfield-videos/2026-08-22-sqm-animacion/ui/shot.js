const { chromium } = require('playwright-core');
(async () => {
  const b = await chromium.launch({ args:['--no-sandbox','--font-render-hinting=none'], executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  for (const f of ['08-insight','10-bandeja','10-caso','11-valor','12-plataforma']) {
    await p.goto('file://' + __dirname + '/' + f + '.html');
    await p.waitForTimeout(400);
    await p.screenshot({ path: f + '.png' });
    console.log('shot', f);
  }
  await b.close();
})();
