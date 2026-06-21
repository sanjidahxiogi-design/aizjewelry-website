import os
import re

base_dir = r"E:\AizJewelry_Project"
langs = ["", "de/", "es/", "fr/", "jp/", "kr/", "pt/"]

def ultimate_fix(path_rel):
    index_file = os.path.join(base_dir, path_rel, "index.html")
    contact_file = os.path.join(base_dir, path_rel, "contact.html")
    
    if not os.path.exists(index_file): return
    
    with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. 确保模板中有“感谢模块”和“大气返回按钮”
    # 如果没有，我们就补全它
    if 'id="ULTIMATE-THANK-YOU"' not in html:
        # 寻找对应的语种翻译文案
        t, m, b = "Thank you!", "Your inquiry has been sent. We will contact you within 12 hours.", "BACK TO HOME"
        if "de/" in path_rel: t, m, b = "Vielen Dank!", "Anfrage gesendet. Wir antworten in 12h.", "ZURÜCK"
        elif "es/" in path_rel: t, m, b = "¡Gracias!", "Su consulta ha sido enviada.", "VOLVER"
        elif "fr/" in path_rel: t, m, b = "Merci !", "Votre demande a été envoyée.", "RETOUR"
        elif "jp/" in path_rel: t, m, b = "ありがとうございます！", "送信されました。12h以内に返信します。", "ホームに戻る"
        elif "kr/" in path_rel: t, m, b = "감사합니다!", "전송되었습니다. 12시간 이내에 연락드립니다.", "홈으로"
        elif "pt/" in path_rel: t, m, b = "Obrigado!", "Sua consulta foi enviada.", "VOLTAR"

        ty_html = f'''
                    <div id="ULTIMATE-THANK-YOU" style="display: none !important; text-align: center; padding: 60px 20px;">
                        <div style="font-size: 4rem; color: #c5a059; margin-bottom: 20px;">✓</div>
                        <h3 style="font-family: 'Bodoni Moda', serif; font-size: 2.2rem; color: #111;">{t}</h3>
                        <p style="color: #666;">{m}</p>
                        <div style="margin-top: 40px;"><a href="index.html" style="display: inline-block; padding: 15px 45px; border: 1px solid #111; color: #111; text-decoration: none; font-weight: 700; letter-spacing: 2px;">{b}</a></div>
                    </div>
                '''
        html = html.replace('</form>', '</form>' + ty_html)

    # 2. 注入强制隐藏和显示逻辑 (仅针对 contact.html)
    css_fix = """<style>
        .hero, section:not(#contact), .material-section, .product-category-nav { display: none !important; }
        #contact { display: block !important; padding-top: 160px !important; min-height: 85vh; background: #fff; }
    </style>"""
    
    js_fix = """<script>
        document.addEventListener('DOMContentLoaded', function() {
            const f = document.querySelector(".inquiry-form");
            if(f) {
                f.onsubmit = function(e) {
                    e.preventDefault();
                    this.style.setProperty('display', 'none', 'important');
                    const ty = document.getElementById('ULTIMATE-THANK-YOU');
                    if(ty) { ty.style.setProperty('display', 'block', 'important'); ty.scrollIntoView({behavior:'smooth', block:'center'}); }
                    fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {method:'POST', body:new FormData(this), headers:{'Accept':'application/json'}});
                };
            }
        });
    </script>"""

    final_html = html.replace('</head>', css_fix + '</head>')
    final_html = final_html.replace('</body>', js_fix + '</body>')
    final_html = final_html.replace('href="#contact"', 'href="contact.html"')
    final_html = final_html.replace('SEND PROJECT BRIEF', 'INQUIRE NOW').replace('Send Project Brief', 'Inquire Now')

    # 3. 强制物理写入 (突破锁定)
    with open(contact_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"ULTRA-FIXED: {contact_file}")

for l in langs:
    ultimate_fix(l)
