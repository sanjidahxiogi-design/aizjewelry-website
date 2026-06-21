import os

base_dir = r"E:\AizJewelry_Project"
langs = ["", "de/", "es/", "fr/", "jp/", "kr/", "pt/"]

def extreme_mirror_fix(lang_path):
    index_file = os.path.join(base_dir, lang_path, "index.html")
    contact_file = os.path.join(base_dir, lang_path, "contact.html")
    
    if not os.path.exists(index_file): return
    
    try:
        # 1. 直接读取首页最完美的源码
        with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
            full_html = f.read()
        
        # 2. 注入核心隐藏样式和反馈逻辑
        # 隐藏首页 Hero、产品等板块，只留导航、询盘和页脚
        css_inject = """<style>
            .hero, section:not(#contact), .product-category-nav, .material-section { display: none !important; }
            #contact { display: block !important; padding-top: 150px !important; min-height: 85vh; background: #fff; }
            .thank-you-inline { display: none; text-align: center; padding: 40px 0; }
            .thank-you-inline.active { display: block !important; }
            .back-home-btn-premium { display: inline-block; padding: 12px 35px; border: 2px solid #111; color: #111; text-decoration: none; font-weight: 700; margin-top: 30px; text-transform: uppercase; }
        </style>"""
        
        js_inject = """<script>
            document.addEventListener('DOMContentLoaded', function() {
                const form = document.querySelector(".inquiry-form");
                if(form) {
                    form.onsubmit = function(e) {
                        e.preventDefault();
                        this.style.display = "none";
                        const ty = document.querySelector(".thank-you-inline");
                        if(ty) { ty.style.display = "block"; ty.scrollIntoView({behavior:"smooth", block:"center"}); }
                        fetch("https://formsubmit.co/ajax/sales@aizjewelry.com", {method:"POST", body:new FormData(this), headers:{"Accept":"application/json"}});
                    };
                }
            });
        </script>"""
        
        # 物理替换
        new_html = full_html.replace('</head>', css_inject + '</head>')
        new_html = new_html.replace('</body>', js_inject + '</body>')
        new_html = new_html.replace('href="#contact"', 'href="contact.html"')
        
        # 强制物理覆盖被锁定的文件
        with open(contact_file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"ULTRA FIXED: {contact_file}")
    except Exception as e:
        print(f"Error on {contact_file}: {e}")

for l in langs:
    extreme_mirror_fix(l)
