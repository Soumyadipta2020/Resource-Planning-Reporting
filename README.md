# Nexus Resource Planning & Operations Dashboard

An interactive, responsive HTML5/JavaScript executive dashboard and capacity management suite for enterprise workforce planning, operational analytics, and forecast tracking.

---

## 📊 Overview

The **Nexus Resource Planning & Operations Dashboard** is an enterprise-grade reporting and decision-support portal modeled after executive presentation visuals. It provides synchronized operational visibility across high-level executive KPIs, capacity funnels, downtime distributions, regional risk matrices, and multi-week actuals vs. forecast plans.

All views are backed by a structured, aligned dummy dataset defined directly in code (`js/data.js`), enabling dynamic multi-dimensional filtering across geographies, reporting periods, base plans, and service lines.

---

## 🚀 Key Features & Views

### 1. Executive Command Centre (`Executive Summary - Sheet 2`)
- **Top Executive KPIs**: Installs, Sales (£M), Leads, Active Heads, Available Hours, and Productivity per Head with Week-over-Week (WoW) and vs. Plan variance badges.
- **Actual vs Plan Weekly Trend**: Dual-axis bar and dashed line combo chart with positive/negative variance indicators across rolling weeks (WK 14 to WK 23).
- **Variance Analysis (Drivers) Waterfall**: Dynamic step-up and step-down waterfall chart decomposing the gap between Plan (2,415) and Actuals (2,510) across productivity, overtime, holidays, sickness, and training.
- **Continuous 12-Week Trajectories**: Smooth SVG sparklines tracking WoW trends for all six primary performance metrics.

### 2. Capacity Overview Suite

#### • Sheet 2: Operational Dashboard
- **Capacity KPIs**: Available Hours, Total Downtime Hours, Capacity Utilisation %, Workforce Availability %, Productivity, and Sickness %.
- **Tiered Capacity Funnel**: Visual loss breakdown from Gross Hours through deductions (Holiday, Sickness, Training, Meetings, Other) to Available and Productive Hours.
- **Downtime by Category**: High-contrast donut chart paired with an exact hours and percentage distribution table.
- **Capacity Risk Heatmap**: 5-Region × 6-Week variance-to-plan matrix with color-graded risk indicators (surplus to deficit risk).
- **Region Efficiency Matrix**: Interactive 2D scatter matrix mapping Productivity against Availability with quadrant dividers.
- **Operational Health Summary**: Real-time bottom indicator strip.

#### • Sheet 3: Weekly Comparison Matrix
- **Comparative Multi-Metric Grid**: Side-by-side comparison of **This Week (WK 23)**, **Last Week (WK 22)**, and **Plan**, complete with absolute variances and percentage variations.
- **Percentage Points (pp) Precision**: Dedicated formatting for rate-based metrics (Workforce Availability %, Sickness %).

#### • Sheet 4: Forecast vs. Actuals Plan Matrix
- **Service Line / Business Unit Switcher**: Toggle views between `Home (All Units)`, `HEC` (Home Energy Care), `KAC` (Kitchen & Appliance Care), and `NZ (EV)` (Net Zero & Electric Vehicles).
- **ES Weekly Actual vs Forecast Chart**: Multi-metric trend visual with an interactive selector for Gross Hours, Available Hours, Productive Hours, Downtime, Productivity, Utilisation, and Sickness %.
- **Master 11-Week Matrix**: 26-row detailed operational planning table displaying:
  - 5 Historical Actuals Weeks (18 May to 15 Jun)
  - Current Reporting Week with Forecast, Actuals, and Variance arrows (`↑` green / `↓` red)
  - 5 Future Forecast Weeks (29 Jun to 27 Jul)
  - Inline progress sparkbars for Utilisation tracking

### 3. Complementary Hubs
- **Demand & Capacity Dispatch**: Backlog monitoring, weekly inbound bookings, fulfillment rates, and segment-level capacity coverage.
- **Geographic Performance HUB**: Regional rankings, league tables, and productivity benchmarks across Scotland, North, Midlands, South, and Wales.
- **Accuracy Dashboard**: Rolling Mean Absolute Percentage Error (MAPE), forecast bias, and weekly prediction accuracy records.
- **Forecast Performance (Lead / Lag)**: Predictive leading signals matched against operational lagging results.

---

## 🎛️ Synchronized Filter Controls

All sheets and tabs stay aligned through a centralized application state engine (`js/app.js`):
- **Geography Selector**: Switch between `All / National`, `Scotland`, `North`, `Midlands`, `South`, and `Wales`. Regional multipliers adjust all KPIs, funnel steps, donut categories, comparison tables, and forecast sheets in unison.
- **Reporting Week Selector**: Toggle between historical, current, and future operational weeks (`WK 21` through `WK 31`).
- **Base / Plan Selector**: Switch benchmarks between `GFF1 2026`, `Budget 2026`, and `Reforecast Q3 2026`.
- **Business Unit Filter**: Filter Sheet 4 data dynamically by service line.
- **Real-Time Data Refresh**: Trigger animated re-calculations and timestamp updates.
- **Print / PDF Export**: Built-in print media stylesheet for one-click clean PDF and report exports.

---

## 📂 Repository Structure

```
Resource-Planning-Reporting/
│
├── index.html            # Main HTML5 application shell & view containers
├── css/
│   └── styles.css        # Corporate styling, custom scrollbars, print layout
├── js/
│   ├── data.js           # Hardcoded dummy dataset (hierarchical & aligned)
│   ├── charts.js         # Chart.js renderers, custom SVG Waterfall & Funnel
│   └── app.js            # State management, filter sync, DOM updates
├── LICENSE               # GNU General Public License v3.0
└── README.md             # Project documentation
```

---

## ⚡ Quick Start

No compilation, npm installation, or build tools are required. The project runs directly in modern web browsers.

### Option 1: Direct File Open
Simply double-click `index.html` or open it in your browser:
```bash
start index.html
```

### Option 2: Local HTTP Server (Python)
To serve locally with HTTP:
```bash
# Python 3
python -m http.server 8080
```
Then navigate to `http://localhost:8080` in your web browser.

---

## 🛠️ Technology Stack
- **HTML5 & Vanilla ES6+ JavaScript**: Lightweight, dependency-free application logic with reactive state updates.
- **Tailwind CSS (CDN)**: Modern utility-first responsive layout grid.
- **Chart.js (CDN)**: Smooth canvas visualizations for bar/line combo, donut, scatter bubble, and line charts.
- **Custom Vector Graphics (SVG)**: Pixel-precise Waterfall driver chart, tiered Funnel visual, and trend sparklines.
