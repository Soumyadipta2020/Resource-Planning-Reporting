import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add getGlobalMultiplier()
mult_func = '''  getGlobalMultiplier() {
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
   */'''

content = content.replace('  /**\n   * Master Update: Recalculates and updates everything based on current state & filters\n   */', mult_func)

# Replace all regional multipliers with this.getGlobalMultiplier() in renderExecutiveSummary, renderCapacitySheet2, etc.

content = content.replace('regional.multiplier', 'this.getGlobalMultiplier()')
content = content.replace('const geoMult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;', 'const geoMult = this.getGlobalMultiplier();')
content = content.replace('const mult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;', 'const mult = this.getGlobalMultiplier();')

# We need to make sure the base non-regional Data also scales by plan and week!
# Wait, if isRegional is false, it currently uses DASHBOARD_DATA.executiveSummary.kpis directly without scaling!
# We should scale it!
# To keep it simple, let's just make the entire dummy data calculation always use the multiplier.

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated js/app.js!")
