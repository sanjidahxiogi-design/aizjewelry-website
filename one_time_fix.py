import os
import re

base_dir = r"E:\AizJewelry_Project"
langs = ["", "de", "es", "fr", "jp", "kr", "pt"]

def final_perfect_mirror(folder):
    index_path = os.path.join(base_dir, folder, "index.html")
    contact_path = os.path.join(base_dir, folder, "contact.html")
    
    if not os.path.exists(index_path): return
    
    try:
        # 1. 读取首页最完美的原始源码
        with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # 2. 注入强制隐藏样式（保持首页颜值，只留询盘）
        css_inject = """<style>
            .hero, section:not(#contact), .material-section, .product-category-nav { display: none !important; }
            #contact { display: block !important; padding-top: 160px !important; min-height: 85vh; background: #fff; }
            .thank-you-inline { display: none !important; text-align: center; padding: 40px 0; }
            .inquire-now-btn { background: #111 !important; letter-spacing: 3px !important; font-weight: 700 !important; }
            .back-home-premium { display: inline-block; margin-top: 30px; padding: 12px 35px; border: 1px solid #111; color: #111 !important; text-decoration: none; font-weight: 700; letter-spacing: 1px; transition: 0.3s; }
            .back-home-premium:hover { background: #111 !important; color: #fff !important; }
        </style>"""
        
        # 3. 确定“返回首页”的翻译
        back_text = "BACK TO HOME"
        if folder == "de": back_text = "ZURÜCK ZUR STARTSEITE"
        elif folder == "es": back_text = "VOLVER AL INICIO"
        elif folder == "fr": back_text = "RETOUR À L'ACCUEIL"
        elif folder == "jp": back_text = "ホームに戻る"
        elif folder == "kr": back_text = "홈으로 돌아가기"
        elif folder == "pt": back_text = "VOLTAR AO INÍCIO"

        # 4. 在表单内物理补全感谢界面和返回按钮
        # 确保它在 </form> 之前
        ty_and_back = f'''
                    <div class="thank-you-inline">
                        <div style="font-size: 4rem; color: #c5a059; margin-bottom: 20px;">✓</div>
                        <h3 style="font-family: 'Bodoni Moda', serif; font-size: 2.2rem; color: #111;">Thank you!</h3>
                        <p>Your inquiry has been sent.</p>
                        <a href="index.html" class="back-home-premium">{back_text}</a>
                    </div>
                    <div class="back-link-wrapper" style="text-align: right; margin-top: 30px;">
                        <a href="index.html" style="color: #bbb; text-decoration: none; font-size: 0.8rem;">← {back_text}</a>
                    </div>
                '''
        
        # 5. 执行代码替换
        html = html.replace('</head>', css_inject + '</head>')
        html = html.replace('</form>', ty_and_back + '</form>')
        html = html.replace('href="#contact"', 'href="contact.html"')
        html = html.replace('SEND PROJECT BRIEF', 'INQUIRE NOW').replace('Send Project Brief', 'Inquire Now')
        
        # 注入逻辑
        js_inject = """<script>
            document.addEventListener('DOMContentLoaded', function() {
                const f = document.querySelector(".inquiry-form");
                if(f) {
                    f.onsubmit = function(e) {
                        e.preventDefault();
                        this.querySelectorAll("div:not(.thank-you-inline), button, input, textarea, p").forEach(el => el.style.display="none");
                        const ty = this.querySelector(".thank-you-inline");
                        if(ty) { ty.style.setProperty("display", "block", "important"); ty.scrollIntoView({behavior:"smooth", block:"center"}); }
                        fetch("https://formsubmit.co/ajax/sales@aizjewelry.com", {method:"POST", body:new FormData(this)});
                    };
                }
            });
        </script>"""
        html = html.replace('</body>', js_inject + '</body>')

        # 6. 强制物理覆盖
        with open(contact_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"ULTRA RECOVERED: {contact_path}")

    except Exception as e:
        print(f"Error on {folder}: {e}")

for l in langs:
    final_perfect_mirror(l)
