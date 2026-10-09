with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update table cells padding
js = js.replace(
    '<td class="py-2.5 px-2 font-semibold text-slate-800">${r.name}</td>',
    '<td class="py-2.5 px-3 font-semibold text-slate-800">${r.name}</td>'
)
js = js.replace('px-2 text-right', 'px-3 text-right')
js = js.replace('px-2 font-bold text-slate-900">Total</td>', 'px-3 font-bold text-slate-900">Total</td>')

# Update Top 5 / Bottom 5 area label widths and margins
js = js.replace(
    '<div class="w-24 truncate" title="${area}">${area}</div>\n           <div class="flex-1 ml-2">',
    '<div class="w-28 font-medium text-slate-700 truncate" title="${area}">${area}</div>\n           <div class="flex-1 ml-3 bg-slate-100 rounded-sm overflow-hidden h-3.5">'
)
js = js.replace(
    '<div class="h-4 bg-emerald-600 rounded-sm"',
    '<div class="h-full bg-emerald-600 rounded-sm"'
)
js = js.replace(
    '<div class="h-4 bg-red-600 rounded-sm"',
    '<div class="h-full bg-red-600 rounded-sm"'
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated js/app.js styling successfully!")

