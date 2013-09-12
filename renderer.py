# -*- coding: utf-8 -*-
import re


START_X = 30
START_Y = 30
POINT_INTERVAL = 2 + 1.5
LETTER_INTERVAL = 5 + 1.5
WORD_INTERVAL = 6.5
LINE_INTERVAL = 5


def point(posx, posy, irow, icol):
    POINT_STR = """
    <circle cx="%(x)smm" cy="%(y)smm" r="0.75mm" />
"""
    def ix():
        assert icol >= 0 and icol <= 1, "Invalid inner column: %s" % icol
        return posx + icol * POINT_INTERVAL

    def iy():
        assert irow >= 0 and irow <= 2, "Invalid inner row: %s" % row
        return posy + irow * POINT_INTERVAL
    return POINT_STR % dict(x=ix(), y=iy())


SVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   version="1.1"
   xmlns="http://www.w3.org/2000/svg"
   width="744.09448819"
   height="1052.3622047">
   %(body)s
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
                (0, 1),
                (1, 1)],
        u"Ї": [
                (1, 1), 
                (0, 1),
                (0, 1)],
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
    print text(u'барвінківський районний')
    # print text(u'барв')
