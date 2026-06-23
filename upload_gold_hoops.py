import os

base_dir = r"E:\AizJewelry_Project"
image_url = "https://sc02.alicdn.com/kf/Sf6054a7ea9944d158f38dac771dfc861s.png"

# 各语言翻译配置
products = {
    ".": {
        "name": "14K Solid Gold Geometric Octagon Huggie Hoops",
        "desc": "Everyday essential geometric statement earrings. Minimalist octagon silhouette with high-mirror polish."
    },
    "de": {
        "name": "14K Massivgold Geometrische Oktogon Huggie Hoops",
        "desc": "Geometrische Statement-Ohrringe für den Alltag. Minimalistische Oktogon-Silhouette mit Hochglanzpolitur."
    },
    "es": {
        "name": "Huggie Hoops Geométricos de Oro Sólido de 14K",
        "desc": "Pendientes geométricos esenciales para el día a día. Silueta de octágono minimalista con pulido de alto espejo."
    },
    "fr": {
        "name": "Créoles Huggie Géométriques en Or Massif 14K",
        "desc": "Boucles d'oreilles géométriques essentielles au quotidien. Silhouette octogonale minimaliste avec poli miroir."
    },
    "jp": {
        "name": "14K ソリッドゴールド ジオメトリック オクタゴン ハギーフープ",
        "desc": "エブリデイ・エッセンシャルな幾何学デザイン。ハイミラーポリッシュ仕上げのミニマルなオクタゴンシルエット。"
    },
    "kr": {
        "name": "14K 솔리드 골드 기하학적 옥타곤 허기 후프",
        "desc": "일상의 필수적인 기하학적 스테이트먼트 이어링. 하이 미러 폴리시 마감의 미니멀한 옥타곤 실루엣."
    },
    "pt": {
        "name": "Argolas Huggie Geométricas de Ouro Maciço 14K",
        "desc": "Brincos geométricos essenciais para o dia a dia. Silhueta de octógono minimalista com polimento de alto espelho."
    }
}

def add_product_to_html(folder, p_info):
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path): return

    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 寻找 K Gold > Earrings 锚点
    # 逻辑：寻找 <section id="gold-category" ... data-category="earrings"> 后的第一个 grid
    new_item = f'''
                    <div class="product-item" data-category="earrings">
                        <div class="product-img-wrapper">
                            <img src="{image_url}" alt="{p_info['name']}">
                            <div class="product-overlay">
                                <a href="contact.html" class="view-details-btn">INQUIRE NOW</a>
                            </div>
                        </div>
                        <div class="product-info-grid">
                            <h3>{p_info['name']}</h3>
                            <p>{p_info['desc']}</p>
                        </div>
                    </div>'''

    # 定位插入位置：在 K Gold 的 grid 开头插入
    # 根据之前 grep，K Gold 在 319 行，Earrings 在 359 行
    # 查找特定标记 <!-- Earrings Grid Start --> 或者根据结构定位
    grid_marker = '<div class="product-grid" data-category="earrings">'
    
    # 因为页面有多个 earrings grid (Stainless/Silver/Gold)，我们需要定位在 K Gold 板块内的那一个
    gold_marker = 'id="gold-category"'
    if gold_marker in content:
        parts = content.split(gold_marker)
        if grid_marker in parts[1]:
            grid_parts = parts[1].split(grid_marker, 1)
            new_html = parts[0] + gold_marker + grid_parts[0] + grid_marker + new_item + grid_parts[1]
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"Product uploaded to: {path}")

for lang, info in products.items():
    add_product_to_html(lang if lang != "." else "", info)
