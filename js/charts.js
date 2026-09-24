/**
 * Visualizations & Chart Rendering Engine
 * Handles rendering and interactive updates for:
 * 1. Installs Combo Chart (Bar + Plan Line + Variance Bars)
 * 2. Variance Analysis Waterfall Chart
 * 3. 12-Week Trend Sparklines
 * 4. Capacity Funnel Component
 * 5. Downtime Donut Chart
 * 6. Capacity Risk Heatmap
 * 7. Region Efficiency Scatter Matrix
 * 8. Sheet 4 ES Weekly Actual vs Forecast Line Chart
 */

const ChartManager = {
  instances: {},

  // Color Palette aligned with corporate enterprise dashboard
  colors: {
    primaryDark: "#0f172a",
    navy: "#1e3a8a",
    blue: "#2563eb",
    cyan: "#0284c7",
    teal: "#0d9488",
    green: "#16a34a",
    emerald: "#10b981",
    red: "#dc2626",
    amber: "#f59e0b",
    greyLight: "#f1f5f9",
    greyBorder: "#e2e8f0",
    textMuted: "#64748b"
  },

  /**
   * Render or update the Installs Weekly Combo Chart (Executive Summary)
   */
  renderWeeklyInstallsChart(containerId, weeklyData) {
    const ctx = document.getElementById(containerId);
    if (!ctx) return;

    if (this.instances.weeklyInstalls) {
      this.instances.weeklyInstalls.destroy();
    }

    const labels = weeklyData.map(d => d.week);
    const actuals = weeklyData.map(d => d.actual);
    const plans = weeklyData.map(d => d.plan);
    const variances = weeklyData.map(d => d.variance);

    this.instances.weeklyInstalls = new Chart(ctx, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            type: "line",
            label: "Plan",
            data: plans,
            borderColor: "#0284c7",
            borderDash: [5, 5],
            borderWidth: 2,
            pointBackgroundColor: "#0284c7",
            pointRadius: 4,
            pointHoverRadius: 6,
            fill: false,
            tension: 0.2,
            order: 1
          },
          {
            type: "bar",
            label: "Actuals",
            data: actuals,
            backgroundColor: "#0f172a",
            hoverBackgroundColor: "#1e293b",
            borderRadius: 3,
            barPercentage: 0.6,
            categoryPercentage: 0.8,
            order: 2
          },
          {
            type: "bar",
            label: "Variance",
            data: variances,
            backgroundColor: variances.map(v => v >= 0 ? "#16a34a" : "#dc2626"),
            borderRadius: 2,
            barPercentage: 0.35,
            yAxisID: "yVariance",
            order: 3
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: "top",
            labels: {
              usePointStyle: true,
              font: { family: "Inter, sans-serif", size: 11, weight: "600" },
              color: "#334155"
            }
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                let label = context.dataset.label || '';
                if (label) label += ': ';
                if (context.parsed.y !== null) {
                  label += context.parsed.y.toLocaleString();
                }
                return label;
              }
            }
          }
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: "500" }, color: "#64748b" }
          },
          y: {
            position: "left",
            beginAtZero: true,
            max: 3200,
            ticks: {
              stepSize: 1000,
              callback: value => (value === 0 ? "0K" : (value / 1000) + "K"),
              font: { size: 11 },
              color: "#64748b"
            },
            grid: { color: "#f1f5f9" }
          },
          yVariance: {
            position: "right",
            display: false,
            min: -500,
            max: 500
          }
        }
      }
    });
  },

  /**
   * Render SVG Waterfall Chart (Variance Analysis Drivers - This Week)
   */
  renderWaterfallChart(containerId, drivers) {
    const container = document.getElementById(containerId);
    if (!container) return;

    let runningTotal = 0;
    const computedBars = [];

    drivers.forEach((driver) => {
      if (driver.name === "Plan") {
        computedBars.push({
          name: driver.name,
          start: 0,
          end: driver.value,
          value: driver.value,
          displayValue: driver.value.toLocaleString(),
          isTotal: true,
          color: "#1e3a8a"
        });
        runningTotal = driver.value;
      } else if (driver.name === "Actuals") {
        computedBars.push({
          name: driver.name,
          start: 0,
          end: runningTotal,
          value: runningTotal,
          displayValue: runningTotal.toLocaleString(),
          isTotal: true,
          color: "#0f172a"
        });
      } else {
        const nextTotal = runningTotal + driver.value;
        const isPos = driver.value >= 0;
        computedBars.push({
          name: driver.name,
          start: isPos ? runningTotal : nextTotal,
          end: isPos ? nextTotal : runningTotal,
          value: driver.value,
          displayValue: (isPos ? "+" : "") + driver.value.toLocaleString(),
          isTotal: false,
          color: isPos ? "#16a34a" : "#dc2626"
        });
        runningTotal = nextTotal;
      }
    });

    const maxValue = 3000;
    const height = 260;
    const barWidth = 42;
    const chartPaddingTop = 40;
    const chartPaddingBottom = 40;
    const chartPaddingLeft = 45;
    const chartPaddingRight = 20;
    const availableHeight = height - chartPaddingTop - chartPaddingBottom;

    const totalWidth = chartPaddingLeft + chartPaddingRight + computedBars.length * 62;
    const svgWidth = Math.max(totalWidth, 540);
    const spacing = (svgWidth - chartPaddingLeft - chartPaddingRight) / computedBars.length;

    let svgHtml = `
      <svg viewBox="0 0 ${svgWidth} ${height}" class="w-full h-full" style="min-height: 240px; font-family: Inter, sans-serif;">
        <!-- Background Gridlines -->
        <line x1="${chartPaddingLeft}" y1="${chartPaddingTop}" x2="${svgWidth - chartPaddingRight}" y2="${chartPaddingTop}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3" />
        <text x="${chartPaddingLeft - 10}" y="${chartPaddingTop + 4}" text-anchor="end" fill="#64748b" font-size="10">3K</text>

        <line x1="${chartPaddingLeft}" y1="${chartPaddingTop + availableHeight * 0.33}" x2="${svgWidth - chartPaddingRight}" y2="${chartPaddingTop + availableHeight * 0.33}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3" />
        <text x="${chartPaddingLeft - 10}" y="${chartPaddingTop + availableHeight * 0.33 + 4}" text-anchor="end" fill="#64748b" font-size="10">2K</text>

        <line x1="${chartPaddingLeft}" y1="${chartPaddingTop + availableHeight * 0.66}" x2="${svgWidth - chartPaddingRight}" y2="${chartPaddingTop + availableHeight * 0.66}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3" />
        <text x="${chartPaddingLeft - 10}" y="${chartPaddingTop + availableHeight * 0.66 + 4}" text-anchor="end" fill="#64748b" font-size="10">1K</text>

        <line x1="${chartPaddingLeft}" y1="${height - chartPaddingBottom}" x2="${svgWidth - chartPaddingRight}" y2="${height - chartPaddingBottom}" stroke="#94a3b8" stroke-width="1.5" />
        <text x="${chartPaddingLeft - 10}" y="${height - chartPaddingBottom + 4}" text-anchor="end" fill="#64748b" font-size="10">0K</text>
    `;

    computedBars.forEach((bar, i) => {
      const x = chartPaddingLeft + i * spacing + (spacing - barWidth) / 2;
      const yBottom = height - chartPaddingBottom - (bar.start / maxValue) * availableHeight;
      const yTop = height - chartPaddingBottom - (bar.end / maxValue) * availableHeight;
      const barHeight = Math.max(Math.abs(yBottom - yTop), 3);
      const actualY = Math.min(yTop, yBottom);

      // Connecting dotted line to next bar if applicable
      if (i < computedBars.length - 1) {
        const nextX = chartPaddingLeft + (i + 1) * spacing + (spacing - barWidth) / 2;
        const connectY = bar.isTotal ? actualY : (bar.value >= 0 ? actualY : yBottom);
        svgHtml += `
          <line x1="${x + barWidth}" y1="${connectY}" x2="${nextX}" y2="${connectY}" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="2,2" />
        `;
      }

      // Bar rect
      svgHtml += `
        <rect x="${x}" y="${actualY}" width="${barWidth}" height="${barHeight}" rx="3" fill="${bar.color}" opacity="0.95" class="transition-all duration-300 hover:opacity-100" />
      `;

      // Value label on top of bar
      svgHtml += `
        <text x="${x + barWidth / 2}" y="${actualY - 6}" text-anchor="middle" fill="#1e293b" font-size="11" font-weight="700">
          ${bar.displayValue}
        </text>
      `;

      // Category label under baseline
      svgHtml += `
        <text x="${x + barWidth / 2}" y="${height - chartPaddingBottom + 16}" text-anchor="middle" fill="#475569" font-size="10.5" font-weight="${bar.isTotal ? '700' : '500'}">
          ${bar.name}
        </text>
      `;
    });

    svgHtml += `</svg>`;
    container.innerHTML = svgHtml;
  },

  /**
   * Render 12-Week Sparklines (Executive Summary Bottom Strip)
   */
  renderSparklines(sparklinesData) {
    Object.keys(sparklinesData).forEach(key => {
      const canvas = document.getElementById(`sparkline-${key}`);
      if (!canvas) return;

      const dataObj = sparklinesData[key];
      const ctx = canvas.getContext("2d");
      const d = dataObj.data;

      const w = canvas.width = canvas.parentElement.clientWidth || 160;
      const h = canvas.height = 42;

      ctx.clearRect(0, 0, w, h);

      const min = Math.min(...d);
      const max = Math.max(...d);
      const range = max - min || 1;
      const padY = 6;
      const padX = 4;

      const points = d.map((val, idx) => {
        const x = padX + (idx / (d.length - 1)) * (w - 2 * padX);
        const y = h - padY - ((val - min) / range) * (h - 2 * padY);
        return { x, y };
      });

      // Gradient Fill
      const grad = ctx.createLinearGradient(0, 0, 0, h);
      if (dataObj.positive) {
        grad.addColorStop(0, "rgba(37, 99, 235, 0.25)");
        grad.addColorStop(1, "rgba(37, 99, 235, 0.0)");
      } else {
        grad.addColorStop(0, "rgba(239, 68, 68, 0.2)");
        grad.addColorStop(1, "rgba(239, 68, 68, 0.0)");
      }

      ctx.beginPath();
      ctx.moveTo(points[0].x, points[0].y);
      for (let i = 1; i < points.length; i++) {
        const xc = (points[i].x + points[i - 1].x) / 2;
        const yc = (points[i].y + points[i - 1].y) / 2;
        ctx.quadraticCurveTo(points[i - 1].x, points[i - 1].y, xc, yc);
      }
      ctx.lineTo(points[points.length - 1].x, points[points.length - 1].y);
      ctx.lineTo(points[points.length - 1].x, h);
      ctx.lineTo(points[0].x, h);
      ctx.closePath();
      ctx.fillStyle = grad;
      ctx.fill();

      // Stroke Line
      ctx.beginPath();
      ctx.moveTo(points[0].x, points[0].y);
      for (let i = 1; i < points.length; i++) {
        const xc = (points[i].x + points[i - 1].x) / 2;
        const yc = (points[i].y + points[i - 1].y) / 2;
        ctx.quadraticCurveTo(points[i - 1].x, points[i - 1].y, xc, yc);
      }
      ctx.lineTo(points[points.length - 1].x, points[points.length - 1].y);
      ctx.strokeStyle = dataObj.positive ? "#1d4ed8" : "#dc2626";
      ctx.lineWidth = 1.8;
      ctx.stroke();

      // End point dot
      const lastPoint = points[points.length - 1];
      ctx.beginPath();
      ctx.arc(lastPoint.x, lastPoint.y, 3, 0, Math.PI * 2);
      ctx.fillStyle = dataObj.positive ? "#1d4ed8" : "#dc2626";
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 1.5;
      ctx.stroke();
    });
  },

  /**
   * Render Capacity Funnel Component (Capacity Sheet 2)
   */
  renderCapacityFunnel(containerId, funnelSteps) {
    const container = document.getElementById(containerId);
    if (!container) return;

    let html = `<div class="funnel-container flex flex-col justify-between h-full py-1">`;

    // Max hours reference is Gross Hours
    const grossStep = funnelSteps.find(s => s.label === "Gross Hours") || funnelSteps[0];
    const maxVal = grossStep.hours || 101500;

    funnelSteps.forEach((step, idx) => {
      let widthPct = 100;
      let bgStyle = "";
      let label = step.label;
      let valText = step.formatted;

      if (step.label === "Gross Hours") {
        widthPct = 100;
        bgStyle = "background: linear-gradient(90deg, #1e3a8a 0%, #2563eb 100%); color: #ffffff;";
      } else if (step.label === "Available Hours") {
        widthPct = Math.round((step.hours / maxVal) * 100);
        bgStyle = "background: linear-gradient(90deg, #0284c7 0%, #0ea5e9 100%); color: #ffffff;";
      } else if (step.label === "Productive Hours") {
        widthPct = Math.round((step.hours / maxVal) * 100);
        bgStyle = "background: linear-gradient(90deg, #0d9488 0%, #14b8a6 100%); color: #ffffff;";
      } else {
        // Deduction tiers
        const decPct = 95 - (idx * 5.5);
        widthPct = Math.max(decPct, 60);
        bgStyle = "background: #38bdf8; color: #0f172a;";
      }

      html += `
        <div class="funnel-tier flex items-center justify-center my-0.5 mx-auto transition-all duration-300"
             style="width: ${widthPct}%; min-height: 24px; border-radius: 4px; ${bgStyle} box-shadow: 0 1px 2px rgba(0,0,0,0.06);">
          <div class="flex justify-between items-center w-full px-3 text-xs font-semibold">
            <span>${label}</span>
            <span>${valText}</span>
          </div>
        </div>
      `;
    });

    html += `</div>`;
    container.innerHTML = html;
  },

  /**
   * Render Downtime Category Donut & Table (Capacity Sheet 2)
   */
  renderDowntimeChart(chartId, tableId, categories, totalHours) {
    const ctx = document.getElementById(chartId);
    const tableContainer = document.getElementById(tableId);
    if (!ctx) return;

    if (this.instances.downtimeDonut) {
      this.instances.downtimeDonut.destroy();
    }

    const labels = categories.map(c => c.name);
    const dataVals = categories.map(c => c.hours);
    const bgColors = categories.map(c => c.color);

    this.instances.downtimeDonut = new Chart(ctx, {
      type: "doughnut",
      data: {
        labels: labels,
        datasets: [{
          data: dataVals,
          backgroundColor: bgColors,
          borderWidth: 2,
          borderColor: "#ffffff",
          hoverOffset: 4
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: "68%",
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: function(context) {
                const cat = categories[context.dataIndex];
                return ` ${cat.name}: ${cat.hours.toLocaleString()} hrs (${cat.percent}%)`;
              }
            }
          }
        }
      }
    });

    // Populate the side table
    if (tableContainer) {
      let tableHtml = `
        <table class="w-full text-xs">
          <thead>
            <tr class="text-slate-500 border-b border-slate-200">
              <th class="text-left font-semibold pb-1">Category</th>
              <th class="text-right font-semibold pb-1">Hours</th>
              <th class="text-right font-semibold pb-1">% Downtime</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 font-medium">
      `;

      categories.forEach(cat => {
        tableHtml += `
          <tr class="hover:bg-slate-50">
            <td class="py-1 flex items-center gap-1.5">
              <span class="inline-block w-2.5 h-2.5 rounded-full" style="background-color: ${cat.color}"></span>
              <span class="text-slate-700">${cat.name}</span>
            </td>
            <td class="text-right text-slate-800">${cat.hours.toLocaleString()}</td>
            <td class="text-right text-slate-600">${cat.percent}%</td>
          </tr>
        `;
      });

      tableHtml += `
          <tr class="border-t-2 border-slate-300 font-bold text-slate-900 bg-slate-50">
            <td class="py-1.5">Total</td>
            <td class="text-right">${totalHours.toLocaleString()}</td>
            <td class="text-right">100%</td>
          </tr>
        </tbody>
      </table>
      `;
      tableContainer.innerHTML = tableHtml;
    }
  },

  /**
   * Render Capacity Risk Heatmap (Capacity Sheet 2)
   */
  renderHeatmap(containerId, heatmapData, selectedRegionId = "all") {
    const container = document.getElementById(containerId);
    if (!container) return;

    let html = `
      <div class="overflow-x-auto">
        <table class="w-full text-xs text-center border-collapse">
          <thead>
            <tr>
              <th class="text-left py-1 px-2 font-semibold text-slate-600 w-24">Region</th>
              ${heatmapData.weeks.map(w => `<th class="py-1 px-1 font-semibold text-slate-600">${w}</th>`).join('')}
            </tr>
          </thead>
          <tbody>
    `;

    heatmapData.regions.forEach(reg => {
      const isSelected = selectedRegionId !== "all" && reg.name.toLowerCase().includes(selectedRegionId.toLowerCase());
      const rowHighlight = isSelected ? "ring-2 ring-blue-500 font-bold" : "";

      html += `<tr class="border-b border-slate-100 ${rowHighlight}">`;
      html += `<td class="text-left py-1.5 px-2 font-semibold text-slate-800">${reg.name}</td>`;

      reg.values.forEach(val => {
        // Color mapping from -20% (green) to 0% (yellow) to +20% (red)
        let cellBg = "#ffffff";
        let textColor = "#0f172a";

        if (val <= -15) {
          cellBg = "#22c55e"; // bright green
          textColor = "#ffffff";
        } else if (val <= -5) {
          cellBg = "#86efac"; // light green
          textColor = "#064e3b";
        } else if (val < 5) {
          cellBg = "#fde047"; // yellow
          textColor = "#713f12";
        } else if (val < 15) {
          cellBg = "#fb923c"; // orange
          textColor = "#ffffff";
        } else {
          cellBg = "#ef4444"; // red
          textColor = "#ffffff";
        }

        const sign = val > 0 ? `+${val}%` : `${val}%`;
        html += `
          <td class="p-1">
            <div class="py-1 px-1.5 rounded text-xs font-semibold transition-transform hover:scale-105"
                 style="background-color: ${cellBg}; color: ${textColor};" title="${reg.name}: ${sign} variance">
              ${sign}
            </div>
          </td>
        `;
      });

      html += `</tr>`;
    });

    html += `
          </tbody>
        </table>
        <!-- Heatmap Color Scale Legend -->
        <div class="flex items-center justify-between text-[11px] text-slate-500 mt-2 px-1">
          <div class="flex items-center gap-1">
            <span class="w-3 h-3 rounded" style="background-color: #22c55e;"></span>
            <span>-20% (Surplus)</span>
          </div>
          <div class="flex items-center gap-1">
            <span class="w-3 h-3 rounded" style="background-color: #fde047;"></span>
            <span>0% (Balanced)</span>
          </div>
          <div class="flex items-center gap-1">
            <span class="w-3 h-3 rounded" style="background-color: #fb923c;"></span>
            <span>+10%</span>
          </div>
          <div class="flex items-center gap-1">
            <span class="w-3 h-3 rounded" style="background-color: #ef4444;"></span>
            <span>+20% (Deficit Risk)</span>
          </div>
        </div>
      </div>
    `;

    container.innerHTML = html;
  },

  /**
   * Render Region Efficiency Matrix Scatter Plot (Capacity Sheet 2)
   */
  renderEfficiencyMatrix(containerId, matrixData, selectedRegionId = "all") {
    const ctx = document.getElementById(containerId);
    if (!ctx) return;

    if (this.instances.efficiencyMatrix) {
      this.instances.efficiencyMatrix.destroy();
    }

    const datasets = matrixData.map(reg => {
      const isSelected = selectedRegionId !== "all" && reg.name.toLowerCase().includes(selectedRegionId.toLowerCase());
      return {
        label: reg.name,
        data: [{ x: reg.x, y: reg.y, r: isSelected ? 12 : 9 }],
        backgroundColor: reg.color,
        borderColor: isSelected ? "#0f172a" : "#ffffff",
        borderWidth: isSelected ? 3 : 1.5,
        hoverRadius: 13
      };
    });

    this.instances.efficiencyMatrix = new Chart(ctx, {
      type: "bubble",
      data: { datasets: datasets },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: "right",
            labels: {
              boxWidth: 10,
              usePointStyle: true,
              font: { size: 10, weight: "600" }
            }
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                return ` ${context.dataset.label}: Prod ${context.raw.x}, Avail ${context.raw.y}%`;
              }
            }
          }
        },
        scales: {
          x: {
            min: 2.5,
            max: 6.5,
            title: {
              display: true,
              text: "Productivity (Installs per Head)",
              font: { size: 11, weight: "600" },
              color: "#475569"
            },
            grid: {
              color: function(context) {
                if (context.tick.value === 4.5) return "#94a3b8"; // Quadrant divider
                return "#f1f5f9";
              },
              lineWidth: function(context) {
                return context.tick.value === 4.5 ? 1.5 : 1;
              }
            }
          },
          y: {
            min: 50,
            max: 85,
            title: {
              display: true,
              text: "Availability %",
              font: { size: 11, weight: "600" },
              color: "#475569"
            },
            ticks: {
              callback: value => value + "%"
            },
            grid: {
              color: function(context) {
                if (context.tick.value === 70) return "#94a3b8"; // Quadrant divider
                return "#f1f5f9";
              },
              lineWidth: function(context) {
                return context.tick.value === 70 ? 1.5 : 1;
              }
            }
          }
        }
      }
    });
  },

  /**
   * Render Sheet 4: ES Weekly Actual vs Forecast Line Chart
   */
  renderWeeklyActualVsForecast(containerId, seriesData, metricKey = "grossHrs") {
    const ctx = document.getElementById(containerId);
    if (!ctx) return;

    if (this.instances.weeklyForecast) {
      this.instances.weeklyForecast.destroy();
    }

    const metric = seriesData.metrics[metricKey] || seriesData.metrics.grossHrs;
    const labels = seriesData.weeks;

    this.instances.weeklyForecast = new Chart(ctx, {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Forecast's",
            data: metric.forecast,
            borderColor: "#2563eb",
            backgroundColor: "#2563eb",
            pointBackgroundColor: "#2563eb",
            pointRadius: 4,
            pointHoverRadius: 6,
            borderWidth: 2.2,
            fill: false,
            tension: 0.15
          },
          {
            label: "Actual's",
            data: metric.actuals,
            borderColor: "#16a34a",
            backgroundColor: "#16a34a",
            pointBackgroundColor: "#16a34a",
            pointRadius: 5,
            pointHoverRadius: 7,
            borderWidth: 2.5,
            fill: false,
            tension: 0.15
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: "top",
            align: "end",
            labels: {
              usePointStyle: true,
              font: { family: "Inter, sans-serif", size: 11, weight: "600" },
              color: "#334155"
            }
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                const val = context.raw;
                if (val === null || val === undefined) return null;
                return ` ${context.dataset.label}: ${val.toLocaleString()} ${metric.unit}`;
              }
            }
          }
        },
        scales: {
          x: {
            grid: { color: "#f8fafc" },
            ticks: { font: { size: 10.5 }, color: "#64748b" }
          },
          y: {
            grid: { color: "#e2e8f0" },
            ticks: {
              font: { size: 10.5 },
              color: "#64748b",
              callback: function(val) {
                if (metric.unit === "%") return val + "%";
                if (val >= 1000) return (val / 1000) + "K";
                return val;
              }
            }
          }
        }
      }
    });
  }
};
