import os
import re

base_dir = r"E:\AizJewelry_Project"

def physical_repair_contact(rel_path, back_text, ty_title, ty_body):
    path = os.path.join(base_dir, rel_path)
    if not os.path.exists(path): return
    
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. 强制统一按钮
    content = re.sub(r'<button type="submit" class="btn primary">.*?</button>', '<button type="submit" class="btn primary">INQUIRE NOW</button>', content)
    
    # 2. 物理插入感谢模块和底部返回链接（放置在表单结束前和容器内）
    repair_block = f'''
                    <div class="thank-you-inline" style="display: none; text-align: center; padding: 60px 20px; background: #fff;">
                        <div style="font-size: 4rem; color: #c5a059; margin-bottom: 25px;">✓</div>
                        <h3 style="font-family: 'Bodoni Moda', serif; font-size: 2.2rem; margin-bottom: 15px;">{ty_title}</h3>
                        <p style="color: #666; font-size: 1.1rem;">{ty_body}</p>
                        <div style="margin-top: 40px;"><a href="index.html" style="display: inline-block; padding: 12px 35px; border: 1px solid #111; color: #111; text-decoration: none; font-weight: 700; text-transform: uppercase;">{back_text}</a></div>
                    </div>
                </form>
                <div id="back-home-bottom" style="text-align: right; margin-top: 30px;">
                    <a href="index.html" style="color: #bbb; text-decoration: none; font-size: 0.8rem;">← {back_text}</a>
                </div>
            </div>
        </div>
    </div>
</section>'''

    # 精准定位替换：找到表单结束的部分
    content = re.sub(r'</form>.*?</section>', repair_block, content, flags=re.DOTALL)
    
    # 3. 强制清理版本号并刷新到 v3.0
    content = re.sub(r'script\.js\?v=[\d\.]+(\?v=[\d\.]+)*', 'script.js?v=3.0', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Physically Repaired: {rel_path}")

# 配置翻译
configs = [
    ("contact.html", "BACK TO HOME", "Thank you!", "Your inquiry has been sent. We will contact you within 12 hours."),
    ("de/contact.html", "ZURÜCK ZUR STARTSEITE", "Vielen Dank!", "Ihre Anfrage wurde gesendet. Wir antworten in 12h."),
    ("es/contact.html", "VOLVER AL INICIO", "¡Gracias!", "Su consulta ha sido enviada. Le contactaremos en 12h."),
    ("fr/contact.html", "RETOUR À L'ACCUEIL", "Merci !", "Demande envoyée. Réponse sous 12h."),
    ("jp/contact.html", "ホームに戻る", "ありがとうございます！", "送信されました。12時間以内に返信します。"),
    ("kr/contact.html", "홈으로 돌아가기", "감사합니다!", "전송되었습니다. 12시간 이내에 답변드리겠습니다."),
    ("pt/contact.html", "VOLTAR AO INÍCIO", "Obrigado!", "Sua consulta foi enviada. Responderemos em 12h.")
]

for cfg in configs:
    physical_repair_contact(cfg[0], cfg[1], cfg[2], cfg[3])
