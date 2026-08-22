/* Scrub determinista: no usa reloj real, se le pide un instante t y pinta ese frame.
   Garantiza que el render sea reproducible frame a frame. */
(function () {
  var SEL = '.dtop, .top, .panel, .card, .metrics .m, .rows .row, .lg, .pipe .col, .pipe .link, table tr, .kicker, h1, h2, .cmt, .act, .nav a, .lock';
  var items = [], DUR = 0.45, SHIFT = 0.9;

  function build(clipDur) {
    var els = Array.prototype.slice.call(document.querySelectorAll(SEL));
    // de-duplicar anidados: si un ancestro ya está en la lista, el hijo no anima aparte
    els = els.filter(function (e) {
      for (var p = e.parentElement; p; p = p.parentElement) if (els.indexOf(p) >= 0) return false;
      return true;
    });
    var n = els.length || 1;
    var step = Math.min(0.13, (0.5 * clipDur) / n);
    items = els.map(function (e, i) {
      return { el: e, t: 0.2 + i * step, hit: e.classList.contains('hit') };
    });
  }

  function clamp01(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }

  window.buildAnim = build;
  window.scrub = function (t, clipDur) {
    items.forEach(function (it) {
      var u = clamp01((t - it.t) / DUR);
      it.el.style.opacity = u;
      var y = (1 - u) * 10;
      var x = 0;
      if (it.hit) {                                  // 7.2: las filas del patrón calzan
        var v = clamp01((t - it.t - 0.25) / SHIFT);
        x = (1 - v) * -70;
      }
      it.el.style.transform = 'translate(' + x.toFixed(2) + 'px,' + y.toFixed(2) + 'px)';
    });
    // deriva lenta y lineal de toda la composición: el sistema pide movimientos lineales
    var s = 1 + 0.012 * clamp01(t / clipDur);
    document.body.style.transformOrigin = '50% 50%';
    document.body.style.transform = 'scale(' + s.toFixed(5) + ')';
  };
})();
