with open('js/charts.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('if (!ctx) return;', 'if (!ctx) return;\n    ctx.parentElement.style.border = "5px solid red";')

with open('js/charts.js', 'w', encoding='utf-8') as f:
    f.write(content)