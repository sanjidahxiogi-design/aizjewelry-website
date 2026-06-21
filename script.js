// Language Switcher Toggle
document.querySelectorAll('.lang-switcher').forEach(switcher => {
    switcher.addEventListener('click', function(e) {
        if (window.innerWidth <= 992) {
            e.stopPropagation();
            this.classList.toggle('active');
        }
    });
});

document.addEventListener('click', function() {
    document.querySelectorAll('.lang-switcher').forEach(s => s.classList.remove('active'));
});

// Smooth Scroll
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        if (targetId.startsWith('#')) {
            e.preventDefault();
            const section = document.querySelector(targetId);
            if (section) {
                const headerOffset = 80;
                const elementPosition = section.getBoundingClientRect().top;
                window.scrollTo({
                    top: elementPosition + window.pageYOffset - headerOffset,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// --- GLOBAL FORM SUBMISSION HANDLER ---
document.querySelectorAll('.inquiry-form').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formContainer = this.parentElement;
        const submitBtn = this.querySelector('button[type="submit"]');
        const thankYouDiv = formContainer.querySelector('.thank-you-inline');

        // 1. Loading State
        submitBtn.disabled = true;
        submitBtn.textContent = 'SENDING...';

        // 2. AJAX Submit (Background)
        const formData = new FormData(this);
        const action = this.action.replace('formsubmit.co/', 'formsubmit.co/ajax/');
        
        fetch(action, {
            method: 'POST',
            body: formData,
            headers: { 'Accept': 'application/json' }
        });

        // 3. INSTANT SUCCESS FEEDBACK (Absolute Visibility)
        this.style.display = 'none';
        if (thankYouDiv) {
            thankYouDiv.style.display = 'block';
            thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    });
});

function updateFileName(input) {
    const fileName = input.files.length > 0 ? input.files[0].name : "";
    const display = input.parentElement.querySelector('.file-name-display');
    if (display && fileName) {
        display.textContent = fileName;
    }
}
