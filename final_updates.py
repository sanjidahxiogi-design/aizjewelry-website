import os

translations = {
    ".": "Back to Home",
    "de": "Zurück zur Startseite",
    "es": "Volver al inicio",
    "fr": "Retour à l'accueil",
    "jp": "ホームに戻る",
    "kr": "홈으로 돌아가기",
    "pt": "Voltar ao início"
}

base_dir = r"E:\AizJewelry_Project"

def update_html_files(folder, lang_code):
    dir_path = os.path.join(base_dir, folder) if folder != "." else base_dir
    
    # 1. Update index.html
    index_path = os.path.join(dir_path, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Replace submit button text
        content = content.replace('SEND PROJECT BRIEF', 'INQUIRE NOW')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated index.html in {folder}")

    # 2. Update contact.html
    contact_path = os.path.join(dir_path, "contact.html")
    if os.path.exists(contact_path):
        with open(contact_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace submit button text
        content = content.replace('SEND PROJECT BRIEF', 'INQUIRE NOW')
        
        # Add Back to Home button if not present
        back_text = translations.get(folder, translations["."])
        back_btn_html = f'<a href="index.html" class="back-home-btn">← {back_text}</a>'
        
        if '<main>' in content and 'back-home-btn' not in content:
            content = content.replace('<main>', f'<main>\n    <div class="container" style="padding-top: 20px;">\n        {back_btn_html}\n    </div>')
        
        with open(contact_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated contact.html in {folder}")

for lang in translations.keys():
    update_html_files(lang, lang)
