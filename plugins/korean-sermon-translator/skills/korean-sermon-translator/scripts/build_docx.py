"""Build the translated sermon as a .docx from a JSON list of paragraphs.

Usage: python build_docx.py <content.json> <output.docx>

Each JSON item is one paragraph:
  {"style": "title" | "h1" | "h2" | "scripture" | "body" | "blank",
   "text": "plain text"}                       # or, for mixed formatting:
   "segs": [{"t": "text", "b": true, "u": true, "c": "0000FF"}, ...]

Segment keys b (bold), u (underline) and c (hex color) override the style.
A line containing Hangul gets no space after it, so each Korean line sits
directly above its English line; other lines get space after.

Uses python-docx on purpose: a docx-js file passed schema validation but
crashed Word (opened in safe mode, blank page).
"""
import json
import re
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

BROWN, BLUE = '834D00', '0000FF'
STYLES = {
    'title':     dict(size=20, b=True, c=BROWN, center=True),
    'h1':        dict(size=15, b=True, c=BROWN, blank_before=True),
    'h2':        dict(size=13, b=True, c=BLUE, blank_before=True),
    'scripture': dict(size=11, b=True),
    'body':      dict(size=11),
}
HANGUL = re.compile('[가-힣]')


def set_fonts(element):
    rpr = element.get_or_add_rPr()
    fonts = rpr.find(qn('w:rFonts'))
    if fonts is None:
        fonts = OxmlElement('w:rFonts')
        rpr.insert(0, fonts)
    for key, name in (('ascii', 'Calibri'), ('hAnsi', 'Calibri'),
                      ('eastAsia', 'Malgun Gothic'), ('cs', 'Times New Roman')):
        fonts.set(qn('w:' + key), name)


def main(src, dst):
    items = json.load(open(src, encoding='utf-8'))
    doc = Document()

    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    for side in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
        setattr(sec, side, Inches(1))

    normal = doc.styles['Normal']
    normal.font.size = Pt(11)
    set_fonts(normal.element)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.25

    prev = None
    for item in items:
        kind = item.get('style', 'body')
        if kind == 'blank':
            doc.add_paragraph()
            prev = kind
            continue
        style = STYLES[kind]
        segs = item.get('segs') or [{'t': item['text']}]
        text = ''.join(s['t'] for s in segs)

        # one blank line before a header pair, not between its Korean and English lines
        if style.get('blank_before') and prev != kind:
            doc.add_paragraph()
        prev = kind
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0 if HANGUL.search(text) else 8)
        if style.get('center'):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for s in segs:
            run = p.add_run(s['t'])
            set_fonts(run._r)
            run.font.size = Pt(style['size'])
            if s.get('b', style.get('b')):
                run.bold = True
            if s.get('u', style.get('u')):
                run.underline = True
            color = s.get('c') or style.get('c')
            if color:
                run.font.color.rgb = RGBColor.from_string(color)

    # centered "- N -" page number
    fp = sec.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.add_run('- ')
    fld = OxmlElement('w:fldSimple')
    fld.set(qn('w:instr'), 'PAGE')
    run, t = OxmlElement('w:r'), OxmlElement('w:t')
    t.text = '1'
    run.append(t)
    fld.append(run)
    fp._p.append(fld)
    fp.add_run(' -')

    # python-docx's template omits the required zoom percent
    zoom = doc.settings.element.find(qn('w:zoom'))
    if zoom is not None:
        zoom.set(qn('w:percent'), '100')

    doc.save(dst)
    print('saved', dst)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
