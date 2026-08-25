/* Scrub determinista: se le pide un instante t y pinta ese frame.
   v4 — agrega subtitulos quemados, tipeo caracter por caracter y envolvente de
   fundido por escena (entra y sale sobre el fondo, sin cross-dissolve entre planos). */
(function () {
  var SEL = '.panel, .card, .metrics .m, .rows .row, .lg, .pipe .col, .pipe .link, table tr,'
          + ' h1, h2, .cmt, .act, .kicker, .ovcard, .ovcard .r, .ovlog .l, .ovtitle, .bignum,'
          + ' .chip, .kv .c, .tbl tr, .bubble, .step';
  var CHROME = '.rail, .top, .dtop, .subs';
  var items = [], nums = [], types = [], DUR = 0.22, COUNT = 0.75;
  var FADE_IN = 0.20, FADE_OUT = 0.35;

  function parseNum(txt) {
    var m = txt.match(/(\d[\d.]*(?:,\d+)?)/);
    if (!m) return null;
    var raw = m[1], miles = raw.indexOf('.') >= 0, dec = 0, c = raw.indexOf(',');
    if (c >= 0) dec = raw.length - c - 1;
    var v = parseFloat(raw.replace(/\./g, '').replace(',', '.'));
    return isNaN(v) ? null : { val: v, dec: dec, miles: miles, raw: raw, tpl: txt };
  }
  function fmt(v, n) {
    var s = v.toFixed(n.dec).replace('.', ',');
    if (n.miles) { var p = s.split(','), e = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
      s = p.length > 1 ? e + ',' + p[1] : e; }
    return s;
  }
  function inChrome(e) {
    for (var p = e; p; p = p.parentElement) if (p.matches && p.matches(CHROME)) return true;
    return false;
  }
  function c01(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }

  function build(clipDur) {
    var els = Array.prototype.slice.call(document.querySelectorAll(SEL))
      .filter(function (e) { return !inChrome(e); });
    els = els.filter(function (e) {
      for (var p = e.parentElement; p; p = p.parentElement) if (els.indexOf(p) >= 0) return false;
      return true;
    });
    var n = els.length || 1;
    // las entradas se reparten por casi toda la ventana: mientras la voz calla,
    // en pantalla todavia esta llegando algo. El ultimo 14 % queda para leer.
    var t0 = clipDur * 0.04, t1 = clipDur * 0.86;
    var step = Math.max((t1 - t0) / n, 0.25);
    items = els.map(function (e, i) { return { el: e, t: t0 + i * step }; });

    nums = [];
    document.querySelectorAll('.m .v, .bignum, .num.count').forEach(function (e) {
      var p = parseNum(e.textContent); if (!p) return;
      var t = 0;
      for (var a = e; a; a = a.parentElement) {
        var f = items.filter(function (it) { return it.el === a; })[0];
        if (f) { t = f.t; break; }
      }
      nums.push({ el: e, n: p, t: t });
    });

    // tipeo: se escribe como en un chat, no aparece de golpe
    types = [];
    document.querySelectorAll('.type').forEach(function (e) {
      types.push({ el: e, full: e.getAttribute('data-full') || e.textContent,
                   t0: parseFloat(e.getAttribute('data-t0') || '0'),
                   dur: parseFloat(e.getAttribute('data-dur') || '2') });
      e.textContent = '';
    });
  }

  window.buildAnim = build;
  window.scrub = function (t, clipDur) {
    items.forEach(function (it) {
      var u = c01((t - it.t) / DUR);
      it.el.style.opacity = u;
      it.el.style.transform = 'translateY(' + ((1 - u) * 10).toFixed(2) + 'px)';
    });
    nums.forEach(function (q) {
      var u = c01((t - q.t) / COUNT), v = q.n.val * (u * (2 - u));
      q.el.textContent = q.n.tpl.replace(q.n.raw, fmt(v, q.n));
    });
    types.forEach(function (q) {
      var u = c01((t - q.t0) / q.dur);
      var k = Math.round(u * q.full.length);
      q.el.textContent = q.full.slice(0, k);
      q.el.classList.toggle('caret', u > 0 && u < 1);
    });
    // subtitulos quemados
    if (window.SUBS) {
      var cur = '';
      for (var i = 0; i < window.SUBS.length; i++)
        if (t >= window.SUBS[i][0] && t < window.SUBS[i][1]) { cur = window.SUBS[i][2]; break; }
      var box = document.querySelector('.subs');
      if (box) { box.textContent = cur; box.style.opacity = cur ? 1 : 0; }
    }
    var on = (t % 1.02) < 0.59;
    document.querySelectorAll('.wm i, .nav a i').forEach(function (e) { e.style.opacity = on ? 1 : 0; });
    // envolvente de escena: entra y sale sobre el fondo. El corte nunca es entre dos imagenes.
    var env = Math.min(c01(t / FADE_IN), c01((clipDur - t) / FADE_OUT));
    var s = 1 + 0.022 * c01(t / clipDur);
    document.body.style.opacity = env;
    document.body.style.transformOrigin = '50% 50%';
    document.body.style.transform = 'scale(' + s.toFixed(5) + ')';
  };
})();
