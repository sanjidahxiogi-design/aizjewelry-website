import os
import re

# 目标：统一全站提交按钮文案为 INQUIRE NOW
# 搜索模式：匹配所有包含 "Briefing" 或 "Brief" 或 "Inquiry" 且位于 <button> 标签内的文字
base_dir = r"E:\AizJewelry_Project"

def extreme_fix(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 强制定位所有提交按钮
    # 模式：<button type="submit" class="btn primary">任何文字</button>
    pattern = r'<button type="submit" class="btn primary">.*?</button>'
    new_btn = '<button type="submit" class="btn primary">Inquire Now</button>'
    
    new_content = re.sub(pattern, new_btn, content)
    
    # 2. 同时清理可能遗留的旧文案
    replacements = {
        "Send Project Brief": "Inquire Now",
        "SEND PROJECT BRIEF": "INQUIRE NOW",
        "Projekt-Briefing senden": "Inquire Now",
        "Enviar resumen del proyecto": "Inquire Now",
        "Envoyer le dossier du projet": "Inquire Now",
        "プロジェクトの概要を送信する": "Inquire Now",
        "프로젝트 브리핑 보내기": "Inquire Now",
        "Enviar resumo do projeto": "Inquire Now"
    }
    
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"ULTRA FIXED: {file_path}")

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            extreme_fix(os.path.join(root, file))
