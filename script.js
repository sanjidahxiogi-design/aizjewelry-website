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

// Handle Form Submission via AJAX
document.querySelectorAll('.inquiry-form').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formContainer = this.parentElement;
        const formData = new FormData(this);
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.textContent;
        
        // Show loading state
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';

        fetch(this.action, {
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                // Hide Form and show Thank You message
                this.style.display = 'none';
                const thankYouDiv = formContainer.querySelector('.thank-you-inline');
                if (thankYouDiv) {
                    thankYouDiv.style.display = 'block';
                    // Scroll to message
                    thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
                gtag('event', 'form_submission_success');
            } else {
                throw new Error('Form submission failed');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Sorry, there was an error sending your message. Please try again or contact us directly via email.');
            submitBtn.disabled = false;
            submitBtn.textContent = originalBtnText;
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
