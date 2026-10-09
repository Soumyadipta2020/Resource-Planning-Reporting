with open('js/charts.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('  renderCapacityWaterfallChart(elementId, waterfallData) {')
if start_idx == -1:
    print("Could not find start")
    exit(1)

# Find the closing brace
brace_count = 0
end_idx = -1
for i in range(start_idx, len(content)):
    if content[i] == '{':
        brace_count += 1
    elif content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            end_idx = i + 1
            break

if end_idx == -1:
    print("Could not find end")
    exit(1)

new_fn = """  renderCapacityWaterfallChart(elementId, waterfallData) {
    const ctx = document.getElementById(elementId);
    if (!ctx) return;
    if (this.instances[elementId]) {
      this.instances[elementId].destroy();
    }
    
    const labels = waterfallData.map(d => d.label);
    const bottomData = [];
    const topData = [];
    const backgroundColors = [];
    
    let currentVal = 0;
    const Y_MIN = 12000;
    
    waterfallData.forEach((item) => {
      if (item.type === 'total') {
        bottomData.push(Y_MIN);
        topData.push(item.value - Y_MIN);
        backgroundColors.push('#1d4ed8');
        currentVal = item.value;
      } else {
        const endVal = currentVal + item.value;
        const lowest = Math.min(currentVal, endVal);
        const diff = Math.abs(item.value);
        
        bottomData.push(lowest);
        topData.push(diff);
        backgroundColors.push(item.value < 0 ? '#ef4444' : '#10b981');
        
        currentVal = endVal;
      }
    });
    
    try {
      this.instances[elementId] = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              label: 'Invisible Base',
              data: bottomData,
              backgroundColor: 'transparent',
              borderColor: 'transparent',
              hoverBackgroundColor: 'transparent',
              borderWidth: 0,
              barPercentage: 0.9,
              categoryPercentage: 0.9
            },
            {
              label: 'Capacity',
              data: topData,
              backgroundColor: backgroundColors,
              borderWidth: 0,
              barPercentage: 0.9,
              categoryPercentage: 0.9
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              filter: function(tooltipItem) {
                return tooltipItem.datasetIndex === 1;
              },
              callbacks: {
                label: function(context) {
                  const item = waterfallData[context.dataIndex];
                  if (item.type === 'total') return item.value.toLocaleString();
                  return Math.abs(item.value).toLocaleString();
                }
              }
            }
          },
          scales: {
            x: {
              stacked: true,
              grid: { display: false },
              ticks: { font: { size: 10 }, color: '#64748b' }
            },
            y: {
              stacked: true,
              min: Y_MIN,
              max: 18000,
              grid: { color: '#f1f5f9' },
              ticks: {
                font: { size: 10 },
                color: '#64748b',
                callback: function(value) { return (value/1000) + 'K'; }
              }
            }
          }
        }
      });
    } catch (e) {
      console.error(e);
      ctx.parentElement.innerHTML = '<div style="color:red;padding:10px;">Chart Error: ' + e.message + '</div>';
    }
  }"""

new_content = content[:start_idx] + new_fn + content[end_idx:]

with open('js/charts.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Successfully replaced function.")