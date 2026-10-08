import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# We know the block starts with "let planMult = 1.0;"
# We will use re to match until the end of the block.
match = re.search(r'let planMult = 1\.0;[\s\S]*?weekMult = 1 \+ \(\(wkNum - 38\) \* 0\.015\);\n\s*\}\n\s*\}', content)

if match:
    old_text = match.group(0)
    new_text = '''let planMult = 1.0;
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
    content = content.replace(old_text, new_text)
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Success")
else:
    print("Failed to match")
