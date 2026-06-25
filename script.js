document.addEventListener('DOMContentLoaded', function() {
    // --- 1. 产品分类切换逻辑 (修复点击无效问题) ---
    const categoryContainers = document.querySelectorAll('.material-section');
    
    categoryContainers.forEach(container => {
        const tabs = container.querySelectorAll('.category-tab');
        const cards = container.querySelectorAll('.product-card');

        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const category = tab.getAttribute('data-category');

                // 更新按钮激活状态
                tabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');

                // 执行分类过滤
                cards.forEach(card => {
                    const cardCategory = card.getAttribute('data-category');
                    if (category === 'all' || cardCategory === category) {
                        card.style.display = 'block';
                        card.style.opacity = '0';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transition = 'opacity 0.4s ease';
                        }, 10);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    });

    // --- 2. 统一处理全站所有询盘表单 (首页底部和独立页) ---
    // --- 2. Handle inquiry forms with one FormSubmit request ---
    document.querySelectorAll('.inquiry-form').forEach(form => {
        form.addEventListener('submit', function(e) {
            if (this.dataset.nativeSubmit === 'true') {
                return;
            }

            if (this.dataset.submitting === 'true') {
                e.preventDefault();
                return;
            }
            this.dataset.submitting = 'true';

            const submitButton = this.querySelector('[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.textContent = 'Sending...';
            }

            // 找感谢 div：优先用 data-thankyou-target，否则找同级 .thank-you-inline
            const targetId = this.getAttribute('data-thankyou-target');
            const thankYouDiv = targetId
                ? document.getElementById(targetId)
                : this.parentElement.querySelector('.thank-you-inline');

            // 用 FormData 直接从表单构建，确保附件包含在内
            form.style.setProperty('display', 'none', 'important');
            if (thankYouDiv) {
                const displayMode = targetId ? 'flex' : 'block';
                thankYouDiv.style.setProperty('display', displayMode, 'important');
                thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }

            if (typeof gtag !== 'undefined') {
                gtag('event', 'form_submission_web', {
                    'event_category': 'Inquiry',
                    'event_label': 'FormSubmit'
                });
            }

            if (this.dataset.nativeSubmit === 'true') {
                return;
            }

            e.preventDefault();
            const formData = new FormData(this);

            fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' }
            }).then(function() {
                // 成功后显示感谢界面
                form.style.setProperty('display', 'none', 'important');
                form.style.setProperty('display', 'none', 'important');
                if (thankYouDiv) {
                    thankYouDiv.style.setProperty('display', 'flex', 'important');
                    thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'form_submission_web', {
                        'event_category': 'Inquiry',
                        'event_label': 'FormSubmit'
                    });
                }
            }).catch(function() {
                // 失败时恢复按钮
                form.dataset.submitting = 'false';
                if (submitButton) {
                    submitButton.disabled = false;
                    submitButton.textContent = 'Inquire Now';
                }
                alert('Something went wrong. Please try again or email us directly at sales@aizjewelry.com');
            });
        });
    });

    // Legacy handler disabled after the footer form moved to the single-send handler above.
    document.querySelectorAll('.inquiry-form-legacy-disabled').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const formContainer = this.parentElement;
            const thankYouDiv = formContainer.querySelector('.thank-you-inline');

            // 瞬间视觉反馈
            this.style.setProperty('display', 'none', 'important');
            if (thankYouDiv) {
                thankYouDiv.style.setProperty('display', 'block', 'important');
                thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }

            // 后台异步发送
            const formData = new FormData(this);
        });
    });

    // --- 3. 语言切换器逻辑 ---
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
});

// --- 4. 文件上传显示辅助函数 ---
function updateFileName(input) {
    const fileName = input.files.length > 0 ? input.files[0].name : "";
    const display = input.parentElement.querySelector('.file-name-display');
    if (display && fileName) { display.textContent = fileName; }
}
