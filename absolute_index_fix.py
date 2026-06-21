import os

base_dir = r"E:\AizJewelry_Project"
langs = ["", "de", "es", "fr", "jp", "kr", "pt"]

def absolute_footer_fix(folder):
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path): return
    
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # 确定各语种翻译
        t, m = "Thank you!", "Your inquiry has been sent. We will contact you within 12 hours."
        if folder == "de": t, m = "Vielen Dank!", "Ihre Anfrage wurde gesendet."
        elif folder == "es": t, m = "¡Gracias!", "Su consulta ha sido enviada."
        elif folder == "fr": t, m = "Merci !", "Votre demande a été envoyée."
        elif folder == "jp": t, m = "ありがとうございます！", "お問い合わせを送信しました。"
        elif folder == "kr": t, m = "감사합니다!", "문의가 전송되었습니다."
        elif folder == "pt": t, m = "Obrigado!", "Sua consulta foi enviada."

        # 1. 物理重写询盘板块的代码，赋予唯一 ID 并绑定物理触发逻辑
        # 我们寻找联系板块的开始标记
        start_marker = '<section id="contact"'
        if start_marker not in html: return

        # 构造全新的、带绝对反馈逻辑的黑白卡片 HTML
        # 注意：这里我们使用 onclick 配合 submit，确保一点击就切换，不等网络
        new_contact_section = f'''
    <section id="contact" class="contact section">
        <div class="container">
            <div class="contact-card" style="display: grid; grid-template-columns: 1fr 1.2fr; box-shadow: 0 30px 70px rgba(0,0,0,0.12); border-radius: 4px; overflow: hidden; background: #fff;">
                <div class="contact-info" style="background: #111; color: #fff; padding: 60px; display: flex; flex-direction: column; justify-content: center;">
                    <h2 style="font-family: 'Bodoni Moda', serif; font-size: 2.8rem; margin-bottom: 25px; line-height: 1.1;">Collaborate with Your Brand Partner</h2>
                    <div style="display: flex; flex-direction: column; gap: 25px;">
                        <div><span style="color: #c5a059; font-size: 0.75rem; text-transform: uppercase;">EMAIL</span><br><strong>sales@aizjewelry.com</strong></div>
                        <div><span style="color: #c5a059; font-size: 0.75rem; text-transform: uppercase;">WHATSAPP</span><br><strong>0086 18902465287</strong></div>
                    </div>
                </div>
                <div class="contact-form" style="padding: 60px; background: #fff; position: relative;">
                    <form id="FOOTER-FORM-UNIQUE" action="https://formsubmit.co/sales@aizjewelry.com" method="POST" onsubmit="event.preventDefault(); document.getElementById('FOOTER-FORM-UNIQUE').style.display='none'; document.getElementById('FOOTER-THANK-YOU-UNIQUE').style.setProperty('display','block','important'); fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {{method:'POST', body:new FormData(this)}});">
                        <input type="email" name="email" placeholder="Business Email" required style="width: 100%; padding: 15px; margin-bottom: 20px; border: 1px solid #eee; background: #f9f9f9;">
                        <textarea name="message" placeholder="Details..." rows="6" required style="width: 100%; padding: 15px; margin-bottom: 25px; border: 1px solid #eee; background: #f9f9f9; resize: none;"></textarea>
                        <button type="submit" style="width: 100%; background: #111; color: #fff; padding: 22px; border: none; font-weight: 700; letter-spacing: 4px; cursor: pointer; text-transform: uppercase;">INQUIRE NOW</button>
                    </form>
                    <div id="FOOTER-THANK-YOU-UNIQUE" style="display: none; text-align: center; padding: 40px 0;">
                        <div style="font-size: 4rem; color: #c5a059; margin-bottom: 20px;">✓</div>
                        <h3 style="font-family: 'Bodoni Moda', serif; font-size: 2.2rem; color: #111;">{t}</h3>
                        <p style="color: #666;">{m}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''
        # 物理级替换整个 Section
        import re
        html = re.sub(r'<section id="contact".*?</section>', new_contact_section, html, flags=re.DOTALL)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Absolute Fix Applied: {path}")

    except Exception as e:
        print(f"Err on {path}: {e}")

for l in langs:
    absolute_footer_fix(l)
