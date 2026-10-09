import re

with open('js/charts.js', 'r', encoding='utf-8') as f:
    content = f.read()

new_methods = """
  renderDemandCapacityChart(containerId, data) {
    const ctx = document.getElementById(containerId);
    if (!ctx) return;
    if (this.instances[containerId]) this.instances[containerId].destroy();

    this.instances[containerId] = new Chart(ctx, {
      type: 'line',
      data: {
        labels: data.labels,
        datasets: [
          {
            label: 'Workload Forecast',
            data: data.workload,
            borderColor: '#1e40af', // blue-800
            backgroundColor: '#1e40af',
            borderWidth: 2,
            pointRadius: 2,
            fill: false,
            order: 1
          },
          {
            label: 'Available Capacity',
            data: data.capacity,
            borderColor: '#10b981', // emerald-500
            backgroundColor: '#10b981',
            borderWidth: 2,
            pointRadius: 2,
            fill: false,
            order: 2
          },
          {
            label: 'Capacity Gap',
            data: data.capacity, // Base for filling
            borderColor: 'transparent',
            backgroundColor: 'rgba(239, 68, 68, 0.2)', // red-500 light
            fill: '-1', // Fill to previous dataset (Workload) - requires some trickery, let's just do a custom fill or use filler plugin properly.
            // Actually, filling between two lines in Chart.js 3+:
            // set fill: '-1' on the top dataset.
            pointRadius: 0,
            order: 3
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            mode: 'index',
            intersect: false
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: function(value) { return (value/1000) + 'K'; },
              font: { size: 9, family: 'Inter' }
            },
            grid: { color: '#f1f5f9' }
          },
          x: {
            ticks: { font: { size: 9, family: 'Inter' }, maxRotation: 0 },
            grid: { display: false }
          }
        }
      }
    });
    
    // To properly fill between two lines:
    // Workload Forecast is dataset 0
    // Available Capacity is dataset 1
    // Let's modify dataset 0 to fill to dataset 1:
    this.instances[containerId].data.datasets[0].fill = {
       target: 1,
       above: 'rgba(239, 68, 68, 0.2)',   // Red if Workload > Capacity
       below: 'transparent'               // Transparent if Workload < Capacity
    };
    this.instances[containerId].update();
  },

  renderForecastAccuracyChart(containerId, data) {
    const ctx = document.getElementById(containerId);
    if (!ctx) return;
    if (this.instances[containerId]) this.instances[containerId].destroy();

    this.instances[containerId] = new Chart(ctx, {
      type: 'line',
      data: {
        labels: data.labels,
        datasets: [{
          data: data.accuracy,
          borderColor: '#1d4ed8', // blue-700
          backgroundColor: '#1d4ed8',
          borderWidth: 2,
          pointRadius: 3,
          pointBackgroundColor: '#1d4ed8',
          fill: false
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 30,
            ticks: {
              callback: function(value) { return value + '%'; },
              stepSize: 10,
              font: { size: 9, family: 'Inter' }
            },
            grid: { color: '#f1f5f9' }
          },
          x: {
            ticks: { font: { size: 9, family: 'Inter' } },
            grid: { display: false }
          }
        }
      }
    });
  },

  renderWorkloadTrendChart(containerId, data) {
    const ctx = document.getElementById(containerId);
    if (!ctx) return;
    if (this.instances[containerId]) this.instances[containerId].destroy();

    this.instances[containerId] = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.labels,
        datasets: [
          { label: 'Install', data: data.install, backgroundColor: '#0f172a' },
          { label: 'Repair', data: data.repair, backgroundColor: '#0f766e' }, // teal-700
          { label: 'EV', data: data.ev, backgroundColor: '#eab308' }, // yellow-500
          { label: 'Warranty', data: data.warranty, backgroundColor: '#059669' }, // emerald-600
          { label: 'Survey', data: data.survey, backgroundColor: '#64748b' } // slate-500
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { mode: 'index', intersect: false }
        },
        scales: {
          x: { stacked: true, grid: { display: false }, ticks: { font: { size: 9 } } },
          y: { 
            stacked: true, 
            grid: { color: '#f1f5f9' },
            ticks: {
               callback: function(value) { return (value/1000) + 'K'; },
               font: { size: 9 }
            }
          }
        }
      }
    });
  },

  renderDemandGapChart(containerId, data) {
    const ctx = document.getElementById(containerId);
    if (!ctx) return;
    if (this.instances[containerId]) this.instances[containerId].destroy();

    this.instances[containerId] = new Chart(ctx, {
      type: 'line',
      data: {
        labels: data.labels,
        datasets: [
          {
            label: 'Demand',
            data: data.demand,
            borderColor: '#ef4444', // red-500
            backgroundColor: '#ef4444',
            borderWidth: 1.5,
            pointRadius: 1,
            fill: {
              target: 1,
              above: 'rgba(239, 68, 68, 0.2)', // fill area
              below: 'transparent'
            }
          },
          {
            label: 'Capacity',
            data: data.capacity,
            borderColor: '#1d4ed8', // blue-700
            backgroundColor: '#1d4ed8',
            borderWidth: 1.5,
            pointRadius: 1,
            fill: false
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: { mode: 'index', intersect: false }
        },
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 8 } } },
          y: { 
            grid: { color: '#f1f5f9' },
            ticks: {
               callback: function(value) { return (value/1000) + 'K'; },
               font: { size: 8 }
            }
          }
        }
      }
    });
  }
"""

if "renderDemandCapacityChart" not in content:
    content = content.replace("};", new_methods + "\n};")
    with open('js/charts.js', 'w', encoding='utf-8') as f:
        f.write(content)

