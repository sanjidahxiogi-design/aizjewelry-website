import os

back_translations = {
    ".": "Back to Home",
    "de": "Zurück zur Startseite",
    "es": "Volver al inicio",
    "fr": "Retour à l'accueil",
    "jp": "ホームに戻る",
    "kr": "홈으로 돌아가기",
    "pt": "Voltar ao início"
}

base_dir = r"E:\AizJewelry_Project"

def restore_back_btn(folder):
    dir_path = os.path.join(base_dir, folder) if folder != "." else base_dir
    file_path = os.path.join(dir_path, "contact.html")
    
    if not os.path.exists(file_path):
        return
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 如果已经有了就跳过
    if 'back-home-wrapper' in content:
        print(f"Already exists in {file_path}")
        return

    # 插入位置：在 </form> 后面，但在 </div><!-- End Contact Card --> 或者最后一个 </div> 前面
    back_text = back_translations.get(folder, back_translations["."])
    back_html = f'''
                    <div class="back-home-wrapper">
                        <a href="index.html" class="back-home-btn">← {back_text}</a>
                    </div>
                </form>'''
    
    if '</form>' in content:
        new_content = content.replace('</form>', back_html)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"RESTORED BACK BTN: {file_path}")

for lang in back_translations.keys():
    restore_back_btn(lang)
