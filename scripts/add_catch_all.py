with open('js/charts.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('  renderCapacityWaterfallChart(elementId, waterfallData) {')
end_idx = content.find('  }\n\n};')

if start_idx != -1 and end_idx != -1:
    body_start = start_idx + len('  renderCapacityWaterfallChart(elementId, waterfallData) {\n')
    body_content = content[body_start:end_idx]
    
    wrapped = """    try {
""" + body_content + """
    } catch (e) {
      console.error(e);
      const ctx = document.getElementById(elementId);
      if (ctx && ctx.parentElement) {
        ctx.parentElement.innerHTML = '<div style="color: red; padding: 20px; font-weight: bold;">Waterfall Chart Error: ' + e.message + '</div>';
      }
    }"""

    new_content = content[:body_start] + wrapped + content[end_idx:]
    with open('js/charts.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Wrapped entire function in try/catch")
else:
    print("Could not find function")