import os

base_dir = r"E:\AizJewelry_Project"

def final_flush(file_path):
    if not os.path.exists(file_path): return
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 强制更新引用，确保加载 v1.2 最新逻辑
        new_content = content.replace('script.js?v=1.1', 'script.js?v=1.2')
        new_content = new_content.replace('script.js', 'script.js?v=1.2')
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Busted: {file_path}")
    except Exception as e:
        print(f"Err: {e}")

# 1. 刷新 HTML 中的脚本引用
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            final_flush(os.path.join(root, file))

# 2. 物理删除 script.js 中任何残余的 alert 逻辑
js_path = os.path.join(base_dir, "script.js")
if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # 彻底移除报错框逻辑
    if "alert(" in js_content:
        import re
        js_content = re.sub(r'alert\(.*?\);', '', js_content)
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
        print("Alerts removed from script.js")
