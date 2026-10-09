with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re
content = re.sub(
    r'const isBold = \["FTE".*?\]\.includes\(row\.metric\);',
    'const isBold = ["DL Headcount", "DL Gross Hours", "Total DL Downtime", "DL Available Hours", "DL Productive Hrs", "DL Utilisation %"].includes(row.metric);',
    content,
    flags=re.DOTALL
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated bold logic')
