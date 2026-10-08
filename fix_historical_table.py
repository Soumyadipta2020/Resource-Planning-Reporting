import re

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

old_cur = """      if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
        const numFc = parseInt(curForecast.replace(/,/g, "")) * fcMult;
        const numAct = parseInt(curActual.replace(/,/g, "")) * actMult;
        curForecast = Math.round(numFc).toLocaleString();
        curActual = Math.round(numAct).toLocaleString();
        const diff = Math.round(numAct - numFc);
        variance = diff.toLocaleString();
      }

      html += `<td class="py-1.5 px-2 text-right bg-cyan-50/40 text-slate-800 ${textWeight}">${curForecast}</td>`;"""

new_cur = """      if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
        const numFc = parseInt(curForecast.replace(/,/g, "")) * fcMult;
        const numAct = parseInt(curActual.replace(/,/g, "")) * actMult;
        curForecast = Math.round(numFc).toLocaleString();
        curActual = Math.round(numAct).toLocaleString();
        const diff = Math.round(numAct - numFc);
        variance = diff.toLocaleString();
      }
      
      if (!mults.isPlanActive) {
          curForecast = "-";
          variance = "-";
      }

      html += `<td class="py-1.5 px-2 text-right bg-cyan-50/40 text-slate-800 ${textWeight}">${curForecast}</td>`;"""
js = js.replace(old_cur, new_cur)


old_fc = """        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * fcMult;
          displayVal = Math.round(num).toLocaleString();
        }

        // Inline sparkbar for Utilisation row"""
new_fc = """        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * fcMult;
          displayVal = Math.round(num).toLocaleString();
        }
        
        if (!mults.isPlanActive) {
            displayVal = "-";
        }

        // Inline sparkbar for Utilisation row"""
js = js.replace(old_fc, new_fc)

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Updated js/app.js table")
