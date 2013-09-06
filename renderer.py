# -*- coding: utf-8 -*-
import re


def point(posx, posy, irow, icol):
    POINT_STR = """
    <path
       style="fill:#373435;fill-rule:evenodd;stroke:#373435;stroke-width:0.26999927"
       inkscape:connector-curvature="0"
       d="m %(x)s,%(y)s c 1.46763,0 2.65747,1.18984 2.65747,2.65748 0,1.46764 -1.18984,2.65747 -2.65747,2.65747 -1.46764,0 -2.65748,-1.18983 -2.65748,-2.65747 0,-1.46764 1.18984,-2.65748 2.65748,-2.65748 z"
       class="fil0 str0" />
"""
    def ix():
        assert icol >= 0 and icol <= 1, "Invalid inner column: %s" % icol
        return posx + 2.657487 + icol * 10.62974

    def iy():
        assert irow >= 0 and irow <= 2, "Invalid inner row: %s" % row
        return posy + irow * 11.51673
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

def letter(char, posx, posy):
    DIGIT_START = [
                (0, 1), 
                (0, 1), 
                (1, 1)]
    CHARS = {
        u"А": [
                (1, 0),
                (0, 0),
                (0, 0)],
        u"Б": [
                (1, 0), 
                (1, 0),
                (0, 0)],
        u"В": [
                (0, 1), 
                (1, 1), 
                (0, 1)],
        u"Г": [
                (1, 1), 
                (1, 1),
                (0, 0)],
        u"Д": [
                (1, 1), 
                (0, 1),
                (0, 0)],
        u"Е": [
                (1, 0), 
                (0, 1),
                (0, 0)],
        u"Ё": [
                (1, 0), 
                (0, 0),
                (0, 1)],
        u"Ж": [
                (0, 1), 
                (1, 1),
                (0, 0)],
        u"З": [
                (1, 0), 
                (0, 1),
                (1, 1)],
        u"И": [
                (0, 1), 
                (1, 0),
                (0, 0)],
        u"Й": [
                (1, 1), 
                (1, 0),
                (1, 1)],
        u"І": [
                (1, 1), 
                (1, 0),
                (1, 1)],
        u"Ї": [
                (1, 1), 
                (1, 0),
                (1, 1)],
        u"К": [
                (1, 0), 
                (0, 0),
                (1, 0)],
        u"Л": [
                (1, 0), 
                (1, 0),
                (1, 0)],
        u"М": [
                (1, 1), 
                (0, 0),
                (1, 0)],
        u"Н": [
                (1, 1), 
                (0, 1),
                (1, 0)],
        u"О": [
                (1, 0), 
                (0, 1),
                (1, 0)],
        u"П": [
                (1, 1), 
                (1, 0), 
                (1, 0)],
        u"Р": [
                (1, 0), 
                (1, 1), 
                (1, 0)],
        u"С": [
                (0, 1), 
                (1, 0), 
                (1, 0)],
        u"Т": [
                (0, 1), 
                (1, 1), 
                (1, 0)],
        u"У": [
                (1, 0), 
                (0, 0), 
                (1, 1)],
        u"Ф": [
                (1, 1), 
                (1, 0), 
                (0, 0)],
        u"Х": [
                (1, 0), 
                (1, 1), 
                (0, 0)],
        u"Ц": [
                (1, 1), 
                (0, 0), 
                (0, 0)],
        u"Ч": [
                (1, 1), 
                (1, 1), 
                (1, 0)],
        u"Ш": [
                (1, 0), 
                (0, 1), 
                (0, 1)],
        u"Щ": [
                (1, 1), 
                (0, 0), 
                (1, 1)],
        u"Ъ": [
                (1, 0), 
                (1, 1), 
                (1, 1)],
        u"Ы": [
                (0, 1), 
                (1, 0), 
                (1, 1)],
        u"Ь": [
                (0, 1), 
                (1, 1), 
                (1, 1)],
        u"Э": [
                (0, 1), 
                (1, 0), 
                (0, 1)],
        u"Є": [
                (1, 1), 
                (1, 0),
                (1, 1)],
        u"Ю": [
                (1, 0), 
                (1, 1), 
                (0, 1)],
        u"Я": [
                (1, 1), 
                (1, 0), 
                (0, 1)],


        u".": [
                (0, 0), 
                (1, 1), 
                (0, 1)],
        u"!": [
                (0, 0), 
                (1, 1), 
                (1, 0)],
        u"-": [
                (0, 0), 
                (0, 0), 
                (1, 1)],
        u'\u201c': [
                (0, 0), 
                (1, 0), 
                (1, 1)],
        u'\u201d': [
                (0, 0), 
                (0, 1), 
                (1, 1)],
        u"(": [
                (0, 1), 
                (1, 0), 
                (1, 0)],
        u")": [
                (1, 0), 
                (0, 1), 
                (0, 1)],
        u",": [
                (0, 0), 
                (1, 0), 
                (0, 0)],
        u"?": [
                (0, 0), 
                (1, 0), 
                (0, 1)],
        u";": [
                (0, 0), 
                (1, 0), 
                (1, 0)],
        u":": [
                (0, 0), 
                (1, 1), 
                (0, 0)],
        u"’": [
                (1, 1), 
                (1, 0), 
                (0, 1)],
        u"1": [
                (1, 0), 
                (0, 0), 
                (0, 0)],
        u"2": [
                (1, 0), 
                (1, 0), 
                (0, 0)],
        u"3": [
                (1, 1), 
                (0, 0), 
                (0, 0)],
        u"4": [
                (1, 1), 
                (0, 1), 
                (0, 0)],
        u"5": [
                (1, 0), 
                (0, 1), 
                (0, 0)],
        u"6": [
                (1, 1), 
                (1, 0), 
                (0, 0)],
        u"7": [
                (1, 1), 
                (1, 1), 
                (0, 0)],
        u"8": [
                (1, 0), 
                (1, 1), 
                (1, 1)],
        u"9": [
                (0, 1), 
                (1, 0), 
                (0, 0)],
        u"0": [
                (0, 1), 
                (1, 1), 
                (0, 0)],
        u"^": DIGIT_START
    }


    points = CHARS[char.upper()]
    svg = ""
    for irow, columns in enumerate(points):
        for icol, exists in enumerate(columns):
            if exists:
                svg += point(posx, posy, irow, icol)
    return svg


START_X = 68.501325
START_Y = 74.513512
LETTER_INTERVAL = 23.03269
WORD_INTERVAL = 38.97373
LINE_INTERVAL = 46.03843

def text(s):
    body = ""
    posx, posy = START_X, START_Y
    for line in s.splitlines():
        line = digit_prefix(line)
        for word in line.split():
            for char in word:
                body += letter(char, posx, posy)
                posx += LETTER_INTERVAL
            posx += WORD_INTERVAL
        posy += LINE_INTERVAL
        posx = START_X
    return SVG % dict(body=body)


def digit_prefix(text):
    assert text.find('^') == -1, text
    return re.sub(r'(\d+)', r'^\1', text)


if __name__ == "__main__":
    # print text(u'барвінківський районний\nтериторіальний центр')
    print text(u'123')
