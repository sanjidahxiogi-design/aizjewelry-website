import os

base_dir = r"E:\AizJewelry_Project"

configs = {
    ".": {"lang": "en", "back": "BACK TO HOME", "quote": "Get a Quote", "t": "Thank you!", "m": "Your inquiry has been sent. We will contact you within 12 hours."},
    "de": {"lang": "de", "back": "ZURÜCK ZUR STARTSEITE", "quote": "Angebot anfordern", "t": "Vielen Dank!", "m": "Ihre Anfrage wurde gesendet. Wir antworten in 12h."},
    "es": {"lang": "es", "back": "VOLVER AL INICIO", "quote": "Solicitar presupuesto", "t": "¡Gracias!", "m": "Su consulta ha sido enviada."},
    "fr": {"lang": "fr", "back": "RETOUR À L'ACCUEIL", "quote": "Obtenir un devis", "t": "Merci !", "m": "Votre demande a été envoyée."},
    "jp": {"lang": "jp", "back": "ホームに戻る", "quote": "お見積り依頼", "t": "ありがとうございます！", "m": "お問い合わせを送信しました。"},
    "kr": {"lang": "kr", "back": "홈으로 돌아가기", "quote": "견적 요청", "t": "감사합니다!", "m": "문의가 전송되었습니다."},
    "pt": {"lang": "pt", "back": "VOLTAR AO INÍCIO", "quote": "Obter orçamento", "t": "Obrigado!", "m": "Sua consulta foi enviada."}
}

def extreme_physical_rewrite(folder, c):
    target_path = os.path.join(base_dir, folder, "contact.html")
    css_ref = "style.css?v=6.0" if folder == "." else "../style.css?v=6.0"
    
    html = f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{css_ref}">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>main {{ padding-top:140px; padding-bottom:100px; min-height:85vh; background:#fff; display:flex; align-items:center; }} #contact {{ width:100%; }} .thank-you-inline {{ display:none !important; text-align:center; padding:60px 0; background:#fff; }} .thank-you-inline.active {{ display:block !important; }}</style>
</head>
<body>
    <header class="header"><nav class="container nav-container" style="display:flex; justify-content:space-between; align-items:center; padding:20px 0;"><a href="index.html" class="logo" style="display:flex; align-items:center; gap:15px; text-decoration:none; color:#111;"><img src="https://sc02.alicdn.com/kf/Se1318a00bc9742468f7f2b69415cb0b7e.png" style="height:50px;"><div class="logo-text" style="display:flex; flex-direction:column;"><span style="font-size:1.6rem; font-weight:800; letter-spacing:2px;">AIZ</span><span style="font-size:0.75rem; letter-spacing:4px; color:#c5a059;">JEWELRY</span></div></a><div class="nav-links" style="display:flex; align-items:center; gap:40px;"><a href="index.html" style="text-decoration:none; color:#111; font-weight:600;">HOME</a><a href="contact.html" style="background:#111; color:#fff; padding:12px 25px; text-decoration:none; font-weight:700;">{c['quote'].upper()}</a></div></nav></header>
    <main><section id="contact"><div class="container"><div class="contact-card" style="display:grid; grid-template-columns:1fr 1.2fr; box-shadow:0 30px 70px rgba(0,0,0,0.12); border-radius:4px; overflow:hidden; background:#fff;"><div class="contact-info" style="background:#111; color:#fff; padding:70px; display:flex; flex-direction:column; justify-content:center;"><h2 style="font-family:'Bodoni Moda', serif; font-size:3.2rem; margin-bottom:25px; line-height:1.1;">Collaborate with Your Brand Partner</h2><p style="color:#888; font-size:1.1rem; margin-bottom:45px;">Discuss your vision with our specialized team.</p><div style="display:flex; flex-direction:column; gap:25px;"><div class="contact-item"><span style="color:#c5a059; font-size:0.75rem; text-transform:uppercase;">EMAIL</span><br><strong style="font-size:1.2rem;">sales@aizjewelry.com</strong></div><div class="contact-item"><span style="color:#c5a059; font-size:0.75rem; text-transform:uppercase;">WHATSAPP</span><br><strong style="font-size:1.2rem;">0086 18902465287</strong></div></div></div><div class="contact-form" style="padding:70px; position:relative;"><form id="F-ULTRA" action="https://formsubmit.co/sales@aizjewelry.com" method="POST"><input type="email" placeholder="Business Email" required style="width:100%; padding:18px; margin-bottom:25px; border:1px solid #eee; background:#fcfcfc;"><textarea placeholder="Message" rows="7" required style="width:100%; padding:18px; margin-bottom:30px; border:1px solid #eee; background:#fcfcfc;"></textarea><button type="submit" style="width:100%; background:#111; color:#fff; padding:24px; border:none; font-weight:700; letter-spacing:4px; cursor:pointer;">INQUIRE NOW</button></form><div id="T-ULTRA" class="thank-you-inline"><div style="font-size:4.5rem; color:#c5a059; margin-bottom:25px;">✓</div><h3 style="font-family:'Bodoni Moda', serif; font-size:2.5rem; color:#111;">{c['t']}</h3><p style="color:#666;">{c['m']}</p><div style="margin-top:40px;"><a href="index.html" style="display:inline-block; padding:15px 45px; border:2px solid #111; color:#111; text-decoration:none; font-weight:700;">BACK TO HOME</a></div></div><div id="B-ULTRA" style="text-align:right; margin-top:40px; border-top:1px solid #eee; padding-top:30px;"><a href="index.html" style="display:inline-block; padding:10px 25px; border:1px solid #111; color:#111; text-decoration:none; font-size:0.8rem; font-weight:700; letter-spacing:1px; background:transparent;">← {c['back']}</a></div></div></div></div></section></main>
    <footer style="text-align:center; padding:50px 0; color:#aaa; font-size:0.8rem; border-top:1px solid #eee; background:#fafafa;"><p>&copy; 2026 Aiz Jewelry. All Rights Reserved.</p></footer>
    <script>document.getElementById("F-ULTRA").onsubmit = function(e){{ e.preventDefault(); this.style.setProperty("display","none","important"); document.getElementById("B-ULTRA").style.setProperty("display","none","important"); const ty=document.getElementById("T-ULTRA"); ty.style.setProperty("display","block","important"); ty.classList.add("active"); fetch("https://formsubmit.co/ajax/sales@aizjewelry.com",{{method:"POST", body:new FormData(this), headers:{'Accept':'application/json'}}}); }};</script>
</body></html>"""
    
    # 强制覆盖：直接物理写入
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"ULTRA REWRITTEN: {target_path}")

for folder, config in configs.items():
    extreme_physical_rewrite("" if folder == "." else folder, config)
