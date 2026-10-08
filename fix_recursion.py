import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the infinite recursion in getGlobalMultiplier
old_func = '''  getGlobalMultiplier() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = this.getGlobalMultiplier();'''

new_func = '''  getGlobalMultiplier() {
    const geo = this.state.selectedGeography;
    const isRegional = geo !== "all" && DASHBOARD_DATA.regionalData[geo];
    const geoMult = isRegional ? DASHBOARD_DATA.regionalData[geo].multiplier : 1.0;'''

content = content.replace(old_func, new_func)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed infinite recursion!")
