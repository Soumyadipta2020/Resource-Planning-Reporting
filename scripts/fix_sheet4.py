with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# For renderSheet4Chart
old_chart = """  renderSheet4Chart() {
    const rawSeries = DASHBOARD_DATA.capacitySheet4.weeklySeries;
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = this.getGlobalMultiplier();

    let buMult = 1.0;
    if (this.state.selectedBusinessUnit === "hec") buMult = 0.58;
    else if (this.state.selectedBusinessUnit === "kac") buMult = 0.28;
    else if (this.state.selectedBusinessUnit === "nzev") buMult = 0.14;

    const totalMult = geoMult * buMult;"""

new_chart = """  renderSheet4Chart() {
    const rawSeries = DASHBOARD_DATA.capacitySheet4.weeklySeries;
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const mults = this.getGlobalMultipliers();

    let buMult = 1.0;
    if (this.state.selectedBusinessUnit === "hec") buMult = 0.58;
    else if (this.state.selectedBusinessUnit === "kac") buMult = 0.28;
    else if (this.state.selectedBusinessUnit === "nzev") buMult = 0.14;

    const actualMult = mults.base * buMult;
    const forecastMult = mults.plan * buMult;"""

js = js.replace(old_chart, new_chart)

old_loop = """      series.metrics[key] = {
        label: metric.label,
        unit: metric.unit,
        actuals: metric.actuals.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * scale))),
        forecast: metric.forecast.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * scale)))
      };"""

new_loop = """      const actScale = isPercentOrRatio ? 1.0 : actualMult;
      const fcScale = isPercentOrRatio ? 1.0 : forecastMult;

      series.metrics[key] = {
        label: metric.label,
        unit: metric.unit,
        actuals: metric.actuals.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * actScale))),
        forecast: metric.forecast.map(v => v === null ? null : (isPercentOrRatio ? v : Math.round(v * fcScale)))
      };"""

js = js.replace(old_loop, new_loop)

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Updated Sheet 4 chart")
