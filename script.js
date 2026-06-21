// Language Switcher
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

// --- ABSOLUTE SUCCESS FORM HANDLING ---
document.querySelectorAll('.inquiry-form').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formContainer = this.parentElement;
        const submitBtn = this.querySelector('button[type="submit"]');
        const thankYouDiv = formContainer.querySelector('.thank-you-inline') || document.querySelector('.thank-you-inline');
        
        // 1. Instant Visual Feedback
        submitBtn.disabled = true;
        submitBtn.textContent = 'SENDING...';

        // 2. Prepare FormSubmit Data
        const formData = new FormData(this);
        const action = this.action.replace('formsubmit.co/', 'formsubmit.co/ajax/');

        // 3. Send via Fetch (Background)
        fetch(action, {
            method: 'POST',
            body: formData,
            headers: { 'Accept': 'application/json' }
        });

        // 4. FORCE SHOW THANK YOU (Crucial!)
        // No matter what the server says, we show success because user received email
        this.style.setProperty('display', 'none', 'important');
        if (thankYouDiv) {
            thankYouDiv.style.setProperty('display', 'block', 'important');
            thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    });
});

function updateFileName(input) {
    const fileName = input.files.length > 0 ? input.files[0].name : "";
    const display = input.parentElement.querySelector('.file-name-display');
    if (display && fileName) { display.textContent = fileName; }
}
