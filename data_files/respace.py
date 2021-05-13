




from __future__ import with_statement

import sys
import os
import re
import codecs


try:
    import xml.etree.ElementTree as ET
except ImportError: 
    import cElementTree as ET










INSERTED_ELEMENT_TAG = "n2t-spc"

INPUT_ENCODING="UTF-8"
OUTPUT_ENCODING="UTF-8"


options = None

newline_wrap_element = set([
        "CURRENT_TITLE",

        "CURRENT_AUTHORLIST",

        "ABSTRACT",
        "P",

        "TABLE",
        "FIGURE",

        "HEADER",

        "REFERENCE",

        "article-title",
        "abstract",
        "title",
        "sec",
        "p",
        "contrib",   
        "aff",       
        "pub-date",  
        "copyright-statement",
        "table",
        "table-wrap",
        "figure",
        "fig",       
        "tr",        
        "kwd-group", 
        ])

space_wrap_element = set([
        "AUTHOR",
        "SURNAME",

        "CURRENT_AUTHOR",
        "CURRENT_SURNAME",

        "TITLE",
        "JOURNAL",

        "YEAR",

        
        "surname",
        "given-names",
        "email",
        
        "volume",
        "issue",
        "year",
        "month",
        "day",
        "fpage",
        "lpage",
        "pub-id",
        "copyright-year",
        
        "journal-id",
        "journal-title",
        "issn",
        "publisher-name",
        
        "article-id",
        "kwd",  
        
        "label",
        "th",
        "td",
        ])



strip_element = newline_wrap_element | space_wrap_element

class Standoff:
    def __init__(self, element, start, end):
        self.element = element
        self.start   = start
        self.end     = end

def txt(s):
    return s if s is not None else ""

def text_and_standoffs(e):
    strings, standoffs = [], []
    _text_and_standoffs(e, 0, strings, standoffs)
    text = "".join(strings)
    return text, standoffs
    
def _text_and_standoffs(e, curroff, strings, standoffs):
    startoff = curroff
    
    
    so = Standoff(e, 0, 0)
    standoffs.append(so)
    if e.text is not None and e.text != "":
        strings.append(e.text)
        curroff += len(e.text)
    curroff = _subelem_text_and_standoffs(e, curroff, strings, standoffs)
    so.start = startoff
    so.end   = curroff
    return curroff

def _subelem_text_and_standoffs(e, curroff, strings, standoffs):
    startoff = curroff
    for s in e:
        curroff = _text_and_standoffs(s, curroff, strings, standoffs)
        if s.tail is not None and s.tail != "":
            strings.append(s.tail)
            curroff += len(s.tail)
    return curroff

def preceding_space(pos, text, rewritten={}):
    while pos > 0:
        pos -= 1
        if pos not in rewritten: 
            
            return text[pos].isspace()           
        elif rewritten[pos] is not None:
            
            return rewritten[pos].isspace()
        else:
            
            pass
    
    return True

def following_space(pos, text, rewritten={}):
    while pos < len(text):
        if pos not in rewritten: 
            
            return text[pos].isspace()           
        elif rewritten[pos] is not None:
            
            return rewritten[pos].isspace()
        else:
            
            pass
        pos += 1
    
    return True

def preceding_linebreak(pos, text, rewritten={}):
    if pos >= len(text):
        return True    
    while pos > 0:
        pos -= 1
        c = rewritten.get(pos, text[pos])
        if c == "\n":
            return True
        elif c is not None and not c.isspace():
            return False
        else:
            
            pass
    return True

def following_linebreak(pos, text, rewritten={}):
    while pos < len(text):
        c = rewritten.get(pos, text[pos])
        if c == "\n":
            return True
        elif c is not None and not c.isspace():
            return False
        else:
            
            pass
        pos += 1
    return True

def index_in_parent(e, p):
    
    index = None
    for i in range(len(p)):
        if p[i] == e:
            index = i
            break
    assert i is not None, "index_in_parent: error: not parent and child"
    return i

