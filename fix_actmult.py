import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'const num = parseInt(val.replace(/,/g, "")) * actMult;',
    'const num = parseInt(val.replace(/,/g, "")) * fcMult;'
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
