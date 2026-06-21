document.addEventListener('DOMContentLoaded', function() {
    // 统一处理全站所有询盘表单 (首页底部和独立页)
    document.querySelectorAll('.inquiry-form').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formContainer = this.parentElement;
            const thankYouDiv = formContainer.querySelector('.thank-you-inline');

            // 1. 瞬间视觉反馈 (最重要：言行一致)
            this.style.setProperty('display', 'none', 'important');
            if (thankYouDiv) {
                thankYouDiv.style.setProperty('display', 'block', 'important');
                thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }

            // 2. 后台悄悄发送
            const formData = new FormData(this);
            fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' }
            });
        });
    });
});

function updateFileName(input) {
    const fileName = input.files.length > 0 ? input.files[0].name : "";
    const display = input.parentElement.querySelector('.file-name-display');
    if (display && fileName) { display.textContent = fileName; }
}