def space_normalize(root, text=None, standoffs=None):
    

    if text is None or standoffs is None:
        text, standoffs = text_and_standoffs(root)

    
    for so in standoffs:
        e = so.element
        if e.text is not None and e.text != "":
            e.text = re.sub(r'\s+', ' ', e.text)
        if e.tail is not None and e.tail != "":
            e.tail = re.sub(r'\s+', ' ', e.tail)

def strip_elements(root, elements_to_strip=set(), text=None, standoffs=None):
    

    if text is None or standoffs is None:
        text, standoffs = text_and_standoffs(root)

    
    
    rewritten = {}
    
    for so in standoffs:
        e = so.element

        
        if e.tag == INSERTED_ELEMENT_TAG:
            continue
        
        
        
        
        if ((e.text is not None and e.text != "" and e.text[0].isspace()) and
            (element_in_set(e, elements_to_strip) or 
             preceding_space(so.start, text, rewritten))):
            l = 0
            while l < len(e.text) and e.text[l].isspace():
                l += 1
            space, end = e.text[:l], e.text[l:]
            for i in range(l):
                assert so.start+i not in rewritten, "ERROR: dup remove at %d"  % (so.start+i)
                rewritten[so.start+i] = None
            e.text = end

        
        
        
        if len(e) == 0:
            if ((e.text is not None and e.text != "" and e.text[-1].isspace()) and
                (element_in_set(e, elements_to_strip) or 
                 following_space(so.end, text, rewritten))):
                l = 0
                while l < len(e.text) and e.text[-l-1].isspace():
                    l += 1
                start, space = e.text[:-l], e.text[-l:]
                for i in range(l):
                    o = so.end-i-1
                    assert o not in rewritten, "ERROR: dup remove"
                    rewritten[o] = None
                e.text = start
                    
        else:
            c = e[-1]
            if ((c.tail is not None and c.tail != "" and c.tail[-1].isspace()) and
                (element_in_set(e, elements_to_strip) or 
                 following_space(so.end, text, rewritten))):
                l = 0
                while l < len(c.tail) and c.tail[-l-1].isspace():
                    l += 1
                start, space = c.tail[:-l], c.tail[-l:]
                for i in range(l):
                    o = so.end-i-1
                    assert o not in rewritten, "ERROR: dup remove"
                    rewritten[o] = None
                c.tail = start

def trim_tails(root):
    

    
    
    
    

    
    text, standoffs = text_and_standoffs(root)

    for so in standoffs:
        e = so.element

        if (e.tail is not None and e.tail != "" and e.tail[0].isspace() and
            preceding_space(so.end, text)):
            l = 0
            while l < len(e.tail) and e.tail[l].isspace():
                l += 1
            space, end = e.tail[:l], e.tail[l:]
            e.tail = end

def reduce_space(root, elements_to_strip=set()):
    

    
    text, standoffs = text_and_standoffs(root)

    strip_elements(root, elements_to_strip, text, standoffs)

    trim_tails(root)

    space_normalize(root, text, standoffs)

def element_in_set(e, s):
    
    if e.tag[0] == "{":
        tag = re.sub(r'\{.*?\}', '', e.tag)
    else:
        tag = e.tag
    return tag in s

