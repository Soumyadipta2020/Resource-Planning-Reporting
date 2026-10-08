import re

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# Make the forecast header dynamic
old_code = """<th colspan="5" class="py-2 px-2 bg-slate-500 border-l border-slate-400">Forecast - GFF1 2026</th>"""

new_code = """<th colspan="5" class="py-2 px-2 bg-slate-500 border-l border-slate-400">Forecast - ${this.state.selectedPlan === 'gff2_2026' ? 'GFF2 2026' : 'GFF1 2026'}</th>"""

if old_code in js:
    js = js.replace(old_code, new_code)
    with open("js/app.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("Fixed forecast header in app.js")
else:
    print("Could not find forecast header in app.js, check manually")
