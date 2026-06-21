import os

languages = {
    "de": {"lang": "de", "back": "Zurück zur Startseite", "title": "Kontakt - Aiz Jewelry"},
    "es": {"lang": "es", "back": "Volver al inicio", "title": "Contacto - Aiz Jewelry"},
    "fr": {"lang": "fr", "back": "Retour à l'accueil", "title": "Contact - Aiz Jewelry"},
    "jp": {"lang": "jp", "back": "ホームに戻る", "title": "お問い合わせ - Aiz Jewelry"},
    "kr": {"lang": "kr", "back": "홈으로 돌아가기", "title": "문의하기 - Aiz Jewelry"},
    "pt": {"lang": "pt", "back": "Voltar ao início", "title": "Contato - Aiz Jewelry"}
}

base_dir = r"E:\AizJewelry_Project"

def rebuild_contact_page(lang_dir, info):
    source_index = os.path.join(base_dir, lang_dir, "index.html")
    dest_contact = os.path.join(base_dir, lang_dir, "contact.html")
    
    if not os.path.exists(source_index): return

    with open(source_index, 'r', encoding='utf-8') as f:
        full = f.read()

    # Extract dynamic parts from index.html
    header = full.split('<header')[1].split('</header>')[0]
    contact_section = full.split('<section id="contact"')[1].split('</section>')[0]
    footer = full.split('<footer')[1].split('</footer>')[0]
    head_content = full.split('<head>')[1].split('</head>')[0]

    # Clean up the contact section if it already has thank-you or broken parts
    # (Simplified approach: We want the raw structure from index.html)
    
    new_page = f"""<!DOCTYPE html>
<html lang="{info['lang']}">
<head>
    {head_content}
    <style>
        main {{ padding-top: 140px; padding-bottom: 80px; background: #fff; min-height: 80vh; display: flex; align-items: center; }}
        #contact {{ width: 100%; padding: 0 !important; }}
    </style>
</head>
<body>
    <header {header}</header>
    
    <main>
        <section id="contact" {contact_section}</section>
    </main>

    <footer {footer}</footer>

    <div class="floating-actions">
        <button onclick="scrollToTop()" id="back-to-top" class="back-to-top-float">
            <svg viewBox="0 0 448 512"><path d="M34.9 289.5l-22.2-22.2c-9.4-9.4-9.4-24.6 0-33.9L207 39c9.4-9.4 24.6-9.4 33.9 0l194.3 194.3c9.4 9.4 9.4 24.6 0 33.9L413 289.4c-9.5 9.5-25 9.3-34.3-.4L256 161.3V464c0 13.3-10.7 24-24 24h-32c-13.3 0-24-10.7-24-24V161.3L53.2 289.1c-9.3 9.8-24.8 10-34.3.4z"/></svg>
        </button>
    </div>

    <script src="../script.js"></script>
    <script>
        function scrollToTop() {{ window.scrollTo({{ top: 0, behavior: 'smooth' }}); }}
        function copyText(text, element) {{
            navigator.clipboard.writeText(text).then(() => {{
                const hint = element.querySelector('.copy-hint');
                hint.innerText = 'Copied!';
                setTimeout(() => {{ hint.innerText = 'Copy'; }}, 2000);
            }});
        }}
    </script>
</body>
</html>"""

    # Post-process to inject the Back to Home button at the very end of contact-form
    back_btn = f'<div class="back-home-wrapper"><a href="index.html" class="back-home-btn">← {info["back"]}</a></div>'
    new_page = new_page.replace('</form>', f'</form>\n                        {back_btn}')

    with open(dest_contact, 'w', encoding='utf-8') as f:
        f.write(new_page)
    print(f"Rebuilt: {dest_contact}")

for lang, info in languages.items():
    rebuild_contact_page(lang, info)
