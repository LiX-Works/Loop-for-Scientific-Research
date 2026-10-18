"""Build the proposed, interchangeable module illustration with standard Python.

The diagram describes a design proposal, not implemented model routing.
Run: python assets/source/build_modules.py
"""

from html import escape
from pathlib import Path
import argparse
import math


def build() -> str:
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="850" viewBox="0 0 1280 850" role="img" aria-labelledby="title desc">',
        '<title id="title">Proposed interchangeable scientific research modules</title>',
        '<desc id="desc">Choose exactly one Advice module: one model for routine work, two independent models for comparison, or a panel of five models for exploration. These are alternatives for the same position in the shared Brief, Advice, Synthesis, Execution and Review workflow, not three sequential stages or three simultaneously active groups. Review, Writing and Search can also have replaceable implementations. Generic model letters do not prescribe vendors or fixed model capabilities. Proposed design only; more models do not establish higher quality.</desc>',
        '<rect width="1280" height="850" fill="#ffffff"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#263646}.title{font-size:34px;font-weight:700}.label{font-size:29px;font-weight:700}.body{font-size:26px}.model{font-size:27px;font-weight:700}.wire{fill:none;stroke-linecap:round;stroke-linejoin:round}</style>',
    ]

    def add(value: str) -> None:
        parts.append(value)

    def text(x: float, y: float, value: str, cls: str = 'body', anchor: str = 'start', color: str | None = None) -> None:
        style = f' style="fill:{color}"' if color else ''
        add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{style}>{escape(value)}</text>')

    def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str, r: float = 18, sw: float = 2, dash: str = '') -> None:
        dashed = f' stroke-dasharray="{dash}"' if dash else ''
        add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dashed}/>')

    def line(points: list[tuple[float, float]], color: str = '#718092', width: float = 3, dash: str = '') -> None:
        path = ' '.join(f'{x},{y}' for x, y in points)
        dashed = f' stroke-dasharray="{dash}"' if dash else ''
        add(f'<polyline points="{path}" class="wire" stroke="{color}" stroke-width="{width}"{dashed}/>')

    def arrow(points: list[tuple[float, float]], color: str = '#7b8a9b', width: float = 3.5) -> None:
        ex, ey = points[-1]
        px, py = points[-2]
        norm = math.hypot(ex - px, ey - py)
        ux, uy = (ex - px) / norm, (ey - py) / norm
        head = min(12, norm * .36)
        half = head * .46
        bx, by = ex - head * ux, ey - head * uy
        line(points[:-1] + [(bx + ux, by + uy)], color, width)
        add(f'<polygon points="{ex},{ey} {bx - half * uy},{by + half * ux} {bx + half * uy},{by - half * ux}" fill="{color}"/>')

    def session(x: float, y: float, w: float, h: float, label: str, accent: str) -> None:
        rect(x, y, w, h, '#ffffff', accent, 11, 2.3)
        line([(x + 1, y + 24), (x + w - 1, y + 24)], accent, 2)
        for n in range(3):
            add(f'<circle cx="{x + 13 + n * 10}" cy="{y + 12}" r="2.4" fill="{accent}"/>')
        text(x + w / 2, y + (58 if h < 100 else 64), label, 'model', 'middle')
        if h >= 100:
            line([(x + 17, y + h - 24), (x + w - 17, y + h - 24)], accent, 3)

    def stage_icon(x: float, y: float, kind: str, color: str) -> None:
        add(f'<g transform="translate({x} {y})" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">')
        if kind == 'brief':
            add('<path d="M-18 -22 H7 L20 -9 V23 H-18 Z M7 -22 V-9 H20 M-8 1 H10 M-8 11 H6"/>')
        elif kind == 'advice':
            add('<path d="M-25 -18 H14 V8 H-2 L-14 19 V8 H-25 Z M-8 -25 H26 V1"/>')
        elif kind == 'synthesis':
            add('<path d="M-25 -18 L-7 -18 L10 0 L-7 18 L-25 18 M-26 0 H10 H25 M18 -7 L25 0 L18 7"/>')
        elif kind == 'execution':
            add('<rect x="-27" y="-20" width="54" height="40" rx="5"/><path d="M-16 -9 L-7 0 L-16 9 M1 10 H15"/>')
        elif kind == 'review':
            add('<circle cx="-4" cy="-4" r="20"/><path d="M11 12 L26 27 M-13 -3 L-5 5 L8 -10"/>')
        elif kind == 'writing':
            add('<path d="M-21 -22 H9 L21 -10 V23 H-21 Z M9 -22 V-10 H21 M-10 1 H11 M-10 11 H7"/>')
        elif kind == 'search':
            add('<circle cx="-4" cy="-4" r="20"/><path d="M11 12 L27 28"/>')
        add('</g>')

    text(30, 48, 'Interchangeable modules', 'title')
    text(1250, 47, 'Proposed design', 'body', 'end', '#657587')

    # A single selection tray makes the three panels alternatives, not branches.
    rect(26, 83, 1228, 328, '#fbfcfe', '#d0d8e3', 23, 2)
    text(48, 124, 'Advice options', 'label')
    rect(1041, 96, 191, 39, '#eee9f8', '#eee9f8', 10, 0)
    text(1136, 124, 'Choose ONE', 'body', 'middle', '#62517d')

    options = [
        (48, '#fbf2e5', '#d8ba8e', '1 model', 'Routine'),
        (452, '#eaf4f3', '#93b9b2', '2 models', 'Compare'),
        (856, '#f0ebf8', '#b5a2d0', '5 models', 'Explore'),
    ]
    for x, fill, stroke, title, purpose in options:
        rect(x, 150, 376, 240, fill, stroke, 17, 1.7)
        add(f'<circle cx="{x + 25}" cy="180" r="9" fill="#ffffff" stroke="{stroke}" stroke-width="2.3"/>')
        text(x + 47, 190, title, 'label')
        text(x + 352, 189, purpose, 'body', 'end')

    session(164, 221, 144, 139, 'Model A', '#c3a575')
    session(480, 221, 145, 139, 'Model A', '#87aaa5')
    session(654, 221, 145, 139, 'Model B', '#87aaa5')
    # Five separate windows keep the model count visible at GitHub page width.
    for x, y, name in [(890, 215, 'A'), (993, 215, 'B'), (1096, 215, 'C'), (941.5, 299, 'D'), (1044.5, 299, 'E')]:
        session(x, y, 82, 77, name, '#ad9ac5')

    # Only one outlet leaves the tray and plugs into the Advice position.
    arrow([(351, 412), (351, 465)], '#927aaa', 4)
    text(374, 448, 'Swap in', 'body', color='#6e5689')

    stages = [
        (26, 178, 'Brief', 'brief', '#fff5e4', '#ceb68e'),
        (255, 192, 'Advice', 'advice', '#eee8f8', '#9982b9'),
        (498, 221, 'Synthesis', 'synthesis', '#edf3fb', '#a8bdd7'),
        (770, 222, 'Execution', 'execution', '#eaf4f0', '#97b6a8'),
        (1043, 211, 'Review', 'review', '#edf3fb', '#a8bdd7'),
    ]
    for x, w, label, kind, fill, border in stages:
        if kind == 'advice':
            # A visible cartridge tab is repeated by the other optional parts.
            rect(x + w / 2 - 24, 466, 48, 24, fill, border, 6, 2.8)
        rect(x, 479, w, 133, fill, border, 18, 2.8 if kind == 'advice' else 2)
        if kind == 'advice':
            add(f'<path d="M{x+w/2-21} 480 H{x+w/2+21}" stroke="{fill}" stroke-width="5"/>')
        stage_icon(x + w / 2, 525, kind, '#657589' if kind != 'advice' else '#786193')
        text(x + w / 2, 587, label, 'label', 'middle')
    for a, b in [(214, 245), (457, 488), (729, 760), (1002, 1033)]:
        arrow([(a, 547), (b, 547)], '#7c8c9c', 3.5)

    # A second small library makes replaceability beyond Advice tangible.
    line([(32, 665), (1248, 665)], '#dce3e9', 2)
    text(32, 721, 'Other swappable', 'label')
    text(32, 758, 'modules', 'label')
    for x, label, kind, fill, border in [
        (423, 'Review', 'review', '#edf3fb', '#a8bdd7'),
        (704, 'Writing', 'writing', '#fff2e7', '#d4b298'),
        (985, 'Search', 'search', '#eaf4f0', '#a1bdb2'),
    ]:
        rect(x + 12, 710, 237, 109, '#ffffff', '#cbd4dd', 15, 1.8, '6 7')
        rect(x + 94, 681, 48, 22, fill, border, 6, 2)
        rect(x, 693, 237, 112, fill, border, 15, 2)
        add(f'<path d="M{x+97} 694 H{x+139}" stroke="{fill}" stroke-width="5"/>')
        stage_icon(x + 48, 747, kind, '#697c8b')
        text(x + 90, 757, label, 'label')
    add('</svg>')
    return '\n'.join(parts) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    output = args.output or Path(__file__).resolve().parents[1] / 'modules.svg'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build(), encoding='utf-8', newline='\n')
    print(output)
