import re

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

old_cap3 = """  renderCapacitySheet3() {
    const tableBody = document.getElementById("capacity-comparison-tbody");
    if (!tableBody) return;

    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const mult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;"""

new_cap3 = """  renderCapacitySheet3() {
    const tableBody = document.getElementById("capacity-comparison-tbody");
    if (!tableBody) return;

    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const mults = this.getGlobalMultipliers();
    const mult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;"""
js = js.replace(old_cap3, new_cap3)

old_cap3_row = """      const isVsPlanDown = vsPlan.includes("-");
      const isVsLWDown = vsLW.includes("-");

      html += `
        <tr class="hover:bg-slate-50/80 transition-colors border-b border-slate-200">
          <td class="py-3 px-4 font-bold text-slate-900">${r.metric}</td>
          <td class="py-3 px-3 text-right font-semibold text-slate-800">${thisWeekAct}</td>
          <td class="py-3 px-3 text-right text-slate-700">${thisWeekPlan}</td>
          <td class="py-3 px-3 text-right font-medium ${isVsPlanDown ? 'text-red-600' : 'text-emerald-600'}">
            ${isVsPlanDown ? '?' : '?'} ${vsPlan}
          </td>"""
          
new_cap3_row = """      if (!mults.isPlanActive) {
        thisWeekPlan = "-";
        vsPlan = "-";
        varPlanAbs = "-";
        varPlanPct = "-";
      }
      
      const isVsPlanDown = vsPlan.includes("-") && vsPlan !== "-";
      const isVsLWDown = vsLW.includes("-") && vsLW !== "-";

      html += `
        <tr class="hover:bg-slate-50/80 transition-colors border-b border-slate-200">
          <td class="py-3 px-4 font-bold text-slate-900">${r.metric}</td>
          <td class="py-3 px-3 text-right font-semibold text-slate-800">${thisWeekAct}</td>
          <td class="py-3 px-3 text-right text-slate-700">${thisWeekPlan}</td>
          <td class="py-3 px-3 text-right font-medium ${isVsPlanDown ? 'text-red-600' : (vsPlan === '-' ? 'text-slate-400' : 'text-emerald-600')}">
            ${vsPlan === '-' ? '-' : (isVsPlanDown ? '?' : '?')} ${vsPlan === '-' ? '' : vsPlan}
          </td>"""
js = js.replace(old_cap3_row, new_cap3_row)

old_cap3_row2 = """          <td class="py-3 px-3 text-right font-semibold ${isVsPlanDown ? 'text-red-600' : 'text-emerald-600'}">
            ${isVsPlanDown ? '?' : '?'} ${varPlanAbs}
          </td>"""
new_cap3_row2 = """          <td class="py-3 px-3 text-right font-semibold ${isVsPlanDown ? 'text-red-600' : (varPlanAbs === '-' ? 'text-slate-400' : 'text-emerald-600')}">
            ${varPlanAbs === '-' ? '-' : (isVsPlanDown ? '?' : '?')} ${varPlanAbs === '-' ? '' : varPlanAbs}
          </td>"""
js = js.replace(old_cap3_row2, new_cap3_row2)

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Updated js/app.js capacitySheet3")
