import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix dsheet-1
# Remove master dashboard card wrapper
content = re.sub(
    r'<div id="demand-dsheet-1" class="demand-sheet-content space-y-4">\s*<div class="dashboard-card p-4 space-y-4">\s*<div class="border-b border-slate-200 pb-2 mb-2">\s*<h2 class="text-lg font-bold text-slate-900 uppercase">Demand Overview</h2>\s*<p class="text-xs text-slate-500 font-medium">[^<]*</p>\s*</div>',
    '<div id="demand-dsheet-1" class="demand-sheet-content space-y-4">',
    content
)

# Convert bg-slate-50 to dashboard-card for charts in dsheet-1
content = re.sub(
    r'class="(lg:col-span-[0-9]+) bg-slate-50 border border-slate-200 rounded p-3([^"]*)"',
    r'class="\1 dashboard-card p-4\2"',
    content
)

# Fix dsheet-2
content = re.sub(
    r'<div id="demand-dsheet-2" class="demand-sheet-content space-y-4 hidden">\s*<div class="dashboard-card p-5">\s*<h2 class="text-lg font-bold text-slate-900 tracking-tight mb-2">DEMAND OVERVIEW - YEARLY COMPARISON</h2>\s*<p class="text-xs text-slate-500 font-medium mb-4">[^<]*</p>',
    '<div id="demand-dsheet-2" class="demand-sheet-content space-y-4 hidden">\s*<div class="dashboard-card p-5">',
    content
)

# Fix dsheet-3
content = re.sub(
    r'<div id="demand-dsheet-3" class="demand-sheet-content space-y-4 hidden">\s*<div class="dashboard-card p-5">\s*<h2 class="text-lg font-bold text-slate-900 tracking-tight mb-4">ES Weekly Workload Jobs Actuals</h2>',
    '<div id="demand-dsheet-3" class="demand-sheet-content space-y-4 hidden">\s*<div class="dashboard-card p-5">\s*<h2 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-4">ES Weekly Workload Jobs Actuals</h2>',
    content
)

# Fix dsheet-4
content = re.sub(
    r'<div id="demand-dsheet-4" class="demand-sheet-content space-y-4 hidden">\s*<div class="dashboard-card p-5">\s*<h2 class="text-lg font-bold text-slate-900 tracking-tight mb-1 text-center">UKI Weekly Waterfalls - Demand</h2>',
    '<div id="demand-dsheet-4" class="demand-sheet-content space-y-4 hidden">\s*<div class="dashboard-card p-5">\s*<h2 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-1 text-center">UKI Weekly Waterfalls - Demand</h2>',
    content
)

# Close the div we opened for dsheet-1 if we removed the dashboard-card wrapper
# Wait, dsheet-1 has </div> at the end for the wrapper we removed! Let's just remove that extra </div>.
content = re.sub(
    r'<!-- Middle Row -->\s*<div class="grid grid-cols-1 lg:grid-cols-12 gap-4">',
    r'<!-- Middle Row -->\n            <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">',
    content
)
# Actually, a safer way to remove the outer wrapper for dsheet-1 is to replace <div class="dashboard-card p-4 space-y-4"> with nothing and the corresponding </div>.
# Let's write a better replacement script for dsheet-1.

