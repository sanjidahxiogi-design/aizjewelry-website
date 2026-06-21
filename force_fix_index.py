import os

base_dir = r"E:\AizJewelry_Project"
langs = ["", "de", "es", "fr", "jp", "kr", "pt"]

def force_fix_index_feedback(folder):
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path): return
    
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # 1. 注入绝对显示的 CSS
        css_inject = """
        <style>
            .thank-you-inline { display: none; text-align: center; padding: 60px 20px; background: #fff !important; }
            .thank-you-inline.active-feedback { display: block !important; visibility: visible !important; opacity: 1 !important; }
            .inquiry-form.hidden-form { display: none !important; }
        </style>
        """
        if css_inject not in html:
            html = html.replace('</head>', css_inject + '</head>')

        # 2. 注入强制反馈 JS（内联在页面底部，最保险）
        js_inject = """
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const forms = document.querySelectorAll('.inquiry-form');
                forms.forEach(f => {
                    f.onsubmit = function(e) {
                        e.preventDefault();
                        // 瞬间物理切换
                        this.classList.add('hidden-form');
                        const ty = this.parentElement.querySelector('.thank-you-inline');
                        if(ty) {
                            ty.classList.add('active-feedback');
                            ty.scrollIntoView({behavior: 'smooth', block: 'center'});
                        }
                        fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {
                            method: 'POST',
                            body: new FormData(this),
                            headers: { 'Accept': 'application/json' }
                        });
                    };
                });
            });
        </script>
        """
        if 'active-feedback' not in html:
            html = html.replace('</body>', js_inject + '</body>')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Index Fixed: {path}")

    except Exception as e:
        print(f"Err: {e}")

for l in langs:
    force_fix_index_feedback(l)
