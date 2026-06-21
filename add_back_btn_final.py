import os

base_dir = r"E:\AizJewelry_Project"
langs = {
    ".": "BACK TO HOME",
    "de": "ZURÜCK ZUR STARTSEITE",
    "es": "VOLVER AL INICIO",
    "fr": "RETOUR À L'ACCUEIL",
    "jp": "ホームに戻る",
    "kr": "홈으로 돌아가기",
    "pt": "VOLTAR AO INÍCIO"
}

def add_premium_back_button(folder, back_text):
    path = os.path.join(base_dir, folder, "contact.html")
    if not os.path.exists(path): return
    
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 定义高级感返回按钮 HTML
        back_btn_html = f'''
                        <div class="back-home-wrapper" style="text-align: right; margin-top: 35px; border-top: 1px solid #eee; padding-top: 25px;">
                            <a href="index.html" class="back-home-premium" style="display: inline-block; padding: 12px 35px; border: 1px solid #111; color: #111; text-decoration: none; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; transition: all 0.3s ease; background: transparent;">← {back_text}</a>
                        </div>
                        <style>
                            .back-home-premium:hover {{ background: #111 !important; color: #fff !important; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }}
                        </style>
                    '''
        
        # 插入位置：就在 </form> 后面，但在右侧白区的 div 闭合前
        if 'back-home-premium' not in content:
            if '</form>' in content:
                content = content.replace('</form>', '</form>' + back_btn_html)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added Back Button: {path}")
    except Exception as e:
        print(f"Err on {path}: {e}")

for folder, text in langs.items():
    add_premium_back_button(folder, text)
