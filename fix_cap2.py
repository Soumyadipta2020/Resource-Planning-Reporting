import re

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

old_cap2 = """  renderCapacitySheet2() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const regional = isRegional ? DASHBOARD_DATA.regionalData[geo] : null;
    
    const mult = this.getGlobalMultiplier();"""
new_cap2 = """  renderCapacitySheet2() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const regional = isRegional ? DASHBOARD_DATA.regionalData[geo] : null;
    
    const mults = this.getGlobalMultipliers();
    const mult = mults.base;"""
js = js.replace(old_cap2, new_cap2)

old_kpis = """       kpis[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val
       };"""
new_kpis = """       kpis[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val,
          vsPlan: mults.isPlanActive ? baseKpis[key].vsPlan : null
       };"""
js = js.replace(old_kpis, new_kpis)

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Updated cap2")
