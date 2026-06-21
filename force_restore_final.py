import os

base_dir = r"E:\AizJewelry_Project"

configs = {
    ".": {"lang": "en", "back": "BACK TO HOME", "title": "Get a Quote - Aiz Jewelry", "quote": "Get a Quote", "t": "Thank you!", "m": "Your inquiry has been sent. We will contact you within 12 hours."},
    "de": {"lang": "de", "back": "ZURÜCK ZUR STARTSEITE", "title": "Angebot anfordern - Aiz Jewelry", "quote": "Angebot anfordern", "t": "Vielen Dank!", "m": "Ihre Anfrage wurde gesendet. Wir antworten innerhalb von 12 Stunden."},
    "es": {"lang": "es", "back": "VOLVER AL INICIO", "title": "Solicitar presupuesto - Aiz Jewelry", "quote": "Solicitar presupuesto", "t": "¡Gracias!", "m": "Su consulta ha sido enviada. Le contactaremos en 12 horas."},
    "fr": {"lang": "fr", "back": "RETOUR À L'ACCUEIL", "title": "Obtenir un devis - Aiz Jewelry", "quote": "Obtenir un devis", "t": "Merci !", "m": "Votre demande a été envoyée. Réponse sous 12h."},
    "jp": {"lang": "jp", "back": "ホームに戻る", "title": "お見積り依頼 - Aiz Jewelry", "quote": "お見積り依頼", "t": "ありがとうございます！", "m": "お問い合わせを送信しました。12時間以内に返信します。"},
    "kr": {"lang": "kr", "back": "홈으로 돌아가기", "title": "견적 요청 - Aiz Jewelry", "quote": "견적 요청", "t": "감사합니다!", "m": "문의가 전송되었습니다. 12시간 이내에 답변드리겠습니다."},
    "pt": {"lang": "pt", "back": "VOLTAR AO INÍCIO", "title": "Obter orçamento - Aiz Jewelry", "quote": "Obter orçamento", "t": "Obrigado!", "m": "Sua consulta foi enviada. Responderemos em 12h."}
}

def write_final_html(folder, c):
    dest_path = os.path.join(base_dir, folder, "contact.html")
    script_src = "script.js?v=2.0" if folder == "." else "../script.js?v=2.0"
    css_src = "style.css" if folder == "." else "../style.css"
    
    html = f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['title']}</title>
    <link rel="stylesheet" href="{css_src}">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>main {{ padding-top: 140px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center; }} #contact {{ width: 100%; }}</style>
</head>
<body>
    <header class="header"><nav class="container nav-container"><a href="index.html" class="logo"><div class="logo-text"><span class="brand-name">AIZ</span><span class="brand-sub">JEWELRY</span></div></a><div class="nav-links"><a href="index.html">HOME</a><a href="contact.html" class="nav-cta">{c['quote']}</a></div></nav></header>
    <main><section id="contact" class="contact section"><div class="container">
        <div class="contact-card">
            <div class="contact-info">
                <h2>Collaborate with Your Brand Partner</h2>
                <p>Discuss your unique brand vision with our specialized team. We excel in small-batch flexible production.</p>
                <div class="contact-details">
                    <div class="contact-item"><span>Direct Email</span><strong>sales@aizjewelry.com</strong></div>
                    <div class="contact-item"><span>WhatsApp Direct</span><strong>0086 18902465287</strong></div>
                </div>
            </div>
            <div class="contact-form">
                <form class="inquiry-form" action="https://formsubmit.co/sales@aizjewelry.com" method="POST" enctype="multipart/form-data">
                    <input type="email" name="email" placeholder="Business Email" required style="width:100%; padding:15px; margin-bottom:15px; border:1px solid #ddd;">
                    <textarea name="message" placeholder="Tell us about your brand vision..." rows="4" required style="width:100%; padding:15px; margin-bottom:15px; border:1px solid #ddd;"></textarea>
                    <div class="file-input-wrapper" style="margin-bottom:20px;">
                        <input type="file" name="attachment" onchange="updateFileName(this)">
                        <span class="file-name-display" style="font-size:0.8rem; color:#999;">Attach designs (Max 10MB)</span>
                    </div>
                    <button type="submit" class="btn primary" style="width:100%; background:#111; color:#fff; padding:20px; border:none; letter-spacing:3px; font-weight:700; cursor:pointer;">INQUIRE NOW</button>
                </form>
                <div class="thank-you-inline" style="display:none; text-align:center; padding:40px 0;">
                    <div style="font-size:3.5rem; color:#c5a059; margin-bottom:20px;">✓</div>
                    <h3 style="font-family:'Bodoni Moda', serif; font-size:2.2rem; margin-bottom:15px;">{c['t']}</h3>
                    <p style="color:#666; line-height:1.6;">{c['m']}</p>
                    <div style="margin-top:40px;"><a href="index.html" class="back-home-btn" style="padding:12px 35px; border:2px solid #111; color:#111; text-decoration:none; font-weight:700; letter-spacing:1px;">{c['back']}</a></div>
                </div>
                <div class="back-home-wrapper" style="margin-top:30px; text-align:right;"><a href="index.html" style="color:#999; font-size:0.8rem; text-decoration:none;">← {c['back']}</a></div>
            </div>
        </div>
    </div></section></main>
    <footer><div class="container" style="text-align:center; padding:40px 0; border-top:1px solid #eee; color:#999;">&copy; 2026 Aiz Jewelry. All Rights Reserved.</div></footer>
    <script src="{script_src}"></script>
</body></html>"""
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Force Restored: {dest_path}")

for folder, config in configs.items():
    write_final_html(folder, config)
