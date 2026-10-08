import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace if (isRegional) logic in renderExecutiveSummary
exec_summary_code = '''  renderExecutiveSummary() {
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
       else if (fmt.includes('£M')) fmt = '£' + (val).toFixed(2) + 'M';
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
  },'''

content = re.sub(r'  renderExecutiveSummary\(\) \{.*?(?=  /\*\*|  updateCapacitySheet)', exec_summary_code, content, flags=re.DOTALL)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated js/app.js logic for Executive Summary filters!")
