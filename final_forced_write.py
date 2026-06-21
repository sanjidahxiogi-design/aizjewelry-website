import os

base_dir = r"E:\AizJewelry_Project"
langs = ["", "de/", "es/", "fr/", "jp/", "kr/", "pt/"]

configs = {
    "": {"lang": "en", "back": "BACK TO HOME", "t": "Thank you!", "m": "Your inquiry has been sent."},
    "de/": {"lang": "de", "back": "ZURÜCK", "t": "Vielen Dank!", "m": "Ihre Anfrage wurde gesendet."},
    "es/": {"lang": "es", "back": "VOLVER", "t": "¡Gracias!", "m": "Su consulta ha sido enviada."},
    "fr/": {"lang": "fr", "back": "RETOUR", "t": "Merci !", "m": "Votre demande a été envoyée."},
    "jp/": {"lang": "jp", "back": "ホームに戻る", "t": "ありがとうございます！", "m": "お問い合わせを送信しました。"},
    "kr/": {"lang": "kr", "back": "홈으로 돌아가기", "t": "감사합니다!", "m": "문의가 전송되었습니다."},
    "pt/": {"lang": "pt", "back": "VOLTAR", "t": "Obrigado!", "m": "Sua consulta foi enviada."}
}

def force_write_final(path_rel, c):
    full_path = os.path.join(base_dir, path_rel, "contact.html")
    css_ref = "style.css" if path_rel == "" else "../style.css"
    
    html = f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{css_ref}?v=3.1">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>main {{ padding-top: 140px; padding-bottom: 80px; background: #fff; display: flex; align-items: center; min-height: 80vh; }} .thank-you-inline {{ display: none; text-align: center; }} .thank-you-inline.visible {{ display: block !important; }}</style>
</head>
<body>
    <header class="header"><nav class="container nav-container" style="display: flex; justify-content: space-between; align-items: center; padding: 25px 0;"><a href="index.html" class="logo" style="display: flex; align-items: center; gap: 15px; text-decoration: none; color: #111;"><img src="https://sc02.alicdn.com/kf/Se1318a00bc9742468f7f2b69415cb0b7e.png" style="height: 50px;"><div class="logo-text" style="display: flex; flex-direction: column;"><span style="font-size: 1.6rem; font-weight: 800; letter-spacing: 2px;">AIZ</span><span style="font-size: 0.75rem; letter-spacing: 4px; color: #c5a059;">JEWELRY</span></div></a><div class="nav-links" style="display: flex; align-items: center; gap: 40px;"><a href="index.html" style="text-decoration: none; color: #111; font-weight: 600;">HOME</a><a href="contact.html" style="background: #111; color: #fff; padding: 12px 25px; text-decoration: none; font-size: 0.8rem; font-weight: 700;">GET A QUOTE</a></div></nav></header>
    <main><section style="width:100%;"><div class="container"><div class="contact-card" style="display: grid; grid-template-columns: 1fr 1.2fr; box-shadow: 0 30px 70px rgba(0,0,0,0.12); overflow: hidden; background: #fff;"><div class="contact-info" style="background: #111; color: #fff; padding: 70px;"><h2 style="font-family: 'Bodoni Moda', serif; font-size: 3rem; margin-bottom: 25px;">Collaborate with Your Brand Partner</h2><p style="color: #888;">Discuss your unique brand vision with our specialized team.</p><div class="contact-details" style="display: flex; flex-direction: column; gap: 20px; margin-top: 40px;"><div class="contact-item"><span style="color: #c5a059; font-size: 0.75rem;">EMAIL</span><br><strong>sales@aizjewelry.com</strong></div><div class="contact-item"><span style="color: #c5a059; font-size: 0.75rem;">WHATSAPP</span><br><strong>0086 18902465287</strong></div></div></div><div class="contact-form" style="padding: 70px; background: #fff;"><form id="f-final" action="https://formsubmit.co/sales@aizjewelry.com" method="POST"><input type="email" placeholder="Business Email" required style="width:100%; padding:15px; margin-bottom:15px; border:1px solid #eee;"><textarea placeholder="Details..." rows="6" required style="width:100%; padding:15px; margin-bottom:15px; border:1px solid #eee;"></textarea><button type="submit" style="width:100%; background:#111; color:#fff; padding:20px; border:none; font-weight:700; cursor:pointer;">INQUIRE NOW</button></form><div id="t-final" class="thank-you-inline"><div style="font-size: 4rem; color: #c5a059;">✓</div><h3 style="font-family: 'Bodoni Moda', serif; font-size: 2.2rem;">{c['t']}</h3><p>{c['m']}</p><div style="margin-top:40px;"><a href="index.html" style="padding:12px 35px; border:1px solid #111; color:#111; text-decoration:none; font-weight:700;">{c['back']}</a></div></div><div id="b-final" style="text-align: right; margin-top: 30px;"><a href="index.html" style="color: #bbb; text-decoration: none; font-size: 0.8rem;">← {c['back']}</a></div></div></div></div></section></main>
    <script>document.getElementById("f-final").onsubmit = function(e){{ e.preventDefault(); this.style.display="none"; document.getElementById("b-final").style.display="none"; document.getElementById("t-final").classList.add("visible"); fetch("https://formsubmit.co/ajax/sales@aizjewelry.com", {{method:"POST", body:new FormData(this)}}); }};</script>
</body></html>"""
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"FORCED: {full_path}")

for l in langs:
    force_write_final(l, configs[l])
