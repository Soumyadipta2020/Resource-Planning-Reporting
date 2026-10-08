import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix weeklyInstalls
old_weekly = 'if (this.state.selectedPlan === "gff2_2026" && d.actual !== null) p = null;'
new_weekly = 'const wkNum = parseInt(d.week.replace("WK ", ""));\n        if (this.state.selectedPlan === "gff2_2026" && wkNum < 37) p = null;'
content = content.replace(old_weekly, new_weekly)

# Fix capacitySheet4 chart
old_sheet4 = 'if (this.state.selectedPlan === "gff2_2026" && metric.actuals[i] !== null) return null;'
new_sheet4 = '''const weekLabel = rawSeries.weeks[i];
              const weekObj = DASHBOARD_DATA.metadata.reportingWeeks.find(w => w.date === weekLabel);
              const wkNum = weekObj ? weekObj.weekNum : (37 + i);
              if (this.state.selectedPlan === "gff2_2026" && wkNum < 37) return null;'''
content = content.replace(old_sheet4, new_sheet4)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
