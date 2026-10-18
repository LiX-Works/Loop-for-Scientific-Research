"""Rebuild the provisional G3/B3 lettermark from archived vector geometry.

Run from the repository root: python assets/source/logo/build_logo.py
Only the Python standard library is required; no installed font is needed.
"""

import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)


def build(data):
    canvas = data['canvas']
    colors = data['colors']
    svg = ET.Element(f'{{{NS}}}svg', {
        'width': str(canvas['width']),
        'height': str(canvas['height']),
        'viewBox': canvas['view_box'],
        'role': 'img',
        'aria-labelledby': 'title desc',
    })
    ET.SubElement(svg, f'{{{NS}}}title', {'id': 'title'}).text = 'Loop for Scientific Research provisional logo'
    ET.SubElement(svg, f'{{{NS}}}desc', {'id': 'desc'}).text = 'An open, curved L-shaped feedback loop around bold calligraphic SR initials. Ink green with a bronze return arrow. Provisional G3 frame and B3 lettering.'
    frame = data['frame']
    ET.SubElement(svg, f'{{{NS}}}path', {
        'd': frame['path'],
        'fill': 'none',
        'stroke': colors['ink'],
        'stroke-width': str(frame['stroke_width']),
        'stroke-linecap': frame['line_cap'],
        'stroke-linejoin': frame['line_join'],
    })
    ET.SubElement(svg, f'{{{NS}}}path', {
        'd': data['arrow']['path'],
        'fill': colors['arrow'],
    })
    lettering = data['lettering']
    group = ET.SubElement(svg, f'{{{NS}}}g', {
        'transform': lettering['transform'],
        'fill': colors['ink'],
        'stroke': colors['ink'],
        'stroke-width': str(lettering['stroke_width_in_font_units']),
        'stroke-linejoin': lettering['line_join'],
        'stroke-linecap': lettering['line_cap'],
        'paint-order': lettering['paint_order'],
    })
    ET.SubElement(group, f'{{{NS}}}path', {'d': lettering['path']})
    ET.indent(svg, space='  ')
    return ET.tostring(svg, encoding='unicode') + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geometry', type=Path, default=Path(__file__).with_name('geometry.json'))
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    geometry = json.loads(args.geometry.read_text(encoding='utf-8'))
    output = args.output or Path(__file__).resolve().parents[2] / 'brand/logo.svg'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build(geometry), encoding='utf-8', newline='\n')
    print(output)
