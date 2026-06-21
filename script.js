document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.inquiry-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            // 1. 隐藏表单
            this.style.display = 'none';
            // 2. 隐藏独立的返回链接
            const staticBack = document.getElementById('back-home-bottom');
            if(staticBack) staticBack.style.display = 'none';
            // 3. 显示感谢模块（它现在在卡片内）
            const ty = document.querySelector('.thank-you-inline');
            if (ty) {
                ty.style.display = 'block';
                ty.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
            // 4. 后台发送
            fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {
                method: 'POST',
                body: new FormData(this),
                headers: { 'Accept': 'application/json' }
            });
        });
    }
});
