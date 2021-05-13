

import sys
import re
try:
    import cElementTree as ET
except:
    import xml.etree.cElementTree as ET



EXCLUDED_TAGS = [


























]
EXCLUDED_TAG = { t:True for t in EXCLUDED_TAGS }


ELIDED_TEXT_STRING = "[[[...]]]"


MAXIMUM_TEXT_DISPLAY_LENGTH = 1000



def c_escape(s):
    return s.replace('\\', '\\\\').replace('\t','\\t').replace('\n','\\n')

def strip_ns(tag):
    
    return tag if tag[0] != '{' else re.sub(r'\{.*?\}', '', tag)

class Standoff:
    def __init__(self, sid, element, start, end, text):
        self.sid     = sid
        self.element = element
        self.start   = start
        self.end     = end
        self.text    = text

    def compress_text(self, l):
        if len(self.text) >= l:
            el = len(ELIDED_TEXT_STRING)
            sl = (l-el)/2
            self.text = (self.text[:sl]+ELIDED_TEXT_STRING+self.text[-(l-sl-el):])
    def tag(self):
        return strip_ns(self.element.tag)

    def attrib(self):
        
        attrib = {}
        for a in self.element.attrib:
            if a[0] == "{":
                an = re.sub(r'\{.*?\}', '', a)
            else:
                an = a
            attrib[an] = self.element.attrib[a]
        return attrib

    def __str__(self):
        return "X%d\t%s %d %d\t%s\t%s" % \
            (self.sid, self.tag(), self.start, self.end, 
             c_escape(self.text.encode("utf-8")),
             " ".join(['%s="%s"' % (k.encode("utf-8"), v.encode("utf-8"))
                       for k,v in self.attrib().items()]))

def txt(s):
    return s if s is not None else ""

next_free_so_id = 1

def text_and_standoffs(e, curroff=0, standoffs=None):
    global next_free_so_id

    if standoffs == None:
        standoffs = []
    startoff = curroff
    
    
    so = Standoff(next_free_so_id, e, 0, 0, "")
    next_free_so_id += 1
    standoffs.append(so)
    setext, dummy = subelem_text_and_standoffs(e, curroff+len(txt(e.text)), standoffs)
    text = txt(e.text) + setext
    curroff += len(text)
    so.start = startoff
    so.end   = curroff
    so.text  = text
    return (text, standoffs)

def subelem_text_and_standoffs(e, curroff, standoffs):
    startoff = curroff
    text = ""
    for s in e:
        stext, dummy = text_and_standoffs(s, curroff, standoffs)
        text += stext
        text += txt(s.tail)
        curroff = startoff + len(text)
    return (text, standoffs)

def empty_elements(e, tags=None):
    if tags is None or strip_ns(e.tag) in tags:
        e.clear()
    for c in e:
        empty_elements(c, tags)

def add_space(e):
    if strip_ns(e.tag) in ('title', ):
        e.tail = (e.tail if e.tail is not None else '') + '\n'
    for c in e:
        add_space(c)

def convert_coresc1(s):
    sostrings = []

    
    

    tid = "T%d" % convert_coresc1._idseq
    sostrings.append('%s\t%s %d %d\t%s' % \
                         (tid, s.attrib()['type'], s.start, s.end, 
                          s.text.encode('utf-8')))

    

    convert_coresc1._idseq += 1

    return sostrings
convert_coresc1._idseq = 1

convert_function = {
    'CoreSc1' : convert_coresc1,
    'annotationART' : convert_coresc1,
}

def main(argv=[]):
    if len(argv) != 4:
        print >> sys.stderr, "Usage:", argv[0], "IN-XML OUT-TEXT OUT-SO"
        return -1

    in_fn, out_txt_fn, out_so_fn = argv[1:]

    
    if in_fn == "-":
        in_fn = "/dev/stdin"
    if out_txt_fn == "-":
        out_txt_fn = "/dev/stdout"
    if out_so_fn == "-":
        out_so_fn = "/dev/stdout"

    tree = ET.parse(in_fn)
    root = tree.getroot()

    
    empty_elements(root, set(['article-categories', 
                              'copyright-statement', 'license', 
                              'copyright-holder', 'copyright-year',
                              'journal-meta', 'article-id',
                              'back', 
                              'fig', 'table-wrap', 
                              'contrib-group',
                              'aff', 'author-notes',
                              'pub-date', 
                              'volume', 'issue', 
                              'fpage', 'lpage', 
                              'history'
                              ]))

    add_space(root)
    

    text, standoffs = text_and_standoffs(root)

    
    standoffs = [s for s in standoffs if not s.tag() in EXCLUDED_TAG]

    
    converted = []
    for s in standoffs:
        if s.tag() in convert_function:
            converted.extend(convert_function[s.tag()](s))


    standoffs = converted

    for so in standoffs:
        try:
            so.compress_text(MAXIMUM_TEXT_DISPLAY_LENGTH)
        except AttributeError:
            pass

    
    out_txt = open(out_txt_fn, "wt")
    out_so  = open(out_so_fn, "wt")

    out_txt.write(text.encode("utf-8"))
    for so in standoffs:
        print >> out_so, so

    out_txt.close()
    out_so.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
