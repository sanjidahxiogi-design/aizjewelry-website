import os
import re

base_dir = r"E:\AizJewelry_Project"

def move_thank_you_outside(file_path):
    if not os.path.exists(file_path): return
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 匹配 thank-you-inline 块
        # 模式：匹配从 <div class="thank-you-inline" 到 </div> 的完整块
        ty_pattern = re.compile(r'<div class="thank-you-inline".*?</div>\s*</div>', re.DOTALL)
        match = ty_pattern.search(content)
        
        if match:
            ty_block = match.group(0)
            # 1. 从原位置删除（假设它在 </form> 之前）
            content_cleaned = content.replace(ty_block, "")
            # 2. 重新插入到 </form> 之后
            new_content = content_cleaned.replace('</form>', '</form>\n' + ty_block)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Structure Adjusted: {file_path}")
    except Exception as e:
        print(f"Error adjusting {file_path}: {e}")

# 遍历并处理
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            move_thank_you_outside(os.path.join(root, file))
