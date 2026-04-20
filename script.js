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
