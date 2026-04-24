document.addEventListener('DOMContentLoaded', () => {

    // ── Navbar scroll shadow ──
    const nav = document.querySelector('nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 30) {
                nav.classList.add('shadow-sm');
            } else {
                nav.classList.remove('shadow-sm');
            }
        }, { passive: true });
    }

    // ── Theme init ──
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
    }

    // ── Smooth scroll for anchor links ──
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ── Intersection Observer: fade-up on scroll ──
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.08, rootMargin: '0px 0px -60px 0px' });

    document.querySelectorAll('.project-card, .skill-card, .about-card, .stat-box').forEach(el => {
        observer.observe(el);
    });

    // ── Contact form async submit ──
    const contactForm = document.querySelector('form[action*="web3forms"]');
    if (contactForm) {
        contactForm.addEventListener('submit', async function (e) {
            e.preventDefault();
            const btn = this.querySelector('button[type="submit"]');
            const original = btn.innerHTML;

            btn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2 text-xs"></i>Sending...';
            btn.disabled = true;

            try {
                const res = await fetch(this.action, { method: 'POST', body: new FormData(this) });
                if (res.ok) {
                    btn.innerHTML = '<i class="fas fa-check mr-2 text-xs"></i>Sent!';
                    btn.classList.add('bg-green-600');
                    btn.classList.remove('bg-accent');
                    this.reset();
                    setTimeout(() => {
                        btn.innerHTML = original;
                        btn.classList.remove('bg-green-600');
                        btn.classList.add('bg-accent');
                        btn.disabled = false;
                    }, 3000);
                } else throw new Error();
            } catch {
                btn.innerHTML = '<i class="fas fa-times mr-2 text-xs"></i>Failed. Try again.';
                btn.classList.add('bg-red-500');
                btn.classList.remove('bg-accent');
                setTimeout(() => {
                    btn.innerHTML = original;
                    btn.classList.remove('bg-red-500');
                    btn.classList.add('bg-accent');
                    btn.disabled = false;
                }, 3000);
            }
        });
    }

    // ── Load complete ──
    window.addEventListener('load', () => {
        document.body.classList.add('loaded');
    });

    // ── ESC key to close mobile menu ──
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const menu = document.getElementById('mobile-menu');
            if (menu && menu.style.right === '0px') {
                toggleMenu();
            }
        }
    });
});

// ── Theme toggle ──
function toggleTheme() {
    document.documentElement.classList.toggle('dark');
    localStorage.theme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
}

// ── Mobile menu toggle ──
function toggleMenu() {
    const menu = document.getElementById('mobile-menu');
    if (!menu) return;
    const isOpen = menu.style.right === '0px';
    menu.style.right = isOpen ? '-288px' : '0px';
    document.body.style.overflow = isOpen ? 'auto' : 'hidden';

    // Backdrop
    let backdrop = document.getElementById('menu-backdrop');
    if (!isOpen) {
        if (!backdrop) {
            backdrop = document.createElement('div');
            backdrop.id = 'menu-backdrop';
            backdrop.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.4);z-index:40;backdrop-filter:blur(2px);opacity:0;transition:opacity 0.3s ease;';
            backdrop.onclick = toggleMenu;
            document.body.appendChild(backdrop);
        }
        setTimeout(() => backdrop.style.opacity = '1', 10);
    } else {
        if (backdrop) {
            backdrop.style.opacity = '0';
            setTimeout(() => backdrop.remove(), 300);
        }
    }
}

// ── Scroll-reveal (lightweight) ──
const reveal = () => {
    document.querySelectorAll('.project-card, .skill-card').forEach(el => {
        const top = el.getBoundingClientRect().top;
        if (top < window.innerHeight - 80) {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }
    });
};

// Debounce
let scrollTimer;
window.addEventListener('scroll', () => {
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(reveal, 10);
}, { passive: true });

window.addEventListener('load', reveal);
