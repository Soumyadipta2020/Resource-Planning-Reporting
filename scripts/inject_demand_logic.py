import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

render_method = """
  renderDemandOverview() {
    const mults = this.getGlobalMultipliers();
    const mult = mults.base;

    // 1. KPIs
    const formatValue = (val, fmt) => {
      if (fmt.includes('K')) return (val / 1000).toFixed(2) + 'K';
      if (fmt === 'int') return Math.round(val).toLocaleString();
      return val.toFixed(1);
    };

    const kpiData = {
      leads: { val: 14650 * mult, fmt: 'K' },
      open: { val: 9661 * mult, fmt: 'int' },
      backlog: { val: 1102 * mult, fmt: 'int' },
      jobs: { val: 2343 * mult, fmt: 'int' },
      age: { val: 9.4 * mult, fmt: 'float' },
      gap: { val: 2100 * mult, fmt: 'K' }
    };

    const updateDemKpi = (id, valObj) => {
       const el = document.getElementById(id);
       if (el) {
          const valEl = el.querySelector(".kpi-value");
          if (valEl) valEl.textContent = formatValue(valObj.val, valObj.fmt);
       }
    };
    
    updateDemKpi("dem1-kpi-leads", kpiData.leads);
    updateDemKpi("dem1-kpi-open", kpiData.open);
    updateDemKpi("dem1-kpi-backlog", kpiData.backlog);
    updateDemKpi("dem1-kpi-jobs", kpiData.jobs);
    updateDemKpi("dem1-kpi-age", kpiData.age);
    updateDemKpi("dem1-kpi-gap", kpiData.gap);

    // 2. Demand vs Capacity Chart
    const labels13 = ['WK 23', 'WK 24', 'WK 25', 'WK 26', 'WK 27', 'WK 28', 'WK 29', 'WK 30', 'WK 31', 'WK 32', 'WK 33', 'WK 34', 'WK 35'];
    const demCapData = {
       labels: labels13,
       workload: [20000, 23000, 25000, 24000, 26000, 31000, 31000, 28000, 27000, 29000, 28000, 27000, 28000].map(v => Math.round(v * mult)),
       capacity: [12000, 15000, 16000, 13000, 15000, 18000, 18000, 17000, 17000, 15000, 12000, 11000, 10000].map(v => Math.round(v * mult))
    };
    ChartManager.renderDemandCapacityChart('dem1-chart-demand-capacity', demCapData);

    // 3. Forecast Accuracy
    const accLabels = ['WK 14', 'WK 15', 'WK 16', 'WK 17', 'WK 18', 'WK 19', 'WK 20', 'WK 21', 'WK 22', 'WK 23'];
    const accData = {
       labels: accLabels,
       accuracy: [18, 13, 16, 14, 15, 11, 10, 11, 13, 13.6]
    };
    ChartManager.renderForecastAccuracyChart('dem1-chart-forecast-accuracy', accData);

    // 4. Top Workload Table
    const workloadCategories = [
       { cat: 'Install', val: 15710, pct: 39.1, vsPlan: 4.6, vsLw: 2.7 },
       { cat: 'Repair', val: 11377, pct: 28.4, vsPlan: 5.3, vsLw: -4.2 },
       { cat: 'EV', val: 4800, pct: 10.9, vsPlan: -3.1, vsLw: 1.0 },
       { cat: 'Warranty', val: 4915, pct: 11.0, vsPlan: 2.1, vsLw: -1.6 },
       { cat: 'Survey', val: 2688, pct: 6.7, vsPlan: -1.1, vsLw: 5.2 }
    ];
    let totalWorkload = workloadCategories.reduce((a, b) => a + b.val, 0);

    const tbody = document.getElementById('dem1-workload-tbody');
    if (tbody) {
       tbody.innerHTML = workloadCategories.map(row => {
          let scaledVal = Math.round(row.val * mult);
          let planCls = row.vsPlan >= 0 ? 'text-emerald-600' : 'text-red-600';
          let planIcn = row.vsPlan >= 0 ? '↑' : '↓';
          let lwCls = row.vsLw >= 0 ? 'text-emerald-600' : 'text-red-600';
          let lwIcn = row.vsLw >= 0 ? '↑' : '↓';
          return `
             <tr class="hover:bg-slate-50 transition-colors">
               <td class="py-1.5 px-2 text-slate-800 font-medium">${row.cat}</td>
               <td class="py-1.5 px-2 text-right text-slate-900 font-bold">${scaledVal.toLocaleString()}</td>
               <td class="py-1.5 px-2 text-right text-slate-600">${row.pct.toFixed(1)}%</td>
               <td class="py-1.5 px-2 text-right ${planCls} font-semibold">${planIcn} ${Math.abs(row.vsPlan)}%</td>
               <td class="py-1.5 px-2 text-right ${lwCls} font-semibold">${lwIcn} ${Math.abs(row.vsLw)}%</td>
             </tr>
          `;
       }).join('') + `
             <tr class="bg-slate-100/80 font-bold border-t border-slate-300">
               <td class="py-1.5 px-2 text-slate-900">Total</td>
               <td class="py-1.5 px-2 text-right text-slate-900">${Math.round(totalWorkload * mult).toLocaleString()}</td>
               <td class="py-1.5 px-2 text-right text-slate-900">100%</td>
               <td class="py-1.5 px-2 text-right text-emerald-600">↑ 3.6%</td>
               <td class="py-1.5 px-2 text-right text-emerald-600">↑ 2.9%</td>
             </tr>
       `;
    }

    // 5. Workload by Job Type Trend (Last 12 Weeks)
    const trendLabels = ['WK 12', 'WK 13', 'WK 14', 'WK 15', 'WK 16', 'WK 17', 'WK 18', 'WK 19', 'WK 20', 'WK 21', 'WK 22', 'WK 23'];
    const trendData = {
       labels: trendLabels,
       install: [1300, 1400, 1450, 1380, 1500, 1550, 1600, 1620, 1590, 1650, 1700, 1571].map(v => Math.round(v * mult * 10)),
       repair: [1100, 1150, 1120, 1080, 1100, 1150, 1180, 1120, 1150, 1100, 1120, 1137].map(v => Math.round(v * mult * 10)),
       ev: [300, 320, 350, 380, 400, 420, 430, 450, 470, 480, 490, 480].map(v => Math.round(v * mult * 10)),
       warranty: [400, 410, 420, 390, 410, 430, 450, 460, 470, 480, 490, 491].map(v => Math.round(v * mult * 10)),
       survey: [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 280, 268].map(v => Math.round(v * mult * 10))
    };
    ChartManager.renderWorkloadTrendChart('dem1-chart-workload-trend', trendData);

    // 6. Demand Gap Forecast
    const gapData = {
       labels: labels13,
       demand: [20000, 23000, 25000, 24000, 26000, 31000, 31000, 28000, 27000, 29000, 28000, 27000, 28000].map(v => Math.round((v + 2000) * mult)),
       capacity: [22000, 21000, 23000, 22000, 24000, 26000, 24000, 22000, 23000, 21000, 24000, 25000, 26000].map(v => Math.round((v - 1000) * mult))
    };
    ChartManager.renderDemandGapChart('dem1-chart-demand-gap', gapData);
  },
"""

idx = -1
for i, line in enumerate(lines):
    if "updateDemandSheet() {" in line:
        idx = i
        break

if idx != -1:
    # insert renderDemandOverview before updateDemandSheet
    lines.insert(idx, render_method)
    
    # Also we need to find where `if (this.state.demandSheet === "dsheet-1") {` is
    # and insert `this.renderDemandOverview();` inside it.
    for j in range(idx + 1, len(lines)):
        if 'if (this.state.demandSheet === "dsheet-1") {' in lines[j]:
            lines[j+1] = '       this.renderDemandOverview();\n'
            break

    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Injected renderDemandOverview successfully")
else:
    print("Could not find updateDemandSheet")

