from xml.etree import ElementTree as ET

tree = ET.parse('images/uk.svg')
root = tree.getroot()

uk_mapping = {
    'GB-UKM': ('Scotland', '#15803d'),
    'GB-UKC': ('North East', '#22c55e'),
    'GB-UKD': ('North West', '#22c55e'),
    'GB-UKE': ('Yorkshire & Humber', '#22c55e'),
    'GB-UKF': ('East Midlands', '#eab308'),
    'GB-UKG': ('West Midlands', '#eab308'),
    'GB-UKH': ('East of England', '#eab308'),
    'GB-UKL': ('Wales', '#ea580c'),
    'GB-UKI': ('Greater London', '#dc2626'),
    'GB-UKJ': ('South East', '#dc2626'),
    'GB-UKK': ('South West', '#dc2626'),
    'GB-UKN': ('Northern Ireland', '#64748b')
}

paths_xml = []
for elem in root.iter():
    if elem.tag.endswith('path'):
        pid = elem.attrib.get('id', '')
        if pid in uk_mapping:
            name, color = uk_mapping[pid]
            d = elem.attrib.get('d', '')
            paths_xml.append(f'  <path id="{pid}" data-name="{name}" d="{d}" fill="{color}" stroke="#ffffff" stroke-width="1.8" stroke-linejoin="round" />')

new_svg = f'''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="280 150 490 1030" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="115%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.12"/>
    </filter>
  </defs>
  <g filter="url(#shadow)">
{chr(10).join(paths_xml)}
  </g>
</svg>
'''

with open('images/uk.svg', 'w', encoding='utf-8') as f:
    f.write(new_svg)

print("Created new images/uk.svg with correct viewBox and regional colors!")

