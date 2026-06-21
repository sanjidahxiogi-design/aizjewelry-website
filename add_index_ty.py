import os
import re

base_dir = r"E:\AizJewelry_Project"
langs = ["", "de", "es", "fr", "jp", "kr", "pt"]

def add_thank_you_to_index(folder):
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path): return
    
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # 确定各语种翻译
        t, m = "Thank you!", "Your inquiry has been sent. We will contact you within 12 hours."
        if folder == "de": t, m = "Vielen Dank!", "Ihre Anfrage wurde gesendet. Wir antworten in 12h."
        elif folder == "es": t, m = "¡Gracias!", "Su consulta ha sido enviada."
        elif folder == "fr": t, m = "Merci !", "Votre demande a été envoyée."
        elif folder == "jp": t, m = "ありがとうございます！", "送信されました。12h以内に返信します。"
        elif folder == "kr": t, m = "감사합니다!", "전송되었습니다. 12시간 이내에 연락드립니다."
        elif folder == "pt": t, m = "Obrigado!", "Sua consulta foi enviada."

        # 构造感谢模块
        ty_html = f'''
                    <div class="thank-you-inline" style="display: none; text-align: center; padding: 40px 0;">
                        <div style="font-size: 4rem; color: #c5a059; margin-bottom: 20px;">✓</div>
                        <h3 style="font-family: 'Bodoni Moda', serif; font-size: 2.2rem; color: #111;">{t}</h3>
                        <p style="color: #666;">{m}</p>
                    </div>
                '''
        
        # 如果已经有了就跳过，没有就插入在 </form> 后面
        if 'thank-you-inline' not in html:
            if '</form>' in html:
                # 寻找表单卡片内的 </form>
                html = html.replace('</form>', '</form>' + ty_html)
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"Thank You added to: {path}")
    except Exception as e:
        print(f"Err on {path}: {e}")

for l in langs:
    add_thank_you_to_index(l)
