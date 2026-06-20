import os

languages = {
    ".": "en",
    "de": "de",
    "es": "es",
    "fr": "fr",
    "jp": "jp",
    "kr": "kr",
    "pt": "pt"
}

base_dir = r"E:\AizJewelry_Project"

def create_contact_page(lang_dir):
    source_dir = os.path.join(base_dir, lang_dir) if lang_dir != "." else base_dir
    index_path = os.path.join(source_dir, "index.html")
    contact_path = os.path.join(source_dir, "contact.html")
    
    if not os.path.exists(index_path):
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        full_content = f.read()

    # Extract Header (from start to end of nav)
    header_end_tag = '</nav>'
    if header_end_tag in full_content:
        header_content = full_content.split(header_end_tag)[0] + header_end_tag + "\n    </header>"
    else:
        return

    # Extract Contact Section
    start_marker = '<section id="contact"'
    end_marker = '</section>'
    if start_marker in full_content:
        contact_section = start_marker + full_content.split(start_marker)[1].split(end_marker)[0] + end_marker
    else:
        return

    # Extract Footer
    footer_start_tag = '<footer'
    if footer_start_tag in full_content:
        footer_content = footer_start_tag + full_content.split(footer_start_tag)[1]
    else:
        return

    # Create Page
    contact_page_content = f"""<!DOCTYPE html>
<html lang="{languages[lang_dir]}">
<head>
    {full_content.split('<head>')[1].split('</head>')[0]}
    <style>
        main {{ padding-top: 140px; padding-bottom: 80px; background: #fff; min-height: 80vh; display: flex; align-items: center; }}
        #contact {{ width: 100%; padding: 0 !important; }}
    </style>
</head>
<body>
    {header_content}
    <main>
        {contact_section}
    </main>
    {footer_content}
</body>
</html>"""

    with open(contact_path, 'w', encoding='utf-8') as f:
        f.write(contact_page_content)
    print(f"Created: {contact_path}")

# 1. Create all contact.html pages
for lang in languages.keys():
    create_contact_page(lang)

# 2. Update navigation links in all index.html and contact.html
def update_nav_links(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'href="#contact"' in content:
        new_content = content.replace('href="#contact"', 'href="contact.html"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated links: {file_path}")

for lang in languages.keys():
    folder = os.path.join(base_dir, lang) if lang != "." else base_dir
    update_nav_links(os.path.join(folder, "index.html"))
    update_nav_links(os.path.join(folder, "contact.html"))
