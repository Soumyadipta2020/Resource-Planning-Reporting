/**
 * Operational Planning & Capacity Management Data Store
 * Hardcoded dummy dataset modeling enterprise capacity, demand, and workforce performance.
 * Fully aligned across all executive views, capacity sheets, and regional dimensions.
 */

const DASHBOARD_DATA = {
  metadata: {
    lastUpdated: "2026-06-01T08:30:00Z",
    reportingWeeks: [
      { id: "wk21", label: "18 May 2026 (WK 21)", date: "18 May 2026", weekNum: 21 },
      { id: "wk22", label: "25 May 2026 (WK 22)", date: "25 May 2026", weekNum: 22 },
      { id: "wk23", label: "1 Jun 2026 (WK 23)", date: "1 Jun 2026", weekNum: 23, isDefault: true },
      { id: "wk24", label: "8 Jun 2026 (WK 24)", date: "8 Jun 2026", weekNum: 24 },
      { id: "wk25", label: "15 Jun 2026 (WK 25)", date: "15 Jun 2026", weekNum: 25 },
      { id: "wk26", label: "22 Jun 2026 (WK 26)", date: "22 Jun 2026", weekNum: 26 },
      { id: "wk27", label: "29 Jun 2026 (WK 27)", date: "29 Jun 2026", weekNum: 27 },
      { id: "wk28", label: "6 Jul 2026 (WK 28)", date: "6 Jul 2026", weekNum: 28 },
      { id: "wk29", label: "13 Jul 2026 (WK 29)", date: "13 Jul 2026", weekNum: 29 },
      { id: "wk30", label: "20 Jul 2026 (WK 30)", date: "20 Jul 2026", weekNum: 30 },
      { id: "wk31", label: "27 Jul 2026 (WK 31)", date: "27 Jul 2026", weekNum: 31 }
    ],
    geographies: [
      { id: "all", name: "All / National", code: "NAT", share: 1.0 },
      { id: "scotland", name: "Scotland", code: "SCT", share: 0.16 },
      { id: "north", name: "North", code: "NTH", share: 0.28 },
      { id: "midlands", name: "Midlands", code: "MID", share: 0.24 },
      { id: "south", name: "South", code: "STH", share: 0.22 },
      { id: "wales", name: "Wales", code: "WLS", share: 0.10 }
    ],
    plans: [
      { id: "gff1_2026", name: "GFF1 2026", isDefault: true },
      { id: "budget_2026", name: "Budget 2026" },
      { id: "reforecast_q3", name: "Reforecast Q3 2026" }
    ],
    businessUnits: [
      { id: "all", name: "All Units", label: "Home" },
      { id: "hec", name: "Home Energy Care", label: "HEC" },
      { id: "kac", name: "Kitchen & Appliance Care", label: "KAC" },
      { id: "nzev", name: "Net Zero & EV Solutions", label: "NZ (EV)" }
    ]
  },

  // 1. Executive Summary Data (Sheet 2 - Executive Command Centre)
  executiveSummary: {
    // Aligned national figures for WK 23
    kpis: {
      installs: { value: 2510, formatted: "2.51K", wow: 7.0, vsPlan: -4.2, status: "good" },
      sales: { value: 3.94, formatted: "£3.94M", unit: "£M", wow: 6.3, vsPlan: -3.1, status: "good" },
      leads: { value: 14650, formatted: "14.65K", wow: -27.0, vsPlan: -27.0, status: "warning" },
      activeHeads: { value: 1980, formatted: "1.98K", wow: -2.7, vsPlan: -2.7, status: "warning" },
      availableHours: { value: 47300, formatted: "47.3K", wow: 2.1, vsPlan: 1.9, status: "good" },
      productivity: { value: 4.75, formatted: "4.75", unit: "per Head", wow: 1.6, vsPlan: -2.2, status: "neutral" }
    },

    // Weekly Actual vs Plan - Installs across 10 weeks
    weeklyInstalls: [
      { week: "WK 14", actual: 2260, plan: 2410, variance: -150 },
      { week: "WK 15", actual: 2320, plan: 2380, variance: -60 },
      { week: "WK 16", actual: 2480, plan: 2450, variance: 30 },
      { week: "WK 17", actual: 2550, plan: 2500, variance: 50 },
      { week: "WK 18", actual: 2600, plan: 2750, variance: -150 },
      { week: "WK 19", actual: 2450, plan: 2620, variance: -170 },
      { week: "WK 20", actual: 2420, plan: 2580, variance: -160 },
      { week: "WK 21", actual: 2460, plan: 2520, variance: -60 },
      { week: "WK 22", actual: 2345, plan: 2480, variance: -135 },
      { week: "WK 23", actual: 2510, plan: 2415, variance: 95 }
    ],

    // Variance Analysis (Drivers) - Waterfall Chart for current week
    waterfallDrivers: [
      { name: "Plan", value: 2415, type: "total", isTotal: true },
      { name: "Productivity", value: 212, type: "positive" },
      { name: "OT", value: 167, type: "positive" },
      { name: "Holiday", value: -142, type: "negative" },
      { name: "Sickness", value: -318, type: "negative" },
      { name: "Training", value: -104, type: "negative" },
      { name: "Other", value: -40, type: "negative" },
      { name: "Actuals", value: 2510, type: "total", isTotal: true }
    ],

    // Trends (Last 12 Weeks) Sparkline arrays
    sparklines: {
      installs: {
        change: "+7.6% WoW",
        positive: true,
        data: [2100, 2180, 2240, 2300, 2260, 2320, 2480, 2550, 2600, 2450, 2345, 2510],
        labels: ["WK 12", "WK 13", "WK 14", "WK 15", "WK 16", "WK 17", "WK 18", "WK 19", "WK 20", "WK 21", "WK 22", "WK 23"]
      },
      sales: {
        change: "+6.3% WoW",
        positive: true,
        data: [3.2, 3.3, 3.4, 3.5, 3.45, 3.55, 3.75, 3.82, 3.90, 3.70, 3.65, 3.94],
        labels: ["WK 12", "WK 13", "WK 14", "WK 15", "WK 16", "WK 17", "WK 18", "WK 19", "WK 20", "WK 21", "WK 22", "WK 23"]
      },
      leads: {
        change: "-27.0% WoW",
        positive: false,
        data: [19.8, 19.5, 18.2, 18.9, 17.5, 18.1, 16.8, 17.2, 16.0, 15.2, 19.8, 14.65],
        labels: ["WK 12", "WK 13", "WK 14", "WK 15", "WK 16", "WK 17", "WK 18", "WK 19", "WK 20", "WK 21", "WK 22", "WK 23"]
      },
      activeHeads: {
        change: "-2.7% WoW",
        positive: false,
        data: [2050, 2040, 2045, 2030, 2025, 2035, 2020, 2015, 2010, 2005, 2035, 1980],
        labels: ["WK 12", "WK 13", "WK 14", "WK 15", "WK 16", "WK 17", "WK 18", "WK 19", "WK 20", "WK 21", "WK 22", "WK 23"]
      },
      availableHours: {
        change: "+2.1% WoW",
        positive: true,
        data: [45.2, 45.8, 46.0, 46.4, 46.1, 46.7, 47.0, 47.5, 47.8, 46.9, 46.3, 47.3],
        labels: ["WK 12", "WK 13", "WK 14", "WK 15", "WK 16", "WK 17", "WK 18", "WK 19", "WK 20", "WK 21", "WK 22", "WK 23"]
      },
      productivity: {
        change: "+1.6% WoW",
        positive: true,
        data: [4.4, 4.45, 4.52, 4.58, 4.5, 4.62, 4.7, 4.78, 4.85, 4.65, 4.69, 4.75],
        labels: ["WK 12", "WK 13", "WK 14", "WK 15", "WK 16", "WK 17", "WK 18", "WK 19", "WK 20", "WK 21", "WK 22", "WK 23"]
      }
    }
  },

  // 2. Capacity Overview - Operational Dashboard (Sheet 2)
  capacitySheet2: {
    kpis: {
      availableHours: { value: 47300, formatted: "47.3K", wow: 2.1, vsPlan: -1.9, status: "neutral" },
      totalDowntime: { value: 8280, formatted: "8,280", unit: "Hrs", wow: 0.6, vsPlan: -2.0, status: "neutral" },
      capacityUtilisation: { value: 88.1, formatted: "88.1%", wow: 2.3, vsPlan: -1.4, status: "neutral" },
      workforceAvailability: { value: 70.4, formatted: "70.4%", wow: 1.8, vsPlan: -1.4, status: "neutral" },
      productivity: { value: 4.75, formatted: "4.75", unit: "Per Head", wow: 1.6, vsPlan: -2.2, status: "neutral" },
      sicknessPercent: { value: 3.54, formatted: "3.54%", wow: 0.3, vsPlan: 0.4, status: "warning" }
    },

    // Funnel Steps
    funnel: [
      { label: "Gross Hours", hours: 101500, formatted: "101.5K", type: "base" },
      { label: "Holiday", delta: -13500, formatted: "-13.5K", type: "deduction" },
      { label: "Sickness", delta: -3000, formatted: "-3.0K", type: "deduction" },
      { label: "Training", delta: -1400, formatted: "-1.4K", type: "deduction" },
      { label: "Meetings", delta: -2300, formatted: "-2.3K", type: "deduction" },
      { label: "Other", delta: -1800, formatted: "-1.8K", type: "deduction" },
      { label: "Available Hours", hours: 79500, formatted: "79.5K", type: "milestone" },
      { label: "Productive Hours", hours: 70000, formatted: "70.0K", type: "final" }
    ],

    // Downtime by Category
    downtimeCategories: [
      { name: "Sickness", hours: 2997, percent: 35.4, color: "#1e3a8a" },
      { name: "Meetings", hours: 2777, percent: 33.5, color: "#0284c7" },
      { name: "Training", hours: 886, percent: 10.7, color: "#10b981" },
      { name: "Holiday", hours: 804, percent: 9.7, color: "#94a3b8" },
      { name: "Other", hours: 866, percent: 10.7, color: "#64748b" }
    ],
    totalDowntimeHours: 8280,

    // Capacity Risk Heatmap (Variance to Plan %)
    heatmap: {
      weeks: ["WK 23", "WK 24", "WK 25", "WK 26", "WK 27", "WK 28"],
      regions: [
        { name: "Scotland", values: [-18, -14, 0, 8, 16, 20] },
        { name: "North", values: [-12, -6, 4, 14, 20, 22] },
        { name: "Midlands", values: [-8, -2, 6, 12, 18, 19] },
        { name: "South", values: [-20, -10, -2, 6, 15, 18] },
        { name: "Wales", values: [-14, -8, 2, 7, 14, 16] }
      ]
    },

    // Region Efficiency Matrix (Productivity vs Availability Scatter)
    efficiencyMatrix: [
      { name: "Scotland", x: 5.2, y: 76.0, size: 28, color: "#06b6d4" },
      { name: "North", x: 4.6, y: 74.0, size: 40, color: "#0d9488" },
      { name: "Midlands", x: 4.1, y: 68.0, size: 36, color: "#eab308" },
      { name: "South", x: 4.8, y: 66.0, size: 34, color: "#a855f7" },
      { name: "Wales", x: 3.8, y: 62.0, size: 22, color: "#ef4444" }
    ],

    // Bottom KPI strip
    bottomKpis: {
      totalDowntimePct: { value: 33.5, formatted: "33.5%", vsPlan: 2.0, isPositive: true },
      capacityUtilisation: { value: 88.1, formatted: "88.1%", vsPlan: 2.3, isPositive: true },
      workforceAvailability: { value: 70.44, formatted: "70.44%", vsPlan: 0.8, isPositive: true },
      sicknessPercent: { value: 3.54, formatted: "3.54%", vsPlan: 0.3, isPositive: true }
    }
  },

  // 3. Capacity Overview – Comparison (Sheet 3)
  capacitySheet3: {
    title: "CAPACITY OVERVIEW – COMPARISON",
    subtitle: "This Week vs Last Week vs Plan",
    rows: [
      {
        metric: "Gross Hours",
        thisWeekActual: "101.5K",
        thisWeekPlan: "102.8K",
        vsPlan: "-1.3K",
        vsPlanDir: "down",
        lastWeekActual: "103.2K",
        vsLW: "-1.7K",
        vsLWDir: "down",
        varPlanAbs: "-1.3K",
        varPlanPct: "-1.3%",
        varLWAbs: "-1.7K",
        varLWPct: "-1.6%"
      },
      {
        metric: "Downtime Hours",
        thisWeekActual: "8,280",
        thisWeekPlan: "8,450",
        vsPlan: "-170",
        vsPlanDir: "down",
        lastWeekActual: "8,540",
        vsLW: "-260",
        vsLWDir: "down",
        varPlanAbs: "-170",
        varPlanPct: "-2.0%",
        varLWAbs: "-260",
        varLWPct: "-3.0%"
      },
      {
        metric: "Available Hours",
        thisWeekActual: "79.5K",
        thisWeekPlan: "79.6K",
        vsPlan: "-0.1K",
        vsPlanDir: "down",
        lastWeekActual: "79.3K",
        vsLW: "+0.2K",
        vsLWDir: "up",
        varPlanAbs: "-0.1K",
        varPlanPct: "-0.1%",
        varLWAbs: "+0.2K",
        varLWPct: "+0.3%"
      },
      {
        metric: "Productive Hours",
        thisWeekActual: "70.0K",
        thisWeekPlan: "70.8K",
        vsPlan: "-0.8K",
        vsPlanDir: "down",
        lastWeekActual: "69.6K",
        vsLW: "+0.4K",
        vsLWDir: "up",
        varPlanAbs: "-0.8K",
        varPlanPct: "-1.1%",
        varLWAbs: "+0.4K",
        varLWPct: "+0.6%"
      },
      {
        metric: "Workforce Availability %",
        thisWeekActual: "70.4%",
        thisWeekPlan: "71.8%",
        vsPlan: "-1.4 pp",
        vsPlanDir: "down",
        lastWeekActual: "71.1%",
        vsLW: "-0.7 pp",
        vsLWDir: "down",
        varPlanAbs: "-1.4 pp",
        varPlanPct: "",
        varLWAbs: "-0.7 pp",
        varLWPct: ""
      },
      {
        metric: "Productivity (Installs per Head)",
        thisWeekActual: "4.75",
        thisWeekPlan: "4.89",
        vsPlan: "-0.14",
        vsPlanDir: "down",
        lastWeekActual: "4.69",
        vsLW: "+0.06",
        vsLWDir: "up",
        varPlanAbs: "-0.14",
        varPlanPct: "-2.9%",
        varLWAbs: "+0.06",
        varLWPct: "+1.3%"
      },
      {
        metric: "Sickness %",
        thisWeekActual: "3.56%",
        thisWeekPlan: "3.45%",
        vsPlan: "+0.11 pp",
        vsPlanDir: "up",
        lastWeekActual: "3.42%",
        vsLW: "+0.14 pp",
        vsLWDir: "up",
        varPlanAbs: "+0.11 pp",
        varPlanPct: "",
        varLWAbs: "+0.14 pp",
        varLWPct: ""
      }
    ],
    footnote: "Note: pp - Percentage Points"
  },

  // 4. Capacity Detailed Actual vs Forecast Matrix (Sheet 4)
  capacitySheet4: {
    title: "Capacity Overview",
    sheetSubtitle: "Sheet - 4",
    chartTitle: "ES Weekly Actual vs Forecast",
    activeBusinessUnit: "all",
    chartMetric: "grossHrs",

    // Time series for the top line chart
    weeklySeries: {
      weeks: ["25 May 2026", "1 Jun 2026", "8 Jun 2026", "15 Jun 2026", "22 Jun 2026", "29 Jun 2026", "6 Jul 2026", "13 Jul 2026", "20 Jul 2026"],
      reportingIndex: 4, // 22 Jun 2026 is current reporting week in Sheet 4
      metrics: {
        grossHrs: {
          label: "Gross Hrs",
          unit: "Hrs",
          actuals: [22056, 27387, 27346, 27227, 27329, null, null, null, null],
          forecast: [21500, 24800, 24850, 24800, 24859, 24805, 24752, 24698, 24643]
        },
        availableHrs: {
          label: "Available Hrs",
          unit: "Hrs",
          actuals: [13401, 17750, 18450, 17667, 16701, null, null, null, null],
          forecast: [14200, 16100, 16150, 16120, 16137, 16204, 16222, 16064, 15341]
        },
        productiveHours: {
          label: "Productive Hours",
          unit: "Hrs",
          actuals: [6937, 8783, 9061, 8283, 7923, null, null, null, null],
          forecast: [7500, 9600, 9650, 9610, 9621, 9661, 9674, 9516, 9087]
        },
        totalDowntime: {
          label: "Total Downtime",
          unit: "Hrs",
          actuals: [8655, 9537, 8896, 9560, 10627, null, null, null, null],
          forecast: [8500, 8700, 8720, 8710, 8722, 8601, 8530, 8634, 9303]
        },
        productivity: {
          label: "Productivity",
          unit: "",
          actuals: [4.1, 4.0, 3.9, 3.8, 3.8, null, null, null, null],
          forecast: [4.2, 4.7, 4.8, 4.8, 4.8, 4.8, 4.8, 4.7, 4.7]
        },
        utilisation: {
          label: "Utilisation",
          unit: "%",
          actuals: [31.7, 32.3, 33.5, 30.7, 29.4, null, null, null, null],
          forecast: [34.0, 39.5, 40.1, 40.0, 40.2, 40.5, 40.6, 40.0, 38.4]
        },
        sicknessPercent: {
          label: "Sickness %",
          unit: "%",
          actuals: [6.8, 6.7, 6.3, 6.2, 6.2, null, null, null, null],
          forecast: [5.2, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7]
        }
      }
    },

    // Master 11-Week Table Layout and Data Rows
    tableColumns: {
      actualsHeaders: ["18 May 2026", "25 May 2026", "1 Jun 2026", "8 Jun 2026", "15 Jun 2026"],
      currentWeek: {
        weekLabel: "22 Jun 2026",
        subHeaders: ["Forecast", "Actual", "Variance"]
      },
      forecastHeaders: ["29 Jun 2026", "6 Jul 2026", "13 Jul 2026", "20 Jul 2026", "27 Jul 2026"]
    },

    // Complete exact rows as captured from the operational presentation snip
    tableRows: [
      {
        metric: "FTE",
        actuals: ["675", "688", "685", "684", "680"],
        currentForecast: "621",
        currentActual: "683",
        variance: "61",
        varDir: "up",
        varType: "positive",
        futureForecast: ["620", "619", "617", "616", "622"],
        hasSparkbar: false
      },
      {
        metric: "Gross Hrs",
        actuals: ["27,057", "22,056", "27,387", "27,346", "27,227"],
        currentForecast: "24,859",
        currentActual: "27,329",
        variance: "2,469",
        varDir: "up",
        varType: "positive",
        futureForecast: ["24,805", "24,752", "24,698", "24,643", "24,869"],
        hasSparkbar: false
      },
      {
        metric: "Core Hrs",
        actuals: ["27,016", "22,031", "27,385", "27,346", "27,211"],
        currentForecast: "24,859",
        currentActual: "27,311",
        variance: "2,451",
        varDir: "up",
        varType: "positive",
        futureForecast: ["24,805", "24,752", "24,698", "24,643", "24,869"],
        hasSparkbar: false
      },
      {
        metric: "Overtime",
        actuals: ["41", "25", "3", "0", "16"],
        currentForecast: "0",
        currentActual: "18",
        variance: "18",
        varDir: "up",
        varType: "positive",
        futureForecast: ["0", "0", "0", "0", "0"],
        hasSparkbar: false
      },
      {
        metric: "Holiday",
        actuals: ["-2,501", "-4,167", "-2,677", "-2,181", "-2,637"],
        currentForecast: "-3,118",
        currentActual: "-3,302",
        variance: "-184",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-3,185", "-3,237", "-3,360", "-4,057", "-5,087"],
        hasSparkbar: false
      },
      {
        metric: "Holiday %",
        actuals: ["-9.3%", "-18.9%", "-9.8%", "-8.0%", "-9.7%"],
        currentForecast: "-12.5%",
        currentActual: "-12.1%",
        variance: "0.5%",
        varDir: "up",
        varType: "positive",
        futureForecast: ["-12.8%", "-13.1%", "-13.6%", "-16.5%", "-20.5%"],
        hasSparkbar: false
      },
      {
        metric: "Sickness",
        actuals: ["-2,006", "-1,509", "-1,829", "-1,721", "-1,697"],
        currentForecast: "-1,180",
        currentActual: "-1,704",
        variance: "-524",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-1,177", "-1,175", "-1,172", "-1,170", "-1,178"],
        hasSparkbar: false
      },
      {
        metric: "Sickness %",
        actuals: ["-7.4%", "-6.8%", "-6.7%", "-6.3%", "-6.2%"],
        currentForecast: "-4.7%",
        currentActual: "-6.2%",
        variance: "-1.5%",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-4.7%", "-4.7%", "-4.7%", "-4.7%", "-4.7%"],
        hasSparkbar: false
      },
      {
        metric: "Training",
        actuals: ["-1,927", "-852", "-1,284", "-1,356", "-1,451"],
        currentForecast: "-1,415",
        currentActual: "-1,540",
        variance: "-125",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-1,414", "-1,392", "-1,389", "-1,382", "-1,323"],
        hasSparkbar: false
      },
      {
        metric: "Training %",
        actuals: ["-7.1%", "-3.9%", "-4.7%", "-5.0%", "-5.3%"],
        currentForecast: "-5.7%",
        currentActual: "-5.6%",
        variance: "0.1%",
        varDir: "up",
        varType: "positive",
        futureForecast: ["-5.7%", "-5.6%", "-5.6%", "-5.6%", "-5.3%"],
        hasSparkbar: false
      },
      {
        metric: "Meeting",
        actuals: ["-426", "-329", "-947", "-804", "-968"],
        currentForecast: "-649",
        currentActual: "-1,434",
        variance: "-785",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-488", "-383", "-382", "-381", "-380"],
        hasSparkbar: false
      },
      {
        metric: "Meeting %",
        actuals: ["-1.6%", "-1.5%", "-3.5%", "-2.9%", "-3.6%"],
        currentForecast: "-2.6%",
        currentActual: "-5.3%",
        variance: "-2.6%",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-2.0%", "-1.5%", "-1.5%", "-1.5%", "-1.5%"],
        hasSparkbar: false
      },
      {
        metric: "Other",
        actuals: ["-2,549", "-1,799", "-2,801", "-2,835", "-2,807"],
        currentForecast: "-2,351",
        currentActual: "-2,648",
        variance: "-297",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-2,357", "-2,343", "-2,330", "-2,313", "-2,295"],
        hasSparkbar: false
      },
      {
        metric: "Other %",
        actuals: ["-9.4%", "-8.2%", "-10.6%", "-10.4%", "-10.3%"],
        currentForecast: "-9.5%",
        currentActual: "-9.7%",
        variance: "-0.2%",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-9.1%", "-9.5%", "-9.4%", "-9.4%", "-9.2%"],
        hasSparkbar: false
      },
      {
        metric: "Total Downtime",
        actuals: ["-9,410", "-8,655", "-9,537", "-8,896", "-9,560"],
        currentForecast: "-8,722",
        currentActual: "-10,627",
        variance: "-1,905",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-8,601", "-8,530", "-8,634", "-9,303", "-10,262"],
        hasSparkbar: false
      },
      {
        metric: "Total Downtime %",
        actuals: ["-34.8%", "-39.3%", "-35.2%", "-32.5%", "-35.1%"],
        currentForecast: "-35.1%",
        currentActual: "-38.9%",
        variance: "-3.8%",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-34.7%", "-34.5%", "-35.0%", "-37.7%", "-41.3%"],
        hasSparkbar: false
      },
      {
        metric: "TD excl. Hol. & Sick.",
        actuals: ["-4,903", "-2,979", "-5,131", "-4,995", "-5,226"],
        currentForecast: "-4,424",
        currentActual: "-5,622",
        variance: "-1,198",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-4,259", "-4,118", "-4,101", "-4,075", "-3,997"],
        hasSparkbar: false
      },
      {
        metric: "TD excl Hol & Sick %",
        actuals: ["-18.1%", "-13.5%", "-18.7%", "-18.3%", "-19.2%"],
        currentForecast: "-17.8%",
        currentActual: "-20.6%",
        variance: "-2.8%",
        varDir: "down",
        varType: "negative",
        futureForecast: ["-17.2%", "-16.6%", "-16.6%", "-16.5%", "-16.1%"],
        hasSparkbar: false
      },
      {
        metric: "Available Hrs",
        actuals: ["17,647", "13,401", "17,750", "18,450", "17,667"],
        currentForecast: "16,137",
        currentActual: "16,701",
        variance: "564",
        varDir: "up",
        varType: "positive",
        futureForecast: ["16,204", "16,222", "16,064", "15,341", "14,607"],
        hasSparkbar: false
      },
      {
        metric: "Available Hrs %",
        actuals: ["65.3%", "60.8%", "64.8%", "67.5%", "64.9%"],
        currentForecast: "64.9%",
        currentActual: "61.2%",
        variance: "-3.8%",
        varDir: "down",
        varType: "negative",
        futureForecast: ["65.3%", "65.5%", "65.0%", "62.3%", "58.7%"],
        hasSparkbar: false
      },
      {
        metric: "Workload Forecast",
        actuals: ["8,826", "6,937", "8,782", "9,061", "8,283"],
        currentForecast: "9,930",
        currentActual: "7,923",
        variance: "-1,007",
        varDir: "down",
        varType: "negative",
        futureForecast: ["8,872", "8,894", "8,782", "8,880", "8,529"],
        hasSparkbar: false
      },
      {
        metric: "Productivity",
        actuals: ["4.0", "4.1", "4.0", "3.9", "3.8"],
        currentForecast: "4.8",
        currentActual: "3.8",
        variance: "-0.97",
        varDir: "down",
        varType: "negative",
        futureForecast: ["4.8", "4.8", "4.7", "4.7", "4.8"],
        hasSparkbar: false
      },
      {
        metric: "Productive Hours",
        actuals: ["8,826", "6,937", "8,783", "9,061", "8,283"],
        currentForecast: "9,621",
        currentActual: "7,923",
        variance: "-1,698",
        varDir: "down",
        varType: "negative",
        futureForecast: ["9,661", "9,674", "9,516", "9,087", "8,689"],
        hasSparkbar: false
      },
      {
        metric: "SPs",
        actuals: ["46", "65", "56", "87", "74"],
        currentForecast: "375",
        currentActual: "99",
        variance: "-276",
        varDir: "down",
        varType: "negative",
        futureForecast: ["375", "375", "375", "375", "375"],
        hasSparkbar: false
      },
      {
        metric: "Prod Hours inc SPs",
        actuals: ["8,872", "7,001", "8,838", "9,149", "8,356"],
        currentForecast: "9,996",
        currentActual: "8,023",
        variance: "-1,974",
        varDir: "down",
        varType: "negative",
        futureForecast: ["10,036", "10,048", "9,890", "9,461", "9,064"],
        hasSparkbar: false
      },
      {
        metric: "Utilisation",
        actuals: ["32.8%", "31.7%", "32.3%", "33.5%", "30.7%"],
        currentForecast: "40.2%",
        currentActual: "29.4%",
        variance: "-10.9%",
        varDir: "down",
        varType: "negative",
        futureForecast: ["40.5%", "40.6%", "40.0%", "38.4%", "36.4%"],
        hasSparkbar: true
      }
    ]
  },

  // 5. Regional Breakdown Data (Used for dynamic filtering across all views)
  regionalData: {
    scotland: {
      multiplier: 0.16,
      name: "Scotland",
      kpis: {
        installs: { value: 402, formatted: "402", wow: 6.8, vsPlan: -3.8 },
        sales: { value: 0.63, formatted: "£0.63M", wow: 5.9, vsPlan: -2.9 },
        leads: { value: 2340, formatted: "2.34K", wow: -25.4, vsPlan: -26.1 },
        activeHeads: { value: 317, formatted: "317", wow: -2.1, vsPlan: -2.4 },
        availableHours: { value: 7570, formatted: "7.57K", wow: 2.3, vsPlan: 2.0 },
        productivity: { value: 5.2, formatted: "5.20", wow: 2.1, vsPlan: -1.8 },
        totalDowntime: { value: 1280, formatted: "1,280", wow: 0.4, vsPlan: -2.2 },
        capacityUtilisation: { value: 89.4, formatted: "89.4%", wow: 2.5, vsPlan: -1.1 },
        workforceAvailability: { value: 76.0, formatted: "76.0%", wow: 2.0, vsPlan: 1.2 },
        sicknessPercent: { value: 3.20, formatted: "3.20%", wow: 0.2, vsPlan: 0.2 }
      },
      funnel: [
        { label: "Gross Hours", hours: 16240, formatted: "16.2K" },
        { label: "Holiday", delta: -2160, formatted: "-2.16K" },
        { label: "Sickness", delta: -480, formatted: "-480" },
        { label: "Training", delta: -224, formatted: "-224" },
        { label: "Meetings", delta: -368, formatted: "-368" },
        { label: "Other", delta: -288, formatted: "-288" },
        { label: "Available Hours", hours: 12720, formatted: "12.7K" },
        { label: "Productive Hours", hours: 11200, formatted: "11.2K" }
      ],
      downtimeCategories: [
        { name: "Sickness", hours: 480, percent: 37.5, color: "#1e3a8a" },
        { name: "Meetings", hours: 416, percent: 32.5, color: "#0284c7" },
        { name: "Training", hours: 138, percent: 10.8, color: "#10b981" },
        { name: "Holiday", hours: 115, percent: 9.0, color: "#94a3b8" },
        { name: "Other", hours: 131, percent: 10.2, color: "#64748b" }
      ]
    },

    north: {
      multiplier: 0.28,
      name: "North",
      kpis: {
        installs: { value: 703, formatted: "703", wow: 7.2, vsPlan: -4.0 },
        sales: { value: 1.10, formatted: "£1.10M", wow: 6.5, vsPlan: -3.0 },
        leads: { value: 4100, formatted: "4.10K", wow: -27.2, vsPlan: -27.5 },
        activeHeads: { value: 554, formatted: "554", wow: -2.8, vsPlan: -2.9 },
        availableHours: { value: 13240, formatted: "13.2K", wow: 2.0, vsPlan: 1.8 },
        productivity: { value: 4.6, formatted: "4.60", wow: 1.5, vsPlan: -2.3 },
        totalDowntime: { value: 2320, formatted: "2,320", wow: 0.7, vsPlan: -1.9 },
        capacityUtilisation: { value: 88.0, formatted: "88.0%", wow: 2.2, vsPlan: -1.5 },
        workforceAvailability: { value: 74.0, formatted: "74.0%", wow: 1.7, vsPlan: -1.5 },
        sicknessPercent: { value: 3.50, formatted: "3.50%", wow: 0.3, vsPlan: 0.4 }
      },
      funnel: [
        { label: "Gross Hours", hours: 28420, formatted: "28.4K" },
        { label: "Holiday", delta: -3780, formatted: "-3.78K" },
        { label: "Sickness", delta: -840, formatted: "-840" },
        { label: "Training", delta: -392, formatted: "-392" },
        { label: "Meetings", delta: -644, formatted: "-644" },
        { label: "Other", delta: -504, formatted: "-504" },
        { label: "Available Hours", hours: 22260, formatted: "22.3K" },
        { label: "Productive Hours", hours: 19600, formatted: "19.6K" }
      ],
      downtimeCategories: [
        { name: "Sickness", hours: 839, percent: 35.2, color: "#1e3a8a" },
        { name: "Meetings", hours: 777, percent: 33.5, color: "#0284c7" },
        { name: "Training", hours: 248, percent: 10.7, color: "#10b981" },
        { name: "Holiday", hours: 225, percent: 9.7, color: "#94a3b8" },
        { name: "Other", hours: 242, percent: 10.4, color: "#64748b" }
      ]
    },

    midlands: {
      multiplier: 0.24,
      name: "Midlands",
      kpis: {
        installs: { value: 602, formatted: "602", wow: 7.1, vsPlan: -4.3 },
        sales: { value: 0.95, formatted: "£0.95M", wow: 6.2, vsPlan: -3.2 },
        leads: { value: 3516, formatted: "3.52K", wow: -26.8, vsPlan: -26.9 },
        activeHeads: { value: 475, formatted: "475", wow: -2.6, vsPlan: -2.6 },
        availableHours: { value: 11350, formatted: "11.4K", wow: 2.2, vsPlan: 1.9 },
        productivity: { value: 4.1, formatted: "4.10", wow: 1.6, vsPlan: -2.1 },
        totalDowntime: { value: 1980, formatted: "1,980", wow: 0.6, vsPlan: -2.1 },
        capacityUtilisation: { value: 87.5, formatted: "87.5%", wow: 2.1, vsPlan: -1.6 },
        workforceAvailability: { value: 68.0, formatted: "68.0%", wow: 1.6, vsPlan: -1.6 },
        sicknessPercent: { value: 3.65, formatted: "3.65%", wow: 0.35, vsPlan: 0.45 }
      },
      funnel: [
        { label: "Gross Hours", hours: 24360, formatted: "24.4K" },
        { label: "Holiday", delta: -3240, formatted: "-3.24K" },
        { label: "Sickness", delta: -720, formatted: "-720" },
        { label: "Training", delta: -336, formatted: "-336" },
        { label: "Meetings", delta: -552, formatted: "-552" },
        { label: "Other", delta: -432, formatted: "-432" },
        { label: "Available Hours", hours: 19080, formatted: "19.1K" },
        { label: "Productive Hours", hours: 16800, formatted: "16.8K" }
      ],
      downtimeCategories: [
        { name: "Sickness", hours: 719, percent: 36.3, color: "#1e3a8a" },
        { name: "Meetings", hours: 666, percent: 33.6, color: "#0284c7" },
        { name: "Training", hours: 213, percent: 10.8, color: "#10b981" },
        { name: "Holiday", hours: 193, percent: 9.7, color: "#94a3b8" },
        { name: "Other", hours: 208, percent: 10.5, color: "#64748b" }
      ]
    },

    south: {
      multiplier: 0.22,
      name: "South",
      kpis: {
        installs: { value: 552, formatted: "552", wow: 6.9, vsPlan: -4.5 },
        sales: { value: 0.87, formatted: "£0.87M", wow: 6.4, vsPlan: -3.3 },
        leads: { value: 3223, formatted: "3.22K", wow: -27.5, vsPlan: -27.2 },
        activeHeads: { value: 436, formatted: "436", wow: -2.9, vsPlan: -2.8 },
        availableHours: { value: 10410, formatted: "10.4K", wow: 2.1, vsPlan: 1.8 },
        productivity: { value: 4.8, formatted: "4.80", wow: 1.7, vsPlan: -2.0 },
        totalDowntime: { value: 1820, formatted: "1,820", wow: 0.5, vsPlan: -2.0 },
        capacityUtilisation: { value: 88.6, formatted: "88.6%", wow: 2.4, vsPlan: -1.3 },
        workforceAvailability: { value: 66.0, formatted: "66.0%", wow: 1.9, vsPlan: -1.2 },
        sicknessPercent: { value: 3.48, formatted: "3.48%", wow: 0.28, vsPlan: 0.38 }
      },
      funnel: [
        { label: "Gross Hours", hours: 22330, formatted: "22.3K" },
        { label: "Holiday", delta: -2970, formatted: "-2.97K" },
        { label: "Sickness", delta: -660, formatted: "-660" },
        { label: "Training", delta: -308, formatted: "-308" },
        { label: "Meetings", delta: -506, formatted: "-506" },
        { label: "Other", delta: -396, formatted: "-396" },
        { label: "Available Hours", hours: 17490, formatted: "17.5K" },
        { label: "Productive Hours", hours: 15400, formatted: "15.4K" }
      ],
      downtimeCategories: [
        { name: "Sickness", hours: 659, percent: 36.2, color: "#1e3a8a" },
        { name: "Meetings", hours: 611, percent: 33.6, color: "#0284c7" },
        { name: "Training", hours: 195, percent: 10.7, color: "#10b981" },
        { name: "Holiday", hours: 177, percent: 9.7, color: "#94a3b8" },
        { name: "Other", hours: 190, percent: 10.4, color: "#64748b" }
      ]
    },

    wales: {
      multiplier: 0.10,
      name: "Wales",
      kpis: {
        installs: { value: 251, formatted: "251", wow: 6.5, vsPlan: -4.8 },
        sales: { value: 0.39, formatted: "£0.39M", wow: 5.8, vsPlan: -3.5 },
        leads: { value: 1465, formatted: "1.47K", wow: -28.1, vsPlan: -28.0 },
        activeHeads: { value: 198, formatted: "198", wow: -3.0, vsPlan: -3.1 },
        availableHours: { value: 4730, formatted: "4.73K", wow: 1.9, vsPlan: 1.7 },
        productivity: { value: 3.8, formatted: "3.80", wow: 1.4, vsPlan: -2.5 },
        totalDowntime: { value: 880, formatted: "880", wow: 0.8, vsPlan: -1.7 },
        capacityUtilisation: { value: 86.8, formatted: "86.8%", wow: 2.0, vsPlan: -1.8 },
        workforceAvailability: { value: 62.0, formatted: "62.0%", wow: 1.5, vsPlan: -1.8 },
        sicknessPercent: { value: 3.80, formatted: "3.80%", wow: 0.4, vsPlan: 0.5 }
      },
      funnel: [
        { label: "Gross Hours", hours: 10150, formatted: "10.2K" },
        { label: "Holiday", delta: -1350, formatted: "-1.35K" },
        { label: "Sickness", delta: -300, formatted: "-300" },
        { label: "Training", delta: -140, formatted: "-140" },
        { label: "Meetings", delta: -230, formatted: "-230" },
        { label: "Other", delta: -180, formatted: "-180" },
        { label: "Available Hours", hours: 7950, formatted: "7.95K" },
        { label: "Productive Hours", hours: 7000, formatted: "7.00K" }
      ],
      downtimeCategories: [
        { name: "Sickness", hours: 300, percent: 34.1, color: "#1e3a8a" },
        { name: "Meetings", hours: 297, percent: 33.8, color: "#0284c7" },
        { name: "Training", hours: 95, percent: 10.8, color: "#10b981" },
        { name: "Holiday", hours: 86, percent: 9.8, color: "#94a3b8" },
        { name: "Other", hours: 93, percent: 10.6, color: "#64748b" }
      ]
    }
  },

  // 6. Additional Complementary Views (Demand, Geographic Hub, Accuracy, Forecast Lead/Lag)
  demandView: {
    backlogWeeks: 2.8,
    inboundDemand: 2780,
    completionRate: "94.2%",
    unmetDemandHours: 420,
    demandBySegment: [
      { segment: "Boiler Installation", volume: 1420, capacityRatio: 1.02 },
      { segment: "Heat Pumps & Renewables", volume: 680, capacityRatio: 0.91 },
      { segment: "Electrical & EV Charger", volume: 410, capacityRatio: 0.88 },
      { segment: "Maintenance & Inspection", volume: 270, capacityRatio: 1.15 }
    ]
  },

  accuracyView: {
    overallMape: "4.8%",
    forecastBias: "+1.2%",
    leadTimeWeeks: 4,
    historicalAccuracy: [
      { week: "WK 18", forecast: 2750, actual: 2600, errorPct: 5.5 },
      { week: "WK 19", forecast: 2620, actual: 2450, errorPct: 6.5 },
      { week: "WK 20", forecast: 2580, actual: 2420, errorPct: 6.2 },
      { week: "WK 21", forecast: 2520, actual: 2460, errorPct: 2.4 },
      { week: "WK 22", forecast: 2480, actual: 2345, errorPct: 5.4 },
      { week: "WK 23", forecast: 2415, actual: 2510, errorPct: 3.9 }
    ]
  }
};
