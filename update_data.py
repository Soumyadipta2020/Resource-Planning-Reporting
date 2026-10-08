import re

with open('js/data.js', 'r', encoding='utf-8') as f:
    data = f.read()

# Update plans
old_plans = """    plans: [
      { id: "gff1_2026", name: "GFF1 2026", isDefault: true },
      { id: "budget_2026", name: "Budget 2026" },
      { id: "reforecast_q3", name: "Reforecast Q3 2026" }
    ],"""

new_plans = """    plans: [
      { id: "gff1_2026", name: "GFF1 2026 (Starts Mar 2026)", isDefault: true },
      { id: "gff2_2026", name: "GFF2 2026 (Starts Sep 2026)" }
    ],"""
data = data.replace(old_plans, new_plans)

# Update weeklyInstalls
old_weekly = """    weeklyInstalls: [
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
    ],"""

new_weekly = """    weeklyInstalls: [
      { week: "WK 14", actual: 2260, plan: 2410, variance: -150 },
      { week: "WK 15", actual: 2320, plan: 2380, variance: -60 },
      { week: "WK 16", actual: 2480, plan: 2450, variance: 30 },
      { week: "WK 17", actual: 2550, plan: 2500, variance: 50 },
      { week: "WK 18", actual: 2600, plan: 2750, variance: -150 },
      { week: "WK 19", actual: 2450, plan: 2620, variance: -170 },
      { week: "WK 20", actual: 2420, plan: 2580, variance: -160 },
      { week: "WK 21", actual: 2460, plan: 2520, variance: -60 },
      { week: "WK 22", actual: 2345, plan: 2480, variance: -135 },
      { week: "WK 23", actual: 2510, plan: 2415, variance: 95 },
      { week: "WK 24", actual: null, plan: 2450, variance: null },
      { week: "WK 25", actual: null, plan: 2480, variance: null },
      { week: "WK 26", actual: null, plan: 2500, variance: null },
      { week: "WK 27", actual: null, plan: 2550, variance: null },
      { week: "WK 28", actual: null, plan: 2600, variance: null },
      { week: "WK 29", actual: null, plan: 2620, variance: null }
    ],"""
data = data.replace(old_weekly, new_weekly)

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(data)

print('Updated data.js')
