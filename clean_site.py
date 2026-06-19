
import os
import re

bad_img = 'https://sc02.alicdn.com/kf/A8112e0a07a6a46e4801bd1059a81addfW.png'
files = ['index.html', 'es/index.html', 'fr/index.html', 'de/index.html', 'pt/index.html', 'jp/index.html', 'kr/index.html']

for f_path in files:
    if not os.path.exists(f_path): continue
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We split by product-card and only keep ones that DONT have the bad image
    # We must preserve the content before the first card and after the last card
    
    parts = content.split('<div class="product-card"')
    new_content = parts[0] # The header part
    
    removed = 0
    for part in parts[1:]:
        # Each 'part' is the content of a card plus everything until the next card or end
        # We need to find where the card actually ends so we don't delete too much
        if bad_img in part:
            # This part contains a bad card.
            # We look for the marker that reliably ends our card block: </div>\s*</div>
            # BUT we must only remove the card part, not the trailing content of the section.
            match = re.search(r'</div>\s*</div>', part)
            if match:
                # Keep everything after the card's closing tags
                new_content += part[match.end():]
                removed += 1
            else:
                # If we can't find a clean break, skip the whole part (unsafe)
                removed += 1
        else:
            new_content += '<div class="product-card"' + part
            
    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Cleaned {f_path}, removed {removed} cards.")
