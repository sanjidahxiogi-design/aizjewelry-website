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

def create_contact_page(lang_dir):
    # Determine source paths
    index_path = os.path.join(r"E:\AizJewelry_Project", lang_dir, "index.html")
    contact_path = os.path.join(r"E:\AizJewelry_Project", lang_dir, "contact.html")
    
    if not os.path.exists(index_path):
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        full_content = f.read()

    # Extract Header (from start to end of nav)
    # We'll take everything until the first <section> or similar
    header_end_tag = '</nav>'
    header_content = full_content.split(header_end_tag)[0] + header_end_tag + "\n    </header>"
    
    # Extract Contact Section
    start_marker = '<section id="contact"'
    end_marker = '</section>'
    if start_marker in full_content:
        contact_section = start_marker + full_content.split(start_marker)[1].split(end_marker)[0] + end_marker
    else:
        print(f"Contact section not found in {index_path}")
        return

    # Extract Footer (from <footer to end)
    footer_start_tag = '<footer'
    footer_content = footer_start_tag + full_content.split(footer_start_tag)[1]

    # Combine into a clean page
    # We need to wrap it in proper body and main tags
    contact_page_content = f"""<!DOCTYPE html>
<html lang="{languages[lang_dir]}">
<head>
    {full_content.split('<head>')[1].split('</head>')[0]}
</head>
<body>
    {header_content}
    
    <main style="padding-top: 120px; padding-bottom: 80px;">
        {contact_section}
    </main>

    {footer_content}
</body>
</html>"""

    with open(contact_path, 'w', encoding='utf-8') as f:
        f.write(contact_page_content)
    print(f"Created: {contact_path}")

for lang in languages.keys():
    create_contact_page(lang)
