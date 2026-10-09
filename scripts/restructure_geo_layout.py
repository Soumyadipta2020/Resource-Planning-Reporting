with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Map Column from lg:col-span-3 to lg:col-span-4
html = html.replace(
    '<!-- Map Column -->\n            <div class="lg:col-span-3 flex flex-col">',
    '<!-- Map Column -->\n            <div class="lg:col-span-4 flex flex-col">'
)

start_marker = '<!-- Table Column -->'
end_marker = '<!-- Bottom Footer Row -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_right_col = '''<!-- Right Column: Region Summary (Top) & Top/Bottom Areas (Bottom) -->
            <div class="lg:col-span-8 flex flex-col justify-between space-y-5">
              
              <!-- Region Summary Table (Spanning Left to Right) -->
              <div>
                <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-2">Region Summary (This Week)</h3>
                <div class="rounded-lg border border-slate-200 overflow-hidden text-xs bg-white shadow-sm">
                  <table class="w-full text-left border-collapse">
                    <thead class="bg-slate-100/80 border-b border-slate-200 text-slate-700">
                      <tr>
                        <th class="py-2.5 px-3 font-bold">Region</th>
                        <th class="py-2.5 px-3 font-bold text-right">Installs</th>
                        <th class="py-2.5 px-3 font-bold text-right">vs Plan</th>
                        <th class="py-2.5 px-3 font-bold text-right">Productivity</th>
                        <th class="py-2.5 px-3 font-bold text-right">vs Plan</th>
                        <th class="py-2.5 px-3 font-bold text-right">Availability %</th>
                        <th class="py-2.5 px-3 font-bold text-right">vs Plan</th>
                      </tr>
                    </thead>
                    <tbody id="geo-region-tbody" class="divide-y divide-slate-100">
                       <!-- JS Populated -->
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- Bottom Row: Top 5 and Bottom 5 Areas Bars Side-by-Side -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-3 border-t border-slate-100">
                <div class="bg-slate-50/60 p-3.5 rounded-lg border border-slate-200/80">
                  <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-3 flex items-center">
                    <span class="w-2 h-2 rounded-full bg-emerald-600 mr-1.5"></span>
                    Top 5 Areas by Productivity
                  </h3>
                  <div id="geo-top-areas" class="space-y-2.5 text-xs">
                     <!-- JS Populated -->
                  </div>
                </div>
                <div class="bg-slate-50/60 p-3.5 rounded-lg border border-slate-200/80">
                  <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-3 flex items-center">
                    <span class="w-2 h-2 rounded-full bg-red-600 mr-1.5"></span>
                    Bottom 5 Areas by Productivity
                  </h3>
                  <div id="geo-bottom-areas" class="space-y-2.5 text-xs">
                     <!-- JS Populated -->
                  </div>
                </div>
              </div>

            </div>

          </div>

          '''
    
    html = html[:start_idx] + new_right_col + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html layout successfully!")
else:
    print(f"Markers not found: start={start_idx}, end={end_idx}")

