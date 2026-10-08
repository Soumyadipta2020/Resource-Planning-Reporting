with open("js/charts.js", "r", encoding="utf-8") as f:
    js = f.read()

old_code = """              afterBody: function(context) {
                 if (context.length > 0) {
                     const index = context[0].dataIndex;
                     const variance = variances[index];
                     const sign = variance > 0 ? "+" : "";
                     return `\\nVariance: ${sign}${variance.toLocaleString()}`;
                 }
              }"""

new_code = """              afterBody: function(context) {
                 if (context.length > 0) {
                     const index = context[0].dataIndex;
                     const variance = variances[index];
                     if (variance === null || variance === undefined) return '';
                     const sign = variance > 0 ? "+" : "";
                     return `\\nVariance: ${sign}${variance.toLocaleString()}`;
                 }
              }"""

if old_code in js:
    js = js.replace(old_code, new_code)
    with open("js/charts.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("Fixed charts.js")
else:
    print("Could not find exact text in charts.js, check manually")
