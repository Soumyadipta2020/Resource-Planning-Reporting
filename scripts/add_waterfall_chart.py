with open('js/charts.js', 'r', encoding='utf-8') as f:
    content = f.read()

waterfall_func = '''
  renderWaterfallChart(elementId, waterfallData) {
    const ctx = document.getElementById(elementId);
    if (!ctx) return;
    
    if (this.instances[elementId]) {
      this.instances[elementId].destroy();
    }

    // Process floating bar data
    const labels = waterfallData.map(d => d.label);
    const data = [];
    const backgroundColors = [];
    
    let currentVal = 0;
    
    waterfallData.forEach((item, idx) => {
      if (item.type === 'total') {
        data.push([0, item.value]);
        backgroundColors.push('#1d4ed8'); // blue-700
        currentVal = item.value;
      } else {
        const endVal = currentVal + item.value;
        data.push([currentVal, endVal]);
        backgroundColors.push(item.value < 0 ? '#ef4444' : '#10b981'); // red-500 : emerald-500
        currentVal = endVal;
      }
    });

    const isScaled = true;
    
    this.instances[elementId] = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          data: data,
          backgroundColor: backgroundColors,
          borderWidth: 0,
          barPercentage: 0.9,
          categoryPercentage: 0.9
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: function(context) {
                const raw = context.raw;
                const diff = Math.abs(raw[1] - raw[0]);
                return diff.toLocaleString();
              }
            }
          },
          datalabels: {
            anchor: 'end',
            align: 'top',
            formatter: (value, ctx) => {
              const diff = value[1] - value[0];
              const displayNum = Math.abs(diff) >= 1000 ? (diff/1000).toFixed(0) + 'K' : diff.toString();
              return diff > 0 && ctx.dataIndex !== 0 && ctx.dataIndex !== data.length-1 ? '+' + displayNum : displayNum;
            },
            font: { size: 10, weight: 'bold' },
            color: '#64748b'
          }
        },
        scales: {
          y: {
            min: 12000,
            max: 18000,
            grid: { color: '#f1f5f9' },
            ticks: {
              font: { size: 10 },
              color: '#64748b',
              callback: function(value) { return (value/1000) + 'K'; }
            }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 10 }, color: '#64748b' }
          }
        }
      }
    });
  },
'''

# Find the end of ChartManager object
content = content.replace('};', waterfall_func + '\\n};')

with open('js/charts.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated js/charts.js")
