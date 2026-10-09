import re
from xml.etree import ElementTree as ET

tree = ET.parse('images/uk.svg')
root = tree.getroot()

uk_ids = ['GB-UKC', 'GB-UKD', 'GB-UKE', 'GB-UKF', 'GB-UKG', 'GB-UKH', 'GB-UKI', 'GB-UKJ', 'GB-UKK', 'GB-UKL', 'GB-UKM', 'GB-UKN']

all_xs = []
all_ys = []

for elem in root.iter():
    if elem.tag.endswith('path'):
        pid = elem.attrib.get('id', '')
        if pid in uk_ids:
            d = elem.attrib.get('d', '')
            # find all numbers in d
            coords = re.findall(r'([0-9]+\.[0-9]+)[,\s]+([0-9]+\.[0-9]+)', d)
            for c in coords:
                x, y = float(c[0]), float(c[1])
                # Skip 0.0 if it's an artifact of relative coordinates
                if x > 10: all_xs.append(x)
                if y > 10: all_ys.append(y)

print(f"UK Bounds: X[{min(all_xs):.1f} to {max(all_xs):.1f}], Y[{min(all_ys):.1f} to {max(all_ys):.1f}]")
width = max(all_xs) - min(all_xs)
height = max(all_ys) - min(all_ys)
print(f"Width: {width:.1f}, Height: {height:.1f}")
print(f"Suggested viewBox: '{min(all_xs)-20:.0f} {min(all_ys)-20:.0f} {width+40:.0f} {height+40:.0f}'")

