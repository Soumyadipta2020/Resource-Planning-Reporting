import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace dsheet-2 (Yearly Comparison)
dsheet2 = """
        <!-- Demand Sheet 2: Yearly Comparison -->
        <div id="demand-dsheet-2" class="demand-sheet-content hidden">
          <div class="dashboard-card p-5">
            <h2 class="text-lg font-bold text-slate-900 tracking-tight mb-2">DEMAND OVERVIEW - YEARLY COMPARISON</h2>
            <p class="text-xs text-slate-500 font-medium mb-4">Actuals and Forecast Comparison by Reporting Year</p>
            
            <div class="overflow-x-auto w-full shadow-sm rounded border border-slate-200">
              <table class="w-full text-xs border-collapse whitespace-nowrap">
                <thead>
                  <tr class="bg-blue-800 text-white text-center font-semibold">
                    <th class="py-2 px-3 text-left border-r border-blue-700">Metric</th>
                    <th class="py-2 px-3 border-r border-blue-700">2023<br><span class="text-[10px] font-normal text-blue-200">Actual</span></th>
                    <th class="py-2 px-3 border-r border-blue-700">2024<br><span class="text-[10px] font-normal text-blue-200">Actual</span></th>
                    <th class="py-2 px-3 border-r border-blue-700">2025<br><span class="text-[10px] font-normal text-blue-200">Actual</span></th>
                    <th class="py-2 px-3 border-r border-blue-700" colspan="4">2026<br><span class="text-[10px] font-normal text-blue-200">Forecast vs Actuals</span></th>
                    <th class="py-2 px-3" colspan="4">2027<br><span class="text-[10px] font-normal text-blue-200">Forecast vs Actuals</span></th>
                  </tr>
                  <tr class="bg-slate-100 text-slate-700 text-center font-semibold text-[11px] border-b border-slate-300">
                    <th class="py-1 px-3 text-left border-r border-slate-300"></th>
                    <th class="py-1 px-3 border-r border-slate-300"></th>
                    <th class="py-1 px-3 border-r border-slate-300"></th>
                    <th class="py-1 px-3 border-r border-slate-300"></th>
                    <th class="py-1 px-2 border-r border-slate-300">GFF2</th>
                    <th class="py-1 px-2 border-r border-slate-300">GFF1</th>
                    <th class="py-1 px-2 border-r border-slate-300">vs GFF2</th>
                    <th class="py-1 px-2 border-r border-slate-300">vs PY</th>
                    <th class="py-1 px-2 border-r border-slate-300">GFF2</th>
                    <th class="py-1 px-2 border-r border-slate-300">GFF1</th>
                    <th class="py-1 px-2 border-r border-slate-300">vs GFF2</th>
                    <th class="py-1 px-2">vs PY</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-200" id="demand-yearly-tbody">
                   <!-- Populated by JS or static for now -->
                   <tr class="hover:bg-slate-50">
                     <td class="py-2 px-3 font-bold text-slate-800 border-r border-slate-200">Leads</td>
                     <td class="py-2 px-3 text-center border-r border-slate-200 text-slate-600">306.8K</td>
                     <td class="py-2 px-3 text-center border-r border-slate-200 text-slate-600">318.4K</td>
                     <td class="py-2 px-3 text-center border-r border-slate-200 text-slate-600">342.1K</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200">355.0K</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200">348.6K</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200 text-red-600 font-semibold">↓ -6.4K</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200 text-emerald-600 font-semibold">↑ +6.5K</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200">367.0K</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200">372.2K</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200 text-emerald-600 font-semibold">↑ +5.2K</td>
                     <td class="py-2 px-2 text-center text-emerald-600 font-semibold">↑ +23.6K</td>
                   </tr>
                   <tr class="hover:bg-slate-50 bg-slate-50/50">
                     <td class="py-2 px-3 font-bold text-slate-800 border-r border-slate-200">Open Jobs</td>
                     <td class="py-2 px-3 text-center border-r border-slate-200 text-slate-600">9,312</td>
                     <td class="py-2 px-3 text-center border-r border-slate-200 text-slate-600">9,661</td>
                     <td class="py-2 px-3 text-center border-r border-slate-200 text-slate-600">10,050</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200">10,200</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200">9,980</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200 text-emerald-600 font-semibold">↓ -220</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200 text-emerald-600 font-semibold">↓ -70</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200">9,750</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200">9,620</td>
                     <td class="py-2 px-2 text-center border-r border-slate-200 text-emerald-600 font-semibold">↓ -130</td>
                     <td class="py-2 px-2 text-center text-emerald-600 font-semibold">↓ -360</td>
                   </tr>
                </tbody>
              </table>
            </div>
            <div class="mt-3 text-[10px] text-slate-500">
              * GFF1 and GFF2 represent forecast versions | PY = Previous Year | pp = Percentage Points | Open Jobs and Backlog are point-in-time year-end measures
            </div>
          </div>
        </div>
"""

