import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

render_code = """
  updateDemandSheet() {
    if (this.state.demandSheet === "dsheet-1") {
       // Demand overview
    } else if (this.state.demandSheet === "dsheet-3") {
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
       ChartManager.renderWeeklyActualVsForecast('demand-workload-chart', series, 'workload');
    } else if (this.state.demandSheet === "dsheet-4") {
       // Render Demand Waterfall chart
       const waterfallData = [
         { label: 'Base', value: 1988, type: 'total' },
         { label: 'DL Installs', value: -176, type: 'down' },
         { label: 'Contr. Installs', value: -113, type: 'down' },
         { label: 'Final', value: 1689, type: 'total' }
       ];
       ChartManager.renderCapacityWaterfallChart('demand-waterfall-chart', waterfallData);
    }
  },
"""

content = re.sub(r'  updateDemandSheet\(\) \{.*?(?=^\s*switchCapacitySheet)', render_code + '  ', content, flags=re.DOTALL | re.MULTILINE)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app.js with demand chart rendering logic")

