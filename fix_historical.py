import re

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# 1. Update multipliers
js = js.replace("""    let planMult = 1.0;
    if (this.state.selectedPlan === "gff2_2026") planMult = 1.15;""",
"""    let planMult = 1.0;
    let isPlanActive = true;
    if (this.state.selectedPlan === "gff2_2026") {
       planMult = 1.15;
       isPlanActive = false; // Historic weeks are before Sep 2026
    }""")

js = js.replace("""    return {
       base: geoMult * weekMult,
       plan: geoMult * weekMult * planMult
    };""",
"""    return {
       base: geoMult * weekMult,
       plan: geoMult * weekMult * planMult,
       isPlanActive: isPlanActive
    };""")

# 2. Update KPI loop in Exec Summary
old_exec_kpi = """    const mult = this.getGlobalMultiplier();

    // Scale KPI Values"""
new_exec_kpi = """    const mults = this.getGlobalMultipliers();
    const mult = mults.base;

    // Scale KPI Values"""
js = js.replace(old_exec_kpi, new_exec_kpi)

old_kpi_assign = """       kpiData[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val
       };"""
new_kpi_assign = """       kpiData[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val,
          vsPlan: mults.isPlanActive ? baseKpis[key].vsPlan : null
       };"""
js = js.replace(old_kpi_assign, new_kpi_assign)

# 3. Update Chart mapping
old_chart = """    let weeklyData = DASHBOARD_DATA.executiveSummary.weeklyInstalls.map(d => {
      const a = d.actual === null ? null : Math.round(d.actual * mults.base);
      const p = d.plan === null ? null : Math.round(d.plan * mults.plan);
      return {"""
new_chart = """    let weeklyData = DASHBOARD_DATA.executiveSummary.weeklyInstalls.map(d => {
      const a = d.actual === null ? null : Math.round(d.actual * mults.base);
      let p = d.plan === null ? null : Math.round(d.plan * mults.plan);
      if (!mults.isPlanActive) p = null;
      return {"""
js = js.replace(old_chart, new_chart)

# 4. Update Waterfall
old_water = """    // Waterfall Chart Drivers
    let drivers = DASHBOARD_DATA.executiveSummary.waterfallDrivers.map(d => ({
      ...d,
      value: Math.round(d.value * mult)
    }));"""
new_water = """    // Waterfall Chart Drivers
    let drivers = DASHBOARD_DATA.executiveSummary.waterfallDrivers.map(d => {
      let v = Math.round(d.value * mults.base);
      if (!mults.isPlanActive) {
          if (d.name === "Plan") v = 0; // nullify plan
          else if (d.name !== "Actuals") v = 0; // nullify drivers
      }
      return {
        ...d,
        value: v
      };
    });"""
js = js.replace(old_water, new_water)

# 5. Update renderKpiCard
old_kpi_card = """    if (planEl) {
      const isUp = vsPlanPct >= 0;
      planEl.innerHTML = `
        <span class="${isUp ? 'text-emerald-700' : 'text-red-700'} font-semibold flex items-center">
          ${isUp ? '?' : '?'} ${Math.abs(vsPlanPct)}% vs Plan
        </span>
      `;
    }"""
new_kpi_card = """    if (planEl) {
      if (vsPlanPct === null || vsPlanPct === undefined || vsPlanPct === "N/A") {
        planEl.innerHTML = `<span class="text-slate-400 font-semibold flex items-center">- vs Plan</span>`;
      } else {
        const isUp = vsPlanPct >= 0;
        planEl.innerHTML = `
          <span class="${isUp ? 'text-emerald-700' : 'text-red-700'} font-semibold flex items-center">
            ${isUp ? '?' : '?'} ${Math.abs(vsPlanPct)}% vs Plan
          </span>
        `;
      }
    }"""
js = js.replace(old_kpi_card, new_kpi_card)


with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Updated js/app.js")
