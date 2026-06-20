import os

translations = {
    ".": ("Choose File", "No file chosen"),
    "de": ("Datei auswählen", "Keine Datei ausgewählt"),
    "es": ("Seleccionar archivo", "Ningún archivo seleccionado"),
    "fr": ("Choisir un fichier", "Aucun fichier choisi"),
    "jp": ("ファイルを選択", "ファイルが選択されていません"),
    "kr": ("파일 선택", "선택된 파일 없음"),
    "pt": ("Escolher arquivo", "Nenhum arquivo seleccionado")
}

def update_file_input(file_path, btn_text, msg_text):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_code = '<input type="file" name="attachment" accept="image/*,.pdf,.doc,.docx" class="file-input">'
    new_code = f'''<div class="file-input-wrapper">
                            <span class="custom-file-btn">{btn_text}</span>
                            <span class="file-name-display">{msg_text}</span>
                            <input type="file" name="attachment" accept="image/*,.pdf,.doc,.docx" class="file-input" onchange="updateFileName(this)">
                        </div>'''
    
    if old_code in content:
        new_content = content.replace(old_code, new_code)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")
    else:
        print(f"Not found in: {file_path}")

base_dir = r"E:\AizJewelry_Project"
for lang, texts in translations.items():
    path = os.path.join(base_dir, lang, "index.html")
    update_file_input(path, texts[0], texts[1])
