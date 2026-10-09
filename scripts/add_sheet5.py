import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

nav_btn = '''            <button data-sheet="sheet-4" class="sheet-toggle-btn px-3.5 py-1.5 text-xs font-semibold rounded-md bg-slate-100 text-slate-700 hover:bg-slate-200 transition-all">
              Forecast vs Actuals Matrix
            </button>
            <button data-sheet="sheet-5" class="sheet-toggle-btn px-3.5 py-1.5 text-xs font-semibold rounded-md bg-slate-100 text-slate-700 hover:bg-slate-200 transition-all">
              Capacity Waterfall
            </button>'''
content = content.replace(
    '<button data-sheet="sheet-4" class="sheet-toggle-btn px-3.5 py-1.5 text-xs font-semibold rounded-md bg-slate-100 text-slate-700 hover:bg-slate-200 transition-all">\\n              Forecast vs Actuals Matrix\\n            </button>',
    nav_btn
)

sheet5_html = '''        <!-- ============================================================== -->
        <!-- CAPACITY SHEET 5: CAPACITY WATERFALL (Image 2)                 -->
        <!-- ============================================================== -->
        <div id="capacity-sheet-5" class="capacity-sheet-content hidden space-y-4">
          <div class="dashboard-card p-4 space-y-4">
            <!-- Header Section -->
            <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-2">
              <h2 class="text-lg font-bold text-slate-900">UKI Weekly Waterfalls - Capacity</h2>
              <div class="flex items-center gap-4">
                <div class="flex flex-col">
                  <label class="text-[10px] text-slate-500 font-semibold uppercase">Select Base</label>
                  <select class="filter-select text-xs font-semibold bg-white border border-slate-300 rounded px-2.5 py-1 text-slate-800 cursor-pointer">
                    <option value="gff1">GFF1 2026</option>
                  </select>
                </div>
                <div class="flex flex-col">
                  <label class="text-[10px] text-slate-500 font-semibold uppercase">Select Final</label>
                  <select class="filter-select text-xs font-semibold bg-white border border-slate-300 rounded px-2.5 py-1 text-slate-800 cursor-pointer">
                    <option value="actuals">Actuals</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- Waterfall Chart Container -->
            <div class="w-full bg-slate-50 rounded border border-slate-200 p-2">
              <div class="text-center text-sm font-bold text-slate-700 mb-1">Base vs Final</div>
              <div class="text-center text-xs font-semibold text-slate-500 mb-2">Capacity Hours</div>
              <div class="relative h-72 w-full">
                <canvas id="sheet5-waterfall-chart"></canvas>
              </div>
            </div>

            <!-- Waterfall Detail Table Container -->
            <div id="sheet5-waterfall-table-container">
              <!-- Rendered via js/app.js -->
            </div>
          </div>
        </div>
        
        </section>'''

content = content.replace('        </section>', sheet5_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
