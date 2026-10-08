with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

old_code = """    // Installs Weekly Combo Chart
    let weeklyData = DASHBOARD_DATA.executiveSummary.weeklyInstalls.map(d => ({
      week: d.week,
      actual: Math.round(d.actual * mult),
      plan: Math.round(d.plan * mult),
      variance: Math.round(d.variance * mult)
    }));"""

new_code = """    // Installs Weekly Combo Chart
    let weeklyData = DASHBOARD_DATA.executiveSummary.weeklyInstalls.map(d => ({
      week: d.week,
      actual: d.actual === null ? null : Math.round(d.actual * mult),
      plan: d.plan === null ? null : Math.round(d.plan * mult),
      variance: d.variance === null ? null : Math.round(d.variance * mult)
    }));"""

if old_code in js:
    js = js.replace(old_code, new_code)
    with open("js/app.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("Fixed app.js")
else:
    print("Could not find exact text in app.js, check manually")
