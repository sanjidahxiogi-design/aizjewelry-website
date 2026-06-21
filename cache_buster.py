import os

base_dir = r"E:\AizJewelry_Project"

def force_version_update(file_path):
    if not os.path.exists(file_path): return
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 强制替换 script.js 引用，增加版本号 v=1.1 以清除缓存
        new_content = content.replace('script.js', 'script.js?v=1.1')
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Version Updated: {file_path}")
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

# 遍历全站 HTML 文件
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            force_version_update(os.path.join(root, file))
