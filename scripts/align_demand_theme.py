import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. dsheet-1 modifications
# Remove outer dashboard-card from dsheet-1 wrapper
content = content.replace('<div class="dashboard-card p-4 space-y-4">', '<div class="space-y-4">', 1)

# Hide the main header for Demand Overview (since Exec Summary doesn't have one)
content = content.replace(
    '<div class="border-b border-slate-200 pb-2 mb-2">\n              <h2 class="text-lg font-bold text-slate-900 uppercase">Demand Overview</h2>',
    '<div class="border-b border-slate-200 pb-2 mb-2 hidden">\n              <h2 class="text-lg font-bold text-slate-900 uppercase">Demand Overview</h2>'
)

# Convert all chart containers in dsheet-1 to dashboard cards
content = re.sub(
    r'bg-slate-50 border border-slate-200 rounded p-3',
    'dashboard-card p-4',
    content
)

# Replace the text formatting for subheaders in dsheet-1 to match Exec Summary
# They currently are: <h3 class="text-xs font-bold text-slate-800 uppercase">
# Exec Summary uses: <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider">
content = content.replace(
    '<h3 class="text-xs font-bold text-slate-800 uppercase">',
    '<h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider">'
)

# 2. dsheet-2 modifications
# Replace large header with Exec Summary style header
dsheet2_old_header = '<h2 class="text-lg font-bold text-slate-900 tracking-tight mb-2">DEMAND OVERVIEW - YEARLY COMPARISON</h2>\n            <p class="text-xs text-slate-500 font-medium mb-4">Actuals and Forecast Comparison by Reporting Year</p>'
dsheet2_new_header = '<div class="flex justify-between items-center mb-4">\n              <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider">Yearly Comparison</h3>\n              <span class="text-[11px] text-slate-500 font-medium">Actuals and Forecast Comparison by Reporting Year</span>\n            </div>'
content = content.replace(dsheet2_old_header, dsheet2_new_header)

# 3. dsheet-3 modifications
dsheet3_old_header = '<h2 class="text-lg font-bold text-slate-900 tracking-tight mb-4">ES Weekly Workload Jobs Actuals</h2>'
dsheet3_new_header = '<div class="flex justify-between items-center mb-4">\n              <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider">ES Weekly Workload Jobs Actuals</h3>\n            </div>'
content = content.replace(dsheet3_old_header, dsheet3_new_header)

# 4. dsheet-4 modifications
dsheet4_old_header = '<h2 class="text-lg font-bold text-slate-900 tracking-tight mb-1 text-center">UKI Weekly Waterfalls - Demand</h2>'
dsheet4_new_header = '<div class="flex justify-between items-center mb-4">\n              <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider">Weekly Waterfalls - Demand</h3>\n            </div>'
content = content.replace(dsheet4_old_header, dsheet4_new_header)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("UI successfully aligned with Exec Summary")
