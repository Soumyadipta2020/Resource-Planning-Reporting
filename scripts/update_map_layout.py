import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Grid Layout Columns for the 3 sections
old_grid = '<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">'
new_grid = '<div class="grid grid-cols-1 lg:grid-cols-12 gap-6">'
html = html.replace(old_grid, new_grid, 1) # Only the first occurrence after map

# Assign col spans
html = html.replace('<!-- Map Column -->\n            <div class="flex flex-col">', '<!-- Map Column -->\n            <div class="lg:col-span-3 flex flex-col">')
html = html.replace('<!-- Table Column -->\n            <div class="flex flex-col">', '<!-- Table Column -->\n            <div class="lg:col-span-6 flex flex-col">')
html = html.replace('<!-- Top/Bottom Areas Column -->\n            <div class="flex flex-col space-y-6 pl-0 lg:pl-4">', '<!-- Top/Bottom Areas Column -->\n            <div class="lg:col-span-3 flex flex-col space-y-6 pl-0">')

# 2. Replace Map Graphic with abstract UK map SVG
old_map = '''                   <!-- Since a full UK SVG is huge, we will use a generic visually pleasing map-like placeholder -->
                   <div class="w-32 h-48 bg-slate-200 rounded-lg flex items-center justify-center transform -rotate-6 shadow-inner">
                     <span class="text-slate-500 text-xs font-bold rotate-6">Map Graphic</span>
                   </div>'''

new_map = '''                   <!-- UK Outline SVG -->
                   <svg viewBox="0 0 100 150" class="w-full h-full opacity-30 drop-shadow-md">
                     <!-- Great Britain Silhouette -->
                     <path d="M 40 140 C 50 140, 60 135, 65 125 C 70 115, 65 110, 60 100 C 70 95, 75 90, 75 80 C 75 70, 70 65, 65 60 C 65 50, 75 40, 70 30 C 65 20, 60 15, 55 10 C 50 5, 45 5, 40 15 C 35 25, 40 35, 45 45 C 50 55, 45 65, 40 70 C 35 75, 45 80, 45 90 C 45 100, 35 110, 40 120 C 45 130, 35 135, 40 140 Z" fill="#94a3b8" />
                     <!-- Northern Ireland Silhouette -->
                     <path d="M 25 70 C 30 70, 35 65, 30 60 C 25 55, 20 60, 20 65 C 20 70, 25 70, 25 70 Z" fill="#94a3b8" />
                   </svg>'''

html = html.replace(old_map, new_map)

# 3. Remove View Level filter section
view_level_section = '''              <div class="mt-4 p-3 bg-slate-50 border border-slate-200 rounded">
                <label class="text-[10px] text-slate-500 font-semibold block mb-1">View Level</label>
                <select class="border border-slate-300 rounded px-2 py-1.5 text-xs font-semibold text-slate-700 bg-white focus:outline-none w-3/4 shadow-sm cursor-pointer">
                  <option>Region</option>
                  <option>Area</option>
                </select>
              </div>'''

if view_level_section in html:
    html = html.replace(view_level_section, '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Modified index.html successfully")

