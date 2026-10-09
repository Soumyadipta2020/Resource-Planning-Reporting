with open('js/charts.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re

new_fn = """  renderCapacityWaterfallChart(elementId, waterfallData) {
    const ctx = document.getElementById(elementId);
    if (!ctx) return;
    if (this.instances[elementId]) {
      this.instances[elementId].destroy();
    }
    const labels = waterfallData.map(d => d.label);
    const data = waterfallData.map(d => d.value);
    
    this.instances[elementId] = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Capacity',
          data: data,
          backgroundColor: '#1d4ed8'
        }]
      }
    });
  }"""

content = re.sub(
    r'  renderCapacityWaterfallChart\(elementId, waterfallData\) \{[\s\S]*?  \}\n',
    new_fn + '\n',
    content
)

with open('js/charts.js', 'w', encoding='utf-8') as f:
    f.write(content)