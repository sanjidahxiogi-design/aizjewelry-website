import os
import re

base_dir = r"E:\AizJewelry_Project"
langs = ["", "de", "es", "fr", "jp", "kr", "pt"]

def remove_duplicate_gold_items(folder):
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path): return
    
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # 1. 匹配并删除 Boutique Pendant 板块
        pendant_pattern = r'<!-- Necklaces -->\s*<div class="product-card" data-category="necklaces">.*?Boutique Pendant.*?</div>'
        content = re.sub(pendant_pattern, '', content, flags=re.DOTALL)

        # 2. 匹配并删除旧的 Artisan Hoops 板块 (保留新品 Octagon)
        hoops_pattern = r'<div class="product-card" data-category="earrings">\s*<div class="product-card-image">\s*<img src="https://sc02\.alicdn\.com/kf/Ac4373793ea844a68ad74ef0edc053496z\.png".*?Artisan Hoops.*?</div>'
        content = re.sub(hoops_pattern, '', content, flags=re.DOTALL)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Duplicates Removed: {path}")

    except Exception as e:
        print(f"Error on {path}: {e}")

for l in langs:
    remove_duplicate_gold_items(l)
