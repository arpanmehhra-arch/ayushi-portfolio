// ==========================================================================
// AYUSHI KANOJIYA PORTFOLIO — core interactions
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {

  /* ---- mobile nav toggle ---- */
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      links.classList.toggle('is-open');
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => links.classList.remove('is-open'));
    });
  }

  /* ---- mark active nav link by pathname ---- */
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a[data-page]').forEach(a => {
    if (a.getAttribute('data-page') === path) a.classList.add('is-active');
  });

  /* ---- scroll reveal ---- */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('is-visible'));
  }

  /* ---- content rail active-state tracking (project pages) ---- */
  const railLinks = document.querySelectorAll('.content-rail a');
  const blocks = document.querySelectorAll('.block[id]');
  if (railLinks.length && blocks.length && 'IntersectionObserver' in window) {
    const railIO = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const id = entry.target.getAttribute('id');
        const link = document.querySelector(`.content-rail a[href="#${id}"]`);
        if (!link) return;
        if (entry.isIntersecting) {
          railLinks.forEach(l => l.classList.remove('is-active'));
          link.classList.add('is-active');
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });
    blocks.forEach(b => railIO.observe(b));
  }

  /* ---- PDF viewer (view-only; disables direct download/right-click on frame) ---- */
  const openers = document.querySelectorAll('[data-pdf-open]');
  const overlay = document.querySelector('.viewer-overlay');
  const closeBtn = document.querySelector('.viewer-close');
  const frameWrap = document.querySelector('.viewer-frame-wrap');
  const viewerTitle = document.querySelector('.viewer-bar strong');

  function openViewer(src, title) {
    if (!overlay || !frameWrap) return;
    frameWrap.innerHTML = '';
    const iframe = document.createElement('iframe');
    // #toolbar=0 hides the browser PDF toolbar (incl. its download icon) where supported
    iframe.src = src + '#toolbar=0&navpanes=0&scrollbar=1';
    iframe.setAttribute('title', title || 'Document viewer');
    frameWrap.appendChild(iframe);
    if (viewerTitle) viewerTitle.textContent = title || 'Document';
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }

  function closeViewer() {
    if (!overlay || !frameWrap) return;
    overlay.classList.remove('is-open');
    frameWrap.innerHTML = '';
    document.body.style.overflow = '';
  }

  openers.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const src = btn.getAttribute('data-pdf-open');
      const title = btn.getAttribute('data-pdf-title');
      openViewer(src, title);
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeViewer);
  if (overlay) {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) closeViewer();
    });
  }
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeViewer();
  });

  /* ---- deter casual right-click save on document imagery ---- */
  document.querySelectorAll('.no-save').forEach(el => {
    el.addEventListener('contextmenu', (e) => e.preventDefault());
  });

  /* ---- slideshow / carousel ----
     Works on any number of .slideshow instances on a page. Each needs:
     .slideshow > .slideshow-viewport > .slideshow-track > .slideshow-slide (N)
     plus [data-slide-prev], [data-slide-next] inside the viewport, and
     optional [data-slide-dots] / [data-slide-counter] containers. */
  document.querySelectorAll('[data-slideshow]').forEach((root) => {
    const track = root.querySelector('.slideshow-track');
    const slides = Array.from(root.querySelectorAll('.slideshow-slide'));
    const prevBtn = root.querySelector('[data-slide-prev]');
    const nextBtn = root.querySelector('[data-slide-next]');
    const dotsWrap = root.querySelector('[data-slide-dots]');
    const counter = root.querySelector('[data-slide-counter]');
    if (!track || slides.length === 0) return;

    let index = 0;
    const total = slides.length;

    // build dots
    let dots = [];
    if (dotsWrap) {
      dotsWrap.innerHTML = '';
      dots = slides.map((_, i) => {
        const b = document.createElement('button');
        b.setAttribute('aria-label', `Go to image ${i + 1}`);
        b.addEventListener('click', () => goTo(i));
        dotsWrap.appendChild(b);
        return b;
      });
    }

    function render() {
      track.style.transform = `translateX(-${index * 100}%)`;
      dots.forEach((d, i) => d.classList.toggle('is-active', i === index));
      if (counter) counter.textContent = `${index + 1} / ${total}`;
    }

    function goTo(i) {
      index = ((i % total) + total) % total;
      render();
    }

    if (prevBtn) prevBtn.addEventListener('click', () => goTo(index - 1));
    if (nextBtn) nextBtn.addEventListener('click', () => goTo(index + 1));

    // keyboard support when the slideshow has focus/hover
    root.setAttribute('tabindex', '0');
    root.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') goTo(index - 1);
      if (e.key === 'ArrowRight') goTo(index + 1);
    });

    // basic touch swipe support
    let touchStartX = null;
    const viewport = root.querySelector('.slideshow-viewport');
    if (viewport) {
      viewport.addEventListener('touchstart', (e) => {
        touchStartX = e.touches[0].clientX;
      }, { passive: true });
      viewport.addEventListener('touchend', (e) => {
        if (touchStartX === null) return;
        const dx = e.changedTouches[0].clientX - touchStartX;
        if (Math.abs(dx) > 40) goTo(dx > 0 ? index - 1 : index + 1);
        touchStartX = null;
      }, { passive: true });
    }

    render();
  });

});
