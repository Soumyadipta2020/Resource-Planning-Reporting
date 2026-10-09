import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = """
       const tbody = document.getElementById('demand-waterfall-tbody');
       if (tbody) {
           let dlBase = Math.round(1073 * activePlanMult);
           let contrBase = Math.round(905 * activePlanMult);
           let dlAct = Math.round(897 * mults.base);
           let contrAct = Math.round(792 * mults.base);
           
           let dlV = dlAct - dlBase;
           let contrV = contrAct - contrBase;
           let totV = actualValue - baseValue;
           
           const formatNum = (v) => v.toLocaleString();
           const formatVar = (v) => {
               if (!mults.isPlanActive) return '-';
               let icon = v >= 0 ? '↑' : '↓';
               let color = v >= 0 ? 'text-emerald-600' : 'text-red-600';
               return `<span class="${color} font-semibold">${v >= 0 ? '+' : ''}${formatNum(v)} <span class="ml-1">${icon}</span></span>`;
           };
           
           tbody.innerHTML = `
               <tr class="bg-slate-50">
                 <td class="py-1.5 px-3 font-bold text-left border-r border-slate-200">${planName}</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${mults.isPlanActive ? formatNum(dlBase) : '-'}</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${mults.isPlanActive ? formatNum(contrBase) : '-'}</td>
                 <td class="py-1.5 px-3 font-semibold">${mults.isPlanActive ? formatNum(baseValue) : '-'}</td>
               </tr>
               <tr>
                 <td class="py-1.5 px-3 font-bold text-left border-r border-slate-200">Actuals</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${formatNum(dlAct)}</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${formatNum(contrAct)}</td>
                 <td class="py-1.5 px-3 font-semibold">${formatNum(actualValue)}</td>
               </tr>
               <tr class="bg-slate-100">
                 <td class="py-1.5 px-3 font-bold text-left border-r border-slate-200">Variance</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${formatVar(dlV)}</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${formatVar(contrV)}</td>
                 <td class="py-1.5 px-3 font-bold">${formatVar(totV)}</td>
               </tr>
           `;
       }
"""

content = content.replace('// Also update the numbers in the table if they exist, but for now just updating plan name helps.', replacement.strip())

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

