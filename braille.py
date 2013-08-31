# -*- coding: utf-8 -*-


def x(col):
    return 17.455055 + col * 31.97757


def y(row):
    assert row == 0, "handle rows"
    return 19.955212


def rect(row, col):
    RECT_STR = """
    <rect
       style="fill:none;stroke:#373435;stroke-width:0.70866126"
       height="28.346407"
       width="15.944846"
       y="%(y)s"
       x="%(x)s"
       class="fil3 str1" />
"""
    return RECT_STR % dict(x=x(col), y=y(row))


def point(row, col, irow, icol):
    POINT_STR = """
    <path
       style="fill:#373435;fill-rule:evenodd;stroke:#373435;stroke-width:0.26999927"
       inkscape:connector-curvature="0"
       d="m %(x)s,%(y)s c 1.46763,0 2.65747,1.18984 2.65747,2.65748 0,1.46764 -1.18984,2.65747 -2.65747,2.65747 -1.46764,0 -2.65748,-1.18983 -2.65748,-2.65747 0,-1.46764 1.18984,-2.65748 2.65748,-2.65748 z"
       class="fil0 str0" />
"""
    def ix():
        assert icol >= 0 and icol <= 1, "Invalid inner column: %s" % icol
        return x(col) + 2.657487 + icol * 10.62974

    def iy():
        assert row >= 0 and row <= 2, "Invalid inner row: %s" % row
        return y(row) + irow * 11.51673
    return POINT_STR % dict(x=ix(), y=iy())


SVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="744.09448819"
   height="1052.3622047"
   id="svg6154"
   version="1.1"
   inkscape:version="0.48.4 r9939"
   sodipodi:docname="ab.svg">
  <defs
     id="defs6156" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.98994949"
     inkscape:cx="325.05521"
     inkscape:cy="777.22673"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="1301"
     inkscape:window-height="744"
     inkscape:window-x="65"
     inkscape:window-y="24"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata6159">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1">
     %(body)s
  </g>
</svg>
"""

def letter(char, row, col):
    CHARS = {
        u"А": [(0, 0)],
        u"Б": [(0, 0), (1, 0)],
        u"П": [(0, 0), (0, 1), (1, 0), (2, 0)],
        u"Р": [(0, 0), (1, 0), (1, 1), (2, 0)],
        u"И": [(0, 1), (1, 0)],
        u"В": [(0, 1), (1, 0), (1, 1), (2, 1)],
        u"Е": [(0, 0), (1, 1)],
        u"Т": [(0, 1), (1, 0), (1, 1), (2, 0)],
    }

    points = CHARS[char.upper()]
    svg = ""
    for irow, icol in points:
        svg += point(row, col, irow, icol)
    svg += rect(row, col)
    return svg


def text(s):
    body = ""
    for col, char in enumerate(s):
        body += letter(char, 0, col)
    return SVG % dict(body=body)


if __name__ == "__main__":
    print text(u'привет')
