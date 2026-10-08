import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = '''    let planMult = 1.0;
    let isPlanActive = true;
    if (this.state.selectedPlan === "gff2_2026") {
       planMult = 1.15;
       isPlanActive = false; // Historic weeks are before Sep 2026
    }

    let weekMult = 1.0;
    if (this.state.selectedWeek) {
       const match = this.state.selectedWeek.match(/wk(\d+)/);
       if (match) {
           const wkNum = parseInt(match[1]);
           weekMult = 1 + ((wkNum - 38) * 0.015);
       }
    }'''

new_block = '''    let planMult = 1.0;
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
    }'''

content = re.sub(r'    let planMult = 1\.0;[\s\S]*?weekMult = 1 \+ \(\(wkNum - 38\) \* 0\.015\);\n         }\n      }', new_block, content)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
