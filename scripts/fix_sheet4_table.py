with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

old_table = """  renderSheet4Table() {
    const tableContainer = document.getElementById("sheet4-matrix-table-container");
    if (!tableContainer) return;

    const data = DASHBOARD_DATA.capacitySheet4;
    const bu = this.state.selectedBusinessUnit;
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = this.getGlobalMultiplier();

    let buMult = 1.0;
    if (bu === "hec") buMult = 0.58;
    else if (bu === "kac") buMult = 0.28;
    else if (bu === "nzev") buMult = 0.14;

    const mult = geoMult * buMult;
    const isScaled = mult !== 1.0;"""

new_table = """  renderSheet4Table() {
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
    const isScaled = actMult !== 1.0 || fcMult !== 1.0;"""

js = js.replace(old_table, new_table)

old_act = """        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * mult;
          displayVal = Math.round(num).toLocaleString();
        }"""
new_act = """        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * actMult;
          displayVal = Math.round(num).toLocaleString();
        }"""
js = js.replace(old_act, new_act)

old_cur = """      if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
        const numFc = parseInt(curForecast.replace(/,/g, "")) * mult;
        const numAct = parseInt(curActual.replace(/,/g, "")) * mult;
        curForecast = Math.round(numFc).toLocaleString();
        curActual = Math.round(numAct).toLocaleString();
        const diff = Math.round(numAct - numFc);
        variance = diff.toLocaleString();
      }"""
new_cur = """      if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
        const numFc = parseInt(curForecast.replace(/,/g, "")) * fcMult;
        const numAct = parseInt(curActual.replace(/,/g, "")) * actMult;
        curForecast = Math.round(numFc).toLocaleString();
        curActual = Math.round(numAct).toLocaleString();
        const diff = Math.round(numAct - numFc);
        variance = diff.toLocaleString();
      }"""
js = js.replace(old_cur, new_cur)

old_fc = """        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * mult;
          displayVal = Math.round(num).toLocaleString();
        }"""
new_fc = """        if (isScaled && !row.metric.includes("%") && !row.metric.includes("Productivity")) {
          const num = parseInt(val.replace(/,/g, "")) * fcMult;
          displayVal = Math.round(num).toLocaleString();
        }"""
js = js.replace(old_fc, new_fc)

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Updated Sheet 4 table")
