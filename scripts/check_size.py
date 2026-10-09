from xml.etree import ElementTree as ET

tree = ET.parse('images/uk.svg')
root = tree.getroot()

uk_mapping = {
    'GB-UKM': ('scotland', '#15803d'),
    'GB-UKC': ('north', '#22c55e'),
    'GB-UKD': ('north', '#22c55e'),
    'GB-UKE': ('north', '#22c55e'),
    'GB-UKF': ('midlands', '#eab308'),
    'GB-UKG': ('midlands', '#eab308'),
    'GB-UKH': ('midlands', '#eab308'),
    'GB-UKL': ('wales', '#f97316'),
    'GB-UKI': ('south', '#dc2626'),
    'GB-UKJ': ('south', '#dc2626'),
    'GB-UKK': ('south', '#dc2626'),
    'GB-UKN': ('ni', '#64748b')
}

total_len = 0
for elem in root.iter():
    if elem.tag.endswith('path'):
        pid = elem.attrib.get('id', '')
        if pid in uk_mapping:
            d = elem.attrib.get('d', '')
            total_len += len(d)

print(f"Total path data length: {total_len} bytes (~{total_len/1024:.1f} KB)")

