import os

def final_text_fix(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 强制替换所有可能的变体
    replacements = {
        "Send Project Brief": "Inquire Now",
        "SEND PROJECT BRIEF": "INQUIRE NOW",
        "project brief has been sent": "inquiry has been sent"
    }
    
    changed = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changed = True
    
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED: {file_path}")

base_dir = r"E:\AizJewelry_Project"
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            final_text_fix(os.path.join(root, file))
