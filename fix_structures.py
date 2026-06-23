import os
import re

base_dir = r"E:\AizJewelry_Project"

def fix_all_html_structures(file_path):
    if not os.path.exists(file_path): return
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 1. 修复多余的 </div> 标签问题 (针对之前上新导致的错误)
        # 模式：寻找连续过多的闭合标签并精简
        bad_structure = '</div>\n                        </div>\n                    </div>\n                </div>'
        good_structure = '</div>\n                </div>'
        if bad_structure in content:
            content = content.replace(bad_structure, good_structure)
        
        # 2. 强刷脚本版本号到 v30.2
        content = re.sub(r'script\.js\?v=[\d\.]+', 'script.js?v=30.2', content)
        content = content.replace('script.js', 'script.js?v=30.2')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed Structure: {file_path}")
    except Exception as e:
        print(f"Err: {e}")

# 处理全站
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            fix_all_html_structures(os.path.join(root, file))
