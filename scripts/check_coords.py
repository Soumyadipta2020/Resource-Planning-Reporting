import re
from xml.etree import ElementTree as ET

tree = ET.parse('images/uk.svg')
root = tree.getroot()

for elem in root.iter():
    if elem.tag.endswith('path'):
        pid = elem.attrib.get('id', '')
        title = elem.attrib.get('title', '')
        d = elem.attrib.get('d', '')
        # extract coords
        coords = re.findall(r'([0-9]+\.[0-9]+)[,\s]+([0-9]+\.[0-9]+)', d)
        if coords:
            xs = [float(c[0]) for c in coords]
            ys = [float(c[1]) for c in coords]
            print(f"{pid} ({title}): X[{min(xs):.1f} - {max(xs):.1f}], Y[{min(ys):.1f} - {max(ys):.1f}]")

