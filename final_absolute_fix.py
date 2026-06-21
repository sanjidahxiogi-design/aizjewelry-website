import os

base_dir = r"E:\AizJewelry_Project"

configs = {
    ".": {"lang": "en", "title": "Get a Quote - Aiz Jewelry", "back": "Back to Home", "quote": "Get a Quote", "t": "Thank you!", "m": "Your inquiry has been sent. We will contact you within 12 hours."},
    "de": {"lang": "de", "title": "Angebot anfordern - Aiz Jewelry", "back": "Zurück zur Startseite", "quote": "Angebot anfordern", "t": "Vielen Dank!", "m": "Ihre Anfrage wurde gesendet. Wir kontaktieren Sie innerhalb von 12h."},
    "es": {"lang": "es", "title": "Solicitar presupuesto - Aiz Jewelry", "back": "Volver al inicio", "quote": "Solicitar presupuesto", "t": "¡Gracias!", "m": "Su consulta ha sido enviada. Le contactaremos en 12h."},
    "fr": {"lang": "fr", "title": "Obtenir un devis - Aiz Jewelry", "back": "Retour à l'accueil", "quote": "Obtenir un devis", "t": "Merci !", "m": "Votre demande a été envoyée. Nous vous répondrons sous 12h."},
    "jp": {"lang": "jp", "title": "お見積り依頼 - Aiz Jewelry", "back": "ホームに戻る", "quote": "お見積り依頼", "t": "ありがとうございます！", "m": "お問い合わせを送信しました。12時間以内に返信します。"},
    "kr": {"lang": "kr", "title": "견적 요청 - Aiz Jewelry", "back": "홈으로 돌아가기", "quote": "견적 요청", "t": "감사합니다!", "m": "문의가 전송되었습니다. 12시간 이내에 답변드리겠습니다."},
    "pt": {"lang": "pt", "title": "Obter orçamento - Aiz Jewelry", "back": "Voltar ao início", "quote": "Obter orçamento", "t": "Obrigado!", "m": "Sua consulta foi enviada. Responderemos em até 12h."}
}

def generate_absolute_contact(folder, c):
    script_path = "script.js?v=1.3" if folder == "." else "../script.js?v=1.3"
    css_path = "style.css" if folder == "." else "../style.css"
    dest_path = os.path.join(base_dir, folder, "contact.html")
    
    html = f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['title']}</title>
    <link rel="stylesheet" href="{css_path}">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>main {{ padding-top: 140px; padding-bottom: 80px; }} #contact {{ width: 100%; }}</style>
</head>
<body>
    <header class="header"><nav class="container nav-container"><a href="index.html" class="logo"><div class="logo-text"><span class="brand-name">AIZ</span><span class="brand-sub">JEWELRY</span></div></a><div class="nav-links"><a href="index.html#products">PRODUCTS</a><a href="contact.html" class="nav-cta">{c['quote']}</a></div></nav></header>
    <main><section id="contact" class="contact section"><div class="container"><div class="contact-card">
        <div class="contact-info"><h2>Collaborate with Your Brand Partner</h2><p>Discuss your vision with our specialized team.</p></div>
        <div class="contact-form">
            <form class="inquiry-form" action="https://formsubmit.co/sales@aizjewelry.com" method="POST">
                <input type="email" name="email" placeholder="Email" required style="width:100%; padding:15px; margin-bottom:15px; border:1px solid #ddd;">
                <textarea name="message" placeholder="Project details" rows="4" required style="width:100%; padding:15px; margin-bottom:15px; border:1px solid #ddd;"></textarea>
                <button type="submit" class="btn primary">INQUIRE NOW</button>
            </form>
            <div class="thank-you-inline" style="display:none !important;">
                <div style="font-size: 3rem; color: #c5a059; margin-bottom: 20px;">✓</div>
                <h3 style="font-family: 'Bodoni Moda', serif; font-size: 2rem;">{c['t']}</h3>
                <p>{c['m']}</p>
            </div>
            <div class="back-home-wrapper" style="margin-top:40px; text-align:right;"><a href="index.html" class="back-home-btn">← {c['back']}</a></div>
        </div>
    </div></div></section></main>
    <script src="{script_path}"></script>
</body></html>"""
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(html)

for folder, config in configs.items():
    generate_absolute_contact(folder, config)
