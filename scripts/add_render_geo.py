import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add to updateAllViews
content = content.replace(
    'this.updateDemandSheet();\n  },',
    'this.updateDemandSheet();\n    this.renderGeographicHub();\n  },'
)

geo_func = '''
  renderGeographicHub() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const regional = isRegional ? DASHBOARD_DATA.regionalData[geo] : null;

    const mults = this.getGlobalMultipliers();
    const mult = mults.base * (mults.plan || 1.0);

    // 1. Update Top KPIs
    const baseKpis = isRegional ? {
      installs: { ...regional.kpis.installs },
      sales: { ...regional.kpis.sales, unit: "\\u00A3M" },
      productivity: { ...regional.kpis.productivity, unit: "per Head" },
      availableHours: { ...regional.kpis.availableHours },
      capacityUtilisation: { ...regional.kpis.capacityUtilisation },
      activeHeads: { ...regional.kpis.activeHeads }
    } : DASHBOARD_DATA.executiveSummary.kpis;

    const updateGeoKpi = (key, domId) => {
       if (!baseKpis[key]) return;
       let val = baseKpis[key].value * (isRegional ? 1.0 : mult);
       let fmt = baseKpis[key].formatted;
       if (fmt.includes('K')) fmt = (val/1000).toFixed(2) + 'K';
       else if (fmt.includes('\\u00A3M') || fmt.includes('M')) fmt = '\\u00A3' + (val).toFixed(2) + 'M';
       else fmt = val.toFixed(2);
       
       if (key === 'capacityUtilisation') {
           val = baseKpis[key].value + (mult - 1)*10;
           fmt = val.toFixed(1) + '%';
       }

       const el = document.getElementById(domId);
       if (el) {
          const valEl = el.querySelector('.kpi-value');
          if (valEl) valEl.textContent = fmt;
          
          const wow = baseKpis[key].wow;
          const wowEl = el.querySelector('.kpi-wow');
          if (wowEl) {
             let wVal = parseFloat(wow);
             if (mult !== 1.0) wVal += (mult > 1 ? 1.2 : -1.2);
             let icon = wVal >= 0 ? '&#8593;' : '&#8595;';
             let color = wVal >= 0 ? 'text-emerald-600' : 'text-red-600';
             wowEl.className = kpi-wow font-semibold \;
             wowEl.innerHTML = \ \% WoW;
          }
       }
    };

    updateGeoKpi('installs', 'geo-kpi-installs');
    updateGeoKpi('sales', 'geo-kpi-sales');
    updateGeoKpi('productivity', 'geo-kpi-productivity');
    updateGeoKpi('availableHours', 'geo-kpi-availhrs');
    updateGeoKpi('capacityUtilisation', 'geo-kpi-util');
    updateGeoKpi('activeHeads', 'geo-kpi-heads');

    // 2. Update Table
    const regions = [
      { name: 'Scotland', ins: 442, insV: 5.2, prod: 5.62, prodV: 3.6, av: 76.5, avV: 1.4 },
      { name: 'North', ins: 612, insV: 3.1, prod: 5.12, prodV: 2.2, av: 75.8, avV: 2.3 },
      { name: 'Midlands', ins: 540, insV: -1.2, prod: 4.78, prodV: 1.1, av: 73.2, avV: -1.2 },
      { name: 'Wales', ins: 312, insV: 2.3, prod: 4.42, prodV: -2.6, av: 72.1, avV: -1.8 },
      { name: 'South', ins: 614, insV: 4.6, prod: 4.11, prodV: -2.8, av: 70.3, avV: -1.9 }
    ];

    let tIns = 0, tProd = 0, tAv = 0;
    regions.forEach(r => {
       r.ins = Math.round(r.ins * mult);
       tIns += r.ins;
       tProd += r.prod;
       tAv += r.av;
    });
    tProd = (tProd / 5);
    tAv = (tAv / 5);

    const formatVar = (v) => {
       let icon = v >= 0 ? '&#8593;' : '&#8595;';
       let color = v >= 0 ? 'text-emerald-600' : 'text-red-600';
       return <span class="\ font-semibold">\ \%</span>;
    };

    const tbody = document.getElementById('geo-region-tbody');
    if (tbody) {
       let html = regions.map(r => 
         <tr class="hover:bg-slate-100 transition-colors">
           <td class="py-2.5 px-2 font-semibold text-slate-800">\</td>
           <td class="py-2.5 px-2 text-right text-slate-900 font-bold">\</td>
           <td class="py-2.5 px-2 text-right">\</td>
           <td class="py-2.5 px-2 text-right font-semibold text-slate-700">\</td>
           <td class="py-2.5 px-2 text-right">\</td>
           <td class="py-2.5 px-2 text-right font-semibold text-slate-700">\%</td>
           <td class="py-2.5 px-2 text-right">\</td>
         </tr>
       ).join('');
       
       // Total row
       html += 
         <tr class="bg-slate-200/50 border-t border-slate-300">
           <td class="py-3 px-2 font-bold text-slate-900">Total</td>
           <td class="py-3 px-2 text-right text-slate-900 font-bold">\</td>
           <td class="py-3 px-2 text-right">\</td>
           <td class="py-3 px-2 text-right font-bold text-slate-900">\</td>
           <td class="py-3 px-2 text-right">\</td>
           <td class="py-3 px-2 text-right font-bold text-slate-900">\%</td>
           <td class="py-3 px-2 text-right">\</td>
         </tr>
       ;
       tbody.innerHTML = html;
    }

    // 3. Top and Bottom Areas
    const topAreas = ['Aberdeen', 'Inverness', 'Dundee', 'Milton Keynes', 'Reading'];
    const botAreas = ['Sunderland', 'Blackpool', 'Hull', 'Doncaster', 'Southend'];
    
    const topContainer = document.getElementById('geo-top-areas');
    if (topContainer) {
       topContainer.innerHTML = topAreas.map((area, i) => 
         <div class="flex items-center">
           <div class="w-4 text-slate-500">\.</div>
           <div class="w-24 truncate" title="\">\</div>
           <div class="flex-1 ml-2">
             <div class="h-4 bg-emerald-600 rounded-sm" style="width: \%"></div>
           </div>
         </div>
       ).join('');
    }

    const botContainer = document.getElementById('geo-bottom-areas');
    if (botContainer) {
       botContainer.innerHTML = botAreas.map((area, i) => 
         <div class="flex items-center">
           <div class="w-4 text-slate-500">\.</div>
           <div class="w-24 truncate" title="\">\</div>
           <div class="flex-1 ml-2">
             <div class="h-4 bg-red-600 rounded-sm" style="width: \%"></div>
           </div>
         </div>
       ).join('');
    }

    // 4. Bottom Metrics
    const botHeads = document.getElementById('geo-bot-heads');
    if (botHeads) botHeads.textContent = Math.round(1980 * mult).toLocaleString();
    
    const botTeams = document.getElementById('geo-bot-teams');
    if (botTeams) botTeams.textContent = Math.round(312 * mult).toLocaleString();

    const botDepots = document.getElementById('geo-bot-depots');
    if (botDepots) botDepots.textContent = Math.round(112 * (mult > 1 ? 1.05 : (mult < 1 ? 0.95 : 1))).toLocaleString();

  },
'''

content = content.replace(
    '  renderExecutiveSummary() {',
    geo_func + '\n  renderExecutiveSummary() {'
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added renderGeographicHub to JS")
