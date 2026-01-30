document.addEventListener("DOMContentLoaded", () => {
    const navMenu = document.getElementById('nav-menu'),
        navToggle = document.getElementById('nav-toggle'),
        navClose = document.getElementById('nav-close'),
        themeButton = document.getElementById('theme-button'),
        header = document.getElementById('header');

    // Mobil menyu ochish
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            navMenu.classList.add('show-menu');
        });
    }

    // Mobil menyu yopish (X tugmasi)
    if (navClose && navMenu) {
        navClose.addEventListener('click', () => {
            navMenu.classList.remove('show-menu');
        });
    }

    // Link bosilganda yopish
    document.querySelectorAll('.nav__link').forEach(n => n.addEventListener('click', () => {
        navMenu.classList.remove('show-menu');
    }));

    // Tashqarini bosganda yopish
    document.addEventListener('click', (e) => {
        if (navMenu && !navMenu.contains(e.target) && !navToggle.contains(e.target)) {
            navMenu.classList.remove('show-menu');
        }
    });

    // Dark / Light Mode
    const selectedTheme = localStorage.getItem('selected-theme');
    if (selectedTheme) {
        document.documentElement.setAttribute('data-theme', selectedTheme);
    }

    if (themeButton) {
        themeButton.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('selected-theme', newTheme);
        });
    }

    // Scroll efekt (Header soya)
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scroll-header');
        } else {
            header.classList.remove('scroll-header');
        }
    });

    // AOS Init
    if (typeof AOS !== 'undefined') {
        AOS.init({duration: 800, once: true});
    }
});