import os

base_dir = r"E:\AizJewelry_Project"

configs = {
    "de": {"lang": "de", "title": "Angebot anfordern", "back": "ZURÜCK ZUR STARTSEITE", "quote": "Angebot anfordern", "t": "Vielen Dank!", "m": "Ihre Anfrage wurde gesendet. Wir antworten in 12h.", "info": "Besprechen Sie Ihre Markenvision mit unserem Expertenteam."},
    "es": {"lang": "es", "title": "Solicitar presupuesto", "back": "VOLVER AL INICIO", "quote": "Solicitar presupuesto", "t": "¡Gracias!", "m": "Su consulta ha sido enviada. Le contactaremos en 12h.", "info": "Hable de su visión de marca con nuestro equipo especializado."},
    "fr": {"lang": "fr", "title": "Obtenir un devis", "back": "RETOUR À L'ACCUEIL", "quote": "Obtenir un devis", "t": "Merci !", "m": "Votre demande a été envoyée. Réponse sous 12h.", "info": "Discutez de votre vision de marque avec notre équipe."},
    "jp": {"lang": "jp", "title": "お見積り依頼", "back": "ホームに戻る", "quote": "お見積り依頼", "t": "ありがとうございます！", "m": "お問い合わせを送信しました。12時間以内に返信します。", "info": "専門チームがお客様のブランドビジョンをサポートします。"},
    "kr": {"lang": "kr", "title": "견적 요청", "back": "홈으로 돌아가기", "quote": "견적 요청", "t": "감사합니다!", "m": "문의가 전송되었습니다. 12시간 이내에 답변드리겠습니다.", "info": "전문 팀과 귀하의 브랜드 비전을 상담하십시오."},
    "pt": {"lang": "pt", "title": "Obter orçamento", "back": "VOLTAR AO INÍCIO", "quote": "Obter orçamento", "t": "Obrigado!", "m": "Sua consulta foi enviada. Responderemos em 12h.", "info": "Discuta sua visão de marca com nossa equipe especializada."}
}

def force_write_premium_contact(folder, c):
    path = os.path.join(base_dir, folder, "contact.html")
    html = f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['title']} - Aiz Jewelry</title>
    <link rel="stylesheet" href="../style.css?v=20260714-4">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>main {{ padding-top: 140px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center; }} .thank-you-inline {{ display: none; text-align: center; padding: 60px 20px; }} .back-home-btn-premium {{ display: inline-block; padding: 12px 35px; border: 1px solid #111; color: #111; text-decoration: none; font-weight: 700; letter-spacing: 1px; margin-top: 30px; text-transform: uppercase; }} .back-home-btn-premium:hover {{ background: #111; color: #fff; }}</style>
</head>
<body>
    <header class="header"><nav class="container nav-container" style="display: flex; justify-content: space-between; align-items: center; padding: 20px 0;"><a href="index.html" class="logo" style="display: flex; align-items: center; gap: 15px; text-decoration: none; color: #111;"><img src="https://sc02.alicdn.com/kf/Se1318a00bc9742468f7f2b69415cb0b7e.png" style="height: 50px;"><div class="logo-text" style="display: flex; flex-direction: column;"><span class="brand-name" style="font-size: 1.5rem; font-weight: 800; letter-spacing: 2px;">AIZ</span><span class="brand-sub" style="font-size: 0.7rem; letter-spacing: 4px; color: #c5a059;">JEWELRY</span></div></a><div class="nav-links" style="display: flex; align-items: center; gap: 30px;"><a href="index.html" style="text-decoration: none; color: #111; font-weight: 600; font-size: 0.8rem;">HOME</a><a href="contact.html" style="background: #111; color: #fff; padding: 12px 25px; text-decoration: none; font-size: 0.8rem; font-weight: 700;">{c['quote'].upper()}</a></div></nav></header>
    <main><section id="contact" class="contact section" style="width:100%;"><div class="container"><div class="contact-card" style="display: grid; grid-template-columns: 1fr 1.2fr; box-shadow: 0 20px 50px rgba(0,0,0,0.1); border-radius: 4px; overflow: hidden; background: #fff;"><div class="contact-info" style="background: #1a1a1a; color: #fff; padding: 60px;"><h2 style="font-family: 'Bodoni Moda', serif; font-size: 2.8rem; margin-bottom: 25px; line-height: 1.1;">Collaborate with Your Brand Partner</h2><p style="color: #aaa; margin-bottom: 40px;">{c['info']}</p><div class="contact-details" style="display: flex; flex-direction: column; gap: 20px;"><div class="contact-item"><span style="color: #c5a059; font-size: 0.7rem; letter-spacing: 2px;">EMAIL</span><br><strong>sales@aizjewelry.com</strong></div><div class="contact-item"><span style="color: #c5a059; font-size: 0.7rem; letter-spacing: 2px;">WHATSAPP</span><br><strong>0086 18902465287</strong></div></div></div><div class="contact-form" style="padding: 60px; background: #fff;"><form id="form-inner" action="https://formsubmit.co/sales@aizjewelry.com" method="POST"><input type="email" placeholder="Email" required style="width: 100%; padding: 15px; margin-bottom: 20px; border: 1px solid #eee; background: #f9f9f9;"><textarea placeholder="Message" rows="6" required style="width: 100%; padding: 15px; margin-bottom: 25px; border: 1px solid #eee; background: #f9f9f9;"></textarea><button type="submit" style="width: 100%; background: #111; color: #fff; padding: 22px; border: none; font-weight: 700; letter-spacing: 4px; cursor: pointer;">INQUIRE NOW</button></form><div id="ty-inner" class="thank-you-inline" style="text-align: center;"><div style="font-size: 4rem; color: #c5a059;">✓</div><h3 style="font-family: 'Bodoni Moda', serif; font-size: 2rem;">{c['t']}</h3><p>{c['m']}</p><a href="index.html" class="back-home-btn-premium">{c['back']}</a></div><div id="back-link" style="text-align: right; margin-top: 30px;"><a href="index.html" style="color: #999; text-decoration: none; font-size: 0.8rem;">← {c['back']}</a></div></div></div></div></section></main>
    <script>document.getElementById('form-inner').addEventListener('submit', function(e) {{ e.preventDefault(); this.style.display = 'none'; document.getElementById('back-link').style.display = 'none'; document.getElementById('ty-inner').style.display = 'block'; fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {{ method: 'POST', body: new FormData(this), headers: {{ 'Accept': 'application/json' }} }}); }});</script>
</body></html>"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Force Fixed: {path}")

for folder, config in configs.items():
    force_write_premium_contact(folder, config)
