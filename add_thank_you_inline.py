import os

thank_you_translations = {
    ".": ("Thank you!", "Your project brief has been sent. We will contact you within 12 hours."),
    "de": ("Vielen Dank!", "Ihre Projektbeschreibung wurde gesendet. Wir werden Sie innerhalb von 12 Stunden kontaktieren."),
    "es": ("¡Gracias!", "Su informe de proyecto ha sido enviado. Nos pondremos en contacto con usted en un plazo de 12 horas."),
    "fr": ("Merci !", "Votre dossier de projet a été envoyé. Nous vous contacterons dans les 12 heures."),
    "jp": ("ありがとうございます！", "プロジェクトの概要が送信されました。12時間以内にご連絡いたします。"),
    "kr": ("감사합니다!", "프로젝트 브리핑이 전송되었습니다. 12시간 이내에 연락드리겠습니다."),
    "pt": ("Obrigado!", "O seu resumo de projeto foi enviado. Entraremos em contacto consigo no prazo de 12 horas.")
}

def update_html_with_thank_you(file_path, lang_code):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title, body = thank_you_translations.get(lang_code, thank_you_translations["."])
    
    # Define the thank you block
    thank_you_html = f'''
                    <div class="thank-you-inline" style="display: none; text-align: center; padding: 40px 20px; background: #f9f9f9; border: 1px solid #eee; border-radius: 4px; margin-top: 20px;">
                        <div style="font-size: 3rem; color: #c5a059; margin-bottom: 20px;">✓</div>
                        <h3 style="font-family: 'Bodoni Moda', serif; font-size: 1.8rem; margin-bottom: 15px;">{title}</h3>
                        <p style="color: #666; line-height: 1.6;">{body}</p>
                    </div>
                </form>'''
    
    if '</form>' in content and 'thank-you-inline' not in content:
        new_content = content.replace('</form>', thank_you_html)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")
    else:
        print(f"Skipped or already updated: {file_path}")

base_dir = r"E:\AizJewelry_Project"
for lang in ["de", "es", "fr", "jp", "kr", "pt"]:
    update_html_with_thank_you(os.path.join(base_dir, lang, "index.html"), lang)
update_html_with_thank_you(os.path.join(base_dir, "index.html"), ".")
