"""Draw the proposed layered research process, including distinct feedback paths.

Uses only the Python standard library. All document and plot symbols are illustrative.
"""

from html import escape
from pathlib import Path
import argparse
import math


def build() -> str:
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1320" height="980" viewBox="0 0 1320 980" role="img" aria-labelledby="title desc">',
        '<title id="title">Inside the proposed scientific research loop</title>',
        '<desc id="desc">The researcher and existing materials feed a shared research brief. Several models assess it independently; a synthesizer turns their views into a plan. A coordinator delegates literature, computation, and data or figure tasks. An evidence package is checked before independent reviewers and review synthesis. Local execution repair, requests for new evidence, and reconsideration of the plan follow distinct return paths. Optional writing and researcher review complete a round. This is a proposed process, not a working system.</desc>',
        '<rect width="1320" height="980" fill="#ffffff"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#243342}.heading{font-size:36px;font-weight:700}.title{font-size:30px;font-weight:700}.section{font-size:28px;font-weight:700}.body{font-size:26px}</style>',
    ]

    def text(x, y, value, cls='body', anchor='start', color=None, rotate=None):
        attrs = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ''
        attrs += f' style="fill:{color}"' if color else ''
        out.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{attrs}>{escape(value)}</text>')

    def box(x, y, w, h, fill='#ffffff', stroke='#c6d0d9', r=16):
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')

    def line(points, color='#69808f', width=3.5, dash=False):
        d = ' '.join(f'{x},{y}' for x, y in points)
        extra = ' stroke-dasharray="8 7"' if dash else ''
        out.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{extra}/>')

    def arrow(points, color='#69808f', width=3.5, dash=False):
        x, y = points[-1]
        px, py = points[-2]
        length = math.hypot(x - px, y - py)
        ux, uy = (x - px) / length, (y - py) / length
        head = min(12, length * .36)
        half = head * .46
        bx, by = x - head * ux, y - head * uy
        line(points[:-1] + [(bx + ux, by + uy)], color, width, dash)
        out.append(f'<polygon points="{x},{y} {bx - half * uy},{by + half * ux} {bx + half * uy},{by - half * ux}" fill="{color}"/>')

    def node(x, y, w, h, title, sub='', fill='#ffffff', stroke='#c6d0d9'):
        box(x, y, w, h, fill, stroke)
        if sub:
            text(x + w / 2, y + (30 if h <= 80 else 36), title, 'title', 'middle')
            text(x + w / 2, y + h - 15, sub, anchor='middle')
        else:
            text(x + w / 2, y + h / 2 + 10, title, 'title', 'middle')

    def memo(x, y, w, label, color):
        box(x, y, w, 100, '#ffffff', color, 13)
        text(x + w / 2, y + 37, label, 'title', 'middle')
        for row, end in [(0, w - 28), (1, w - 46), (2, w - 35)]:
            line([(x + 18, y + 58 + 13 * row), (x + end, y + 58 + 13 * row)], color, 3)

    blue = '#5d7c98'
    teal = '#5f9188'
    purple = '#8b76a6'
    amber = '#ac8950'

    text(60, 46, 'Inside the research loop', 'heading')
    text(1220, 46, 'Proposed process · v0.01', anchor='end', color='#586b7b')

    node(60, 110, 350, 100, 'Researcher', 'Question + context', '#fff6e5', '#dcc9a7')
    node(465, 110, 350, 100, 'Clarify & frame', 'Shared brief + evidence', '#fff6e5', '#dcc9a7')
    node(870, 110, 350, 100, 'Existing materials', 'Sources + prior results', '#f5f7f9', '#c6d0d9')
    arrow([(422, 139), (453, 139)], amber)
    arrow([(453, 183), (422, 183)], amber, 3, True)
    arrow([(858, 160), (827, 160)])

    # Three adjacent stages keep the complete process readable at README width.
    box(60, 260, 350, 530, '#faf8fd', '#d4c9e4', 22)
    box(465, 260, 350, 530, '#f6faf9', '#bfd6d1', 22)
    box(870, 260, 350, 530, '#f6f8fc', '#c5d0e0', 22)
    text(235, 307, '1  PLAN', 'section', 'middle', '#6c5588')
    text(640, 307, '2  EXECUTE', 'section', 'middle', '#466f67')
    text(1045, 307, '3  REVIEW', 'section', 'middle', '#506c8d')

    text(235, 345, 'Independent model views', anchor='middle')
    line([(640, 222), (640, 235), (395, 235), (395, 365), (130, 365)], purple, 3)
    for cx in (130, 240, 350):
        arrow([(cx, 365), (cx, 388)], purple, 3)
    for x, label in [(85, 'A'), (195, 'B'), (305, 'C')]:
        memo(x, 400, 90, label, '#b4a2cc')
    for cx in (130, 240, 350):
        line([(cx, 512), (cx, 530)], purple, 3)
    line([(130, 530), (350, 530)], purple, 3)
    text(235, 574, 'Options · assumptions', anchor='middle', color='#6c5588')
    text(235, 610, 'Tests · uncertainties', anchor='middle', color='#6c5588')
    arrow([(240, 622), (240, 668)], purple, 3)
    node(85, 680, 300, 80, 'Compare & choose', 'Plan + open questions', '#f0eaf8', '#bca9d3')

    node(490, 350, 300, 65, 'Task coordinator', fill='#e8f3f0', stroke='#aac9c1')
    arrow([(397, 720), (438, 720), (438, 398), (478, 398)], teal)
    line([(610, 425), (610, 440), (500, 440), (500, 606)], teal, 3)
    for y, label in [(475, 'Literature'), (529, 'Computation'), (583, 'Data & figures')]:
        node(540, y, 230, 46, label, fill='#ffffff', stroke='#b4d0c9')
        arrow([(500, y + 23), (528, y + 23)], teal, 3)
        line([(782, y + 23), (800, y + 23)], teal, 3)
    line([(800, 498), (800, 642), (640, 642)], teal, 3)
    arrow([(640, 642), (640, 668)], teal, 3)
    node(490, 680, 300, 80, 'Evidence package', 'Check sources & outputs', '#e8f3f0', '#aac9c1')

    # Local repair stays inside execution. A later review can request new work.
    arrow([(478, 720), (475, 720), (475, 455), (730, 455), (730, 425)], amber, 3)
    text(1045, 345, 'Independent reviewers', anchor='middle')
    line([(802, 720), (843, 720), (843, 365), (1160, 365)], blue, 3)
    for cx in (940, 1050, 1160):
        arrow([(cx, 365), (cx, 388)], blue, 3)
    for x, label in [(895, 'A'), (1005, 'B'), (1115, 'C')]:
        memo(x, 400, 90, label, '#a5b8d0')
    for cx in (940, 1050, 1160):
        line([(cx, 512), (cx, 530)], blue, 3)
    line([(940, 530), (1160, 530)], blue, 3)
    text(1045, 574, 'Evidence · alternatives', anchor='middle', color='#506c8d')
    text(1045, 610, 'Targeted follow-up', anchor='middle', color='#506c8d')
    arrow([(1050, 622), (1050, 668)], blue, 3)
    node(895, 680, 300, 80, 'Review synthesis', 'Resolve or retain doubts', '#e9f0fa', '#acbfd9')

    # Feedback uses the outer margins instead of extending the figure vertically.
    arrow([(1005, 772), (1005, 810), (30, 810), (30, 700), (73, 700)], purple, 3.5)
    arrow([(1080, 772), (1080, 830), (450, 830), (450, 367), (478, 367)], teal, 3.5)

    node(870, 865, 350, 90, 'Optional writing', 'Report & explain', '#f3f1f8', '#cfc5df')
    node(465, 865, 350, 90, 'Researcher review', 'Findings + next choices', '#fff6e5', '#dcc9a7')
    arrow([(1207, 720), (1260, 720), (1260, 910), (1232, 910)], blue)
    text(1293, 817, 'Ready', anchor='middle', color='#506c8d', rotate=90)
    arrow([(858, 910), (827, 910)], amber)
    for y, color, label in [(879, amber, 'Repair execution'), (915, teal, 'Add evidence'), (951, purple, 'Reconsider the plan')]:
        line([(60, y - 8), (86, y - 8)], color, 4)
        text(100, y, label, color=color)
    out.append('</svg>')
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    output = args.output or Path(__file__).resolve().parents[1] / 'research-cycle.svg'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build(), encoding='utf-8', newline='\n')
    print(output)
