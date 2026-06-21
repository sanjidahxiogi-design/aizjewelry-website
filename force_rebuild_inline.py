import os

base_dir = r"E:\AizJewelry_Project"

configs = {
    "de": {"lang": "de", "title": "Angebot anfordern", "back": "ZURÜCK ZUR STARTSEITE", "t": "Vielen Dank!", "m": "Ihre Anfrage wurde gesendet. Wir antworten in 12h."},
    "es": {"lang": "es", "title": "Solicitar presupuesto", "back": "VOLVER AL INICIO", "t": "¡Gracias!", "m": "Su consulta ha sido enviada. Le contactaremos en 12h."},
    "fr": {"lang": "fr", "title": "Obtenir un devis", "back": "RETOUR À L'ACCUEIL", "t": "Merci !", "m": "Votre demande a été envoyée. Réponse sous 12h."},
    "jp": {"lang": "jp", "title": "お見積り依頼", "back": "ホームに戻る", "t": "ありがとうございます！", "m": "お問い合わせを送信しました。12時間以内に返信します。"},
    "kr": {"lang": "kr", "title": "견적 요청", "back": "홈으로 돌아가기", "t": "감사합니다!", "m": "문의가 전송되었습니다. 12시간 이내에 답변드리겠습니다."},
    "pt": {"lang": "pt", "title": "Obter orçamento", "back": "VOLTAR AO INÍCIO", "t": "Obrigado!", "m": "Sua consulta foi enviada. Responderemos em 12h."}
}

def force_write_contact(folder, c):
    path = os.path.join(base_dir, folder, "contact.html")
    html = f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['title']} - Aiz Jewelry</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>main {{ padding-top: 140px; padding-bottom: 80px; }} .inquiry-form.hidden {{ display: none !important; }} .thank-you-inline {{ display: none; text-align: center; padding: 60px 20px; background: #fff; border: 1px solid #eee; margin-top: 20px; }} .thank-you-inline.visible {{ display: block !important; }}</style>
</head>
<body>
    <header class="header"><nav class="container nav-container"><a href="index.html" class="logo"><div class="logo-text"><span class="brand-name">AIZ</span><span class="brand-sub">JEWELRY</span></div></a><div class="nav-links"><a href="index.html">HOME</a><a href="contact.html" class="nav-cta">Get a Quote</a></div></nav></header>
    <main><section id="contact" class="contact section"><div class="container"><div class="contact-card">
        <div class="contact-info"><h2>Collaborate with Your Brand Partner</h2><p>Discuss your vision with our specialized team.</p></div>
        <div class="contact-form">
            <form id="inquiry-form" class="inquiry-form" action="https://formsubmit.co/sales@aizjewelry.com" method="POST">
                <input type="email" name="email" placeholder="Email" required style="width:100%; padding:15px; margin-bottom:15px; border:1px solid #ddd;">
                <textarea name="message" placeholder="Details" rows="4" required style="width:100%; padding:15px; margin-bottom:15px; border:1px solid #ddd;"></textarea>
                <button type="submit" class="btn primary" style="width:100%; background:#111; color:#fff; padding:20px; border:none; letter-spacing:3px; cursor:pointer;">INQUIRE NOW</button>
            </form>
            <div id="thank-you-message" class="thank-you-inline">
                <div style="font-size: 3rem; color: #c5a059; margin-bottom: 20px;">✓</div>
                <h3 style="font-family: 'Bodoni Moda', serif; font-size: 2rem;">{c['t']}</h3><p>{c['m']}</p>
                <div style="margin-top:40px;"><a href="index.html" class="back-home-btn" style="padding:12px 30px; border:1px solid #111; text-decoration:none; color:#111;">← {c['back']}</a></div>
            </div>
            <div id="back-home-link" class="back-home-wrapper" style="margin-top:40px; text-align:right;"><a href="index.html" class="back-home-btn" style="text-decoration:none; color:#111; font-weight:600; border:1px solid #ddd; padding:10px 20px;">← {c['back']}</a></div>
        </div>
    </div></div></section></main>
    <script>
        document.getElementById('inquiry-form').addEventListener('submit', function(e) {{
            e.preventDefault();
            const form = this;
            const btn = form.querySelector('button');
            btn.textContent = 'SENDING...';
            btn.disabled = true;
            fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {{
                method: 'POST',
                body: new FormData(form),
                headers: {{ 'Accept': 'application/json' }}
            }});
            form.classList.add('hidden');
            document.getElementById('back-home-link').style.display = 'none';
            document.getElementById('thank-you-message').classList.add('visible');
            document.getElementById('thank-you-message').scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        }});
    </script>
</body></html>"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Force Rebuilt: {path}")

for folder, config in configs.items():
    force_write_contact(folder, config)
