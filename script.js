document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Thank you for your inquiry. Our equestrian designers will get back to you shortly!');
    this.reset();
});

// Category Filtering Logic
document.querySelectorAll('.category-tab').forEach(tab => {
    tab.addEventListener('click', function() {
        const materialSection = this.closest('.material-section');
        const category = this.getAttribute('data-category');
        
        // Update active tab
        materialSection.querySelectorAll('.category-tab').forEach(t => t.classList.remove('active'));
        this.classList.add('active');
        
        // Filter products
        const products = materialSection.querySelectorAll('.product-card');
        products.forEach(product => {
            if (category === 'all' || product.getAttribute('data-category') === category) {
                product.classList.remove('hidden');
            } else {
                product.classList.add('hidden');
            }
        });
    });
});

// Smooth Scrolling for navigation
document.querySelectorAll('nav a, .product-category-nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId.startsWith('#')) {
            const section = document.querySelector(targetId);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});
