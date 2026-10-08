with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

old_code = """    let planMult = 1.0;
    if (this.state.selectedPlan === "budget_2026") planMult = 0.95;
    else if (this.state.selectedPlan === "reforecast_q3") planMult = 1.04;"""

new_code = """    let planMult = 1.0;
    if (this.state.selectedPlan === "gff2_2026") planMult = 1.15;"""

if old_code in js:
    js = js.replace(old_code, new_code)
    with open("js/app.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("Fixed app.js plan filter")
else:
    print("Could not find exact text in app.js, check manually")
