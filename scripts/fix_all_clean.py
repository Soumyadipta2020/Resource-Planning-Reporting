import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add getGlobalMultiplier()
mult_func = """  getGlobalMultiplier() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;

    let planMult = 1.0;
    if (this.state.selectedPlan === "budget_2026") planMult = 0.95;
    else if (this.state.selectedPlan === "reforecast_q3") planMult = 1.04;

    let weekMult = 1.0;
    if (this.state.selectedWeek) {
       const match = this.state.selectedWeek.match(/wk(\d+)/);
       if (match) {
           const wkNum = parseInt(match[1]);
           weekMult = 1 + ((wkNum - 23) * 0.015);
       }
    }
    return geoMult * planMult * weekMult;
  },

  /**
   * Master Update: Recalculates and updates everything based on current state & filters
   */"""

content = content.replace('  /**\n   * Master Update: Recalculates and updates everything based on current state & filters\n   */', mult_func)

# 2. Executive Summary
exec_summary_code = """  renderExecutiveSummary() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const regional = isRegional ? DASHBOARD_DATA.regionalData[geo] : null;

    const mult = this.getGlobalMultiplier();

    // Scale KPI Values
    const baseKpis = isRegional ? {
      installs: { ...regional.kpis.installs },
      sales: { ...regional.kpis.sales, unit: "£M" },
      leads: { ...regional.kpis.leads },
      activeHeads: { ...regional.kpis.activeHeads },
      availableHours: { ...regional.kpis.availableHours },
      productivity: { ...regional.kpis.productivity, unit: "per Head" }
    } : DASHBOARD_DATA.executiveSummary.kpis;

    const kpiData = {};
    for (let key in baseKpis) {
       let val = baseKpis[key].value * (isRegional ? 1.0 : mult);
       let fmt = baseKpis[key].formatted;
       if (fmt.includes('K')) fmt = (val/1000).toFixed(2) + 'K';
       else if (fmt.includes('£M') || fmt.includes('A£M')) fmt = '£' + (val).toFixed(2) + 'M';
       else fmt = val.toFixed(2);
       
       kpiData[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val
       };
    }

    this.renderKpiCard("exec-kpi-installs", kpiData.installs.formatted, kpiData.installs.wow, kpiData.installs.vsPlan);
    this.renderKpiCard("exec-kpi-sales", kpiData.sales.formatted, kpiData.sales.wow, kpiData.sales.vsPlan);
    this.renderKpiCard("exec-kpi-leads", kpiData.leads.formatted, kpiData.leads.wow, kpiData.leads.vsPlan);
    this.renderKpiCard("exec-kpi-heads", kpiData.activeHeads.formatted, kpiData.activeHeads.wow, kpiData.activeHeads.vsPlan);
    this.renderKpiCard("exec-kpi-availhrs", kpiData.availableHours.formatted, kpiData.availableHours.wow, kpiData.availableHours.vsPlan);
    this.renderKpiCard("exec-kpi-productivity", kpiData.productivity.formatted, kpiData.productivity.wow, kpiData.productivity.vsPlan);

    // Installs Weekly Combo Chart
    let weeklyData = DASHBOARD_DATA.executiveSummary.weeklyInstalls.map(d => ({
      week: d.week,
      actual: Math.round(d.actual * mult),
      plan: Math.round(d.plan * mult),
      variance: Math.round(d.variance * mult)
    }));
    ChartManager.renderWeeklyInstallsChart("chart-weekly-installs", weeklyData);

    // Waterfall Chart Drivers
    let drivers = DASHBOARD_DATA.executiveSummary.waterfallDrivers.map(d => ({
      ...d,
      value: Math.round(d.value * mult)
    }));
    ChartManager.renderWaterfallChart("waterfall-chart-container", drivers);

    // Sparklines
    ChartManager.renderSparklines(DASHBOARD_DATA.executiveSummary.sparklines);
  },"""

content = re.sub(r'  renderExecutiveSummary\(\) \{.*?(?=  /\*\*|  updateCapacitySheet)', exec_summary_code, content, flags=re.DOTALL)


