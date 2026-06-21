import os

base_dir = r"E:\AizJewelry_Project"
langs = {
    ".": ("Thank you!", "Your inquiry has been sent."),
    "de": ("Vielen Dank!", "Ihre Anfrage wurde gesendet."),
    "es": ("¡Gracias!", "Su consulta ha sido enviada."),
    "fr": ("Merci !", "Votre demande a été envoyée."),
    "jp": ("ありがとうございます！", "送信されました。"),
    "kr": ("감사합니다!", "전송되었습니다."),
    "pt": ("Obrigado!", "Sua consulta foi enviada.")
}

def inject_logic_with_high_fidelity(folder, texts):
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path): return
    
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. 注入绝对反馈逻辑到 form 标签（保持类名和属性完全不动）
    html = html.replace('<form class="inquiry-form"', '<form id="FOOTER-FORM-REAL" class="inquiry-form"')
    html = html.replace('method="POST"', 'method="POST" onsubmit="event.preventDefault(); this.style.setProperty(\'display\',\'none\',\'important\'); document.getElementById(\'FOOTER-TY-REAL\').style.setProperty(\'display\',\'block\',\'important\'); fetch(\'https://formsubmit.co/ajax/sales@aizjewelry.com\', {method:\'POST\', body:new FormData(this)});"')

    # 2. 插入感谢模块（直接在 </form> 后面，物理锁定显示）
    ty_html = f'''
                </form>
                <div id="FOOTER-TY-REAL" style="display: none !important; text-align: center; padding: 40px 0;">
                    <div style="font-size: 4rem; color: #c5a059; margin-bottom: 20px;">✓</div>
                    <h3 style="font-family: 'Bodoni Moda', serif; font-size: 2.2rem; color: #111;">{texts[0]}</h3>
                    <p style="color: #666;">{texts[1]}</p>
                </div>'''
    
    if 'id="FOOTER-TY-REAL"' not in html:
        html = html.replace('</form>', ty_html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Hifi-Fixed: {path}")

for folder, t in langs.items():
    inject_logic_with_high_fidelity(folder, t)
