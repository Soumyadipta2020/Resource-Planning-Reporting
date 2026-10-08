with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

old_mult_code = """  getGlobalMultiplier() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;

    let planMult = 1.0;
    if (this.state.selectedPlan === "gff2_2026") planMult = 1.15;

    let weekMult = 1.0;
    if (this.state.selectedWeek) {
       const match = this.state.selectedWeek.match(/wk(\d+)/);
       if (match) {
           const wkNum = parseInt(match[1]);
           weekMult = 1 + ((wkNum - 23) * 0.015);
       }
    }
    return geoMult * planMult * weekMult;
  },"""

new_mult_code = """  getGlobalMultipliers() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;

    let planMult = 1.0;
    if (this.state.selectedPlan === "gff2_2026") planMult = 1.15;

    let weekMult = 1.0;
    if (this.state.selectedWeek) {
       const match = this.state.selectedWeek.match(/wk(\d+)/);
       if (match) {
           const wkNum = parseInt(match[1]);
           weekMult = 1 + ((wkNum - 23) * 0.015);
       }
    }
    return {
       base: geoMult * weekMult,
       plan: geoMult * weekMult * planMult
    };
  },
  
  getGlobalMultiplier() {
    return this.getGlobalMultipliers().base; // Fallback for things that just need a quick scale
  },"""

js = js.replace(old_mult_code, new_mult_code)

old_chart_code = """    // Installs Weekly Combo Chart
    let weeklyData = DASHBOARD_DATA.executiveSummary.weeklyInstalls.map(d => ({
      week: d.week,
      actual: d.actual === null ? null : Math.round(d.actual * mult),
      plan: d.plan === null ? null : Math.round(d.plan * mult),
      variance: d.variance === null ? null : Math.round(d.variance * mult)
    }));"""

new_chart_code = """    // Installs Weekly Combo Chart
    const mults = this.getGlobalMultipliers();
    let weeklyData = DASHBOARD_DATA.executiveSummary.weeklyInstalls.map(d => {
      const a = d.actual === null ? null : Math.round(d.actual * mults.base);
      const p = d.plan === null ? null : Math.round(d.plan * mults.plan);
      return {
        week: d.week,
        actual: a,
        plan: p,
        variance: (a === null || p === null) ? null : (a - p)
      };
    });"""

js = js.replace(old_chart_code, new_chart_code)

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Updated multipliers and chart logic in app.js")
