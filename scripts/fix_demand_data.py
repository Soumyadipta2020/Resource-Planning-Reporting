import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Make Demand Overview (dsheet-1) numbers change with both mults.base and mults.plan
# Line: const mult = mults.base;
content = content.replace(
    'const mult = mults.base;',
    'const mult = mults.base * (mults.plan || 1.0);'
)

# Fix dsheet-3 to scale with mults
dsheet3_old = '''      } else if (this.state.demandSheet === "dsheet-3") {
         // Render ES Weekly Workload chart
         const series = {
           weeks: ["25 May", "1 Jun", "8 Jun", "15 Jun", "22 Jun", "29 Jun", "6 Jul", "13 Jul", "20 Jul"],
           metrics: {
             workload: {
               label: "Jobs",
               unit: "",
               actuals: [5944, 4804, 6090, 6099, 5671, 5478, null, null, null],
               forecast: [5000, 5200, 5400, 5300, 5500, 5600, 5700, 5800, 5900]
             }
           }
         };
         ChartManager.renderWeeklyActualVsForecast('demand-workload-chart', series, 'workload');'''

dsheet3_new = '''      } else if (this.state.demandSheet === "dsheet-3") {
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
         ChartManager.renderWeeklyActualVsForecast('demand-workload-chart', series, 'workload');'''

content = content.replace(dsheet3_old, dsheet3_new)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Data dynamically scaled")
