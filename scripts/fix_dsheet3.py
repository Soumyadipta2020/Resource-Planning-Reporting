import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_dsheet3(match):
    return """    } else if (this.state.demandSheet === "dsheet-3") {
       const mults = this.getGlobalMultipliers();
       const bMult = mults.base;
       const pMult = mults.plan || 1.0;
       
       // Render ES Weekly Workload chart
       const series = {
         weeks: ["25 May", "1 Jun", "8 Jun", "15 Jun", "22 Jun", "29 Jun", "6 Jul", "13 Jul", "20 Jul"],
         metrics: {
           workload: {
             label: "Jobs",
             unit: "",
             actuals: [5944, 4804, 6090, 6099, 5671, 5478, null, null, null].map(v => v === null ? null : Math.round(v * bMult)),
             forecast: [5000, 5200, 5400, 5300, 5500, 5600, 5700, 5800, 5900].map(v => Math.round(v * bMult * pMult))
           }
         }
       };
       ChartManager.renderWeeklyActualVsForecast('demand-workload-chart', series, 'workload');"""

content = re.sub(
    r'    } else if \(this\.state\.demandSheet === "dsheet-3"\) \{\s*// Render ES Weekly Workload chart\s*const series = \{\s*weeks: \["25 May".*?metrics: \{\s*workload: \{\s*label: "Jobs",\s*unit: "",\s*actuals: \[[0-9, null]+\],\s*forecast: \[[0-9, ]+\]\s*\}\s*\}\s*\};\s*ChartManager\.renderWeeklyActualVsForecast\(\'demand-workload-chart\', series, \'workload\'\);',
    replace_dsheet3,
    content,
    flags=re.DOTALL
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
