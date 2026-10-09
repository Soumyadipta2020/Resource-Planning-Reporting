import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_hub_html = '''      <section id="view-geographic-hub" class="tab-view-container hidden space-y-4">
        <!-- 6 KPI Cards -->
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
          <!-- Installs -->
          <div id="geo-kpi-installs" class="kpi-card flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-slate-500">Installs</span>
              <div class="w-7 h-7 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path></svg>
              </div>
            </div>
            <div class="kpi-value text-2xl font-bold text-slate-900 my-1">2.51K</div>
            <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
              <span class="kpi-wow text-emerald-600 font-semibold">&#8593; 4.2% WoW</span>
            </div>
          </div>

          <!-- Sales -->
          <div id="geo-kpi-sales" class="kpi-card flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-slate-500">Sales (&pound;)</span>
              <div class="w-7 h-7 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs font-bold">&pound;</div>
            </div>
            <div class="kpi-value text-2xl font-bold text-slate-900 my-1">&pound;3.94M</div>
            <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
              <span class="kpi-wow text-emerald-600 font-semibold">&#8593; 6.1% WoW</span>
            </div>
          </div>

          <!-- Productivity (Per Head) -->
          <div id="geo-kpi-productivity" class="kpi-card flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-slate-500">Productivity <span class="text-[10px]">(Per Head)</span></span>
              <div class="w-7 h-7 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
              </div>
            </div>
            <div class="kpi-value text-2xl font-bold text-slate-900 my-1">4.75</div>
            <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
              <span class="kpi-wow text-red-600 font-semibold">&#8595; 1.6% WoW</span>
            </div>
          </div>

          <!-- Available Hours -->
          <div id="geo-kpi-availhrs" class="kpi-card flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-slate-500">Available Hours</span>
              <div class="w-7 h-7 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
            </div>
            <div class="kpi-value text-2xl font-bold text-slate-900 my-1">47.3K</div>
            <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
              <span class="kpi-wow text-emerald-600 font-semibold">&#8593; 2.1% WoW</span>
            </div>
          </div>

          <!-- Capacity Utilisation -->
          <div id="geo-kpi-util" class="kpi-card flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-slate-500">Capacity Utilisation</span>
              <div class="w-7 h-7 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
              </div>
            </div>
            <div class="kpi-value text-2xl font-bold text-slate-900 my-1">88.1%</div>
            <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
              <span class="kpi-wow text-emerald-600 font-semibold">&#8593; 2.3% WoW</span>
            </div>
          </div>

          <!-- Active Heads -->
          <div id="geo-kpi-heads" class="kpi-card flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-slate-500">Active Heads</span>
              <div class="w-7 h-7 rounded-full bg-slate-800 text-white flex items-center justify-center text-xs">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
              </div>
            </div>
            <div class="kpi-value text-2xl font-bold text-slate-900 my-1">1.98K</div>
            <div class="flex items-center justify-between text-[11px] pt-1 border-t border-slate-100">
              <span class="kpi-wow text-emerald-600 font-semibold">&#8593; 2.7% WoW</span>
            </div>
          </div>
        </div>

        <!-- Main Dashboard Card -->
        <div class="dashboard-card p-4 space-y-4 flex flex-col bg-white">
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            <!-- Map Column -->
            <div class="flex flex-col">
              <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-2">Performance Map (By Productivity)</h3>
              <div class="flex-1 bg-slate-50 rounded flex flex-col items-center justify-center border border-slate-200 relative min-h-[350px] p-2">
                <div class="absolute inset-0 flex items-center justify-center">
                   <!-- Since a full UK SVG is huge, we will use a generic visually pleasing map-like placeholder -->
                   <div class="w-32 h-48 bg-slate-200 rounded-lg flex items-center justify-center transform -rotate-6 shadow-inner">
                     <span class="text-slate-500 text-xs font-bold rotate-6">Map Graphic</span>
                   </div>
                   <!-- Abstract regions color overlays -->
                   <div class="absolute top-[20%] left-[45%] w-14 h-14 bg-green-500/60 rounded-full blur-xl"></div>
                   <div class="absolute top-[40%] left-[35%] w-16 h-12 bg-green-500/60 rounded-full blur-xl"></div>
                   <div class="absolute top-[55%] left-[40%] w-16 h-16 bg-yellow-500/60 rounded-full blur-xl"></div>
                   <div class="absolute top-[65%] left-[30%] w-12 h-10 bg-red-500/60 rounded-full blur-xl"></div>
                   <div class="absolute bottom-[15%] left-[45%] w-20 h-16 bg-red-500/60 rounded-full blur-xl"></div>
                </div>
              </div>
            </div>

            <!-- Table Column -->
            <div class="flex flex-col">
              <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-2">Region Summary (This Week)</h3>
              <div class="flex-1 rounded border border-slate-200 overflow-hidden text-[10px] bg-slate-50">
                <table class="w-full text-left border-collapse">
                  <thead class="bg-slate-100 border-b border-slate-200">
                    <tr>
                      <th class="py-2 px-2 font-bold text-slate-800">Region</th>
                      <th class="py-2 px-2 font-bold text-slate-800 text-right">Installs</th>
                      <th class="py-2 px-2 font-bold text-slate-800 text-right">vs Plan</th>
                      <th class="py-2 px-2 font-bold text-slate-800 text-right">Productivity</th>
                      <th class="py-2 px-2 font-bold text-slate-800 text-right">vs Plan</th>
                      <th class="py-2 px-2 font-bold text-slate-800 text-right">Availability %</th>
                      <th class="py-2 px-2 font-bold text-slate-800 text-right">vs Plan</th>
                    </tr>
                  </thead>
                  <tbody id="geo-region-tbody" class="divide-y divide-slate-200">
                     <!-- JS Populated -->
                  </tbody>
                </table>
              </div>
              <div class="mt-4 p-3 bg-slate-50 border border-slate-200 rounded">
                <label class="text-[10px] text-slate-500 font-semibold block mb-1">View Level</label>
                <select class="border border-slate-300 rounded px-2 py-1.5 text-xs font-semibold text-slate-700 bg-white focus:outline-none w-3/4 shadow-sm cursor-pointer">
                  <option>Region</option>
                  <option>Area</option>
                </select>
              </div>
            </div>

            <!-- Top/Bottom Areas Column -->
            <div class="flex flex-col space-y-6 pl-0 lg:pl-4">
              <div class="flex-1">
                <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-3">Top 5 Areas by Productivity</h3>
                <div id="geo-top-areas" class="space-y-3">
                   <!-- JS Populated -->
                </div>
              </div>
              <div class="flex-1">
                <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-3">Bottom 5 Areas by Productivity</h3>
                <div id="geo-bottom-areas" class="space-y-3">
                   <!-- JS Populated -->
                </div>
              </div>
            </div>

          </div>

          <!-- Bottom Footer Row -->
          <div class="grid grid-cols-5 gap-3 border-t border-slate-200 pt-4 mt-4 text-center">
             <div>
               <p class="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Total Regions</p>
               <p id="geo-bot-regions" class="text-xl font-bold text-slate-900 mt-1">5</p>
             </div>
             <div>
               <p class="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Total Areas</p>
               <p id="geo-bot-areas" class="text-xl font-bold text-slate-900 mt-1">28</p>
             </div>
             <div>
               <p class="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Total Depots</p>
               <p id="geo-bot-depots" class="text-xl font-bold text-slate-900 mt-1">112</p>
             </div>
             <div>
               <p class="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Active Teams</p>
               <p id="geo-bot-teams" class="text-xl font-bold text-slate-900 mt-1">312</p>
             </div>
             <div>
               <p class="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Active Heads</p>
               <p id="geo-bot-heads" class="text-xl font-bold text-slate-900 mt-1">1,980</p>
             </div>
          </div>
        </div>
      </section>'''

start_tag = '<section id="view-geographic-hub" class="tab-view-container hidden space-y-4">'
end_tag = '      </section>'
start_idx = content.find(start_tag)
if start_idx != -1:
    end_idx = content.find(end_tag, start_idx)
    if end_idx != -1:
        end_idx += len(end_tag)
        content = content[:start_idx] + new_hub_html + content[end_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("HTML successfully updated")
    else:
        print("End tag not found")
else:
    print("Start tag not found")
