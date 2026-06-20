// Language Switcher Toggle for Mobile
document.querySelectorAll('.lang-switcher').forEach(switcher => {
    switcher.addEventListener('click', function(e) {
        if (window.innerWidth <= 992) {
            e.stopPropagation();
            this.classList.toggle('active');
        }
    });
});

// Close dropdown when clicking outside
document.addEventListener('click', function() {
    document.querySelectorAll('.lang-switcher').forEach(s => s.classList.remove('active'));
});

// Category Filtering Logic
document.querySelectorAll('.category-tab').forEach(tab => {
    tab.addEventListener('click', function() {
        const materialSection = this.closest('.material-section');
        const category = this.getAttribute('data-category');
        
        // Update active tab style
        materialSection.querySelectorAll('.category-tab').forEach(t => t.classList.remove('active'));
        this.classList.add('active');
        
        // Filter products with a slight fade effect
        const products = materialSection.querySelectorAll('.product-card');
        products.forEach(product => {
            product.style.opacity = '0';
            setTimeout(() => {
                if (category === 'all' || product.getAttribute('data-category') === category) {
                    product.classList.remove('hidden');
                    setTimeout(() => { product.style.opacity = '1'; }, 50);
                } else {
                    product.classList.add('hidden');
                }
            }, 200);
        });
    });
});

// Smooth Scrolling for navigation
document.querySelectorAll('nav a, .product-category-nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        if (targetId.startsWith('#')) {
            e.preventDefault();
            const section = document.querySelector(targetId);
            if (section) {
                const headerOffset = 80;
                const elementPosition = section.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// GA4 Click Tracking for Navigation & Global Elements
document.addEventListener('DOMContentLoaded', function() {
    // Track Logo clicks
    document.querySelector('.logo').addEventListener('click', function() {
        gtag('event', 'nav_logo_click');
    });

    // Track Material Category Tab clicks
    document.querySelectorAll('.category-tab').forEach(tab => {
        tab.addEventListener('click', function() {
            gtag('event', 'category_tab_view', {
                'material': this.closest('.material-section').id,
                'category': this.getAttribute('data-category')
            });
        });
    });

    // Track Footer/Header contact clicks
    document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
        link.addEventListener('click', function() {
            gtag('event', 'contact_email_click', {
                'event_label': this.href
            });
        });
    });
});

// Update File Name Display on Upload
function updateFileName(input) {
    const fileName = input.files.length > 0 ? input.files[0].name : "";
    const display = input.parentElement.querySelector('.file-name-display');
    if (display && fileName) {
        display.textContent = fileName;
    }
}
