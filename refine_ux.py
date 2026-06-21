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

def refine_html_structure(folder):
    dir_path = os.path.join(base_dir, folder) if folder != "." else base_dir
    
    # Process both index.html and contact.html
    for filename in ["index.html", "contact.html"]:
        file_path = os.path.join(dir_path, filename)
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Update Submit Button Text (Case insensitive replace to be safe)
        content = content.replace('SEND PROJECT BRIEF', 'INQUIRE NOW')
        
        # 2. Re-position Back to Home button (Only for contact.html)
        if filename == "contact.html":
            # Remove existing back button if any
            import re
            content = re.sub(r'<a href="index\.html" class="back-home-btn">.*?</a>', '', content)
            content = re.sub(r'<div class="container" style="padding-top: 20px;">\s*</div>', '', content)
            
            # Place it at the bottom of the contact-card
            back_text = back_translations.get(folder, back_translations["."])
            back_html = f'''
                    <div class="back-home-wrapper">
                        <a href="index.html" class="back-home-btn">{back_text}</a>
                    </div>
                </div>''' # Place it inside the contact-card before it closes
            
            if '</div><!-- End Contact Card -->' in content:
                 content = content.replace('</div><!-- End Contact Card -->', back_html)
            elif '</div>\n            </div>\n        </div>\n    </section>' in content:
                 # Fallback if marker not found
                 content = content.replace('</div>\n            </div>\n        </div>\n    </section>', back_html + '\n        </div>\n    </section>')
            else:
                # Last resort: after the form
                content = content.replace('</form>', '</form>' + back_html)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Refined {filename} in {folder}")

for lang in back_translations.keys():
    refine_html_structure(lang)
