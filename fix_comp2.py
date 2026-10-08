import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

comp_code = '''  renderComplementaryViews() {
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
    if (demUnmet) demUnmet.textContent = Math.round(demand.unmetDemandHours * (2-mult)).toLocaleString(); // Unmet goes down if mult goes up

    const demandBody = document.getElementById("demand-segments-tbody");
    if (demandBody) {
      demandBody.innerHTML = demand.demandBySegment.map(seg => 
        <tr class="hover:bg-slate-50 border-b border-slate-100">
          <td class="py-2.5 px-3 font-medium text-slate-800"></td>
          <td class="py-2.5 px-3 text-right font-semibold text-slate-900"></td>
          <td class="py-2.5 px-3 text-right">
            <span class="px-2 py-0.5 rounded text-xs font-semibold ">
              %
            </span>
          </td>
        </tr>
      ).join("");
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
      accuracyBody.innerHTML = accuracy.historicalAccuracy.map(row => 
        <tr class="hover:bg-slate-50 border-b border-slate-100">
          <td class="py-2 px-3 font-medium text-slate-800"></td>
          <td class="py-2 px-3 text-right text-slate-700"></td>
          <td class="py-2 px-3 text-right text-slate-900 font-semibold"></td>
          <td class="py-2 px-3 text-right font-semibold ">
            %
          </td>
        </tr>
      ).join("");
    }
  },'''

content = re.sub(r'  renderComplementaryViews\(\) \{.*?(?=  /\*\*|  triggerDataRefresh)', comp_code, content, flags=re.DOTALL)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated comp views with IDs!")
