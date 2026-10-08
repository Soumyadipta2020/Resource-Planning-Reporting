import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'forecast: metric.forecast.map(v => {',
    'forecast: metric.forecast.map((v, i) => {'
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