def process(fn):
    global strip_element
    global options

    
    if fn == "-":
        fn = "/dev/stdin"

    try:
        tree = ET.parse(fn)
    except:
        print >> sys.stderr, "Error parsing %s" % fn
        raise

    root = tree.getroot()

    

    reduce_space(root, strip_element)

    

    
    text, standoffs = text_and_standoffs(root)

    
    
    
    
    
    respace = {}
    for so in standoffs:
        e = so.element
        if element_in_set(e, newline_wrap_element):
            
            if not (so.start in respace and (respace[so.start][0] == "\n" and
                                             respace[so.start][1] == False)):
                respace[so.start] = ("\n", True)
            respace[so.end] = ("\n", False)
        elif element_in_set(e, space_wrap_element):
            
            if not (so.start in respace and (respace[so.start][0] == "\n" or
                                             respace[so.start][1] == False)):
                respace[so.start] = (" ", True)
            if not (so.end in respace and respace[so.end][0] == "\n"):
                respace[so.end] = (" ", False)

    
    

    
    
    
    
    
    
    rewritten = {}

    filtered = {}
    for pos in sorted(respace.keys()):
        if respace[pos][0] == " ":
            
            
            if not (preceding_space(pos, text, rewritten) or
                    following_space(pos, text, rewritten)):
                filtered[pos] = respace[pos]
                rewritten[pos-1] = " "
        else:
            assert respace[pos][0] == "\n", "INTERNAL ERROR"
            
            
            if not (preceding_linebreak(pos, text, rewritten) or 
                    following_linebreak(pos, text, rewritten)):
                filtered[pos] = respace[pos]                
                rewritten[pos-1] = "\n"
    respace = filtered

    
    parent_map = {}
    for parent in root.getiterator():
        for child in parent:
            parent_map[child] = parent

    
    
    
    
    end_map = {}
    for so in standoffs:
        if so.end not in end_map:
            end_map[so.end] = []
        end_map[so.end].append(so)

    
    for so in standoffs:

        if so.start in respace and respace[so.start][1] == True:
            
            
            
            
            
            

            e = so.element
            assert e in parent_map, "INTERNAL ERROR: add space before root?"
            p = parent_map[e]
            i = index_in_parent(e, p)

            rse = ET.Element(INSERTED_ELEMENT_TAG)
            rse.text = respace[so.start][0]
            p.insert(i, rse)

            
            del respace[so.start]

        if so.end in respace and respace[so.end][1] == False:
            
            
            
            maxlen = max([s.end-s.start for s in end_map[so.end]])
            if so.end-so.start != maxlen:
                continue
            longest = [s for s in end_map[so.end] if s.end-s.start == maxlen]
            if so != longest[0]:
                continue

            
            e = so.element
            assert e in parent_map, "INTERNAL ERROR: add space after root?"
            p = parent_map[e]
            i = index_in_parent(e, p)

            rse = ET.Element(INSERTED_ELEMENT_TAG)
            rse.text = respace[so.end][0]
            p.insert(i+1, rse)
            
            rse.tail = e.tail
            e.tail = ""

            
            del respace[so.end]

    assert len(respace) == 0, "INTERNAL ERROR: failed to insert %s" % str(respace)

    
    
    strip_elements(root)
    trim_tails(root)

    

    if options.stdout:
        tree.write(sys.stdout, encoding=OUTPUT_ENCODING)
        return True

    if options is not None and options.directory is not None:
        output_dir = options.directory
    else:
        output_dir = ""

    output_fn = os.path.join(output_dir, os.path.basename(fn))

    
    
    if output_fn == fn and not options.overwrite:
        print >> sys.stderr, 'respace: skipping output for %s: file would overwrite input (consider -d and -o options)' % fn
    else:
        
        try:
            with open(output_fn, 'w') as of:
                tree.write(of, encoding=OUTPUT_ENCODING)
        except IOError, ex:
            print >> sys.stderr, 'respace: failed write: %s' % ex
                
    return True


def argparser():
    import argparse
    ap=argparse.ArgumentParser(description='Revise whitespace content of a PMC NXML file for text extraction.')
    ap.add_argument('-d', '--directory', default=None, metavar='DIR', help='output directory')
    ap.add_argument('-o', '--overwrite', default=False, action='store_true', help='allow output to overwrite input files')
    ap.add_argument('-s', '--stdout', default=False, action='store_true', help='output to stdout')
    ap.add_argument('file', nargs='+', help='input PubMed Central NXML file')
    return ap

def main(argv):
    global options

    options = argparser().parse_args(argv[1:])

    for fn in options.file:
        process(fn)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
