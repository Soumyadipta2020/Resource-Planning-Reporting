import re

html_content = """        <!-- Demand Sheet 1: Demand Overview -->
        <div id="demand-dsheet-1" class="demand-sheet-content space-y-4">
          <div class="dashboard-card p-4 space-y-4">
            
            <div class="border-b border-slate-200 pb-2 mb-2">
              <h2 class="text-lg font-bold text-slate-900 uppercase">Demand Overview</h2>
              <p class="text-xs text-slate-500 font-medium">Track demand trends, workload and job backlog</p>
            </div>

            <!-- Top 6 KPIs -->
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
              <!-- KPI 1 -->
              <div id="dem1-kpi-leads" class="kpi-card flex flex-col justify-between">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-semibold text-slate-500">Leads</span>
                  <div class="w-6 h-6 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                  </div>
                </div>
                <div class="kpi-value text-xl font-bold text-slate-900 my-1">14.65K</div>
                <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
                  <span class="kpi-wow text-red-600 font-semibold">↓ 27.3% WoW</span>
                  <span class="kpi-plan text-red-600 font-semibold">↓ 27.1% vs Plan</span>
                </div>
              </div>
              
              <!-- KPI 2 -->
              <div id="dem1-kpi-open" class="kpi-card flex flex-col justify-between">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-semibold text-slate-500">Open Jobs</span>
                  <div class="w-6 h-6 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                  </div>
                </div>
                <div class="kpi-value text-xl font-bold text-slate-900 my-1">9,661</div>
                <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
                  <span class="kpi-wow text-emerald-600 font-semibold">↑ 4.2% WoW</span>
                  <span class="kpi-plan text-emerald-600 font-semibold">↑ 3.1% vs Plan</span>
                </div>
              </div>

              <!-- KPI 3 -->
              <div id="dem1-kpi-backlog" class="kpi-card flex flex-col justify-between">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-semibold text-slate-500">Backlog > 14 Days</span>
                  <div class="w-6 h-6 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                  </div>
                </div>
                <div class="kpi-value text-xl font-bold text-slate-900 my-1">1,102</div>
                <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
                  <span class="kpi-wow text-emerald-600 font-semibold">↑ 5.6% WoW</span>
                  <span class="kpi-plan text-emerald-600 font-semibold">↑ 4.7% vs Plan</span>
                </div>
              </div>

              <!-- KPI 4 -->
              <div id="dem1-kpi-jobs" class="kpi-card flex flex-col justify-between">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-semibold text-slate-500">Jobs Completed</span>
                  <div class="w-6 h-6 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                  </div>
                </div>
                <div class="kpi-value text-xl font-bold text-slate-900 my-1">2,343</div>
                <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
                  <span class="kpi-wow text-emerald-600 font-semibold">↑ 6.8% WoW</span>
                  <span class="kpi-plan text-emerald-600 font-semibold">↑ 5.0% vs Plan</span>
                </div>
              </div>

              <!-- KPI 5 -->
              <div id="dem1-kpi-age" class="kpi-card flex flex-col justify-between">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-semibold text-slate-500">Average Age (Days)</span>
                  <div class="w-6 h-6 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                  </div>
                </div>
                <div class="kpi-value text-xl font-bold text-slate-900 my-1">9.4</div>
                <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
                  <span class="kpi-wow text-red-600 font-semibold">↑ 0.6% WoW</span>
                  <span class="kpi-plan text-red-600 font-semibold">↑ 1.2% vs Plan</span>
                </div>
              </div>

              <!-- KPI 6 -->
              <div id="dem1-kpi-gap" class="kpi-card flex flex-col justify-between">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-semibold text-slate-500">Capacity Gap</span>
                  <div class="w-6 h-6 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                  </div>
                </div>
                <div class="kpi-value text-xl font-bold text-slate-900 my-1">2.1K</div>
                <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
                  <span class="kpi-wow text-emerald-600 font-semibold">↑ 12.4% WoW</span>
                  <span class="kpi-plan text-emerald-600 font-semibold">↑ 11.9% vs Plan</span>
                </div>
              </div>
            </div>

            <!-- Middle Row -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
               <!-- Col 1: Demand vs Capacity (span 6) -->
               <div class="lg:col-span-6 bg-slate-50 border border-slate-200 rounded p-3">
                 <div class="flex justify-between items-center mb-2">
                   <h3 class="text-xs font-bold text-slate-800 uppercase">Demand vs Capacity (Next 13 Weeks)</h3>
                 </div>
                 <div class="flex items-center gap-4 text-[10px] font-semibold text-slate-600 mb-2">
                   <div class="flex items-center gap-1"><span class="w-3 h-0.5 bg-blue-800 block"></span> Workload Forecast</div>
                   <div class="flex items-center gap-1"><span class="w-3 h-0.5 bg-emerald-500 block"></span> Available Capacity</div>
                   <div class="flex items-center gap-1"><span class="w-3 h-0.5 bg-red-500 block"></span> Capacity Gap</div>
                 </div>
                 <div class="relative h-44 w-full">
                   <canvas id="dem1-chart-demand-capacity"></canvas>
                 </div>
               </div>
               
               <!-- Col 2: Forecast Accuracy (span 3) -->
               <div class="lg:col-span-3 bg-slate-50 border border-slate-200 rounded p-3">
                 <div class="flex justify-between items-center mb-2">
                   <h3 class="text-xs font-bold text-slate-800 uppercase">Forecast Accuracy (MAPE%)</h3>
                 </div>
                 <div class="relative h-44 w-full">
                   <canvas id="dem1-chart-forecast-accuracy"></canvas>
                 </div>
               </div>
               
               <!-- Col 3: Job Mix Treemap (span 3) -->
               <div class="lg:col-span-3 bg-slate-50 border border-slate-200 rounded p-3 flex flex-col">
                 <div class="flex justify-between items-center mb-2">
                   <h3 class="text-xs font-bold text-slate-800 uppercase">Job Mix (This Week)</h3>
                 </div>
                 <!-- Simple Flex Box blocks as Treemap -->
                 <div class="flex-1 flex gap-1 h-44 w-full text-white text-[10px] font-semibold">
                   <!-- Install Box -->
                   <div class="bg-[#0f172a] w-[50%] h-full flex flex-col justify-between p-1.5 rounded-sm">
                     <span>Install</span>
                     <span class="text-sm">49.1%</span>
                   </div>
                   <!-- Right Column -->
                   <div class="w-[50%] h-full flex flex-col gap-1">
                     <!-- Repair Box -->
                     <div class="bg-teal-700 h-[60%] w-full flex flex-col justify-between p-1.5 rounded-sm">
                       <span>Repair</span>
                       <span class="text-sm">24.7%</span>
                     </div>
                     <!-- Bottom Right Row -->
                     <div class="flex gap-1 h-[40%] w-full">
                        <div class="bg-emerald-600 w-[65%] h-full flex flex-col justify-between p-1.5 rounded-sm">
                          <span>EV</span>
                          <span>15.8%</span>
                        </div>
                        <div class="bg-slate-500 w-[35%] h-full flex flex-col justify-between p-1.5 rounded-sm text-center">
                          <span>Warranty</span>
                          <span>5.5%</span>
                        </div>
                     </div>
                   </div>
                 </div>
               </div>
            </div>

            <!-- Bottom Row -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
               <!-- Col 1: Top Workload Table (span 4) -->
               <div class="lg:col-span-4 bg-slate-50 border border-slate-200 rounded p-3">
                 <div class="flex justify-between items-center mb-2">
                   <h3 class="text-xs font-bold text-slate-800 uppercase">Top Workload Categories (This Week)</h3>
                 </div>
                 <table class="w-full text-[10px] text-left border-collapse">
                    <thead>
                      <tr class="bg-slate-200/50 text-slate-700 border-b border-slate-300 font-semibold">
                        <th class="py-1.5 px-2">Category</th>
                        <th class="py-1.5 px-2 text-right">Workload</th>
                        <th class="py-1.5 px-2 text-right">% of Total</th>
                        <th class="py-1.5 px-2 text-right">vs Plan</th>
                        <th class="py-1.5 px-2 text-right">vs LW</th>
                      </tr>
                    </thead>
                    <tbody id="dem1-workload-tbody" class="divide-y divide-slate-100">
                      <!-- Rendered by JS -->
                    </tbody>
                 </table>
               </div>
               
               <!-- Col 2: Workload Trend Bar (span 5) -->
               <div class="lg:col-span-5 bg-slate-50 border border-slate-200 rounded p-3">
                 <div class="flex justify-between items-center mb-2">
                   <h3 class="text-xs font-bold text-slate-800 uppercase">Workload by Job Type - Trend (Last 12 Weeks)</h3>
                 </div>
                 <div class="flex items-center gap-3 text-[9px] font-semibold text-slate-600 mb-2">
                   <div class="flex items-center gap-1"><span class="w-2 h-2 bg-[#0f172a] block"></span> Install</div>
                   <div class="flex items-center gap-1"><span class="w-2 h-2 bg-teal-700 block"></span> Repair</div>
                   <div class="flex items-center gap-1"><span class="w-2 h-2 bg-yellow-500 block"></span> EV</div>
                   <div class="flex items-center gap-1"><span class="w-2 h-2 bg-emerald-600 block"></span> Warranty</div>
                   <div class="flex items-center gap-1"><span class="w-2 h-2 bg-slate-500 block"></span> Survey</div>
                 </div>
                 <div class="relative h-40 w-full">
                   <canvas id="dem1-chart-workload-trend"></canvas>
                 </div>
               </div>
               
               <!-- Col 3: Demand Gap Forecast (span 3) -->
               <div class="lg:col-span-3 bg-slate-50 border border-slate-200 rounded p-3">
                 <div class="flex justify-between items-center mb-2">
                   <h3 class="text-xs font-bold text-slate-800 uppercase">Demand Gap Forecast</h3>
                 </div>
                 <div class="relative h-48 w-full">
                   <canvas id="dem1-chart-demand-gap"></canvas>
                 </div>
               </div>
            </div>
          </div>
        </div>"""

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<div id="demand-dsheet-1" class="demand-sheet-content">' in line:
        start_idx = i - 1
    if '<div id="demand-dsheet-2" class="demand-sheet-content hidden">' in line:
        end_idx = i - 2
        break

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx] + [html_content + '\n\n'] + lines[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Updated index.html successfully")
else:
    print("Could not find boundaries")