dsheet3 = """
        <!-- Demand Sheet 3: ES Weekly Workload -->
        <div id="demand-dsheet-3" class="demand-sheet-content hidden">
          <div class="dashboard-card p-5">
            <h2 class="text-lg font-bold text-slate-900 tracking-tight mb-4">ES Weekly Workload Jobs Actuals</h2>
            
            <div class="h-64 mb-6">
              <canvas id="demand-workload-chart"></canvas>
            </div>

            <div class="overflow-x-auto w-full shadow-sm rounded border border-slate-200">
              <table class="w-full text-[10px] border-collapse whitespace-nowrap">
                <thead class="bg-cyan-700 text-white text-center font-semibold">
                  <tr>
                    <th class="py-1.5 px-2 text-left sticky left-0 bg-cyan-800 z-10 w-24 border-r border-cyan-600">Metric</th>
                    <th class="py-1.5 px-2 border-r border-cyan-600">6 Apr 2026</th>
                    <th class="py-1.5 px-2 border-r border-cyan-600">13 Apr 2026</th>
                    <th class="py-1.5 px-2 border-r border-cyan-600">20 Apr 2026</th>
                    <th class="py-1.5 px-2 border-r border-cyan-600">27 Apr 2026</th>
                    <th class="py-1.5 px-2 border-r border-cyan-600">4 May 2026</th>
                    <th class="py-1.5 px-2">11 May 2026</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-200 text-slate-700">
                  <tr class="hover:bg-slate-50">
                    <td class="py-1.5 px-2 font-bold sticky left-0 bg-white border-r border-slate-200 z-10">Total</td>
                    <td class="py-1.5 px-2 text-right">5,314</td>
                    <td class="py-1.5 px-2 text-right">6,580</td>
                    <td class="py-1.5 px-2 text-right">6,266</td>
                    <td class="py-1.5 px-2 text-right">5,917</td>
                    <td class="py-1.5 px-2 text-right">5,338</td>
                    <td class="py-1.5 px-2 text-right">5,932</td>
                  </tr>
                  <tr class="hover:bg-slate-50 bg-slate-50/50">
                    <td class="py-1.5 px-2 font-medium sticky left-0 bg-slate-50/50 border-r border-slate-200 z-10">EV</td>
                    <td class="py-1.5 px-2 text-right">8</td>
                    <td class="py-1.5 px-2 text-right">5</td>
                    <td class="py-1.5 px-2 text-right">11</td>
                    <td class="py-1.5 px-2 text-right">16</td>
                    <td class="py-1.5 px-2 text-right">19</td>
                    <td class="py-1.5 px-2 text-right">6</td>
                  </tr>
                  <tr class="hover:bg-slate-50">
                    <td class="py-1.5 px-2 font-medium sticky left-0 bg-white border-r border-slate-200 z-10">EV Char Survey</td>
                    <td class="py-1.5 px-2 text-right">5</td>
                    <td class="py-1.5 px-2 text-right">2</td>
                    <td class="py-1.5 px-2 text-right">5</td>
                    <td class="py-1.5 px-2 text-right">11</td>
                    <td class="py-1.5 px-2 text-right">2</td>
                    <td class="py-1.5 px-2 text-right">7</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
"""

dsheet4 = """
        <!-- Demand Sheet 4: Demand Waterfall -->
        <div id="demand-dsheet-4" class="demand-sheet-content hidden">
          <div class="dashboard-card p-5">
            <h2 class="text-lg font-bold text-slate-900 tracking-tight mb-1 text-center">UKI Weekly Waterfalls - Demand</h2>
            <div class="text-center text-sm font-semibold text-white bg-blue-700 py-1 mb-1 mt-4">Base Vs Final</div>
            <div class="text-center text-xs font-semibold text-white bg-cyan-600 py-1 mb-6">Demand Jobs</div>
            
            <div class="h-[350px] w-full mb-6">
              <canvas id="demand-waterfall-chart"></canvas>
            </div>
            
            <div class="flex justify-center">
              <div class="w-full max-w-4xl overflow-x-auto shadow-sm rounded border border-slate-200">
                <table class="w-full text-[11px] border-collapse whitespace-nowrap">
                  <thead>
                    <tr class="bg-cyan-600 text-white text-center font-semibold">
                      <th class="py-1.5 px-3 text-left w-32 border-r border-cyan-500"></th>
                      <th class="py-1.5 px-3 border-r border-cyan-500">DL Installs (Jobs)</th>
                      <th class="py-1.5 px-3 border-r border-cyan-500">Contr. Installs (Jobs)</th>
                      <th class="py-1.5 px-3">Total Installs (Jobs)</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-200 text-slate-700 text-center">
                    <tr class="bg-slate-50">
                      <td class="py-1.5 px-3 font-bold text-left border-r border-slate-200">GFF1 2026</td>
                      <td class="py-1.5 px-3 border-r border-slate-200">1,073</td>
                      <td class="py-1.5 px-3 border-r border-slate-200">905</td>
                      <td class="py-1.5 px-3 font-semibold">1,988</td>
                    </tr>
                    <tr>
                      <td class="py-1.5 px-3 font-bold text-left border-r border-slate-200">Actuals</td>
                      <td class="py-1.5 px-3 border-r border-slate-200">897</td>
                      <td class="py-1.5 px-3 border-r border-slate-200">792</td>
                      <td class="py-1.5 px-3 font-semibold">1,689</td>
                    </tr>
                    <tr class="bg-slate-100">
                      <td class="py-1.5 px-3 font-bold text-left border-r border-slate-200">Variance</td>
                      <td class="py-1.5 px-3 border-r border-slate-200 text-red-600 font-semibold">-176 <span class="ml-1">↓</span></td>
                      <td class="py-1.5 px-3 border-r border-slate-200 text-red-600 font-semibold">-113 <span class="ml-1">↓</span></td>
                      <td class="py-1.5 px-3 text-red-600 font-bold">-299 <span class="ml-1">↓</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            
          </div>
        </div>
"""

content = re.sub(r'<!-- Demand Sheet 2: Yearly Comparison -->.*?(?=<!-- Demand Sheet 3:)', dsheet2, content, flags=re.DOTALL)
content = re.sub(r'<!-- Demand Sheet 3: ES Weekly Workload -->.*?(?=<!-- Demand Sheet 4:)', dsheet3, content, flags=re.DOTALL)
content = re.sub(r'<!-- Demand Sheet 4: Demand Waterfall -->.*?(?=</section>)', dsheet4, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html with real UI placeholders")

