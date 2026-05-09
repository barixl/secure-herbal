// ============================================================
// Secure Herbal Pest Control - Main JS
// ============================================================

// Sticky header
window.addEventListener('scroll', () => {
  const header = document.getElementById('header');
  if (header) {
    header.classList.toggle('scrolled', window.scrollY > 50);
  }
});

// Mobile hamburger menu
const hamburger = document.getElementById('hamburger');
const nav = document.getElementById('nav');
const overlay = document.createElement('div');
overlay.className = 'nav-overlay';
document.body.appendChild(overlay);

if (hamburger && nav) {
  hamburger.addEventListener('click', () => {
    nav.classList.toggle('open');
    overlay.classList.toggle('active');
    hamburger.innerHTML = nav.classList.contains('open')
      ? '<i class="fas fa-times"></i>'
      : '<i class="fas fa-bars"></i>';
    document.body.style.overflow = nav.classList.contains('open') ? 'hidden' : '';
  });

  overlay.addEventListener('click', () => {
    nav.classList.remove('open');
    overlay.classList.remove('active');
    hamburger.innerHTML = '<i class="fas fa-bars"></i>';
    document.body.style.overflow = '';
  });

  // Handle dropdowns on mobile
  const dropdownLinks = nav.querySelectorAll('.has-dropdown > a');
  dropdownLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        const dropdown = link.nextElementSibling;
        dropdown.classList.toggle('active');
        link.querySelector('i').classList.toggle('fa-chevron-up');
        link.querySelector('i').classList.toggle('fa-chevron-down');
      }
    });
  });

  // Close nav on direct link click (not dropdown toggle)
  nav.querySelectorAll('a:not(.has-dropdown > a)').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      overlay.classList.remove('active');
      hamburger.innerHTML = '<i class="fas fa-bars"></i>';
      document.body.style.overflow = '';
    });
  });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Set active nav link
const currentPath = window.location.pathname;
document.querySelectorAll('.nav a').forEach(link => {
  if (link.getAttribute('href') === currentPath) {
    link.classList.add('active');
  }
});

// Animate elements on scroll (intersection observer)
const animateOnScroll = () => {
  const elements = document.querySelectorAll(
    '.step-card, .service-card, .branch-card, .why-card, .stat-item, .testimonial-card'
  );
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, (entry.target.dataset.delay || 0) * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  elements.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    el.dataset.delay = i % 4;
    observer.observe(el);
  });
};

document.addEventListener('DOMContentLoaded', animateOnScroll);

// Counter animation for stat numbers
const animateCounters = () => {
  const counters = document.querySelectorAll('.stat-num');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const text = el.innerText;
        const num = parseInt(text.replace(/\D/g, ''));
        const suffix = text.replace(/[\d,]/g, '');
        if (num) {
          let count = 0;
          const step = Math.ceil(num / 50);
          const timer = setInterval(() => {
            count = Math.min(count + step, num);
            el.innerHTML = count.toLocaleString('en-IN') + suffix;
            if (count >= num) clearInterval(timer);
          }, 30);
        }
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.5 });
  counters.forEach(c => observer.observe(c));
};

document.addEventListener('DOMContentLoaded', animateCounters);

// FAQ accordion — works on all pages (home + service/location detail pages)
function toggleFaq(el) {
  const item = el.parentElement;
  const isOpen = item.classList.contains('open');
  document.querySelectorAll('.faq-item').forEach(f => {
    f.classList.remove('open');
    const a = f.querySelector('.faq-a');
    if (a) a.style.maxHeight = '0';
  });
  if (!isOpen) {
    item.classList.add('open');
    const a = item.querySelector('.faq-a');
    if (a) a.style.maxHeight = a.scrollHeight + 'px';
  }
}
