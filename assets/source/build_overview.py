"""Build the original concept illustration using only the Python standard library.

Run from any directory: python assets/source/build_overview.py
The SVG is a proposal, not a record of an executed scientific task.
"""

from html import escape
from pathlib import Path
import argparse
import math


def build() -> str:
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="750" viewBox="0 0 1280 750" role="img" aria-labelledby="title desc">',
        '<title id="title">Loop for Scientific Research proposed architecture</title>',
        '<desc id="desc">A research brief is shared with independent model advisors. Their perspectives are synthesized into a plan, followed by execution and evidence collection. Independent review can request a specific check, revisit the plan, or return findings to the researcher. Model panels and other modules are replaceable. This is a concept preview, not a working integration.</desc>',
        '<rect width="1280" height="750" fill="#ffffff"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#243342} .label{font-size:30px;font-weight:700} .body{font-size:26px} .small{font-size:25px} .ink{fill:none;stroke:#526576;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}</style>',
    ]

    def add(s: str) -> None:
        parts.append(s)

    def text(x: float, y: float, value: str, cls: str = 'body', anchor: str = 'start', fill: str | None = None) -> None:
        color = f' style="fill:{fill}"' if fill else ''
        add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{color}>{escape(value)}</text>')

    def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str, radius: int = 20, sw: float = 2) -> None:
        add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def line(points: list[tuple[float, float]], color: str = '#526576', width: float = 3) -> None:
        p = ' '.join(f'{x},{y}' for x, y in points)
        add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>')

    def arrow(points: list[tuple[float, float]], color: str = '#697e8c', width: float = 4) -> None:
        # One terminal vector defines the shaft and the triangle, avoiding marker offsets.
        end, prev = points[-1], points[-2]
        dx, dy = end[0] - prev[0], end[1] - prev[1]
        size = math.hypot(dx, dy)
        ux, uy = dx / size, dy / size
        head = min(12, size * .36)
        half = head * .46
        base = (end[0] - head * ux, end[1] - head * uy)
        shaft_end = (base[0] + ux, base[1] + uy)
        line(points[:-1] + [shaft_end], color, width)
        a = (base[0] - half * uy, base[1] + half * ux)
        b = (base[0] + half * uy, base[1] - half * ux)
        add(f'<polygon points="{end[0]},{end[1]} {a[0]},{a[1]} {b[0]},{b[1]}" fill="{color}"/>')

    def document(x: float, y: float, color: str = '#526576', scale: float = 1) -> None:
        add(f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">')
        add('<path d="M0 0 H39 L55 16 V65 H0 Z M39 0 V16 H55"/>')
        add('<path d="M12 29 H41 M12 41 H41 M12 53 H31"/>')
        add('</g>')

    # Header remains deliberately modest: the README supplies the project title.
    text(40, 43, 'A proposed research loop', 'label')
    text(1230, 43, 'v0.01 · Concept preview', 'small', 'end', '#526576')

    # Six major stages. No vendor logos: the roles are independent of providers.
    rect(40, 95, 230, 225, '#fff6e5', '#dcc9a7')
    rect(330, 80, 500, 255, '#f4f0fa', '#c8badf')
    rect(900, 95, 330, 225, '#eaf4f3', '#aecac6')
    rect(840, 410, 390, 215, '#eaf4f3', '#aecac6')
    rect(330, 410, 420, 215, '#edf3fb', '#b8c9df')
    rect(40, 410, 230, 215, '#fff6e5', '#dcc9a7')

    # Frame a common research question.
    text(62, 135, 'Frame the', 'label')
    text(62, 171, 'question', 'label')
    document(72, 195, '#8a734c', .93)
    add('<circle cx="194" cy="225" r="25" fill="#f7e4bc"/>')
    text(194, 235, '?', 'label', 'middle', '#79613c')
    text(62, 294, 'Goals & context', 'small')

    # A panel can be one, two, or more independent model sessions.
    text(355, 123, 'Independent perspectives', 'label')
    for x, color, label in [(355, '#d9cee9', 'Model A'), (510, '#d5e4ed', 'Model B'), (665, '#e8d9cb', 'Model C')]:
        rect(x, 148, 140, 125, '#ffffff', color, 13)
        add(f'<circle cx="{x + 25}" cy="172" r="7" fill="{color}"/>')
        line([(x + 44, 172), (x + 113, 172)], color, 5)
        line([(x + 20, 193), (x + 109, 193)], '#a4adba', 3)
        line([(x + 20, 210), (x + 94, 210)], '#a4adba', 3)
        text(x + 70, 250, label, 'small', 'middle')
    text(580, 310, 'Different views on one question', 'body', 'middle', '#655277')

    # Synthesis makes a next step while retaining material disagreements.
    text(925, 138, 'Synthesize a plan', 'label')
    for y in (180, 210, 240):
        add(f'<circle cx="942" cy="{y}" r="7" fill="#6b9992"/>')
        line([(956, y), (988, y), (1021, 210)], '#7b9e98', 3)
    arrow([(1021, 210), (1083, 210)], '#527d76', 3)
    document(1103, 177, '#527d76', .96)
    text(1065, 294, 'Choose the next test', 'body', 'middle')

    # Execution produces real source and calculation artifacts.
    text(867, 454, 'Execute & collect', 'label')
    document(875, 484, '#527d76', .9)
    rect(962, 484, 83, 64, '#ffffff', '#90b6b0', 6)
    for x in (978, 994, 1010, 1026):
        line([(x, 487), (x, 545)], '#a5c2bd', 1.5)
    for y in (500, 516, 532):
        line([(965, y), (1042, y)], '#a5c2bd', 1.5)
    line([(1080, 487), (1080, 546), (1187, 546)], '#527d76', 2.8)
    line([(1089, 533), (1110, 520), (1133, 524), (1154, 498), (1181, 488)], '#648b85', 4)
    text(1035, 595, 'Sources · data · plots', 'body', 'middle')

    # Review has access to the evidence, rather than only to a fluent summary.
    text(357, 454, 'Independent review', 'label')
    document(390, 482, '#647f9f', .92)
    document(485, 482, '#647f9f', .92)
    add('<circle cx="637" cy="509" r="29" fill="#ffffff" stroke="#647f9f" stroke-width="3"/>')
    line([(658, 530), (681, 552)], '#647f9f', 5)
    line([(625, 510), (635, 520), (651, 498)], '#647f9f', 3.5)
    text(540, 595, 'Check the evidence', 'body', 'middle')

    # The human remains the recipient of decisions and unresolved questions.
    text(62, 453, 'Researcher', 'label')
    document(88, 482, '#8a734c', 1.05)
    line([(111, 542), (126, 527), (144, 531)], '#9a8054', 3)
    text(62, 584, 'Findings &', 'body')
    text(62, 613, 'decisions', 'body')

    # Main direction, plus two distinct scientific feedback routes.
    arrow([(280, 207), (318, 207)])
    arrow([(842, 207), (888, 207)])
    arrow([(1065, 332), (1065, 398)], '#527d76')
    arrow([(828, 520), (762, 520)])
    arrow([(318, 520), (282, 520)], '#9a8054')
    arrow([(540, 398), (540, 347)], '#8c79a7')
    text(557, 380, 'Revisit the plan', 'small', fill='#6f588b')
    arrow([(540, 637), (540, 670), (1035, 670), (1035, 637)], '#648b85')
    text(788, 707, 'Request a specific check', 'body', 'middle', '#466d66')

    text(40, 704, 'Decide from evidence', 'small', fill='#526576')
    text(40, 735, 'Shared brief · evidence · decisions', 'small', fill='#526576')
    add('</svg>')
    return '\n'.join(parts) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    output = args.output or Path(__file__).resolve().parents[1] / 'overview.svg'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build(), encoding='utf-8', newline='\n')
    print(output)
