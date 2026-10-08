import re

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# 1. Update getGlobalMultipliers
old_mult = """    let planMult = 1.0;
    if (this.state.selectedPlan === "gff2_2026") planMult = 1.15;"""

new_mult = """    let planMult = 1.0;
    let isPlanActive = true;
    if (this.state.selectedPlan === "gff2_2026") {
        planMult = 1.15;
        // Since all dashboard weeks are < Sept 2026, GFF2 has no plan data yet
        isPlanActive = false;
    }"""
js = js.replace(old_mult, new_mult)

old_ret = """    return {
       base: geoMult * weekMult,
       plan: geoMult * weekMult * planMult
    };"""

new_ret = """    return {
       base: geoMult * weekMult,
       plan: geoMult * weekMult * planMult,
       isPlanActive: isPlanActive
    };"""
js = js.replace(old_ret, new_ret)


# 2. Update KPI formatting loop in Executive Summary
old_kpi_loop = """       kpiData[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val
       };"""

new_kpi_loop = """       kpiData[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val,
          vsPlan: mults.isPlanActive ? baseKpis[key].vsPlan : "N/A"
       };"""
# Note: we need to replace it in renderExecutiveSummary, wait, renderExecutiveSummary doesn't have `mults`. It has `mult`.
