// Motor del corte v7 (pitch). Determinista: scrub(t) pinta el frame exacto.
// Diferencia con anim.js: cada elemento entra en el segundo en que la voz lo nombra.
// data-in / data-out van en FRACCION de la locucion (0..1) y se escalan por window.VO,
// que es la duracion real medida del audio de esa escena.
(function () {
  var items = [], nums = [], types = [], VO = 1, CLIP = 1;
  var IN = 0.26, OUT = 0.30, COUNT = 0.7, FADE_IN = 0.16, FADE_OUT = 0.26;

  function c01(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function ease(u) { return u * (2 - u); }

  function parseNum(s) {
    var m = String(s).match(/-?[\d.]*\d(?:,\d+)?/);
    if (!m) return null;
    var raw = m[0], val = parseFloat(raw.replace(/\./g, '').replace(',', '.'));
    if (isNaN(val)) return null;
    return { raw: raw, val: val, tpl: String(s), dec: (raw.split(',')[1] || '').length };
  }
  function fmt(v, q) {
    var s = q.dec ? v.toFixed(q.dec).replace('.', ',') : String(Math.round(v));
    var p = s.split(','), e = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return p[1] ? e + ',' + p[1] : e;
  }

  function build(clipDur) {
    CLIP = clipDur;
    VO = window.VO || clipDur;
    items = [];
    document.querySelectorAll('[data-in]').forEach(function (e) {
      var o = e.getAttribute('data-out');
      items.push({ el: e, t: parseFloat(e.getAttribute('data-in')) * VO,
                   o: o === null ? null : parseFloat(o) * VO });
    });
    nums = [];
    document.querySelectorAll('.count').forEach(function (e) {
      var p = parseNum(e.textContent); if (!p) return;
      var t = 0;
      for (var a = e; a; a = a.parentElement) {
        for (var i = 0; i < items.length; i++) if (items[i].el === a) { t = items[i].t; break; }
        if (t) break;
      }
      nums.push({ el: e, n: p, t: t });
    });
    types = [];
    document.querySelectorAll('.type').forEach(function (e) {
      types.push({ el: e, full: e.getAttribute('data-full') || e.textContent,
                   t0: parseFloat(e.getAttribute('data-t0') || '0') * VO,
                   dur: parseFloat(e.getAttribute('data-dur') || '0.2') * VO });
      e.textContent = '';
    });
    if (window.buildExtra) window.buildExtra(clipDur, VO);
  }

  window.buildAnim = build;
  window.scrub = function (t, clipDur) {
    items.forEach(function (it) {
      var u = ease(c01((t - it.t) / IN));
      var d = it.o === null ? 0 : c01((t - it.o) / OUT);
      it.el.style.opacity = u * (1 - d);
      it.el.style.transform = 'translateY(' + ((1 - u) * 16 - d * 22).toFixed(2) + 'px)';
    });
    nums.forEach(function (q) {
      var v = q.n.val * ease(c01((t - q.t) / COUNT));
      q.el.textContent = q.n.tpl.replace(q.n.raw, fmt(v, q.n));
    });
    types.forEach(function (q) {
      var u = c01((t - q.t0) / q.dur), k = Math.round(u * q.full.length);
      q.el.textContent = q.full.slice(0, k);
      q.el.classList.toggle('caret', u > 0 && u < 1);
    });
    if (window.scrubExtra) window.scrubExtra(t, clipDur, VO);
    // camara: un push corto y con destino, no un creep global
    var s = 1 + 0.014 * ease(c01(t / clipDur));
    var env = Math.min(c01(t / FADE_IN), c01((clipDur - t) / FADE_OUT));
    document.body.style.opacity = env;
    document.body.style.transformOrigin = '50% 50%';
    document.body.style.transform = 'scale(' + s.toFixed(5) + ')';
  };
})();