# 3. Capacity Sheet 2
cap2_code = """  renderCapacitySheet2() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const regional = isRegional ? DASHBOARD_DATA.regionalData[geo] : null;
    
    const mult = this.getGlobalMultiplier();

    // Top KPIs
    const baseKpis = isRegional ? {
      availableHours: { ...regional.kpis.availableHours },
      totalDowntime: { ...regional.kpis.totalDowntime },
      capacityUtilisation: { ...regional.kpis.capacityUtilisation },
      workforceAvailability: { ...regional.kpis.workforceAvailability },
      productivity: { ...regional.kpis.productivity },
      sicknessPercent: { ...regional.kpis.sicknessPercent }
    } : DASHBOARD_DATA.capacitySheet2.kpis;

    const kpis = {};
    for (let key in baseKpis) {
       let val = baseKpis[key].value * (isRegional ? 1.0 : mult);
       // exceptions for percentages
       if (key === 'capacityUtilisation' || key === 'workforceAvailability' || key === 'sicknessPercent') {
           val = baseKpis[key].value + (mult - 1)*10; // slightly shift percent
       }
       
       let fmt = baseKpis[key].formatted;
       if (fmt.includes('%')) fmt = val.toFixed(1) + '%';
       else if (fmt.includes('K')) fmt = (val/1000).toFixed(1) + 'K';
       else fmt = val.toFixed(1) > 10 ? Math.round(val).toLocaleString() : val.toFixed(2);
       
       kpis[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val
       };
    }

    this.renderKpiCard("cap-kpi-availhrs", kpis.availableHours.formatted, kpis.availableHours.wow, kpis.availableHours.vsPlan);
    this.renderKpiCard("cap-kpi-downtime", kpis.totalDowntime.formatted, kpis.totalDowntime.wow, kpis.totalDowntime.vsPlan);
    this.renderKpiCard("cap-kpi-util", kpis.capacityUtilisation.formatted, kpis.capacityUtilisation.wow, kpis.capacityUtilisation.vsPlan);
    this.renderKpiCard("cap-kpi-avail", kpis.workforceAvailability.formatted, kpis.workforceAvailability.wow, kpis.workforceAvailability.vsPlan);
    this.renderKpiCard("cap-kpi-prod", kpis.productivity.formatted, kpis.productivity.wow, kpis.productivity.vsPlan);
    this.renderKpiCard("cap-kpi-sick", kpis.sicknessPercent.formatted, kpis.sicknessPercent.wow, kpis.sicknessPercent.vsPlan);

    // Funnel
    let funnelSteps = isRegional ? [...regional.funnel] : [...DASHBOARD_DATA.capacitySheet2.funnel];
    funnelSteps = funnelSteps.map(s => ({
        ...s,
        hours: Math.round(s.hours * mult),
        formatted: s.formatted.includes('K') ? (s.hours * mult / 1000).toFixed(1) + 'K' : Math.round(s.hours * mult).toLocaleString()
    }));
    ChartManager.renderCapacityFunnel("capacity-funnel-container", funnelSteps);

    // Downtime Categories Donut & Table
    let categories = isRegional ? [...regional.downtimeCategories] : [...DASHBOARD_DATA.capacitySheet2.downtimeCategories];
    categories = categories.map(c => ({
        ...c,
        hours: Math.round(c.hours * mult)
    }));
    const totalDowntimeHrs = isRegional ? Math.round(regional.kpis.totalDowntime.value) : Math.round(DASHBOARD_DATA.capacitySheet2.totalDowntimeHours * mult);
    ChartManager.renderDowntimeChart("downtime-donut-chart", "downtime-table-container", categories, totalDowntimeHrs);

    // Capacity Risk Heatmap
    ChartManager.renderHeatmap("heatmap-container", DASHBOARD_DATA.capacitySheet2.heatmap, geo);

    // Region Efficiency Matrix
    ChartManager.renderEfficiencyMatrix("efficiency-matrix-chart", DASHBOARD_DATA.capacitySheet2.efficiencyMatrix, geo);

    // Bottom KPIs
    const bottom = DASHBOARD_DATA.capacitySheet2.bottomKpis;
    document.getElementById("bot-kpi-coverage").textContent = (parseFloat(bottom.coverage) + (mult-1)*10).toFixed(1) + "%";
    document.getElementById("bot-kpi-gap").textContent = Math.round(bottom.gapHrs * mult).toLocaleString() + " Hrs";
    document.getElementById("bot-kpi-risk").textContent = bottom.riskIndex;
  },"""

