import os

base_dir = r"E:\AizJewelry_Project"
image_url = "https://sc02.alicdn.com/kf/Sf6054a7ea9944d158f38dac771dfc861s.png"

# 各语言配置
trans = {
    ".": ("14K Solid Gold Geometric Octagon Huggie Hoops", "Everyday essential statement earrings with high-mirror polish."),
    "de": ("14K Massivgold Geometrische Oktogon Huggie Hoops", "Geometrische Statement-Ohrringe für den Alltag."),
    "es": ("Huggie Hoops Geométricos de Oro Sólido de 14K", "Pendientes esenciales con pulido de alto espejo."),
    "fr": ("Créoles Huggie Géométriques en Or Massif 14K", "Boucles d'oreilles essentielles avec poli miroir."),
    "jp": ("14K ソリッドゴールド オクタゴン ハギーフープ", "ハイミラーポリッシュ仕上げのミニマルデザイン。"),
    "kr": ("14K 솔리드 골드 옥타곤 허기 후프", "하이 미러 폴리시 마감의 기하학적 스테이트먼트 이어링."),
    "pt": ("Argolas Huggie Geométricas de Ouro Maciço 14K", "Brincos essenciais com polimento de espelho.")
}

def force_upload_product(folder, t):
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path): return

    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    new_item = f'''
                    <!-- New Arrival: Octagon Hoops -->
                    <div class="product-card" data-category="earrings">
                        <div class="product-card-image">
                            <img src="{image_url}" alt="{t[0]}">
                        </div>
                        <div class="product-card-info">
                            <h4>Solid K-Gold</h4>
                            <h3>{t[0]}</h3>
                            <p>{t[1]}</p>
                        </div>
                    </div>'''

    # 定位点：在现有 Artisan Hoops 后面插入，确保 100% 显示在 Gold 板块
    if 'Artisan Hoops</h3>' in html:
        html = html.replace('Meticulously executed for the luxury boutique market.</p>', 
                           'Meticulously executed for the luxury boutique market.</p>\n                        </div>\n                    </div>' + new_item)
    elif 'data-category="earrings"' in html:
        # 备选定位
        html = html.replace('<div class="product-card" data-category="earrings">', new_item + '\n                    <div class="product-card" data-category="earrings">')

    # 强制刷新缓存版本号
    html = html.replace('style.css?v=20260714-4', 'style.css?v=20260714-4')
    html = html.replace('script.js?v=2.1', 'script.js?v=30.1')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"FORCED UPLOADED: {path}")

for folder, t in trans.items():
    force_upload_product(folder if folder != "." else "", t)
