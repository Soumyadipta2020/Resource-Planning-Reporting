import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'<th class="py-1 px-1 bg-cyan-700 border-r border-cyan-600">Forecast</th>\s*<th class="py-1 px-1 bg-cyan-700 border-r border-cyan-600">Actual</th>',
    '<th class="py-1 px-1 bg-cyan-700 border-r border-cyan-600">Actual</th>\\n                <th class="py-1 px-1 bg-cyan-700 border-r border-cyan-600">Forecast</th>',
    content
)

old_td = '''html += <td class="py-1 px-1 text-right bg-cyan-50/40 text-slate-800 \>\</td>;
        html += <td class="py-1 px-1 text-right bg-cyan-50/40 text-slate-900 \>\</td>;'''
new_td = '''html += <td class="py-1 px-1 text-right bg-cyan-50/40 text-slate-900 \>\</td>;
        html += <td class="py-1 px-1 text-right bg-cyan-50/40 text-slate-800 \>\</td>;'''

content = content.replace(old_td, new_td)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app.js")
