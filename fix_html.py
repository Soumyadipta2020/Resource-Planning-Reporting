with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace hardcoded WK 14 - WK 23 above weekly installs chart
old_text = '<span class="text-[11px] text-slate-500 font-medium">WK 14 - WK 23</span>'
new_text = '<span class="text-[11px] text-slate-500 font-medium">WK 14 - WK 29</span>'

if old_text in html:
    html = html.replace(old_text, new_text)
    print("Replaced WK label in index.html")
else:
    print("Could not find exact text in index.html, check manually")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
