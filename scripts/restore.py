with open('index.html', 'r', encoding='utf-8') as f: content = f.read()
content = content.replace('<div class="w-full shadow-sm rounded border border-slate-200">', '<div class="overflow-x-auto w-full shadow-sm rounded border border-slate-200">')
with open('index.html', 'w', encoding='utf-8') as f: f.write(content)

with open('js/app.js', 'r', encoding='utf-8') as f: content = f.read()
content = content.replace('<div class="w-full shadow-sm rounded border border-slate-200">', '<div class="overflow-x-auto w-full shadow-sm rounded border border-slate-200">')
with open('js/app.js', 'w', encoding='utf-8') as f: f.write(content)

with open('js/charts.js', 'r', encoding='utf-8') as f: content = f.read()
content = content.replace('<div class="w-full">\n        <table class="w-full text-[10px] text-center border-collapse">', '<div class="overflow-x-auto w-full">\n        <table class="w-full text-[10px] text-center border-collapse">')
with open('js/charts.js', 'w', encoding='utf-8') as f: f.write(content)
