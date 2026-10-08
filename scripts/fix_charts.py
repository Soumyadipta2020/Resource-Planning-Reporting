import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'if (!mults.isPlanActive) p = null;',
    'if (this.state.selectedPlan === "gff2_2026" && d.actual !== null) p = null;'
)

content = content.replace(
    'if (!mults.isPlanActive) return null;',
    'if (this.state.selectedPlan === "gff2_2026" && metric.actuals[i] !== null) return null;'
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
