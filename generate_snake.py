import math

COLS = 60
ROWS = 25
SIZE = 12
GAP = 2

WIDTH = COLS * SIZE
HEIGHT = ROWS * SIZE

# Snake path
path = []

for x in range(COLS):
    if (x // 5) % 2 == 0:
        for y in range(ROWS):
            path.append((x, y))
    else:
        for y in range(ROWS - 1, -1, -1):
            path.append((x, y))

# SVG
svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}" height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<rect width="100%" height="100%" fill="#0d1117"/>

<style>
.square {{
    rx: 2;
}}

.snake {{
    fill: #39d353;
}}

.head {{
    fill: #58ff70;
}}

.food {{
    fill: #26a641;
}}

@keyframes moveSnake {{
    0% {{
        transform: translate(0px,0px);
    }}
    100% {{
        transform: translate(0px,0px);
    }}
}}
</style>
'''

# Draw all squares
for y in range(ROWS):
    for x in range(COLS):

        # GitHub-like green intensity
        level = (x * 7 + y * 3) % 5

        colors = [
            "#161b22",
            "#0e4429",
            "#006d32",
            "#26a641",
            "#39d353"
        ]

        color = colors[level]

        px = x * SIZE + GAP
        py = y * SIZE + GAP

        svg += f'''
        <rect
            class="square"
            x="{px}"
            y="{py}"
            width="{SIZE-GAP}"
            height="{SIZE-GAP}"
            fill="{color}"/>
        '''

# Animated snake
snake_length = 18
duration = 20

points = path

for i in range(snake_length):

    delay = -(i * 0.18)

    svg += f'''
    <circle
        class="snake"
        r="4"
        cx="0"
        cy="0">
        <animateMotion
            dur="{duration}s"
            begin="{delay}s"
            repeatCount="indefinite"
            path="
    '''

    d = ""

    first = True

    for x, y in points:
        px = x * SIZE + SIZE / 2
        py = y * SIZE + SIZE / 2

        if first:
            d += f"M {px} {py} "
            first = False
        else:
            d += f"L {px} {py} "

    svg += d

    svg += '''"/>
    </circle>
    '''

# Snake head
svg += f'''
<circle
    r="6"
    class="head"
    cx="0"
    cy="0">

    <animateMotion
        dur="{duration}s"
        repeatCount="indefinite"
        path="
'''

d = ""
first = True

for x, y in points:
    px = x * SIZE + SIZE / 2
    py = y * SIZE + SIZE / 2

    if first:
        d += f"M {px} {py} "
        first = False
    else:
        d += f"L {px} {py} "

svg += d

svg += '''"/>
</circle>
'''

svg += "</svg>"

with open("dist/github-big-snake.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Big Snake generated successfully!")
