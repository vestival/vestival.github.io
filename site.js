// Theme toggle and font zoom, shared by every page.
(function () {
  const html = document.documentElement;
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
  };

  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  html.setAttribute('data-theme', store.get('theme') || (prefersDark ? 'dark' : 'light'));
  document.getElementById('themeToggle').addEventListener('click', () => {
    const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    store.set('theme', next);
  });

  // Font size: 100% to 300% in 25% steps
  const ZOOM = [1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3];
  const down = document.getElementById('fontDown');
  const up = document.getElementById('fontUp');
  let i = Math.min(Math.max(parseInt(store.get('font-level') || '0', 10) || 0, 0), ZOOM.length - 1);
  function apply() {
    document.body.style.zoom = ZOOM[i];
    store.set('font-level', i);
    down.disabled = i === 0;
    up.disabled = i === ZOOM.length - 1;
  }
  apply();
  down.addEventListener('click', () => { if (i > 0) { i--; apply(); } });
  up.addEventListener('click', () => { if (i < ZOOM.length - 1) { i++; apply(); } });
})();
