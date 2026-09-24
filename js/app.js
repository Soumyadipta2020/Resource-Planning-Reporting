/**
 * Application Controller & State Engine
 * Synchronizes global filters, renders views, and ensures data consistency across all tabs.
 */

const App = {
  state: {
    activeTab: "executive-summary", // Default is Executive Summary
    capacitySheet: "sheet-2", // "sheet-2" (Dashboard), "sheet-3" (Comparison), "sheet-4" (Detailed Matrix)
    selectedGeography: "all",
    selectedWeek: "wk23",
    selectedPlan: "gff1_2026",
    selectedBusinessUnit: "all",
    sheet4ChartMetric: "grossHrs",
    lastRefreshed: new Date()
  },

  init() {
    this.populateFilterDropdowns();
    this.bindEvents();
    this.switchTab(this.state.activeTab);
    this.updateAllViews();
    this.renderLastRefreshed();
  },

  /**
   * Populate filter dropdown controls dynamically
   */
  populateFilterDropdowns() {
    // Populate Geography selects across header and sheet 4
    const geoSelects = document.querySelectorAll(".geo-selector");
    geoSelects.forEach(select => {
      select.innerHTML = DASHBOARD_DATA.metadata.geographies.map(g =>
        `<option value="${g.id}" ${g.id === this.state.selectedGeography ? "selected" : ""}>${g.name}</option>`
      ).join("");
    });

    // Populate Reporting Week selects
    const weekSelects = document.querySelectorAll(".week-selector");
    weekSelects.forEach(select => {
      select.innerHTML = DASHBOARD_DATA.metadata.reportingWeeks.map(w =>
        `<option value="${w.id}" ${w.id === this.state.selectedWeek ? "selected" : ""}>${w.label}</option>`
      ).join("");
    });

    // Populate Plan selects
    const planSelects = document.querySelectorAll(".plan-selector");
    planSelects.forEach(select => {
      select.innerHTML = DASHBOARD_DATA.metadata.plans.map(p =>
        `<option value="${p.id}" ${p.id === this.state.selectedPlan ? "selected" : ""}>${p.name}</option>`
      ).join("");
    });
  },

  /**
   * Bind event listeners
   */
  bindEvents() {
    // Main sidebar tab navigation
    document.querySelectorAll(".nav-item").forEach(item => {
      item.addEventListener("click", (e) => {
        e.preventDefault();
        const tabId = item.getAttribute("data-tab");
        if (tabId) {
          this.switchTab(tabId);
        }
      });
    });

    // Capacity Overview Sheet sub-navigation buttons
    document.querySelectorAll(".sheet-toggle-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const sheetId = btn.getAttribute("data-sheet");
        if (sheetId) {
          this.switchCapacitySheet(sheetId);
        }
      });
    });

    // Sheet 4 Business Unit filter buttons (HEC, KAC, NZ EV, Home)
    document.querySelectorAll(".bu-toggle-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const buId = btn.getAttribute("data-bu");
        if (buId) {
          this.switchBusinessUnit(buId);
        }
      });
    });

    // Sheet 4 Chart Metric selector dropdown
    const metricSelect = document.getElementById("sheet4-metric-select");
    if (metricSelect) {
      metricSelect.addEventListener("change", (e) => {
        this.state.sheet4ChartMetric = e.target.value;
        this.renderSheet4Chart();
      });
    }

    // Global Filter change handlers (Geography, Week, Plan)
    document.querySelectorAll(".geo-selector").forEach(el => {
      el.addEventListener("change", (e) => {
        this.state.selectedGeography = e.target.value;
        this.syncDropdownValues(".geo-selector", e.target.value);
        this.updateAllViews();
      });
    });

    document.querySelectorAll(".week-selector").forEach(el => {
      el.addEventListener("change", (e) => {
        this.state.selectedWeek = e.target.value;
        this.syncDropdownValues(".week-selector", e.target.value);
        this.updateAllViews();
      });
    });

    document.querySelectorAll(".plan-selector").forEach(el => {
      el.addEventListener("change", (e) => {
        this.state.selectedPlan = e.target.value;
        this.syncDropdownValues(".plan-selector", e.target.value);
        this.updateAllViews();
      });
    });

    // Refresh Data button
    const refreshBtn = document.getElementById("btn-refresh-data");
    if (refreshBtn) {
      refreshBtn.addEventListener("click", () => {
        this.triggerDataRefresh();
      });
    }

    // Export CSV / Print
    const exportBtn = document.getElementById("btn-export-data");
    if (exportBtn) {
      exportBtn.addEventListener("click", () => {
        this.exportCurrentView();
      });
    }
  },

  syncDropdownValues(selector, value) {
    document.querySelectorAll(selector).forEach(sel => {
      sel.value = value;
    });
  },

  /**
   * Switch Active Main Tab
   */
  switchTab(tabId) {
    this.state.activeTab = tabId;

    // Update sidebar UI: strictly ensure ONLY the active tab has .active class
    document.querySelectorAll(".nav-item").forEach(item => {
      const isCurrent = item.getAttribute("data-tab") === tabId;
      if (isCurrent) {
        item.classList.add("active");
        item.classList.add("text-white");
        item.classList.remove("text-slate-400");
      } else {
        item.classList.remove("active");
        item.classList.remove("text-white");
        item.classList.add("text-slate-400");
      }
    });

    // Update top header title
    const titleEl = document.getElementById("top-view-title");
    if (tabId === "executive-summary") {
      if (titleEl) titleEl.textContent = "Executive Command Centre";
    } else if (tabId === "capacity-overview") {
      if (titleEl) titleEl.textContent = "Capacity Overview";
    } else if (tabId === "demand") {
      if (titleEl) titleEl.textContent = "Demand & Capacity Dispatch";
    } else if (tabId === "geographic-hub") {
      if (titleEl) titleEl.textContent = "Geographic Performance HUB";
    } else if (tabId === "accuracy-dashboard") {
      if (titleEl) titleEl.textContent = "Accuracy Dashboard";
    } else if (tabId === "forecast-leadlag") {
      if (titleEl) titleEl.textContent = "Forecast Performance (Lead/Lag)";
    }

    // Show/hide capacity views sub-navigation bar (ONLY for capacity overview tab!)
    const capTabs = document.getElementById("capacity-nav-tabs");
    if (capTabs) {
      if (tabId === "capacity-overview") {
        capTabs.style.setProperty("display", "flex", "important");
        capTabs.classList.remove("hidden");
      } else {
        capTabs.style.setProperty("display", "none", "important");
        capTabs.classList.add("hidden");
      }
    }

    // Update visible view container
    document.querySelectorAll(".tab-view-container").forEach(view => {
      if (view.id === `view-${tabId}`) {
        view.classList.remove("hidden");
      } else {
        view.classList.add("hidden");
      }
    });

    // Trigger chart resize/render for active view
    setTimeout(() => {
      this.updateAllViews();
    }, 50);
  },

  /**
   * Switch Capacity Overview View (Operational Dashboard, Comparison, or Matrix)
   */
  switchCapacitySheet(sheetId) {
    this.state.capacitySheet = sheetId;

    document.querySelectorAll(".sheet-toggle-btn").forEach(btn => {
      if (btn.getAttribute("data-sheet") === sheetId) {
        btn.classList.add("bg-blue-700", "text-white", "shadow-sm");
        btn.classList.remove("bg-slate-100", "text-slate-700", "hover:bg-slate-200");
      } else {
        btn.classList.remove("bg-blue-700", "text-white", "shadow-sm");
        btn.classList.add("bg-slate-100", "text-slate-700", "hover:bg-slate-200");
      }
    });

    document.querySelectorAll(".capacity-sheet-content").forEach(content => {
      if (content.id === `capacity-${sheetId}`) {
        content.classList.remove("hidden");
      } else {
        content.classList.add("hidden");
      }
    });

    setTimeout(() => {
      this.updateCapacitySheet();
    }, 50);
  },

  /**
   * Switch Business Unit for Sheet 4
   */
  switchBusinessUnit(buId) {
    this.state.selectedBusinessUnit = buId;

    document.querySelectorAll(".bu-toggle-btn").forEach(btn => {
      if (btn.getAttribute("data-bu") === buId) {
        btn.classList.add("bg-emerald-600", "text-white", "border-emerald-600");
        btn.classList.remove("bg-white", "text-emerald-700", "border-emerald-500", "hover:bg-emerald-50");
      } else {
        btn.classList.remove("bg-emerald-600", "text-white", "border-emerald-600");
        btn.classList.add("bg-white", "text-emerald-700", "border-emerald-500", "hover:bg-emerald-50");
      }
    });

    this.renderSheet4Table();
    this.renderSheet4Chart();
  },

  /**
   * Master Update: Recalculates and updates everything based on current state & filters
   */
  updateAllViews() {
    this.renderExecutiveSummary();
    this.updateCapacitySheet();
    this.renderComplementaryViews();
  },

  /**
   * Render Executive Summary (Image 4)
   */
  renderExecutiveSummary() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const regional = isRegional ? DASHBOARD_DATA.regionalData[geo] : null;

    // KPI Values
    const kpiData = isRegional ? {
      installs: { ...regional.kpis.installs },
      sales: { ...regional.kpis.sales, unit: "£M" },
      leads: { ...regional.kpis.leads },
      activeHeads: { ...regional.kpis.activeHeads },
      availableHours: { ...regional.kpis.availableHours },
      productivity: { ...regional.kpis.productivity, unit: "per Head" }
    } : DASHBOARD_DATA.executiveSummary.kpis;

    this.renderKpiCard("exec-kpi-installs", kpiData.installs.formatted, kpiData.installs.wow, kpiData.installs.vsPlan);
    this.renderKpiCard("exec-kpi-sales", kpiData.sales.formatted, kpiData.sales.wow, kpiData.sales.vsPlan);
    this.renderKpiCard("exec-kpi-leads", kpiData.leads.formatted, kpiData.leads.wow, kpiData.leads.vsPlan);
    this.renderKpiCard("exec-kpi-heads", kpiData.activeHeads.formatted, kpiData.activeHeads.wow, kpiData.activeHeads.vsPlan);
    this.renderKpiCard("exec-kpi-availhrs", kpiData.availableHours.formatted, kpiData.availableHours.wow, kpiData.availableHours.vsPlan);
    this.renderKpiCard("exec-kpi-productivity", kpiData.productivity.formatted, kpiData.productivity.wow, kpiData.productivity.vsPlan);

    // Installs Weekly Combo Chart
    let weeklyData = [...DASHBOARD_DATA.executiveSummary.weeklyInstalls];
    if (isRegional) {
      weeklyData = weeklyData.map(d => ({
        week: d.week,
        actual: Math.round(d.actual * regional.multiplier),
        plan: Math.round(d.plan * regional.multiplier),
        variance: Math.round(d.variance * regional.multiplier)
      }));
    }
    ChartManager.renderWeeklyInstallsChart("chart-weekly-installs", weeklyData);

    // Waterfall Chart Drivers
    let drivers = [...DASHBOARD_DATA.executiveSummary.waterfallDrivers];
    if (isRegional) {
      drivers = drivers.map(d => ({
        ...d,
        value: Math.round(d.value * regional.multiplier)
      }));
    }
    ChartManager.renderWaterfallChart("waterfall-chart-container", drivers);

    // Sparklines
    ChartManager.renderSparklines(DASHBOARD_DATA.executiveSummary.sparklines);
  },

  /**
   * Helper to format KPI cards with WoW and vs Plan pills
   */
  renderKpiCard(elementId, valueText, wowPct, vsPlanPct) {
    const el = document.getElementById(elementId);
    if (!el) return;

    const valEl = el.querySelector(".kpi-value");
    const wowEl = el.querySelector(".kpi-wow");
    const planEl = el.querySelector(".kpi-plan");

    if (valEl) valEl.textContent = valueText;

    if (wowEl) {
      const isUp = wowPct >= 0;
      wowEl.innerHTML = `
        <span class="${isUp ? 'text-emerald-700' : 'text-red-700'} font-semibold flex items-center">
          ${isUp ? '↑' : '↓'} ${Math.abs(wowPct)}% WoW
        </span>
      `;
    }

    if (planEl) {
      const isUp = vsPlanPct >= 0;
      planEl.innerHTML = `
        <span class="${isUp ? 'text-emerald-700' : 'text-red-700'} font-semibold flex items-center">
          ${isUp ? '↑' : '↓'} ${Math.abs(vsPlanPct)}% vs Plan
        </span>
      `;
    }
  },

  /**
   * Update the active sheet within Capacity Overview
   */
  updateCapacitySheet() {
    if (this.state.capacitySheet === "sheet-2") {
      this.renderCapacitySheet2();
    } else if (this.state.capacitySheet === "sheet-3") {
      this.renderCapacitySheet3();
    } else if (this.state.capacitySheet === "sheet-4") {
      this.renderCapacitySheet4();
    }
  },

  /**
   * Render Capacity Overview - Sheet 2 (Image 3)
   */
  renderCapacitySheet2() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const regional = isRegional ? DASHBOARD_DATA.regionalData[geo] : null;

    // Top KPIs
    const kpis = isRegional ? {
      availableHours: { ...regional.kpis.availableHours },
      totalDowntime: { ...regional.kpis.totalDowntime },
      capacityUtilisation: { ...regional.kpis.capacityUtilisation },
      workforceAvailability: { ...regional.kpis.workforceAvailability },
      productivity: { ...regional.kpis.productivity },
      sicknessPercent: { ...regional.kpis.sicknessPercent }
    } : DASHBOARD_DATA.capacitySheet2.kpis;

    this.renderKpiCard("cap2-kpi-availhrs", kpis.availableHours.formatted, kpis.availableHours.wow, kpis.availableHours.vsPlan);
    this.renderKpiCard("cap2-kpi-downtime", kpis.totalDowntime.formatted, kpis.totalDowntime.wow, kpis.totalDowntime.vsPlan);
    this.renderKpiCard("cap2-kpi-utilisation", kpis.capacityUtilisation.formatted, kpis.capacityUtilisation.wow, kpis.capacityUtilisation.vsPlan);
    this.renderKpiCard("cap2-kpi-workforce", kpis.workforceAvailability.formatted, kpis.workforceAvailability.wow, kpis.workforceAvailability.vsPlan);
    this.renderKpiCard("cap2-kpi-productivity", kpis.productivity.formatted, kpis.productivity.wow, kpis.productivity.vsPlan);
    this.renderKpiCard("cap2-kpi-sickness", kpis.sicknessPercent.formatted, kpis.sicknessPercent.wow, kpis.sicknessPercent.vsPlan);

    // Funnel
    const funnelSteps = isRegional ? regional.funnel : DASHBOARD_DATA.capacitySheet2.funnel;
    ChartManager.renderCapacityFunnel("capacity-funnel-container", funnelSteps);

    // Downtime Categories Donut & Table
    const categories = isRegional ? regional.downtimeCategories : DASHBOARD_DATA.capacitySheet2.downtimeCategories;
    const totalDowntimeHrs = isRegional ? regional.kpis.totalDowntime.value : DASHBOARD_DATA.capacitySheet2.totalDowntimeHours;
    ChartManager.renderDowntimeChart("downtime-donut-chart", "downtime-table-container", categories, totalDowntimeHrs);

    // Capacity Risk Heatmap
    ChartManager.renderHeatmap("heatmap-container", DASHBOARD_DATA.capacitySheet2.heatmap, geo);

    // Region Efficiency Matrix
    ChartManager.renderEfficiencyMatrix("efficiency-matrix-chart", DASHBOARD_DATA.capacitySheet2.efficiencyMatrix, geo);

    // Bottom KPIs
    const bottom = DASHBOARD_DATA.capacitySheet2.bottomKpis;
    document.getElementById("bottom-downtime-val").textContent = isRegional ? (33.0 + (regional.multiplier * 2)).toFixed(1) + "%" : bottom.totalDowntimePct.formatted;
    document.getElementById("bottom-utilisation-val").textContent = isRegional ? kpis.capacityUtilisation.formatted : bottom.capacityUtilisation.formatted;
    document.getElementById("bottom-availability-val").textContent = isRegional ? kpis.workforceAvailability.formatted : bottom.workforceAvailability.formatted;
    document.getElementById("bottom-sickness-val").textContent = isRegional ? kpis.sicknessPercent.formatted : bottom.sicknessPercent.formatted;
  },

  /**
   * Render Capacity Overview - Sheet 3 (Comparison Matrix - Image 2)
   */
  renderCapacitySheet3() {
    const tableBody = document.getElementById("capacity-comparison-tbody");
    if (!tableBody) return;

    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const mult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;

    const rows = DASHBOARD_DATA.capacitySheet3.rows;
    let html = "";

    rows.forEach(r => {
      let thisWeekAct = r.thisWeekActual;
      let thisWeekPlan = r.thisWeekPlan;
      let vsPlan = r.vsPlan;
      let lastWeekAct = r.lastWeekActual;
      let vsLW = r.vsLW;
      let varPlanAbs = r.varPlanAbs;
      let varPlanPct = r.varPlanPct;
      let varLWAbs = r.varLWAbs;
      let varLWPct = r.varLWPct;

      // Adjust for regional multiplier if numbers are scaled
      if (isRegional && !r.metric.includes("%")) {
        if (r.thisWeekActual.includes("K")) {
          const raw = parseFloat(r.thisWeekActual) * 1000 * mult;
          thisWeekAct = (raw / 1000).toFixed(1) + "K";
          const rawPlan = parseFloat(r.thisWeekPlan) * 1000 * mult;
          thisWeekPlan = (rawPlan / 1000).toFixed(1) + "K";
          vsPlan = ((raw - rawPlan) / 1000).toFixed(1) + "K";
          const rawLW = parseFloat(r.lastWeekActual) * 1000 * mult;
          lastWeekAct = (rawLW / 1000).toFixed(1) + "K";
          vsLW = ((raw - rawLW) / 1000).toFixed(1) + "K";
          varPlanAbs = vsPlan;
          varLWAbs = vsLW;
        } else if (!r.metric.includes("Productivity")) {
          const raw = parseInt(r.thisWeekActual.replace(/,/g, "")) * mult;
          thisWeekAct = Math.round(raw).toLocaleString();
          const rawPlan = parseInt(r.thisWeekPlan.replace(/,/g, "")) * mult;
          thisWeekPlan = Math.round(rawPlan).toLocaleString();
          vsPlan = Math.round(raw - rawPlan).toLocaleString();
          const rawLW = parseInt(r.lastWeekActual.replace(/,/g, "")) * mult;
          lastWeekAct = Math.round(rawLW).toLocaleString();
          vsLW = Math.round(raw - rawLW).toLocaleString();
          varPlanAbs = vsPlan;
          varLWAbs = vsLW;
        }
      }

      const isVsPlanDown = vsPlan.includes("-");
      const isVsLWDown = vsLW.includes("-");

      html += `
        <tr class="hover:bg-slate-50/80 transition-colors border-b border-slate-200">
          <td class="py-3 px-4 font-bold text-slate-900">${r.metric}</td>
          <td class="py-3 px-3 text-right font-semibold text-slate-800">${thisWeekAct}</td>
          <td class="py-3 px-3 text-right text-slate-700">${thisWeekPlan}</td>
          <td class="py-3 px-3 text-right font-medium ${isVsPlanDown ? 'text-red-600' : 'text-emerald-600'}">
            ${isVsPlanDown ? '↓' : '↑'} ${vsPlan}
          </td>
          <td class="py-3 px-3 text-right text-slate-800">${lastWeekAct}</td>
          <td class="py-3 px-3 text-right font-medium ${isVsLWDown ? 'text-red-600' : 'text-emerald-600'}">
            ${isVsLWDown ? '↓' : '↑'} ${vsLW}
          </td>
          <td class="py-3 px-3 text-right font-semibold ${isVsPlanDown ? 'text-red-600' : 'text-emerald-600'}">
            ${isVsPlanDown ? '↓' : '↑'} ${varPlanAbs}
          </td>
          <td class="py-3 px-3 text-right text-slate-600 font-medium">${varPlanPct}</td>
          <td class="py-3 px-3 text-right font-semibold ${isVsLWDown ? 'text-red-600' : 'text-emerald-600'}">
            ${isVsLWDown ? '↓' : '↑'} ${varLWAbs}
          </td>
          <td class="py-3 px-3 text-right text-slate-600 font-medium">${varLWPct}</td>
        </tr>
      `;
    });

    tableBody.innerHTML = html;
  },

  /**
   * Render Capacity Overview - Sheet 4 (Detailed Matrix & Chart - Image 1)
   */
  renderCapacitySheet4() {
    this.renderSheet4Chart();
    this.renderSheet4Table();
  },

  renderSheet4Chart() {
    const rawSeries = DASHBOARD_DATA.capacitySheet4.weeklySeries;
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;

    let buMult = 1.0;
    if (this.state.selectedBusinessUnit === "hec") buMult = 0.58;
    else if (this.state.selectedBusinessUnit === "kac") buMult = 0.28;
    else if (this.state.selectedBusinessUnit === "nzev") buMult = 0.14;

    const totalMult = geoMult * buMult;

    // Create scaled series
    const series = {
      weeks: rawSeries.weeks,
      reportingIndex: rawSeries.reportingIndex,
      metrics: {}
    };

    Object.keys(rawSeries.metrics).forEach(key => {
      const metric = rawSeries.metrics[key];
      const isPercentOrRatio = metric.unit === "%" || key === "productivity";
      const scale = isPercentOrRatio ? 1.0 : totalMult;

      series.metrics[key] = {
        label: metric.label,
        unit: metric.unit,
        actuals: metric.actuals.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * scale))),
        forecast: metric.forecast.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * scale)))
      };
    });

    ChartManager.renderWeeklyActualVsForecast("sheet4-actual-forecast-chart", series, this.state.sheet4ChartMetric);
  },

  renderSheet4Table() {
    const tableContainer = document.getElementById("sheet4-matrix-table-container");
    if (!tableContainer) return;

    const data = DASHBOARD_DATA.capacitySheet4;
    const bu = this.state.selectedBusinessUnit;
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;

    let buMult = 1.0;
    if (bu === "hec") buMult = 0.58;
    else if (bu === "kac") buMult = 0.28;
    else if (bu === "nzev") buMult = 0.14;

    const mult = geoMult * buMult;
    const isScaled = mult !== 1.0;

    const selectedWeekObj = DASHBOARD_DATA.metadata.reportingWeeks.find(w => w.id === this.state.selectedWeek) || { date: "22 Jun 2026" };
    const currentWeekLabel = selectedWeekObj.date;

    let html = `
      <div class="overflow-x-auto shadow-sm rounded border border-slate-200">
        <table class="w-full text-xs border-collapse">
          <thead>
            <!-- Top Header Category Row -->
            <tr class="text-white text-center font-bold">
              <th class="py-2 px-3 text-left bg-slate-600 sticky left-0 z-20 w-44">Metric</th>
              <th colspan="5" class="py-2 px-2 bg-slate-500 border-l border-r border-slate-400">Actuals</th>
              <th class="py-2 px-2 bg-cyan-700 border-r border-cyan-600">Forecast</th>
              <th class="py-2 px-2 bg-cyan-700 border-r border-cyan-600">Actual</th>
              <th class="py-2 px-2 bg-cyan-700 border-r border-cyan-600">Variance</th>
              <th colspan="5" class="py-2 px-2 bg-slate-500 border-l border-slate-400">Forecast - GFF1 2026</th>
            </tr>
            <!-- Sub-Header Date Row -->
            <tr class="bg-slate-100 text-slate-700 text-center font-semibold border-b border-slate-300">
              <th class="py-1 px-3 text-left sticky left-0 bg-slate-100 z-20"></th>
              ${data.tableColumns.actualsHeaders.map(h => `<th class="py-1 px-2">${h}</th>`).join('')}
              <th class="py-1 px-2 bg-cyan-50 text-cyan-900 border-l border-cyan-200">${currentWeekLabel}</th>
              <th class="py-1 px-2 bg-cyan-50 text-cyan-900">${currentWeekLabel}</th>
              <th class="py-1 px-2 bg-cyan-50 text-cyan-900 border-r border-cyan-200">${currentWeekLabel}</th>
              ${data.tableColumns.forecastHeaders.map(h => `<th class="py-1 px-2">${h}</th>`).join('')}
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200">
    `;

    data.tableRows.forEach((row, idx) => {
      const isAlt = idx % 2 === 1 ? "bg-slate-50/60" : "bg-white";
      const isBold = ["FTE", "Gross Hrs", "Total Downtime", "Available Hrs", "Productive Hours", "Utilisation"].includes(row.metric);
      const textWeight = isBold ? "font-bold text-slate-900" : "text-slate-700 font-medium";

      html += `<tr class="${isAlt} hover:bg-blue-50/50 transition-colors">`;
      // Sticky Metric column
      html += `<td class="py-1.5 px-3 text-left sticky left-0 ${isAlt} z-10 ${textWeight} border-r border-slate-200 shadow-[1px_0_0_rgba(0,0,0,0.05)]">${row.metric}</td>`;

      // 5 Actuals Columns
      row.actuals.forEach(val => {
        let displayVal = val;
        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * mult;
          displayVal = Math.round(num).toLocaleString();
        }
        html += `<td class="py-1.5 px-2 text-right ${textWeight}">${displayVal}</td>`;
      });

      // Current Week: Forecast, Actual, Variance
      let curForecast = row.currentForecast;
      let curActual = row.currentActual;
      let variance = row.variance;
      if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
        const numFc = parseInt(curForecast.replace(/,/g, "")) * mult;
        const numAct = parseInt(curActual.replace(/,/g, "")) * mult;
        curForecast = Math.round(numFc).toLocaleString();
        curActual = Math.round(numAct).toLocaleString();
        const diff = Math.round(numAct - numFc);
        variance = diff.toLocaleString();
      }

      html += `<td class="py-1.5 px-2 text-right bg-cyan-50/40 text-slate-800 ${textWeight}">${curForecast}</td>`;
      html += `<td class="py-1.5 px-2 text-right bg-cyan-50/40 text-slate-900 ${textWeight}">${curActual}</td>`;

      // Variance arrow and color
      const isUp = row.varDir === "up";
      const isPositive = row.varType === "positive";
      const varColor = isPositive ? "text-emerald-700 font-semibold" : "text-red-700 font-semibold";
      const arrowIcon = isUp ? "↑" : "↓";

      html += `
        <td class="py-1.5 px-2 text-right bg-cyan-50/60 ${varColor} border-r border-cyan-200">
          <span class="inline-flex items-center gap-0.5 justify-end">
            ${variance} <span>${arrowIcon}</span>
          </span>
        </td>
      `;

      // 5 Future Forecast Columns
      row.futureForecast.forEach(val => {
        let displayVal = val;
        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * mult;
          displayVal = Math.round(num).toLocaleString();
        }

        // Inline sparkbar for Utilisation row
        let sparkbarHtml = "";
        if (row.hasSparkbar) {
          const pct = parseFloat(val) || 35;
          sparkbarHtml = `
            <div class="w-12 h-1.5 bg-slate-200 rounded-full inline-block ml-1 align-middle overflow-hidden">
              <div class="h-full bg-blue-600 rounded-full" style="width: ${pct * 2}%;"></div>
            </div>
          `;
        }

        html += `<td class="py-1.5 px-2 text-right ${textWeight}">${displayVal}${sparkbarHtml}</td>`;
      });

      html += `</tr>`;
    });

    html += `
          </tbody>
        </table>
      </div>
    `;

    tableContainer.innerHTML = html;
  },

  /**
   * Render Supplementary Views (Demand, Geographic Hub, Accuracy, Forecast Lead/Lag)
   */
  renderComplementaryViews() {
    // Demand View
    const demand = DASHBOARD_DATA.demandView;
    const demandBody = document.getElementById("demand-segments-tbody");
    if (demandBody) {
      demandBody.innerHTML = demand.demandBySegment.map(seg => `
        <tr class="hover:bg-slate-50 border-b border-slate-100">
          <td class="py-2.5 px-3 font-medium text-slate-800">${seg.segment}</td>
          <td class="py-2.5 px-3 text-right font-semibold text-slate-900">${seg.volume.toLocaleString()}</td>
          <td class="py-2.5 px-3 text-right">
            <span class="px-2 py-0.5 rounded text-xs font-semibold ${seg.capacityRatio >= 1.0 ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'}">
              ${(seg.capacityRatio * 100).toFixed(0)}%
            </span>
          </td>
        </tr>
      `).join("");
    }

    // Accuracy View
    const accuracy = DASHBOARD_DATA.accuracyView;
    const accuracyBody = document.getElementById("accuracy-table-tbody");
    if (accuracyBody) {
      accuracyBody.innerHTML = accuracy.historicalAccuracy.map(row => `
        <tr class="hover:bg-slate-50 border-b border-slate-100">
          <td class="py-2 px-3 font-medium text-slate-800">${row.week}</td>
          <td class="py-2 px-3 text-right text-slate-700">${row.forecast.toLocaleString()}</td>
          <td class="py-2 px-3 text-right text-slate-900 font-semibold">${row.actual.toLocaleString()}</td>
          <td class="py-2 px-3 text-right font-semibold ${row.errorPct > 5 ? 'text-amber-600' : 'text-emerald-600'}">
            ${row.errorPct}%
          </td>
        </tr>
      `).join("");
    }
  },

  /**
   * Animated Refresh
   */
  triggerDataRefresh() {
    const icon = document.querySelector("#btn-refresh-data svg");
    if (icon) icon.classList.add("animate-spin");

    setTimeout(() => {
      this.state.lastRefreshed = new Date();
      this.renderLastRefreshed();
      this.updateAllViews();
      if (icon) icon.classList.remove("animate-spin");
    }, 400);
  },

  renderLastRefreshed() {
    const el = document.getElementById("last-refreshed-time");
    if (el) {
      const d = this.state.lastRefreshed;
      const hours = String(d.getHours()).padStart(2, "0");
      const mins = String(d.getMinutes()).padStart(2, "0");
      el.textContent = `1 Jun 2026 (WK 23) • Refreshed at ${hours}:${mins}`;
    }
  },

  /**
   * Export or Print current view
   */
  exportCurrentView() {
    window.print();
  }
};

// Initialize App when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  App.init();
});
