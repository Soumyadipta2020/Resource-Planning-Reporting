import re
from datetime import datetime, timedelta

def shift_match(m):
    prefix = m.group(1)
    num = int(m.group(2))
    return f"{prefix}{num + 15}"

def shift_dates(m):
    date_str = m.group(0)
    try:
        dt = datetime.strptime(date_str, '%d %b %Y')
        dt = dt + timedelta(days=15*7)
        return dt.strftime('%-d %b %Y').replace(' 0', ' ') # Handle no-pad on windows?
    except:
        return date_str

with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'(WK |wk)(\d+)', shift_match, content)

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'(WK |wk)(\d+)', shift_match, content)
content = content.replace('1 Jun 2026', '14 Sep 2026')
content = content.replace('22 Jun 2026', '5 Oct 2026')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
