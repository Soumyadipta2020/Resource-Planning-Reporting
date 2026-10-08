import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix capacity sheet 2
cap2_code = '''  renderCapacitySheet2() {
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
  },'''

content = re.sub(r'  renderCapacitySheet2\(\) \{.*?(?=  /\*\*|  renderCapacitySheet3)', cap2_code, content, flags=re.DOTALL)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated cap2")
