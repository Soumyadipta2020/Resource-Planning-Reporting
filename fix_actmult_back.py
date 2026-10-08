import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# The first one is in row.actuals.forEach
content = re.sub(
    r'(row\.actuals\.forEach\([\s\S]*?const num = parseInt\(val\.replace\(/,/g, ""\)\) \*) fcMult;',
    r'\1 actMult;',
    content
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
