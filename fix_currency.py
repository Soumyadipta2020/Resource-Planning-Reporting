import re

with open('js/app.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

content = re.sub(r'A\ufffdM', '£M', content)
content = re.sub(r'AM', '£M', content)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced!")
