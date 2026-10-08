import re

with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace reportingWeeks fully
reporting_weeks = '''reportingWeeks: [
      { id: "wk36", label: "31 Aug 2026 (WK 36)", date: "31 Aug 2026", weekNum: 36 },
      { id: "wk37", label: "7 Sep 2026 (WK 37)", date: "7 Sep 2026", weekNum: 37 },
      { id: "wk38", label: "14 Sep 2026 (WK 38)", date: "14 Sep 2026", weekNum: 38, isDefault: true },
      { id: "wk39", label: "21 Sep 2026 (WK 39)", date: "21 Sep 2026", weekNum: 39 },
      { id: "wk40", label: "28 Sep 2026 (WK 40)", date: "28 Sep 2026", weekNum: 40 },
      { id: "wk41", label: "5 Oct 2026 (WK 41)", date: "5 Oct 2026", weekNum: 41 },
      { id: "wk42", label: "12 Oct 2026 (WK 42)", date: "12 Oct 2026", weekNum: 42 },
      { id: "wk43", label: "19 Oct 2026 (WK 43)", date: "19 Oct 2026", weekNum: 43 },
      { id: "wk44", label: "26 Oct 2026 (WK 44)", date: "26 Oct 2026", weekNum: 44 },
      { id: "wk45", label: "2 Nov 2026 (WK 45)", date: "2 Nov 2026", weekNum: 45 },
      { id: "wk46", label: "9 Nov 2026 (WK 46)", date: "9 Nov 2026", weekNum: 46 }
    ]'''
content = re.sub(r'reportingWeeks:\s*\[[\s\S]*?\]', reporting_weeks, content)

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(content)
