with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("v=6", "v=7")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
