/* Scrub determinista: se le pide un instante t y pinta ese frame.
   v3 — el chrome (rail, nav, cabecera) esta desde el frame 0; solo anima el
   contenido. Los numeros cuentan desde que entra su bloque. */
(function () {
  var SEL = '.panel, .card, .metrics .m, .rows .row, .lg, .pipe .col, .pipe .link, table tr,'
          + ' h1, h2, .cmt, .act, .kicker, .ovcard, .ovcard .r, .ovlog .l, .ovtitle, .bignum';
  var CHROME = '.rail, .top, .dtop';           // interfaz: no aparece, ya esta
  var items = [], nums = [], DUR = 0.30, SHIFT = 0.75, COUNT = 1.1;

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
    if (n.miles) {
      var p = s.split(','), e = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
      s = p.length > 1 ? e + ',' + p[1] : e;
    }
    return s;
  }
  function inChrome(e) {
    for (var p = e; p; p = p.parentElement) if (p.matches && p.matches(CHROME)) return true;
    return false;
  }

  function build(clipDur) {
    var els = Array.prototype.slice.call(document.querySelectorAll(SEL)).filter(function (e) {
      return !inChrome(e);
    });
    els = els.filter(function (e) {                 // si un ancestro ya anima, el hijo no
      for (var p = e.parentElement; p; p = p.parentElement) if (els.indexOf(p) >= 0) return false;
      return true;
    });
    var n = els.length || 1;
    var t0 = clipDur * 0.10, t1 = clipDur * 0.80;
    // pocos elementos no deben quedar separados 4s entre si, ni muchos amontonarse
    var step = Math.min((t1 - t0) / n, 1.15);
    items = els.map(function (e, i) {
      return { el: e, t: t0 + i * step, hit: e.classList.contains('hit') };
    });
    nums = [];
    document.querySelectorAll('.m .v, .bignum, .num.count').forEach(function (e) {
      var p = parseNum(e.textContent);
      if (!p) return;
      var t = 0;
      for (var a = e; a; a = a.parentElement) {
        var f = items.filter(function (it) { return it.el === a; })[0];
        if (f) { t = f.t; break; }
      }
      nums.push({ el: e, n: p, t: t });
    });
  }
  function c01(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }

  window.buildAnim = build;
  window.scrub = function (t, clipDur) {
    items.forEach(function (it) {
      var u = c01((t - it.t) / DUR);
      it.el.style.opacity = u;
      var y = (1 - u) * 12, x = 0;
      if (it.hit) x = (1 - c01((t - it.t - 0.2) / SHIFT)) * -70;
      it.el.style.transform = 'translate(' + x.toFixed(2) + 'px,' + y.toFixed(2) + 'px)';
    });
    nums.forEach(function (q) {
      var u = c01((t - q.t) / COUNT), v = q.n.val * (u * (2 - u));
      q.el.textContent = q.n.tpl.replace(q.n.raw, fmt(v, q.n));
    });
    var on = (t % 1.02) < 0.59;
    document.querySelectorAll('.wm i, .nav a i').forEach(function (e) { e.style.opacity = on ? 1 : 0; });
    var s = 1 + 0.016 * c01(t / clipDur);
    document.body.style.transformOrigin = '50% 50%';
    document.body.style.transform = 'scale(' + s.toFixed(5) + ')';
  };
})();
