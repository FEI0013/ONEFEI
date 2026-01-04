(() => {
  const isFormField = (node) => {
    if (!node || !node.closest) return false;
    return node.closest('input, textarea, select, [contenteditable="true"]');
  };

  const block = (event) => {
    if (isFormField(event.target)) {
      return;
    }
    event.preventDefault();
  };

  document.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('no-copy');
  });

  document.addEventListener('contextmenu', block);
  document.addEventListener('copy', block);
  document.addEventListener('cut', block);
  document.addEventListener('selectstart', block);

  document.addEventListener('dragstart', (event) => {
    const target = event.target;
    if (!target || !target.tagName) return;
    const tag = target.tagName.toUpperCase();
    if (tag === 'IMG' || tag === 'VIDEO') {
      event.preventDefault();
    }
  });

  document.addEventListener('keydown', (event) => {
    const key = (event.key || '').toLowerCase();
    const isMac = /MAC/i.test(navigator.platform || '');
    const cmdOrCtrl = isMac ? event.metaKey : event.ctrlKey;
    if (!cmdOrCtrl) return;
    if (key === 's' || key === 'u' || key === 'c' || key === 'p') {
      event.preventDefault();
    }
  });
})();
