import os

base_dir = r"E:\AizJewelry_Project"

def mirror_fix(folder, lang_code, back_text):
    index_path = os.path.join(base_dir, folder, "index.html")
    contact_path = os.path.join(base_dir, folder, "contact.html")
    
    if not os.path.exists(index_path): return

    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. 注入 CSS：隐藏首页多余部分，保持首页 100% 颜值
    # 我们不在 HTML 里乱改类名，只通过样式显隐
    css_inject = """
    <style>
        /* 强制隐藏首页其他所有板块，只留导航、询盘和页脚 */
        .hero, .products, .sustainability, .workflow, .moq, .about, .material-section, .product-category-nav, .insights { 
            display: none !important; 
        }
        #contact { 
            display: block !important; 
            padding-top: 160px !important; 
            min-height: 80vh; 
        }
        /* 提交成功后的感谢界面样式 */
        .thank-you-inline { display: none !important; text-align: center; padding: 40px 0; }
        .thank-you-inline.active { display: block !important; }
        /* 强力返回按钮样式 */
        .premium-btn-home { 
            display: inline-block; background: #111; color: #fff !important; 
            padding: 14px 40px; text-decoration: none; font-weight: 700; 
            letter-spacing: 2px; margin-top: 30px; text-transform: uppercase;
        }
        .premium-btn-home:hover { background: #333; box-shadow: 0 10px 30px rgba(0,0,0,0.15); }
    </style>
    """
    
    # 2. 注入 JS：物理插入按钮 + 锁定反馈逻辑
    js_inject = f"""
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const form = document.querySelector(".inquiry-form");
            const whiteArea = document.querySelector(".contact-form");
            
            // 物理插入返回按钮到白区右下角
            if(whiteArea) {{
                const bWrap = document.createElement("div");
                bWrap.style.cssText = "text-align: right; margin-top: 40px; border-top: 1px solid #eee; padding-top: 20px;";
                bWrap.id = "UI-BACK-WRAP";
                bWrap.innerHTML = `<a href="index.html" class="premium-btn-home" style="padding:10px 25px; font-size:0.75rem;">← {back_text}</a>`;
                whiteArea.appendChild(bWrap);
            }}

            // 锁定反馈逻辑
            if(form) {{
                // 插入隐藏的感谢模块
                const ty = document.createElement("div");
                ty.className = "thank-you-inline";
                ty.id = "UI-THANK-YOU";
                ty.innerHTML = `
                    <div style="font-size:4.5rem; color:#c5a059; margin-bottom:20px;">✓</div>
                    <h2 style="font-family:'Bodoni Moda', serif; font-size:2.5rem; color:#111;">Thank you!</h2>
                    <p style="color:#666;">Your inquiry has been sent.</p>
                    <a href="index.html" class="premium-btn-home">BACK TO HOME</a>`;
                form.parentNode.insertBefore(ty, form.nextSibling);

                form.onsubmit = function(e) {{
                    e.preventDefault();
                    this.style.setProperty("display", "none", "important");
                    document.getElementById("UI-BACK-WRAP").style.setProperty("display", "none", "important");
                    const tyBlock = document.getElementById("UI-THANK-YOU");
                    tyBlock.classList.add("active");
                    tyBlock.style.setProperty("display", "block", "important");
                    tyBlock.scrollIntoView({{behavior: "smooth", block: "center"}});
                    fetch("https://formsubmit.co/ajax/sales@aizjewelry.com", {{method:"POST", body:new FormData(this)}});
                }};
            }}
        }});
    </script>
    """

    # 执行合并
    new_html = html.replace('</head>', css_inject + '</head>')
    new_html = new_html.replace('</body>', js_inject + '</body>')
    new_html = new_html.replace('href="#contact"', 'href="contact.html"')
    # 统一按钮文案
    new_html = new_html.replace('SEND PROJECT BRIEF', 'INQUIRE NOW').replace('Send Project Brief', 'Inquire Now')

    # 物理写入
    with open(contact_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"MIRROR FIXED: {contact_path}")

# 执行各语种修复
tasks = [
    (".", "BACK TO HOME"),
    ("de", "ZURÜCK ZUR STARTSEITE"),
    ("es", "VOLVER AL INICIO"),
    ("fr", "RETOUR À L'ACCUEIL"),
    ("jp", "ホームに戻る"),
    ("kr", "홈으로 돌아가기"),
    ("pt", "VOLTAR AO INÍCIO")
]

for folder, back in tasks:
    mirror_fix(folder if folder != "." else "", folder, back)
