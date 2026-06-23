import os

base_dir = r"E:\AizJewelry_Project"
langs = ["", "de", "es", "fr", "jp", "kr", "pt"]

def surgical_cleanup(folder):
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path): return
    
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    new_lines = []
    skip = False
    skip_count = 0
    
    # 物理定位：精准匹配需要删除的卡片内容
    targets_to_remove = ["Boutique Pendant", "Artisan Hoops", "Boutique-Anhänger", "Artisan-Creolen", "ブティック・ペンダント", "職人によるフープピアス"]

    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 如果当前行包含需要删除的产品标题
        if any(target in line for target in targets_to_remove):
            # 向上回溯寻找 <div class="product-card"
            back_idx = len(new_lines) - 1
            while back_idx >= 0 and '<div class="product-card"' not in new_lines[back_idx]:
                new_lines.pop()
                back_idx -= 1
            if back_idx >= 0:
                new_lines.pop() # 移除 <div class="product-card" 这一行
            
            # 向下跳过直到闭合的 </div>
            while i < len(lines) and '</div>' not in lines[i]:
                i += 1
            # 再多跳两行以处理嵌套闭合
            i += 2
            print(f"Surgically removed a duplicate from {path}")
            continue
            
        new_lines.append(line)
        i += 1

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

for l in langs:
    surgical_cleanup(l)
