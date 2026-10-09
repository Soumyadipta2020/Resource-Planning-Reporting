/**
 * Application Controller & State Engine
 * Synchronizes global filters, renders views, and ensures data consistency across all tabs.
 */

const App = {
  state: {
    activeTab: "executive-summary", // Default is Executive Summary
    capacitySheet: "sheet-2",
    demandSheet: "dsheet-1", // "sheet-2" (Dashboard), "sheet-3" (Comparison), "sheet-4" (Detailed Matrix)
    selectedGeography: "all",
    selectedWeek: "wk38",
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


    // Demand Overview Sheet sub-navigation buttons
    document.querySelectorAll(".dsheet-toggle-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const sheetId = btn.getAttribute("data-dsheet");
        if (sheetId) {
          this.switchDemandSheet(sheetId);
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


    // Show/hide demand views sub-navigation bar
    const demandTabs = document.getElementById("demand-nav-tabs");
    if (demandTabs) {
      if (tabId === "demand") {
        demandTabs.style.setProperty("display", "flex", "important");
        demandTabs.classList.remove("hidden");
      } else {
        demandTabs.style.setProperty("display", "none", "important");
        demandTabs.classList.add("hidden");
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

  switchDemandSheet(sheetId) {
    this.state.demandSheet = sheetId;

    document.querySelectorAll(".dsheet-toggle-btn").forEach(btn => {
      if (btn.getAttribute("data-dsheet") === sheetId) {
        btn.classList.add("bg-blue-700", "text-white", "shadow-sm");
        btn.classList.remove("bg-slate-100", "text-slate-700", "hover:bg-slate-200");
      } else {
        btn.classList.remove("bg-blue-700", "text-white", "shadow-sm");
        btn.classList.add("bg-slate-100", "text-slate-700", "hover:bg-slate-200");
      }
    });

    document.querySelectorAll(".demand-sheet-content").forEach(content => {
      if (content.id === `demand-${sheetId}`) {
        content.classList.remove("hidden");
      } else {
        content.classList.add("hidden");
      }
    });

    setTimeout(() => {
      this.updateDemandSheet();
    }, 50);
  },


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
       const mults = this.getGlobalMultipliers();
       const planObj = DASHBOARD_DATA.metadata.plans.find(p => p.id === this.state.selectedPlan);
       const planName = planObj ? planObj.name : 'GFF1 2026';
       
       let activePlanMult = mults.isPlanActive ? mults.plan : 0;
       
       let baseValue = Math.round(1988 * activePlanMult);
       let actualValue = Math.round(1689 * mults.base);
       
       let dlDiff = Math.round(-176 * mults.base);
       let contrDiff = (actualValue - baseValue) - dlDiff;
       
       const waterfallData = [
         { label: planName, value: baseValue, type: 'total' },
         { label: 'DL Installs', value: dlDiff, type: dlDiff >= 0 ? 'up' : 'down' },
         { label: 'Contr. Installs', value: contrDiff, type: contrDiff >= 0 ? 'up' : 'down' },
         { label: 'Actuals', value: actualValue, type: 'total' }
       ];
       ChartManager.renderCapacityWaterfallChart('demand-waterfall-chart', waterfallData);
       
       const planNameEl = document.getElementById('demand-waterfall-plan-name');
       if (planNameEl) {
           planNameEl.textContent = planName;
           const tbody = document.getElementById('demand-waterfall-tbody');
       if (tbody) {
           let dlBase = Math.round(1073 * activePlanMult);
           let contrBase = Math.round(905 * activePlanMult);
           let dlAct = Math.round(897 * mults.base);
           let contrAct = Math.round(792 * mults.base);
           
           let dlV = dlAct - dlBase;
           let contrV = contrAct - contrBase;
           let totV = actualValue - baseValue;
           
           const formatNum = (v) => v.toLocaleString();
           const formatVar = (v) => {
               if (!mults.isPlanActive) return '-';
               let icon = v >= 0 ? '↑' : '↓';
               let color = v >= 0 ? 'text-emerald-600' : 'text-red-600';
               return `<span class="${color} font-semibold">${v >= 0 ? '+' : ''}${formatNum(v)} <span class="ml-1">${icon}</span></span>`;
           };
           
           tbody.innerHTML = `
               <tr class="bg-slate-50">
                 <td class="py-1.5 px-3 font-bold text-left border-r border-slate-200">${planName}</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${mults.isPlanActive ? formatNum(dlBase) : '-'}</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${mults.isPlanActive ? formatNum(contrBase) : '-'}</td>
                 <td class="py-1.5 px-3 font-semibold">${mults.isPlanActive ? formatNum(baseValue) : '-'}</td>
               </tr>
               <tr>
                 <td class="py-1.5 px-3 font-bold text-left border-r border-slate-200">Actuals</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${formatNum(dlAct)}</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${formatNum(contrAct)}</td>
                 <td class="py-1.5 px-3 font-semibold">${formatNum(actualValue)}</td>
               </tr>
               <tr class="bg-slate-100">
                 <td class="py-1.5 px-3 font-bold text-left border-r border-slate-200">Variance</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${formatVar(dlV)}</td>
                 <td class="py-1.5 px-3 border-r border-slate-200">${formatVar(contrV)}</td>
                 <td class="py-1.5 px-3 font-bold">${formatVar(totV)}</td>
               </tr>
           `;
       }
       }
    }
  },
  
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

  getGlobalMultipliers() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;

    let planMult = 1.0;
      let isPlanActive = true;
      let weekMult = 1.0;
      let currentWkNum = 38;
      
      if (this.state.selectedWeek) {
         const match = this.state.selectedWeek.match(/wk(\d+)/);
         if (match) {
             currentWkNum = parseInt(match[1]);
             weekMult = 1 + ((currentWkNum - 38) * 0.015);
         }
      }

      if (this.state.selectedPlan === "gff2_2026") {
         planMult = 1.15;
         isPlanActive = currentWkNum >= 37; // Historic weeks are before Sep 2026 (WK 37)
      }
    return {
       base: geoMult * weekMult,
       plan: geoMult * weekMult * planMult,
       isPlanActive: isPlanActive
    };
  },
  
  getGlobalMultiplier() {
    return this.getGlobalMultipliers().base; // Fallback for things that just need a quick scale
  },

  /**
   * Master Update: Recalculates and updates everything based on current state & filters
   */
  updateAllViews() {
    this.renderExecutiveSummary();
    this.updateCapacitySheet();
    this.renderComplementaryViews();
    this.updateDemandSheet();
  },

  /**
   * Render Executive Summary (Image 4)
   */
  renderExecutiveSummary() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const regional = isRegional ? DASHBOARD_DATA.regionalData[geo] : null;

    const mults = this.getGlobalMultipliers();
    const mult = mults.base;

    // Scale KPI Values
    const baseKpis = isRegional ? {
      installs: { ...regional.kpis.installs },
      sales: { ...regional.kpis.sales, unit: "£M" },
      leads: { ...regional.kpis.leads },
      activeHeads: { ...regional.kpis.activeHeads },
      availableHours: { ...regional.kpis.availableHours },
      productivity: { ...regional.kpis.productivity, unit: "per Head" }
    } : DASHBOARD_DATA.executiveSummary.kpis;

    const kpiData = {};
    for (let key in baseKpis) {
       let val = baseKpis[key].value * (isRegional ? 1.0 : mult);
       let fmt = baseKpis[key].formatted;
       if (fmt.includes('K')) fmt = (val/1000).toFixed(2) + 'K';
       else if (fmt.includes('£M') || fmt.includes('A£M')) fmt = '£' + (val).toFixed(2) + 'M';
       else fmt = val.toFixed(2);
       
       kpiData[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val,
          vsPlan: mults.isPlanActive ? baseKpis[key].vsPlan : null
       };
    }

    this.renderKpiCard("exec-kpi-installs", kpiData.installs.formatted, kpiData.installs.wow, kpiData.installs.vsPlan);
    this.renderKpiCard("exec-kpi-sales", kpiData.sales.formatted, kpiData.sales.wow, kpiData.sales.vsPlan);
    this.renderKpiCard("exec-kpi-leads", kpiData.leads.formatted, kpiData.leads.wow, kpiData.leads.vsPlan);
    this.renderKpiCard("exec-kpi-heads", kpiData.activeHeads.formatted, kpiData.activeHeads.wow, kpiData.activeHeads.vsPlan);
    this.renderKpiCard("exec-kpi-availhrs", kpiData.availableHours.formatted, kpiData.availableHours.wow, kpiData.availableHours.vsPlan);
    this.renderKpiCard("exec-kpi-productivity", kpiData.productivity.formatted, kpiData.productivity.wow, kpiData.productivity.vsPlan);

    // Installs Weekly Combo Chart
    let weeklyData = DASHBOARD_DATA.executiveSummary.weeklyInstalls.map(d => {
      const a = d.actual === null ? null : Math.round(d.actual * mults.base);
      let p = d.plan === null ? null : Math.round(d.plan * mults.plan);
      const wkNum = parseInt(d.week.replace("WK ", ""));
        if (this.state.selectedPlan === "gff2_2026" && wkNum < 37) p = null;
      return {
        week: d.week,
        actual: a,
        plan: p,
        variance: (a === null || p === null) ? null : (a - p)
      };
    });
    ChartManager.renderWeeklyInstallsChart("chart-weekly-installs", weeklyData);

    // Waterfall Chart Drivers
    let drivers = DASHBOARD_DATA.executiveSummary.waterfallDrivers.map(d => {
      let v;
      if (d.name === "Plan") {
          v = Math.round(d.value * mults.plan);
      } else {
          v = Math.round(d.value * mults.base);
      }
      if (!mults.isPlanActive) {
          if (d.name === "Plan") v = 0; // nullify plan
          else if (d.name !== "Actuals") v = 0; // nullify drivers
      }
      return {
        ...d,
        value: v
      };
    });
    ChartManager.renderWaterfallChart("waterfall-chart-container", drivers);

    // Sparklines
    ChartManager.renderSparklines(DASHBOARD_DATA.executiveSummary.sparklines);
  },  /**
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
      if (wowPct === null || wowPct === undefined || wowPct === "N/A") {
        wowEl.innerHTML = `
          <span class="text-slate-500 font-semibold flex items-center">
            - WoW
          </span>
        `;
      } else {
        const isUp = wowPct >= 0;
        wowEl.innerHTML = `
          <span class="${isUp ? 'text-emerald-700' : 'text-red-700'} font-semibold flex items-center">
            ${isUp ? '↑' : '↓'} ${Math.abs(wowPct)}% WoW
          </span>
        `;
      }
    }

    if (planEl) {
      if (vsPlanPct === null || vsPlanPct === undefined || vsPlanPct === "N/A") {
        planEl.innerHTML = `
          <span class="text-slate-500 font-semibold flex items-center">
            - vs Plan
          </span>
        `;
      } else {
        const isUp = vsPlanPct >= 0;
        planEl.innerHTML = `
          <span class="${isUp ? 'text-emerald-700' : 'text-red-700'} font-semibold flex items-center">
            ${isUp ? '↑' : '↓'} ${Math.abs(vsPlanPct)}% vs Plan
          </span>
        `;
      }
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
    } else if (this.state.capacitySheet === "sheet-5") {
      this.renderSheet5();
    }
  },

  /**
   * Render Capacity Overview - Sheet 2 (Image 3)
   */
  renderCapacitySheet2() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const regional = isRegional ? DASHBOARD_DATA.regionalData[geo] : null;
    
    const mults = this.getGlobalMultipliers();
    const mult = mults.base;

    // Top KPIs
    const baseKpis = isRegional ? {
      availableHours: { ...regional.kpis.availableHours },
      totalDowntime: { ...regional.kpis.totalDowntime },
      capacityUtilisation: { ...regional.kpis.capacityUtilisation },
      workforceAvailability: { ...regional.kpis.workforceAvailability },
      productivity: { ...regional.kpis.productivity },
      sicknessPercent: { ...regional.kpis.sicknessPercent }
    } : DASHBOARD_DATA.capacitySheet2.kpis;

    const kpis = {};
    for (let key in baseKpis) {
       let val = baseKpis[key].value * (isRegional ? 1.0 : mult);
       // exceptions for percentages
       if (key === 'capacityUtilisation' || key === 'workforceAvailability' || key === 'sicknessPercent') {
           val = baseKpis[key].value + (mult - 1)*10; // slightly shift percent
       }
       
       let fmt = baseKpis[key].formatted;
       if (fmt.includes('%')) fmt = val.toFixed(1) + '%';
       else if (fmt.includes('K')) fmt = (val/1000).toFixed(1) + 'K';
       else fmt = val.toFixed(1) > 10 ? Math.round(val).toLocaleString() : val.toFixed(2);
       
       kpis[key] = {
          ...baseKpis[key],
          formatted: fmt,
          value: val,
          vsPlan: mults.isPlanActive ? baseKpis[key].vsPlan : null
       };
    }

    this.renderKpiCard("cap-kpi-availhrs", kpis.availableHours.formatted, kpis.availableHours.wow, kpis.availableHours.vsPlan);
    this.renderKpiCard("cap-kpi-downtime", kpis.totalDowntime.formatted, kpis.totalDowntime.wow, kpis.totalDowntime.vsPlan);
    this.renderKpiCard("cap-kpi-util", kpis.capacityUtilisation.formatted, kpis.capacityUtilisation.wow, kpis.capacityUtilisation.vsPlan);
    this.renderKpiCard("cap-kpi-avail", kpis.workforceAvailability.formatted, kpis.workforceAvailability.wow, kpis.workforceAvailability.vsPlan);
    this.renderKpiCard("cap-kpi-prod", kpis.productivity.formatted, kpis.productivity.wow, kpis.productivity.vsPlan);
    this.renderKpiCard("cap-kpi-sick", kpis.sicknessPercent.formatted, kpis.sicknessPercent.wow, kpis.sicknessPercent.vsPlan);

    // Funnel
    let funnelSteps = isRegional ? [...regional.funnel] : [...DASHBOARD_DATA.capacitySheet2.funnel];
    funnelSteps = funnelSteps.map(s => ({
        ...s,
        hours: Math.round(s.hours * mult),
        formatted: s.formatted.includes('K') ? (s.hours * mult / 1000).toFixed(1) + 'K' : Math.round(s.hours * mult).toLocaleString()
    }));
    ChartManager.renderCapacityFunnel("capacity-funnel-container", funnelSteps);

    // Downtime Categories Donut & Table
    let categories = isRegional ? [...regional.downtimeCategories] : [...DASHBOARD_DATA.capacitySheet2.downtimeCategories];
    categories = categories.map(c => ({
        ...c,
        hours: Math.round(c.hours * mult)
    }));
    const totalDowntimeHrs = isRegional ? Math.round(regional.kpis.totalDowntime.value) : Math.round(DASHBOARD_DATA.capacitySheet2.totalDowntimeHours * mult);
    ChartManager.renderDowntimeChart("downtime-donut-chart", "downtime-table-container", categories, totalDowntimeHrs);

    // Capacity Risk Heatmap
    ChartManager.renderHeatmap("heatmap-container", DASHBOARD_DATA.capacitySheet2.heatmap, geo);

    // Region Efficiency Matrix
    ChartManager.renderEfficiencyMatrix("efficiency-matrix-chart", DASHBOARD_DATA.capacitySheet2.efficiencyMatrix, geo);

    // Bottom KPIs
    const bottom = DASHBOARD_DATA.capacitySheet2.bottomKpis;
    if (document.getElementById("bottom-downtime-val")) {
      document.getElementById("bottom-downtime-val").textContent = (bottom.totalDowntimePct.value * mult).toFixed(1) + "%";
    }
    if (document.getElementById("bottom-utilisation-val")) {
      document.getElementById("bottom-utilisation-val").textContent = (bottom.capacityUtilisation.value * mult).toFixed(1) + "%";
    }
    if (document.getElementById("bottom-availability-val")) {
      document.getElementById("bottom-availability-val").textContent = (bottom.workforceAvailability.value * mult).toFixed(1) + "%";
    }
    if (document.getElementById("bottom-sickness-val")) {
      document.getElementById("bottom-sickness-val").textContent = (bottom.sicknessPercent.value * mult).toFixed(2) + "%";
    }
  },  /**
   * Render Capacity Overview - Sheet 3 (Comparison Matrix - Image 2)
   */
  renderCapacitySheet3() {
    const tableBody = document.getElementById("capacity-comparison-tbody");
    if (!tableBody) return;

    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const mults = this.getGlobalMultipliers();
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
      const doScale = isRegional || mults.base !== 1.0 || mults.plan !== 1.0;
      if (doScale && !r.metric.includes("%")) {
        if (r.thisWeekActual.includes("K")) {
          const raw = parseFloat(r.thisWeekActual) * 1000 * mults.base;
          thisWeekAct = (raw / 1000).toFixed(1) + "K";
          const rawPlan = parseFloat(r.thisWeekPlan) * 1000 * mults.plan;
          thisWeekPlan = (rawPlan / 1000).toFixed(1) + "K";
          vsPlan = ((raw - rawPlan) / 1000).toFixed(1) + "K";
          const rawLW = parseFloat(r.lastWeekActual) * 1000 * mults.base;
          lastWeekAct = (rawLW / 1000).toFixed(1) + "K";
          vsLW = ((raw - rawLW) / 1000).toFixed(1) + "K";
          varPlanAbs = vsPlan;
          varLWAbs = vsLW;
        } else if (!r.metric.includes("Productivity")) {
          const raw = parseInt(r.thisWeekActual.replace(/,/g, "")) * mults.base;
          thisWeekAct = Math.round(raw).toLocaleString();
          const rawPlan = parseInt(r.thisWeekPlan.replace(/,/g, "")) * mults.plan;
          thisWeekPlan = Math.round(rawPlan).toLocaleString();
          vsPlan = Math.round(raw - rawPlan).toLocaleString();
          const rawLW = parseInt(r.lastWeekActual.replace(/,/g, "")) * mults.base;
          lastWeekAct = Math.round(rawLW).toLocaleString();
          vsLW = Math.round(raw - rawLW).toLocaleString();
          varPlanAbs = vsPlan;
          varLWAbs = vsLW;
        }
      }

      if (!mults.isPlanActive) {
          thisWeekPlan = "-";
          vsPlan = "-";
          varPlanAbs = "-";
          varPlanPct = "-";
      }

      const isVsPlanDown = vsPlan.includes("-") && vsPlan !== "-";
      const isVsLWDown = vsLW.includes("-");

      html += `
        <tr class="hover:bg-slate-50/80 transition-colors border-b border-slate-200">
          <td class="py-1 px-2 font-bold text-slate-900">${r.metric}</td>
          <td class="py-1 px-1 text-right font-semibold text-slate-800">${thisWeekAct}</td>
          <td class="py-1 px-1 text-right text-slate-700">${thisWeekPlan}</td>
          <td class="py-1 px-1 text-right font-medium ${vsPlan === '-' ? 'text-slate-500' : (isVsPlanDown ? 'text-red-600' : 'text-emerald-600')}">
            ${vsPlan === '-' ? '' : (isVsPlanDown ? '↓' : '↑')} ${vsPlan === '-' ? '-' : vsPlan.replace('-', '')}
          </td>
          <td class="py-1 px-1 text-right text-slate-800">${lastWeekAct}</td>
          <td class="py-1 px-1 text-right font-medium ${isVsLWDown ? 'text-red-600' : 'text-emerald-600'}">
            ${isVsLWDown ? '↓' : '↑'} ${vsLW.replace('-', '')}
          </td>
          <td class="py-1 px-1 text-right font-semibold ${vsPlan === '-' ? 'text-slate-500' : (isVsPlanDown ? 'text-red-600' : 'text-emerald-600')}">
            ${vsPlan === '-' ? '' : (isVsPlanDown ? '↓' : '↑')} ${varPlanAbs === '-' ? '-' : varPlanAbs.replace('-', '')}
          </td>
          <td class="py-1 px-1 text-right text-slate-600 font-medium">${varPlanPct}</td>
          <td class="py-1 px-1 text-right font-semibold ${isVsLWDown ? 'text-red-600' : 'text-emerald-600'}">
            ${isVsLWDown ? '↓' : '↑'} ${varLWAbs.replace('-', '')}
          </td>
          <td class="py-1 px-1 text-right text-slate-600 font-medium">${varLWPct}</td>
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
    const mults = this.getGlobalMultipliers();

    let buMult = 1.0;
    if (this.state.selectedBusinessUnit === "hec") buMult = 0.58;
    else if (this.state.selectedBusinessUnit === "kac") buMult = 0.28;
    else if (this.state.selectedBusinessUnit === "nzev") buMult = 0.14;

    const actualMult = mults.base * buMult;
    const forecastMult = mults.plan * buMult;

    // Create scaled series
    const series = {
      weeks: rawSeries.weeks,
      reportingIndex: rawSeries.reportingIndex,
      metrics: {}
    };

    Object.keys(rawSeries.metrics).forEach(key => {
      const metric = rawSeries.metrics[key];
      const isPercentOrRatio = metric.unit === "%" || key === "productivity";

      const actScale = isPercentOrRatio ? 1.0 : actualMult;
      const fcScale = isPercentOrRatio ? 1.0 : forecastMult;

      series.metrics[key] = {
        label: metric.label,
        unit: metric.unit,
        actuals: metric.actuals.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * actScale))),
        forecast: metric.forecast.map((v, i) => {
            const weekLabel = rawSeries.weeks[i];
              const weekObj = DASHBOARD_DATA.metadata.reportingWeeks.find(w => w.date === weekLabel);
              const wkNum = weekObj ? weekObj.weekNum : (37 + i);
              if (this.state.selectedPlan === "gff2_2026" && wkNum < 37) return null;
            return v === null ? null : (isPercentOrRatio ? v : Math.round(v * fcScale));
        })
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
    const mults = this.getGlobalMultipliers();

    let buMult = 1.0;
    if (bu === "hec") buMult = 0.58;
    else if (bu === "kac") buMult = 0.28;
    else if (bu === "nzev") buMult = 0.14;

    const actMult = mults.base * buMult;
    const fcMult = mults.plan * buMult;
    const isScaled = actMult !== 1.0 || fcMult !== 1.0;

    const selectedWeekObj = DASHBOARD_DATA.metadata.reportingWeeks.find(w => w.id === this.state.selectedWeek) || { date: "5 Oct 2026" };
    const currentWeekLabel = selectedWeekObj.date;

    let html = `
      <div class="overflow-x-auto w-full shadow-sm rounded border border-slate-200">
        <table class="w-full text-[10px] border-collapse">
          <thead>
            <!-- Top Header Category Row -->
            <tr class="text-white text-center font-bold">
              <th class="py-1 px-1 text-left bg-slate-600 sticky left-0 z-20 w-32">Metric</th>
              <th colspan="5" class="py-1 px-1 bg-slate-500 border-l border-r border-slate-400">Actuals</th>
              <th class="py-1 px-1 bg-cyan-700 border-r border-cyan-600">Actual</th>
                <th class="py-1 px-1 bg-cyan-700 border-r border-cyan-600">Forecast</th>
              <th class="py-1 px-1 bg-cyan-700 border-r border-cyan-600">Variance</th>
              <th colspan="5" class="py-1 px-1 bg-slate-500 border-l border-slate-400">Forecast - ${this.state.selectedPlan === 'gff2_2026' ? 'GFF2 2026' : 'GFF1 2026'}</th>
            </tr>
            <!-- Sub-Header Date Row -->
            <tr class="bg-slate-100 text-slate-700 text-center font-semibold border-b border-slate-300">
              <th class="py-1 px-1 text-left sticky left-0 bg-slate-100 z-20"></th>
              ${data.tableColumns.actualsHeaders.map(h => `<th class="py-1 px-1">${h}</th>`).join('')}
              <th class="py-1 px-1 bg-cyan-50 text-cyan-900 border-l border-cyan-200">${currentWeekLabel}</th>
              <th class="py-1 px-1 bg-cyan-50 text-cyan-900">${currentWeekLabel}</th>
              <th class="py-1 px-1 bg-cyan-50 text-cyan-900 border-r border-cyan-200">${currentWeekLabel}</th>
              ${data.tableColumns.forecastHeaders.map(h => `<th class="py-1 px-1">${h}</th>`).join('')}
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200">
    `;

    data.tableRows.forEach((row, idx) => {
      const isAlt = idx % 2 === 1 ? "bg-slate-50/60" : "bg-white";
      const isBold = ["DL Headcount", "DL Gross Hours", "Total DL Downtime", "DL Available Hours", "DL Productive Hrs", "DL Utilisation %"].includes(row.metric);
      const textWeight = isBold ? "font-bold text-slate-900" : "text-slate-700 font-medium";

      html += `<tr class="${isAlt} hover:bg-blue-50/50 transition-colors">`;
      // Sticky Metric column
      html += `<td class="py-1 px-1 text-left sticky left-0 ${isAlt} z-10 ${textWeight} border-r border-slate-200 shadow-[1px_0_0_rgba(0,0,0,0.05)]">${row.metric}</td>`;

      // 5 Actuals Columns
      row.actuals.forEach(val => {
        let displayVal = val;
        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * actMult;
          displayVal = Math.round(num).toLocaleString();
        }
        html += `<td class="py-1 px-1 text-right ${textWeight}">${displayVal}</td>`;
      });

      // Current Week: Forecast, Actual, Variance
      let curForecast = row.currentForecast;
      let curActual = row.currentActual;
      let variance = row.variance;
      if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
        const numFc = parseInt(curForecast.replace(/,/g, "")) * fcMult;
        const numAct = parseInt(curActual.replace(/,/g, "")) * actMult;
        curForecast = Math.round(numFc).toLocaleString();
        curActual = Math.round(numAct).toLocaleString();
        const diff = Math.round(numAct - numFc);
        variance = diff.toLocaleString();
      }
      
      if (!mults.isPlanActive) {
          curForecast = "-";
          variance = "-";
      }

      html += `<td class="py-1 px-1 text-right bg-cyan-50/40 text-slate-900 ${textWeight}">${curActual}</td>`;
      html += `<td class="py-1 px-1 text-right bg-cyan-50/40 text-slate-800 ${textWeight}">${curForecast}</td>`;

      // Variance arrow and color
      const isUp = row.varDir === "up";
      const isPositive = row.varType === "positive";
      const varColor = isPositive ? "text-emerald-700 font-semibold" : "text-red-700 font-semibold";
      const arrowIcon = isUp ? "↑" : "↓";

      html += `
        <td class="py-1 px-1 text-right bg-cyan-50/60 ${varColor} border-r border-cyan-200">
          <span class="inline-flex items-center gap-0.5 justify-end">
            ${variance} <span>${arrowIcon}</span>
          </span>
        </td>
      `;

      // 5 Future Forecast Columns
      row.futureForecast.forEach(val => {
        let displayVal = val;
        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * fcMult;
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

        html += `<td class="py-1 px-1 text-right ${textWeight}">${displayVal}${sparkbarHtml}</td>`;
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
    const mult = this.getGlobalMultiplier();

    // Demand View
    const demand = DASHBOARD_DATA.demandView;
    const demBacklog = document.getElementById("dem-kpi-backlog");
    if (demBacklog) demBacklog.textContent = (demand.backlogWeeks * (1 + (mult-1)*0.5)).toFixed(1);
    
    const demInbound = document.getElementById("dem-kpi-inbound");
    if (demInbound) demInbound.textContent = Math.round(demand.inboundDemand * mult).toLocaleString();
    
    const demComp = document.getElementById("dem-kpi-comp");
    if (demComp) demComp.textContent = (parseFloat(demand.completionRate) + (mult-1)*5).toFixed(1) + "%";
    
    const demUnmet = document.getElementById("dem-kpi-unmet");
    if (demUnmet) demUnmet.textContent = Math.round(demand.unmetDemandHours * (2-mult)).toLocaleString();

    const demandBody = document.getElementById("demand-segments-tbody");
    if (demandBody) {
      demandBody.innerHTML = demand.demandBySegment.map(seg => `
        <tr class="hover:bg-slate-50 border-b border-slate-100">
          <td class="py-2.5 px-3 font-medium text-slate-800">${seg.segment}</td>
          <td class="py-2.5 px-3 text-right font-semibold text-slate-900">${Math.round(seg.volume * mult).toLocaleString()}</td>
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
    const accMape = document.getElementById("acc-kpi-mape");
    if (accMape) accMape.textContent = (parseFloat(accuracy.overallMape) * (1 + (mult-1)*0.2)).toFixed(1) + "%";
    
    const accBias = document.getElementById("acc-kpi-bias");
    if (accBias) {
       const bias = parseFloat(accuracy.forecastBias) * (1 + (mult-1)*0.5);
       accBias.textContent = (bias > 0 ? "+" : "") + bias.toFixed(1) + "%";
    }

    const accuracyBody = document.getElementById("accuracy-table-tbody");
    if (accuracyBody) {
      accuracyBody.innerHTML = accuracy.historicalAccuracy.map(row => `
        <tr class="hover:bg-slate-50 border-b border-slate-100">
          <td class="py-2 px-3 font-medium text-slate-800">${row.week}</td>
          <td class="py-2 px-3 text-right text-slate-700">${Math.round(row.forecast * mult).toLocaleString()}</td>
          <td class="py-2 px-3 text-right text-slate-900 font-semibold">${Math.round(row.actual * mult).toLocaleString()}</td>
          <td class="py-2 px-3 text-right font-semibold ${row.errorPct > 5 ? 'text-amber-600' : 'text-emerald-600'}">
            ${(row.errorPct * (1 + (mult-1)*0.1)).toFixed(1)}%
          </td>
        </tr>
      `).join("");
    }
  },  /**
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
      el.textContent = `14 Sep 2026 (WK 38) • Refreshed at ${hours}:${mins}`;
    }
  },

  /**
   * Export or Print current view
   */
  
  renderSheet5() {
    const data = DASHBOARD_DATA.capacitySheet5;
    if (!data) return;

    const mults = this.getGlobalMultipliers();
    
    // Get selected plan name from metadata
    const planObj = DASHBOARD_DATA.metadata.plans.find(p => p.id === this.state.selectedPlan);
    const planName = planObj ? planObj.name : 'GFF1 2026';

    // If GFF2 is selected but not active for this week, we should show empty or zero out plan
    let activePlanMult = mults.isPlanActive ? mults.plan : 0;

    let baseVal = Math.round(data.waterfallData[0].value * activePlanMult);
    let actVal = Math.round(data.waterfallData[data.waterfallData.length - 1].value * mults.base);
    let totalVar = actVal - baseVal;
    
    // sum of old drivers
    let oldVarTotal = 0;
    for (let i = 1; i < data.waterfallData.length - 1; i++) {
        oldVarTotal += data.waterfallData[i].value;
    }
    
    let runningVar = 0;

    // Clone waterfallData and replace "Base" label with the plan name
    const chartData = data.waterfallData.map((item, idx) => {
      if (idx === 0) {
        return { ...item, label: planName, value: baseVal };
      }
      if (idx === data.waterfallData.length - 1) {
        return { ...item, label: 'Actuals', value: actVal };
      }
      
      let driverVal = 0;
      if (oldVarTotal !== 0) {
         driverVal = Math.round(item.value * (totalVar / oldVarTotal));
      }
      
      // Handle rounding error on the last driver to ensure exact match
      if (idx === data.waterfallData.length - 2) {
          driverVal = totalVar - runningVar;
      }
      runningVar += driverVal;
      
      return { ...item, value: driverVal, type: driverVal >= 0 ? "up" : "down" };
    });

    ChartManager.renderCapacityWaterfallChart('sheet5-waterfall-chart', chartData);
    
    const tableContainer = document.getElementById('sheet5-waterfall-table-container');
    if (!tableContainer) return;

    // Function to parse formatted number
    const parseNum = (str) => {
        if (typeof str !== "string") return 0;
        return parseFloat(str.replace(/,/g, '').replace(/%/g, ''));
    };
    
    const formatNum = (num, isPct, isDecimal) => {
        if (isPct) return num.toFixed(1) + "%";
        if (isDecimal) return num.toFixed(2);
        return Math.round(num).toLocaleString();
    };

    // Calculate dynamic rows
    const planRow = data.tableRows[0].values.map((v, i) => {
        const isPct = v.includes("%");
        const isProd = i === 14; 
        const val = parseNum(v);
        if (!mults.isPlanActive) return isPct || isProd ? "-" : "0";
        if (isPct || isProd) return v;
        return formatNum(val * mults.plan, false, false);
    });
    
    const actRow = data.tableRows[1].values.map((v, i) => {
        const isPct = v.includes("%");
        const isProd = i === 14; 
        const val = parseNum(v);
        if (isPct || isProd) return v;
        return formatNum(val * mults.base, false, false);
    });
    
    const varRow = planRow.map((pv, i) => {
        const av = actRow[i];
        if (!mults.isPlanActive) return { val: "-", dir: "down", color: "text-slate-500" };
        
        const isPct = pv.includes("%");
        const isProd = i === 14;
        
        let pVal = parseNum(pv);
        let aVal = parseNum(av);
        let diff = aVal - pVal;
        
        // Inverse logic for Downtime/Sickness/Holiday/Meeting/Other
        const inverseCols = [1,2,3,4,7,8,9,10,11,12];
        let color = diff > 0 ? "text-emerald-700" : "text-red-700";
        let dir = diff > 0 ? "up" : "down";
        if (inverseCols.includes(i)) {
            color = diff < 0 ? "text-emerald-700" : "text-red-700";
            dir = diff < 0 ? "up" : "down";
        }
        
        let diffFmt = formatNum(Math.abs(diff), isPct, isProd);
        diffFmt = (diff < 0 ? "-" : "") + diffFmt;
        
        if (diff === 0) color = "text-slate-600";

        return { val: diffFmt, dir: dir, color: color };
    });

    let html = `
      <div class="overflow-x-auto w-full shadow-sm rounded border border-slate-200">
        <table class="w-full text-[10px] border-collapse">
          <thead>
            <tr class="bg-cyan-600 text-white text-center font-semibold">
              <th class="py-1 px-1 text-left sticky left-0 bg-cyan-700 z-10 w-16 border-r border-cyan-500"></th>
              ${data.tableColumns.map(col => `<th class="py-1 px-1 border-r border-cyan-500 leading-tight">${col}</th>`).join('')}
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200">
    `;
    
    const dynamicRows = [
      { rowLabel: planName, values: planRow, isVariance: false },
      { rowLabel: "Actuals", values: actRow, isVariance: false },
      { rowLabel: "Variance", values: varRow, isVariance: true }
    ];

    dynamicRows.forEach((row, idx) => {
      const isAlt = idx % 2 === 1 ? 'bg-slate-50/60' : 'bg-white';
      const isVariance = row.isVariance;
      const textWeight = isVariance ? 'font-bold text-slate-800' : 'text-slate-700 font-medium';
      const bgClass = isVariance ? 'bg-slate-100' : isAlt;

      html += `<tr class="${bgClass} hover:bg-blue-50/50 transition-colors">`;
      html += `<td class="py-1.5 px-1 text-left sticky left-0 ${bgClass} z-10 font-bold text-slate-700 border-r border-slate-200 shadow-[1px_0_0_rgba(0,0,0,0.05)] ">${row.rowLabel}</td>`;
      
      if (isVariance) {
        row.values.forEach(valObj => {
          if (valObj.val === "-") {
             html += `<td class="py-1 px-1 text-right border-r border-slate-200 ${valObj.color} font-semibold ">-</td>`;
          } else {
             const arrowIcon = valObj.dir === 'up' ? '↑' : '↓';
             html += `<td class="py-1 px-1 text-right border-r border-slate-200 ${valObj.color} font-semibold ">
               <span class="inline-flex items-center gap-0.5 justify-end">
                 ${valObj.val} <span>${arrowIcon}</span>
               </span>
             </td>`;
          }
        });
      } else {
        row.values.forEach(val => {
          html += `<td class="py-1.5 px-1 text-right border-r border-slate-200 ${textWeight} ">${val}</td>`;
        });
      }
      html += `</tr>`;
    });
    
    html += `</tbody></table></div>`;
    tableContainer.innerHTML = html;
  },

  exportCurrentView() {
    window.print();
  }
};

// Initialize App when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  App.init();
});

