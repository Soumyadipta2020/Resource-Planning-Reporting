with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<canvas id="sheet5-waterfall-chart"></canvas>', '<canvas id="sheet5-waterfall-chart" width="800" height="288"></canvas>')
content = content.replace('v=11', 'v=19')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)