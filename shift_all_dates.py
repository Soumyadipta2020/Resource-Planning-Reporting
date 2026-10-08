import re
from datetime import datetime, timedelta

def shift_dates(m):
    date_str = m.group(1)
    try:
        dt = datetime.strptime(date_str, '%d %b %Y')
        dt = dt + timedelta(days=15*7)
        new_date = dt.strftime('%d %b %Y')
        if new_date.startswith('0'):
            new_date = new_date[1:]
        return '"' + new_date + '"'
    except Exception as e:
        return m.group(0)

with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'"(\d{1,2} [A-Z][a-z]{2} 2026)"', shift_dates, content)

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(content)
