with open('images/uk.svg', 'r', encoding='utf-8') as f:
    svg_content = f.read()

# Strip <?xml ... ?> header
if svg_content.startswith('<?xml'):
    svg_content = svg_content.split('?>', 1)[1].strip()

# Add styling classes to svg
svg_content = svg_content.replace(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="280 150 490 1030" width="100%" height="100%">',
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="280 150 490 1030" class="w-full h-full max-h-[380px] object-contain drop-shadow-md select-none">'
)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Target block to replace
start_marker = '<h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-2">Performance Map (By Productivity)</h3>'
end_marker = '<!-- Table Column -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_map_col = f'''<h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-2">Performance Map (By Productivity)</h3>
                <div class="flex-1 bg-slate-50/70 rounded-lg flex flex-col items-center justify-center border border-slate-200 relative min-h-[380px] p-3 overflow-hidden shadow-inner">
                  {svg_content}
                  <div class="mt-2 flex items-center justify-center space-x-3 text-[10px] text-slate-500 font-medium">
                    <span class="flex items-center"><span class="w-2.5 h-2.5 rounded-full bg-emerald-700 mr-1"></span>High (&gt;5.5)</span>
                    <span class="flex items-center"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500 mr-1"></span>Good (5.0-5.5)</span>
                    <span class="flex items-center"><span class="w-2.5 h-2.5 rounded-full bg-amber-500 mr-1"></span>Avg (4.5-5.0)</span>
                    <span class="flex items-center"><span class="w-2.5 h-2.5 rounded-full bg-red-600 mr-1"></span>Low (&lt;4.5)</span>
                  </div>
                </div>
              </div>

              '''
    
    html = html[:start_idx] + new_map_col + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Inlined clean UK map SVG into index.html successfully!")
else:
    print(f"Markers not found: start={start_idx}, end={end_idx}")

