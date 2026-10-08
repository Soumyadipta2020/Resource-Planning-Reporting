import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('selectedWeek: "wk23"', 'selectedWeek: "wk38"')
content = content.replace('wkNum - 23', 'wkNum - 38')
content = content.replace('date: "22 Jun 2026"', 'date: "5 Oct 2026"')
content = content.replace('1 Jun 2026 (WK 23)', '14 Sep 2026 (WK 38)')

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
