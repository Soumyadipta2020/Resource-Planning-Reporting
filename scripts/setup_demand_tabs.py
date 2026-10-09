import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add demand-nav-tabs to header
nav_html = """
        <!-- Demand Sub-Navigation Views Bar -->
        <div id="demand-nav-tabs" class="w-full flex items-center justify-between border-t border-slate-100 pt-2.5 mt-2.5 hidden" style="display: none !important;">
          <div class="flex items-center space-x-2">
            <span class="text-xs font-bold text-slate-500 uppercase px-1">Views:</span>
            <button data-dsheet="dsheet-1" class="dsheet-toggle-btn px-3.5 py-1.5 text-xs font-semibold rounded-md bg-blue-700 text-white shadow-sm transition-all">
              Demand Overview
            </button>
            <button data-dsheet="dsheet-2" class="dsheet-toggle-btn px-3.5 py-1.5 text-xs font-semibold rounded-md bg-slate-100 text-slate-700 hover:bg-slate-200 transition-all">
              Yearly Comparison
            </button>
            <button data-dsheet="dsheet-3" class="dsheet-toggle-btn px-3.5 py-1.5 text-xs font-semibold rounded-md bg-slate-100 text-slate-700 hover:bg-slate-200 transition-all">
              ES Weekly Workload
            </button>
            <button data-dsheet="dsheet-4" class="dsheet-toggle-btn px-3.5 py-1.5 text-xs font-semibold rounded-md bg-slate-100 text-slate-700 hover:bg-slate-200 transition-all">
              Demand Waterfall
            </button>
          </div>
          <div class="text-xs text-slate-500 font-medium hidden sm:block">
            Demand & Workload Dispatch
          </div>
        </div>
      </header>
"""
content = re.sub(r'      </header>', nav_html, content)

# 2. Modify view-demand
demand_view_pattern = re.compile(r'(<section id="view-demand".*?>\s*)(.*?)(?=</section>)', re.DOTALL)

def replacer(m):
    original_inner = m.group(2)
    return m.group(1) + f"""
        <!-- Demand Sheet 1: Demand Overview -->
        <div id="demand-dsheet-1" class="demand-sheet-content">
{original_inner}
        </div>

        <!-- Demand Sheet 2: Yearly Comparison -->
        <div id="demand-dsheet-2" class="demand-sheet-content hidden">
          <div class="dashboard-card p-5 min-h-[500px] flex flex-col">
            <h2 class="text-lg font-bold text-slate-900 tracking-tight mb-4">DEMAND OVERVIEW - YEARLY COMPARISON</h2>
            <div class="flex-1 flex items-center justify-center bg-slate-50 border-2 border-dashed border-slate-200 rounded-lg">
              <span class="text-slate-400 font-semibold">Yearly Comparison Table (To be implemented)</span>
            </div>
          </div>
        </div>

        <!-- Demand Sheet 3: ES Weekly Workload -->
        <div id="demand-dsheet-3" class="demand-sheet-content hidden">
          <div class="dashboard-card p-5 min-h-[500px] flex flex-col">
            <h2 class="text-lg font-bold text-slate-900 tracking-tight mb-4">ES Weekly Workload Jobs Actuals</h2>
            <div class="flex-1 flex items-center justify-center bg-slate-50 border-2 border-dashed border-slate-200 rounded-lg">
              <span class="text-slate-400 font-semibold">ES Weekly Workload Chart & Table (To be implemented)</span>
            </div>
          </div>
        </div>

        <!-- Demand Sheet 4: Demand Waterfall -->
        <div id="demand-dsheet-4" class="demand-sheet-content hidden">
          <div class="dashboard-card p-5 min-h-[500px] flex flex-col">
            <h2 class="text-lg font-bold text-slate-900 tracking-tight mb-4">UKI Weekly Waterfalls - Demand</h2>
            <div class="flex-1 flex items-center justify-center bg-slate-50 border-2 border-dashed border-slate-200 rounded-lg">
              <span class="text-slate-400 font-semibold">Demand Waterfall Chart & Table (To be implemented)</span>
            </div>
          </div>
        </div>
"""

content = demand_view_pattern.sub(replacer, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")

