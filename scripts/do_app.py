import re
with open('js/app.js', 'r', encoding='utf-8') as f: content = f.read()
sheet5_render = '''
  renderSheet5() {
    const data = DASHBOARD_DATA.capacitySheet5;
    if (!data) return;
    if (window.ChartManager && typeof window.ChartManager.renderWaterfallChart === 'function') {
      window.ChartManager.renderWaterfallChart('sheet5-waterfall-chart', data.waterfallData);
    }
    const tableContainer = document.getElementById('sheet5-waterfall-table-container');
    if (!tableContainer) return;
    let html = `
      <div class="overflow-x-auto w-full shadow-sm rounded border border-slate-200">
        <table class="w-full text-[10px] border-collapse whitespace-nowrap">
          <thead>
            <tr class="bg-cyan-600 text-white text-center font-semibold">
              <th class="py-1.5 px-2 text-left sticky left-0 bg-cyan-700 z-10 w-24 border-r border-cyan-500"></th>
              ${data.tableColumns.map(col => `<th class="py-1.5 px-2 border-r border-cyan-500">${col}</th>`).join('')}
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200">
    `;
    data.tableRows.forEach((row, idx) => {
      const isAlt = idx % 2 === 1 ? 'bg-slate-50/60' : 'bg-white';
      const isVariance = row.rowLabel === 'Variance';
      const textWeight = isVariance ? 'font-bold text-slate-800' : 'text-slate-700 font-medium';
      const bgClass = isVariance ? 'bg-slate-100' : isAlt;
      html += `<tr class="${bgClass} hover:bg-blue-50/50 transition-colors">`;
      html += `<td class="py-1.5 px-2 text-left sticky left-0 ${bgClass} z-10 font-bold text-slate-700 border-r border-slate-200 shadow-[1px_0_0_rgba(0,0,0,0.05)]">${row.rowLabel}</td>`;
      if (isVariance) {
        row.values.forEach(valObj => {
          const arrowIcon = valObj.dir === 'up' ? '?' : '?';
          html += `<td class="py-1 px-2 text-right border-r border-slate-200 ${valObj.color} font-semibold">
            <span class="inline-flex items-center gap-0.5 justify-end">
              ${valObj.val} <span>${arrowIcon}</span>
            </span>
          </td>`;
        });
      } else {
        row.values.forEach(val => {
          html += `<td class="py-1.5 px-2 text-right border-r border-slate-200 ${textWeight}">${val}</td>`;
        });
      }
      html += `</tr>`;
    });
    html += `</tbody></table></div>`;
    tableContainer.innerHTML = html;
  },
'''
content = content.replace('this.renderSheet4Chart();\n    this.renderSheet4Table();', 'this.renderSheet4Chart();\n    this.renderSheet4Table();\n    this.renderSheet5();')
content = re.sub(r'  updateCapacitySheet4Chart\(\) \{\n.*?\}\n\n\}', lambda m: m.group(0).replace('\n\n}', '\n' + sheet5_render + '\n}'), content, flags=re.DOTALL)
with open('js/app.js', 'w', encoding='utf-8') as f: f.write(content)
