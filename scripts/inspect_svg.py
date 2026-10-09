import re

with open('images/uk.svg', 'r', encoding='utf-8') as f:
    text = f.read()

paths = re.findall(r'<path[^>]+id="([^"]+)"[^>]+title="([^"]+)"', text)
for pid, title in paths:
    print(f"{pid}: {title}")

