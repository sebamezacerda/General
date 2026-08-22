/* Scrub determinista: se le pide un instante t y pinta ese frame.
   v2 — el movimiento se reparte por casi toda la ventana, los numeros cuentan,
   y siempre queda algo vivo en pantalla. */
(function () {
  var SEL = '.dtop, .top, .panel, .card, .metrics .m, .rows .row, .lg, .pipe .col, .pipe .link, table tr, .kicker, h1, h2, .cmt, .act, .nav a, .lock';
  var items = [], nums = [], DUR = 0.30, SHIFT = 0.75;

  // "US$ 1,34 M" -> {val:1.34, dec:2, miles:false}
  function parseNum(txt) {
    var m = txt.match(/(\d[\d.]*(?:,\d+)?)/);
    if (!m) return null;
    var raw = m[1], miles = raw.indexOf('.') >= 0, dec = 0;
    var c = raw.indexOf(',');
    if (c >= 0) dec = raw.length - c - 1;
    var v = parseFloat(raw.replace(/\./g, '').replace(',', '.'));
    if (isNaN(v)) return null;
    return { val: v, dec: dec, miles: miles, raw: raw, tpl: txt };
  }
  function fmt(v, n) {
    var s = v.toFixed(n.dec).replace('.', ',');
    if (n.miles) {
      var p = s.split(','), e = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
      s = p.length > 1 ? e + ',' + p[1] : e;
    }
    return s;
  }

  function build(clipDur) {
    var els = Array.prototype.slice.call(document.querySelectorAll(SEL));
    els = els.filter(function (e) {
      for (var p = e.parentElement; p; p = p.parentElement) if (els.indexOf(p) >= 0) return false;
      return true;
    });
    var n = els.length || 1;
    // el reparto ocupa del 12% al 78% de la ventana: nunca hay un tramo largo sin nada
    var t0 = clipDur * 0.12, t1 = clipDur * 0.78, step = (t1 - t0) / n;
    items = els.map(function (e, i) {
      return { el: e, t: t0 + i * step, hit: e.classList.contains('hit') };
    });
    // contadores
    nums = [];
    document.querySelectorAll('.m .v, .num, .bignum').forEach(function (e) {
      var p = parseNum(e.textContent);
      if (!p) return;
      var owner = e;
      for (var a = e.parentElement; a; a = a.parentElement) {
        for (var k = 0; k < items.length; k++) if (items[k].el === a || items[k].el === e) { owner = items[k]; break; }
        if (owner !== e) break;
      }
      nums.push({ el: e, n: p, t: (owner.t !== undefined ? owner.t : 0) });
      e.setAttribute('data-tpl', p.tpl);
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
    // los numeros cuentan durante 1,1s desde que entra su bloque
    nums.forEach(function (q) {
      var u = c01((t - q.t) / 1.1);
      var v = q.n.val * (u * (2 - u));            // desaceleracion suave, sin rebote
      q.el.textContent = q.n.tpl.replace(q.n.raw, fmt(v, q.n));
    });
    // el guion bajo del wordmark y de la nav pestañea de verdad (vblink, 1.02s)
    var on = (t % 1.02) < 0.59;
    document.querySelectorAll('.wm i, .nav a i').forEach(function (e) { e.style.opacity = on ? 1 : 0; });
    // deriva lenta y lineal
    var s = 1 + 0.016 * c01(t / clipDur);
    document.body.style.transformOrigin = '50% 50%';
    document.body.style.transform = 'scale(' + s.toFixed(5) + ')';
  };
})();
