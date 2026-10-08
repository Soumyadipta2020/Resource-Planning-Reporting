with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("v=7", "v=8")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