content = re.sub(r'  renderCapacitySheet2\(\) \{.*?(?=  /\*\*|  renderCapacitySheet3)', cap2_code, content, flags=re.DOTALL)


# 4. Complementary Views
comp_code = """  renderComplementaryViews() {
    const mult = this.getGlobalMultiplier();

    // Demand View
    const demand = DASHBOARD_DATA.demandView;
    const demBacklog = document.getElementById("dem-kpi-backlog");
    if (demBacklog) demBacklog.textContent = (demand.backlogWeeks * (1 + (mult-1)*0.5)).toFixed(1);
    
    const demInbound = document.getElementById("dem-kpi-inbound");
    if (demInbound) demInbound.textContent = Math.round(demand.inboundDemand * mult).toLocaleString();
    
    const demComp = document.getElementById("dem-kpi-comp");
    if (demComp) demComp.textContent = (parseFloat(demand.completionRate) + (mult-1)*5).toFixed(1) + "%";
    
    const demUnmet = document.getElementById("dem-kpi-unmet");
    if (demUnmet) demUnmet.textContent = Math.round(demand.unmetDemandHours * (2-mult)).toLocaleString();

    const demandBody = document.getElementById("demand-segments-tbody");
    if (demandBody) {
      demandBody.innerHTML = demand.demandBySegment.map(seg => `
        <tr class="hover:bg-slate-50 border-b border-slate-100">
          <td class="py-2.5 px-3 font-medium text-slate-800">${seg.segment}</td>
          <td class="py-2.5 px-3 text-right font-semibold text-slate-900">${Math.round(seg.volume * mult).toLocaleString()}</td>
          <td class="py-2.5 px-3 text-right">
            <span class="px-2 py-0.5 rounded text-xs font-semibold ${seg.capacityRatio >= 1.0 ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'}">
              ${(seg.capacityRatio * 100).toFixed(0)}%
            </span>
          </td>
        </tr>
      `).join("");
    }

    // Accuracy View
    const accuracy = DASHBOARD_DATA.accuracyView;
    const accMape = document.getElementById("acc-kpi-mape");
    if (accMape) accMape.textContent = (parseFloat(accuracy.overallMape) * (1 + (mult-1)*0.2)).toFixed(1) + "%";
    
    const accBias = document.getElementById("acc-kpi-bias");
    if (accBias) {
       const bias = parseFloat(accuracy.forecastBias) * (1 + (mult-1)*0.5);
       accBias.textContent = (bias > 0 ? "+" : "") + bias.toFixed(1) + "%";
    }

    const accuracyBody = document.getElementById("accuracy-table-tbody");
    if (accuracyBody) {
      accuracyBody.innerHTML = accuracy.historicalAccuracy.map(row => `
        <tr class="hover:bg-slate-50 border-b border-slate-100">
          <td class="py-2 px-3 font-medium text-slate-800">${row.week}</td>
          <td class="py-2 px-3 text-right text-slate-700">${Math.round(row.forecast * mult).toLocaleString()}</td>
          <td class="py-2 px-3 text-right text-slate-900 font-semibold">${Math.round(row.actual * mult).toLocaleString()}</td>
          <td class="py-2 px-3 text-right font-semibold ${row.errorPct > 5 ? 'text-amber-600' : 'text-emerald-600'}">
            ${(row.errorPct * (1 + (mult-1)*0.1)).toFixed(1)}%
          </td>
        </tr>
      `).join("");
    }
  },"""

content = re.sub(r'  renderComplementaryViews\(\) \{.*?(?=  /\*\*|  triggerDataRefresh)', comp_code, content, flags=re.DOTALL)

# 5. Fix remaining getGlobalMultiplier dependencies (Sheet 3 and Sheet 4)
content = content.replace('const geoMult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;', 'const geoMult = this.getGlobalMultiplier();')


with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Safely applied modifications!")
