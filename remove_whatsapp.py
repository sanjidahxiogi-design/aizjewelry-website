import os
import re

base_dir = r"E:\AizJewelry_Project"

def remove_whatsapp_info(file_path):
    if not os.path.exists(file_path): return
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # 匹配 WhatsApp 整个联系项块
        # 模式：匹配包含 WHATSAPP 和号码的 div/contact-item 块
        # 包含不同 HTML 结构下的变体
        patterns = [
            r'<div class="contact-item">\s*<span>WHATSAPP.*?0086 18902465287.*?</div>',
            r'<div class="contact-item">.*?WHATSAPP.*?WhatsApp Direct.*?</div>',
            r'<div>\s*<span style="color:#c5a059; font-size:0.75rem; text-transform:uppercase; letter-spacing:2px; display:block; margin-bottom:8px;">WHATSAPP</span>\s*<strong>0086 18902465287</strong>\s*</div>',
            r'<div class="contact-item">.*?WHATSAPP.*?</div>'
        ]

        new_content = content
        for p in patterns:
            new_content = re.sub(p, '', new_content, flags=re.DOTALL | re.IGNORECASE)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"WhatsApp Removed: {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")

# 遍历全站 HTML 文件执行删除
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            remove_whatsapp_info(os.path.join(root, file))
