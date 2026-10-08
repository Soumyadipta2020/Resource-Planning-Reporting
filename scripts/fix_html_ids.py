import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add IDs to accuracy KPIs
content = content.replace('<div class="text-2xl font-bold text-slate-900 mt-1">4.8%</div>', '<div id="acc-kpi-mape" class="text-2xl font-bold text-slate-900 mt-1">4.8%</div>')
content = content.replace('<div class="text-2xl font-bold text-slate-900 mt-1">+1.2%</div>', '<div id="acc-kpi-bias" class="text-2xl font-bold text-slate-900 mt-1">+1.2%</div>')
content = content.replace('<div class="text-2xl font-bold text-slate-900 mt-1">4 Weeks</div>', '<div id="acc-kpi-lead" class="text-2xl font-bold text-slate-900 mt-1">4 Weeks</div>')

# Demand View might have hardcoded KPIs too! Let's check:
content = content.replace('<div class="text-2xl font-bold text-slate-900 mt-1 mb-1">2.8</div>', '<div id="dem-kpi-backlog" class="text-2xl font-bold text-slate-900 mt-1 mb-1">2.8</div>')
content = content.replace('<div class="text-xl font-bold text-slate-900 mt-1">2,780</div>', '<div id="dem-kpi-inbound" class="text-xl font-bold text-slate-900 mt-1">2,780</div>')
content = content.replace('<div class="text-xl font-bold text-slate-900 mt-1">94.2%</div>', '<div id="dem-kpi-comp" class="text-xl font-bold text-slate-900 mt-1">94.2%</div>')
content = content.replace('<div class="text-xl font-bold text-slate-900 mt-1">420</div>', '<div id="dem-kpi-unmet" class="text-xl font-bold text-slate-900 mt-1">420</div>')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html with IDs")
