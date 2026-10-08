with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("v=8", "v=9")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
