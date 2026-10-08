import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'const arrowIcon = isUp \? \".*?\" : \".*?\";', 'const arrowIcon = isUp ? "?" : "?";', content)
with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
