import os

# 最终确定的生成脚本
base_dir = r"E:\AizJewelry_Project"

configs = {
    "es": {"lang": "es", "title": "Contacto - Aiz Jewelry", "back": "Volver al inicio", "copy": "Copiar", "copied": "¡Copiado!", "quote": "Solicitar presupuesto", "products": "PRODUCTOS", "custom": "PROCESO PERSONALIZADO", "sus": "SOSTENIBILIDAD", "flow": "FLUJO DE TRABAJO", "moq": "MOQ y MATERIALES", "about": "SOBRE NOSOTROS", "t": "¡Gracias!", "m": "Su consulta ha sido enviada."},
    "fr": {"lang": "fr", "title": "Contact - Aiz Jewelry", "back": "Retour à l'accueil", "copy": "Copier", "copied": "Copié !", "quote": "Obtenir un devis", "products": "PRODUITS", "custom": "PROCESSUS PERSONNALISÉ", "sus": "DURABILITÉ", "flow": "FLUX DE TRAVAIL", "moq": "MOQ et MATÉRIAUX", "about": "À PROPOS DE NOUS", "t": "Merci !", "m": "Votre demande a été envoyée."},
    "jp": {"lang": "jp", "title": "お問い合わせ - Aiz Jewelry", "back": "ホームに戻る", "copy": "コピー", "copied": "コピーしました！", "quote": "お見積り依頼", "products": "製品紹介", "custom": "カスタムプロセス", "sus": "サステナビリティ", "flow": "ワークフロー", "moq": "MOQ素材", "about": "私たちについて", "t": "ありがとうございます！", "m": "お問い合わせが送信されました。"},
    "kr": {"lang": "kr", "title": "문의하기 - Aiz Jewelry", "back": "홈으로 돌아가기", "copy": "복사", "copied": "복사됨!", "quote": "견적 요청", "products": "제품 소개", "custom": "맞춤형 프로세스", "sus": "지속 가능성", "flow": "워크플로우", "moq": "MOQ 소재", "about": "회사 소개", "t": "감사합니다!", "m": "문의가 전송되었습니다."},
    "pt": {"lang": "pt", "title": "Contato - Aiz Jewelry", "back": "Voltar ao início", "copy": "Copiar", "copied": "Copiado!", "quote": "Obter orçamento", "products": "PRODUTOS", "custom": "PROCESSO PERSONALIZADO", "sus": "SUSTENTABILIDADE", "flow": "FLUXO DE TRABALHO", "moq": "MOQ e MATERIAIS", "about": "SOBRE NÓS", "t": "Obrigado!", "m": "Sua consulta foi enviada."}
}

def write_contact_page(folder, c):
    path = os.path.join(base_dir, folder, "contact.html")
    html = f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['title']}</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>main {{ padding-top: 140px; padding-bottom: 80px; background: #fff; min-height: 80vh; display: flex; align-items: center; }} #contact {{ width: 100%; padding: 0 !important; }}</style>
</head>
<body>
    <header class="header"><nav class="container nav-container"><a href="index.html" class="logo"><img src="https://sc02.alicdn.com/kf/Se1318a00bc9742468f7f2b69415cb0b7e.png" alt="Aiz Jewelry Logo"><div class="logo-text"><span class="brand-name">AIZ</span><span class="brand-sub">JEWELRY</span></div></a><div class="nav-links"><a href="index.html#products">{c['products']}</a><a href="index.html#custom">{c['custom']}</a><a href="index.html#sustainability">{c['sus']}</a><a href="index.html#workflow">{c['flow']}</a><a href="index.html#moq">{c['moq']}</a><a href="index.html#about">{c['about']}</a><div class="lang-switcher"><button class="lang-btn">{c['lang'].upper()}</button><div class="lang-dropdown"><a href="../index.html">EN</a><a href="../de/index.html">DE</a><a href="../es/index.html">ES</a><a href="../fr/index.html">FR</a><a href="../jp/index.html">JP</a><a href="../kr/index.html">KR</a><a href="../pt/index.html">PT</a></div></div><a href="contact.html" class="nav-cta">{c['quote']}</a></div></nav></header>
    <main><section id="contact" class="contact section"><div class="container"><div class="contact-card"><div class="contact-info"><h2>Collaborate with Your Brand Partner</h2><p>Discuss your unique brand vision with our specialized team. We excel in small-batch flexible production, tailored specifically for independent jewelry brands.</p><div class="contact-details"><div class="contact-item"><span>Direct Email</span><div class="copy-box" onclick="copyText('sales@aizjewelry.com', this)"><strong>sales@aizjewelry.com</strong><span class="copy-hint">{c['copy']}</span></div></div><div class="contact-item"><span>WhatsApp Direct</span><a href="https://wa.me/8618902465287" target="_blank" class="whatsapp-secure-btn"><img src="/images/whatsapp-logo.png?v=20260714-8" alt="WhatsApp"><strong>Start Inquiry</strong></a></div><div class="contact-item"><span>Company Address:</span><strong style="font-size: 0.85rem; font-weight: 600;">B05 2F Baolin Building, Cuizhu Street, LuoHu, Shenzhen</strong></div></div></div><div class="contact-form"><form class="inquiry-form" action="https://formsubmit.co/sales@aizjewelry.com" method="POST" enctype="multipart/form-data"><div class="form-group"><label>Business Email</label><input type="email" name="email" id="form-email" required></div><div class="form-group"><label>Core Material</label><select name="material" id="form-material" required><option value="">Select Material Interest</option><option value="Stainless Steel">Stainless Steel (SUS304 / SUS316)</option><option value="925 Silver">925 Sterling Silver (S925)</option><option value="Solid K-Gold">Solid K-Gold (9K/14K/18K)</option></select></div><div class="form-group"><label>Project Vision</label><textarea name="message" id="form-message" rows="4" required></textarea></div><div class="form-group"><label>Upload Designs / References (Max 10MB)</label><div class="file-input-wrapper"><span class="custom-file-btn">Choose File</span><span class="file-name-display">No file chosen</span><input type="file" name="attachment" accept="image/*,.pdf,.doc,.docx" class="file-input" onchange="updateFileName(this)"></div></div><button type="submit" class="btn primary">Inquire Now</button><div class="thank-you-inline" style="display: none; text-align: center; padding: 40px 20px; background: #f9f9f9; border: 1px solid #eee; border-radius: 4px; margin-top: 20px;"><div style="font-size: 3rem; color: #c5a059; margin-bottom: 20px;">✓</div><h3 style="font-family: 'Bodoni Moda', serif; font-size: 1.8rem; margin-bottom: 15px;">{c['t']}</h3><p style="color: #666; line-height: 1.6;">{c['m']}</p></div></form><div class="back-home-wrapper"><a href="index.html" class="back-home-btn">← {c['back']}</a></div></div></div></div></section></main>
    <footer><div class="container footer-content"><p>&copy; 2026 Shenzhen Aiz Jewelry Co., Ltd. All Rights Reserved.</p></div></footer>
    <script src="../script.js"></script><script>function scrollToTop() {{ window.scrollTo({{ top: 0, behavior: 'smooth' }}); }} function copyText(text, element) {{ navigator.clipboard.writeText(text).then(() => {{ const hint = element.querySelector('.copy-hint'); hint.innerText = '{c['copied']}'; setTimeout(() => {{ hint.innerText = '{c['copy']}'; }}, 2000); }}); }}</script>
</body></html>"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {path}")

for lang, c in configs.items():
    write_contact_page(lang, c)
