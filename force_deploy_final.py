import os

# 终极物理重写脚本 - 100% 确保返回按钮和感谢逻辑在每一个文件中
base_dir = r"E:\AizJewelry_Project"

configs = {
    ".": {"lang": "en", "title": "Get a Quote - Aiz Jewelry", "back": "BACK TO HOME", "quote": "Get a Quote", "t": "Thank you!", "m": "Your inquiry has been sent. We will contact you within 12 hours."},
    "de": {"lang": "de", "title": "Angebot anfordern - Aiz Jewelry", "back": "ZURÜCK ZUR STARTSEITE", "quote": "Angebot anfordern", "t": "Vielen Dank!", "m": "Ihre Anfrage wurde gesendet. Wir antworten in 12h."},
    "es": {"lang": "es", "title": "Solicitar presupuesto - Aiz Jewelry", "back": "VOLVER AL INICIO", "quote": "Solicitar presupuesto", "t": "¡Gracias!", "m": "Su consulta ha sido enviada."},
    "fr": {"lang": "fr", "title": "Obtenir un devis - Aiz Jewelry", "back": "RETOUR À L'ACCUEIL", "quote": "Obtenir un devis", "t": "Merci !", "m": "Votre demande a été envoyée."},
    "jp": {"lang": "jp", "title": "お見積り依頼 - Aiz Jewelry", "back": "ホームに戻る", "quote": "お見積り依頼", "t": "ありがとうございます！", "m": "お問い合わせを送信しました。"},
    "kr": {"lang": "kr", "title": "견적 요청 - Aiz Jewelry", "back": "홈으로 돌아가기", "quote": "견적 요청", "t": "감사합니다!", "m": "문의가 전송되었습니다."},
    "pt": {"lang": "pt", "title": "Obter orçamento - Aiz Jewelry", "back": "VOLTAR AO INÍCIO", "quote": "Obter orçamento", "t": "Obrigado!", "m": "Sua consulta foi enviada."}
}

def force_write(folder, c):
    dest = os.path.join(base_dir, folder, "contact.html")
    css = "style.css?v=20260714-6" if folder == "." else "../style.css?v=20260714-6"
    
    html = f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['title']}</title>
    <link rel="stylesheet" href="{css}">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>main {{ padding-top: 140px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center; }} .thank-you-inline {{ display: none !important; text-align: center; padding: 60px 20px; }}</style>
</head>
<body>
    <header class="header"><nav class="container nav-container" style="display:flex; justify-content:space-between; align-items:center; padding:20px 0;"><a href="index.html" class="logo"><div class="logo-text"><span style="font-size:1.5rem; font-weight:800; letter-spacing:2px;">AIZ</span><span style="font-size:0.7rem; letter-spacing:4px; color:#c5a059;">JEWELRY</span></div></a><div class="nav-links"><a href="index.html">HOME</a><a href="contact.html" class="nav-cta" style="background:#111; color:#fff; padding:12px 25px; text-decoration:none; font-size:0.8rem; font-weight:700;">{c['quote'].upper()}</a></div></nav></header>
    <main><section id="contact" style="width:100%;"><div class="container"><div class="contact-card" style="display:grid; grid-template-columns:1fr 1.2fr; box-shadow:0 20px 50px rgba(0,0,0,0.1); border-radius:4px; overflow:hidden; background:#fff;">
        <div class="contact-info" style="background:#1a1a1a; color:#fff; padding:60px;">
            <h2 style="font-family:'Bodoni Moda', serif; font-size:2.8rem; margin-bottom:25px; line-height:1.1;">Collaborate with Your Brand Partner</h2>
            <p style="color:#aaa; margin-bottom:40px;">Discuss your vision with our specialized team.</p>
            <div style="display:flex; flex-direction:column; gap:20px;">
                <div><span style="color:#c5a059; font-size:0.7rem; letter-spacing:2px;">EMAIL</span><br><strong>sales@aizjewelry.com</strong></div>
                <div><span style="color:#c5a059; font-size:0.7rem; letter-spacing:2px;">WHATSAPP</span><br><strong>0086 18902465287</strong></div>
            </div>
        </div>
        <div class="contact-form" style="padding:60px; position:relative;">
            <form id="FORCE-FORM" action="https://formsubmit.co/sales@aizjewelry.com" method="POST">
                <input type="email" placeholder="Business Email" required style="width:100%; padding:15px; margin-bottom:20px; border:1px solid #eee; background:#f9f9f9;">
                <textarea placeholder="Message" rows="6" required style="width:100%; padding:15px; margin-bottom:25px; border:1px solid #eee; background:#f9f9f9; resize:none;"></textarea>
                <button type="submit" style="width:100%; background:#111; color:#fff; padding:22px; border:none; font-weight:700; letter-spacing:4px; cursor:pointer;">INQUIRE NOW</button>
            </form>
            <div id="FORCE-TY" class="thank-you-inline">
                <div style="font-size:4rem; color:#c5a059;">✓</div>
                <h3 style="font-family:'Bodoni Moda', serif; font-size:2.2rem;">{c['t']}</h3><p>{c['m']}</p>
                <div style="margin-top:40px;"><a href="index.html" style="display:inline-block; padding:15px 45px; border:2px solid #111; color:#111; text-decoration:none; font-weight:700;">{c['back']}</a></div>
            </div>
            <!-- 核心点：白区右下角返回按钮 -->
            <div id="B-FORCE" style="text-align:right; margin-top:40px;"><a href="index.html" style="display:inline-block; padding:10px 25px; border:1px solid #ddd; color:#999; text-decoration:none; font-size:0.8rem; font-weight:600;">← {c['back']}</a></div>
        </div>
    </div></div></section></main>
    <script>
        document.getElementById('FORCE-FORM').addEventListener('submit', function(e) {{
            e.preventDefault();
            this.style.setProperty('display', 'none', 'important');
            document.getElementById('B-FORCE').style.setProperty('display', 'none', 'important');
            const ty = document.getElementById('FORCE-TY');
            ty.style.setProperty('display', 'block', 'important');
            fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {{ method: 'POST', body: new FormData(this), headers: {{ 'Accept': 'application/json' }} }});
        }});
    </script>
</body></html>"""
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"FORCED WRITE: {dest}")

for folder, config in configs.items():
    force_write(folder if folder != "." else "", config)
