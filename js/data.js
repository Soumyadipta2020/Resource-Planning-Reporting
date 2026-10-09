/**
 * Operational Planning & Capacity Management Data Store
 * Hardcoded dummy dataset modeling enterprise capacity, demand, and workforce performance.
 * Fully aligned across all executive views, capacity sheets, and regional dimensions.
 */

const DASHBOARD_DATA = {
  metadata: {
    lastUpdated: "2026-06-01T08:30:00Z",
    reportingWeeks: [
      { id: "wk36", label: "31 Aug (WK 36)", date: "31 Aug", weekNum: 36 },
      { id: "wk37", label: "7 Sep (WK 37)", date: "7 Sep", weekNum: 37 },
      { id: "wk38", label: "14 Sep (WK 38)", date: "14 Sep", weekNum: 38, isDefault: true },
      { id: "wk39", label: "21 Sep (WK 39)", date: "21 Sep", weekNum: 39 },
      { id: "wk40", label: "28 Sep (WK 40)", date: "28 Sep", weekNum: 40 },
      { id: "wk41", label: "5 Oct (WK 41)", date: "5 Oct", weekNum: 41 },
      { id: "wk42", label: "12 Oct (WK 42)", date: "12 Oct", weekNum: 42 },
      { id: "wk43", label: "19 Oct (WK 43)", date: "19 Oct", weekNum: 43 },
      { id: "wk44", label: "26 Oct (WK 44)", date: "26 Oct", weekNum: 44 },
      { id: "wk45", label: "2 Nov (WK 45)", date: "2 Nov", weekNum: 45 },
      { id: "wk46", label: "9 Nov (WK 46)", date: "9 Nov", weekNum: 46 }
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
      { id: "gff2_2026", name: "GFF2 2026" }
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
    // Aligned national figures for WK 38
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
      { week: "WK 29", actual: 2260, plan: 2410, variance: -150 },
      { week: "WK 30", actual: 2320, plan: 2380, variance: -60 },
      { week: "WK 31", actual: 2480, plan: 2450, variance: 30 },
      { week: "WK 32", actual: 2550, plan: 2500, variance: 50 },
      { week: "WK 33", actual: 2600, plan: 2750, variance: -150 },
      { week: "WK 34", actual: 2450, plan: 2620, variance: -170 },
      { week: "WK 35", actual: 2420, plan: 2580, variance: -160 },
      { week: "WK 36", actual: 2460, plan: 2520, variance: -60 },
      { week: "WK 37", actual: 2345, plan: 2480, variance: -135 },
      { week: "WK 38", actual: 2510, plan: 2415, variance: 95 },
      { week: "WK 39", actual: null, plan: 2450, variance: null },
      { week: "WK 40", actual: null, plan: 2480, variance: null },
      { week: "WK 41", actual: null, plan: 2500, variance: null },
      { week: "WK 42", actual: null, plan: 2550, variance: null },
      { week: "WK 43", actual: null, plan: 2600, variance: null },
      { week: "WK 44", actual: null, plan: 2620, variance: null }
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
        labels: ["WK 27", "WK 28", "WK 29", "WK 30", "WK 31", "WK 32", "WK 33", "WK 34", "WK 35", "WK 36", "WK 37", "WK 38"]
      },
      sales: {
        change: "+6.3% WoW",
        positive: true,
        data: [3.2, 3.3, 3.4, 3.5, 3.45, 3.55, 3.75, 3.82, 3.90, 3.70, 3.65, 3.94],
        labels: ["WK 27", "WK 28", "WK 29", "WK 30", "WK 31", "WK 32", "WK 33", "WK 34", "WK 35", "WK 36", "WK 37", "WK 38"]
      },
      leads: {
        change: "-27.0% WoW",
        positive: false,
        data: [19.8, 19.5, 18.2, 18.9, 17.5, 18.1, 16.8, 17.2, 16.0, 15.2, 19.8, 14.65],
        labels: ["WK 27", "WK 28", "WK 29", "WK 30", "WK 31", "WK 32", "WK 33", "WK 34", "WK 35", "WK 36", "WK 37", "WK 38"]
      },
      activeHeads: {
        change: "-2.7% WoW",
        positive: false,
        data: [2050, 2040, 2045, 2030, 2025, 2035, 2020, 2015, 2010, 2005, 2035, 1980],
        labels: ["WK 27", "WK 28", "WK 29", "WK 30", "WK 31", "WK 32", "WK 33", "WK 34", "WK 35", "WK 36", "WK 37", "WK 38"]
      },
      availableHours: {
        change: "+2.1% WoW",
        positive: true,
        data: [45.2, 45.8, 46.0, 46.4, 46.1, 46.7, 47.0, 47.5, 47.8, 46.9, 46.3, 47.3],
        labels: ["WK 27", "WK 28", "WK 29", "WK 30", "WK 31", "WK 32", "WK 33", "WK 34", "WK 35", "WK 36", "WK 37", "WK 38"]
      },
      productivity: {
        change: "+1.6% WoW",
        positive: true,
        data: [4.4, 4.45, 4.52, 4.58, 4.5, 4.62, 4.7, 4.78, 4.85, 4.65, 4.69, 4.75],
        labels: ["WK 27", "WK 28", "WK 29", "WK 30", "WK 31", "WK 32", "WK 33", "WK 34", "WK 35", "WK 36", "WK 37", "WK 38"]
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
      weeks: ["WK 38", "WK 39", "WK 40", "WK 41", "WK 42", "WK 43"],
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
        varPlanPct: "-1.9%",
        varLWAbs: "-0.7 pp",
        varLWPct: "-1.0%"
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
        varPlanPct: "+3.2%",
        varLWAbs: "+0.14 pp",
        varLWPct: "+4.1%"
      }
    ],
    footnote: "Note: pp - Percentage Points"
  },

  // 4. Capacity Detailed Actual vs Forecast Matrix
  capacitySheet4: {
    title: "Capacity Overview",
    viewName: "Forecast vs Actuals Matrix",
    chartTitle: "ES Weekly Actual vs Forecast",
    activeBusinessUnit: "all",
    chartMetric: "grossHrs",

    // Time series for the top line chart
    weeklySeries: {
      weeks: ["7 Sep", "14 Sep", "21 Sep", "28 Sep", "5 Oct", "12 Oct", "19 Oct", "26 Oct", "2 Nov"],
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
        actualsHeaders: ["17 Aug", "24 Aug", "31 Aug", "07 Sep", "14 Sep"],
        currentWeek: {
          weekLabel: "21 Sep",
          subHeaders: ["Actual", "Forecast", "Variance"]
        },
        forecastHeaders: ["28 Sep", "05 Oct", "12 Oct", "19 Oct", "26 Oct"]
      },
      tableRows: [
        { metric: "DL Headcount", actuals: ["691", "692", "692", "691", "689"], currentActual: "690", currentForecast: "698", variance: "8", varDir: "down", varType: "negative", futureForecast: ["697", "708", "708", "708", "708"], hasSparkbar: false },
        { metric: "DL Gross Hours", actuals: ["25,696", "25,820", "26,110", "25,390", "25,689"], currentActual: "25,762", currentForecast: "26,927", variance: "-1,165", varDir: "down", varType: "negative", futureForecast: ["27,271", "27,326", "27,326", "27,326", "27,326"], hasSparkbar: false },
        { metric: "DL Holiday", actuals: ["5,740", "6,723", "3,178", "2,776", "3,399"], currentActual: "3,220", currentForecast: "3,150", variance: "70", varDir: "down", varType: "negative", futureForecast: ["2,616", "2,444", "2,444", "2,444", "2,444"], hasSparkbar: false },
        { metric: "DL Holiday %", actuals: ["22.3%", "26.0%", "12.2%", "10.9%", "13.2%"], currentActual: "12.5%", currentForecast: "11.7%", variance: "0.8%", varDir: "down", varType: "negative", futureForecast: ["9.6%", "8.9%", "8.9%", "8.9%", "8.9%"], hasSparkbar: false },
        { metric: "DL Sickness", actuals: ["1,539", "1,663", "1,225", "1,547", "1,338"], currentActual: "1,382", currentForecast: "1,141", variance: "241", varDir: "down", varType: "negative", futureForecast: ["1,254", "1,258", "1,258", "1,258", "1,258"], hasSparkbar: false },
        { metric: "DL Sickness %", actuals: ["6.0%", "6.4%", "4.7%", "6.1%", "5.2%"], currentActual: "5.4%", currentForecast: "4.2%", variance: "1.1%", varDir: "down", varType: "negative", futureForecast: ["4.6%", "4.6%", "4.6%", "4.6%", "4.6%"], hasSparkbar: false },
        { metric: "DL Downtime excl. Hol & Sick", actuals: ["2,932", "2,568", "7,246", "2,927", "2,586"], currentActual: "4,005", currentForecast: "3,759", variance: "246", varDir: "down", varType: "negative", futureForecast: ["5,009", "3,814", "3,814", "3,814", "3,814"], hasSparkbar: false },
        { metric: "DL Downtime % excl. Hol & Sick", actuals: ["11.4%", "9.9%", "27.8%", "11.5%", "10.1%"], currentActual: "15.5%", currentForecast: "14.0%", variance: "1.5%", varDir: "down", varType: "negative", futureForecast: ["18.4%", "14.0%", "14.0%", "14.0%", "14.0%"], hasSparkbar: false },
        { metric: "Total DL Downtime", actuals: ["10,211", "10,954", "11,650", "7,250", "7,324"], currentActual: "8,607", currentForecast: "8,051", variance: "556", varDir: "down", varType: "negative", futureForecast: ["8,879", "7,515", "7,515", "7,515", "7,515"], hasSparkbar: false },
        { metric: "Total DL Downtime %", actuals: ["39.7%", "42.4%", "44.6%", "28.6%", "28.5%"], currentActual: "33.4%", currentForecast: "29.9%", variance: "3.5%", varDir: "down", varType: "negative", futureForecast: ["32.6%", "27.5%", "27.5%", "27.5%", "27.5%"], hasSparkbar: false },
        { metric: "DL Available Hours", actuals: ["15,485", "14,866", "14,460", "18,140", "18,365"], currentActual: "17,155", currentForecast: "18,877", variance: "-1,722", varDir: "down", varType: "negative", futureForecast: ["18,392", "19,810", "19,810", "19,810", "19,810"], hasSparkbar: false },
        { metric: "DL Availability %", actuals: ["60.3%", "57.6%", "55.4%", "71.4%", "71.5%"], currentActual: "66.6%", currentForecast: "70.1%", variance: "-3.5%", varDir: "down", varType: "negative", futureForecast: ["67.4%", "72.5%", "72.5%", "72.5%", "72.5%"], hasSparkbar: false },
        { metric: "DL Utilisation %", actuals: ["53.7%", "51.4%", "46.0%", "63.0%", "63.0%"], currentActual: "59.4%", currentForecast: "65.7%", variance: "-6.3%", varDir: "down", varType: "negative", futureForecast: ["63.2%", "68.0%", "68.0%", "68.0%", "68.0%"], hasSparkbar: false },
        { metric: "DL Gaps", actuals: ["1,691", "1,607", "2,450", "2,141", "2,194"], currentActual: "1,852", currentForecast: "1,191", variance: "661", varDir: "down", varType: "negative", futureForecast: ["1,147", "1,231", "1,231", "1,231", "1,231"], hasSparkbar: false },
        { metric: "DL Gaps %", actuals: ["6.6%", "6.2%", "9.4%", "8.4%", "8.5%"], currentActual: "7.2%", currentForecast: "4.4%", variance: "2.8%", varDir: "down", varType: "negative", futureForecast: ["4.2%", "4.5%", "4.5%", "4.5%", "4.5%"], hasSparkbar: false },
        { metric: "DL Productivity", actuals: ["1.9", "1.9", "1.9", "1.9", "1.9"], currentActual: "2.0", currentForecast: "2.2", variance: "-0.2", varDir: "down", varType: "negative", futureForecast: ["2.3", "2.4", "2.4", "2.4", "2.4"], hasSparkbar: false },
        { metric: "DL Productive Hrs", actuals: ["13,794", "13,259", "12,010", "15,999", "16,171"], currentActual: "15,303", currentForecast: "17,686", variance: "-2,383", varDir: "down", varType: "negative", futureForecast: ["17,245", "18,579", "18,579", "18,579", "18,579"], hasSparkbar: false },
        { metric: "DL Installs", actuals: ["781", "775", "726", "920", "944"], currentActual: "897", currentForecast: "1,073", variance: "-176", varDir: "down", varType: "negative", futureForecast: ["1,101", "1,217", "1,217", "1,217", "1,217"], hasSparkbar: false },
        { metric: "Total Installs", actuals: ["1,450", "1,460", "1,247", "1,696", "1,734"], currentActual: "1,689", currentForecast: "1,988", variance: "-299", varDir: "down", varType: "negative", futureForecast: ["2,160", "2,276", "2,276", "2,276", "2,276"], hasSparkbar: false },
        { metric: "DL Planning Efficeincy %", actuals: ["89.1%", "89.2%", "83.1%", "88.2%", "88.1%"], currentActual: "89.2%", currentForecast: "93.7%", variance: "-4.5%", varDir: "down", varType: "negative", futureForecast: ["93.8%", "93.8%", "93.8%", "93.8%", "93.8%"], hasSparkbar: false }
      ]
  },

  // 5. Regional Breakdown Data (Used for dynamic filtering across all views)
  capacitySheet5: {
    title: "Capacity Waterfall",
    waterfallData: [
      { label: "Base", value: 17686, type: "total" },
      { label: "DL Gross Hours", value: -1166, type: "down" },
      { label: "DL Holiday", value: -70, type: "down" },
      { label: "DL Sickness", value: -241, type: "down" },
      { label: "DL Downtime", value: -246, type: "down" },
      { label: "Prod Impact", value: -661, type: "down" },
      { label: "Final", value: 15303, type: "total" }
    ],
    tableColumns: [
      "Gross Hrs", "Holiday", "Holiday %", "Sickness", "Sickness %", "Training", "Training %", "Meeting", "Meeting %", "Other", "Other %", "Total Downtime", "Total Downtime %", "Available Hours", "Prod", "Productive Hrs"
    ],
    tableRows: [
      {
        rowLabel: "GFF1 2026",
        values: ["26,927", "3,150", "11.7%", "1,141", "4.2%", "932", "3.5%", "822", "3.1%", "1,422", "5.3%", "8,051", "29.9%", "18,877", "2.19", "17,686"]
      },
      {
        rowLabel: "Actuals",
        values: ["25,762", "3,220", "11.7%", "1,382", "5.4%", "352", "1.4%", "2,202", "8.5%", "1,023", "4.0%", "8,607", "33.4%", "17,155", "1.95", "15,303"]
      },
      {
        rowLabel: "Variance",
        values: [
          { val: "-1166", dir: "down", color: "text-red-700" },
          { val: "-70", dir: "down", color: "text-red-700" },
          { val: "-0.8%", dir: "down", color: "text-red-700" },
          { val: "-241", dir: "down", color: "text-red-700" },
          { val: "-1.1%", dir: "down", color: "text-red-700" },
          { val: "580", dir: "up", color: "text-emerald-700" },
          { val: "2.1%", dir: "up", color: "text-emerald-700" },
          { val: "-1381", dir: "down", color: "text-red-700" },
          { val: "-5.5%", dir: "down", color: "text-red-700" },
          { val: "399", dir: "up", color: "text-emerald-700" },
          { val: "1.3%", dir: "up", color: "text-emerald-700" },
          { val: "-556", dir: "down", color: "text-red-700" },
          { val: "-3.5%", dir: "down", color: "text-red-700" },
          { val: "-1722", dir: "down", color: "text-red-700" },
          { val: "-0.24", dir: "down", color: "text-red-700" },
          { val: "-2383", dir: "down", color: "text-red-700" }
        ]
      }
    ]
  },

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
      { week: "WK 33", forecast: 2750, actual: 2600, errorPct: 5.5 },
      { week: "WK 34", forecast: 2620, actual: 2450, errorPct: 6.5 },
      { week: "WK 35", forecast: 2580, actual: 2420, errorPct: 6.2 },
      { week: "WK 36", forecast: 2520, actual: 2460, errorPct: 2.4 },
      { week: "WK 37", forecast: 2480, actual: 2345, errorPct: 5.4 },
      { week: "WK 38", forecast: 2415, actual: 2510, errorPct: 3.9 }
    ]
  }
};
