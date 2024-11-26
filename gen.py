def generate_svg(char):
    """
    指定された文字のSVGファイルを生成する関数。

    引数:
        char: SVGファイルに書き込む文字 (0~9, a~z, その他記号)。

    戻り値:
        生成されたSVG文字列。
    """

    svg_template = """<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <g transform="translate(-233.58556,-160.86111)">
        <g fill="#ffffff" stroke="none" stroke-miterlimit="10" font-family="Pixel" font-weight="400" font-size="40">
            <text transform="translate(240,180) scale(0.5,0.5)" font-size="40" xml:space="preserve" fill="#ffffff">
                <tspan x="0" dy="0">{char}</tspan>
            </text>
        </g>
    </g>
</svg><!--rotationCenter:6.414441853761673:19.13888931274414-->"""

    return svg_template.format(char=char)

# 0~9のSVGファイルを生成
for i in range(10):
    svg_string = generate_svg(str(i))
    with open(f"{i}.svg", "w") as f:
        f.write(svg_string)

# a~zのSVGファイルを生成
for i in range(ord('a'), ord('z') + 1):
    svg_string = generate_svg(chr(i))
    with open(f"{chr(i)}.svg", "w") as f:
        f.write(svg_string)

# その他記号のSVGファイルを生成 (例として !@#$%^&*() を生成)
# symbols = "!@#$%^&*()"
symbols = "!@#$%^()"
for symbol in symbols:
    svg_string = generate_svg(symbol)
    with open(f"{symbol}.svg", "w") as f:
        f.write(svg_string)