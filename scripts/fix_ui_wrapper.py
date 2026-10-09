import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix capacity-sheet-4 back to normal
content = content.replace(
    '<div id="capacity-sheet-4" class="capacity-sheet-content hidden space-y-4">\n          <!-- Top Controls & Mini Bar -->\n          <div class="space-y-4">',
    '<div id="capacity-sheet-4" class="capacity-sheet-content hidden space-y-4">\n          <!-- Top Controls & Mini Bar -->\n          <div class="dashboard-card p-4 space-y-4">'
)

# Fix demand-dsheet-1 wrapper
content = content.replace(
    '<div id="demand-dsheet-1" class="demand-sheet-content space-y-4">\n          <div class="dashboard-card p-4 space-y-4">',
    '<div id="demand-dsheet-1" class="demand-sheet-content space-y-4">\n          <div class="space-y-4">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
