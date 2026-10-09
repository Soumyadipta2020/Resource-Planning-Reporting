with open('js/charts.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('this.instances[elementId] = new Chart(ctx, {')
end_idx = content.find('  }\n\n};')

if start_idx != -1 and end_idx != -1:
    chart_block = content[start_idx:end_idx]
    
    wrapped = """try {
      """ + chart_block.replace('\n', '\n      ') + """
    } catch (e) {
      console.error(e);
      const container = ctx.parentElement;
      container.innerHTML = '<div style="color: red; padding: 20px; font-weight: bold;">Chart Error: ' + e.message + '</div>';
    }"""

    new_content = content[:start_idx] + wrapped + content[end_idx:]
    with open('js/charts.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Wrapped Chart in try/catch")
else:
    print("Could not find Chart block")