




from __future__ import with_statement

import sys
import re
import os

def char_offsets(text, start, end, ttext):
    
    
    
    
    
    

    
    idx, nospcidx = 0,0
    while True:
        while idx < len(text) and text[idx].isspace():
            idx += 1
        assert idx < len(text), "Error in data"
        if nospcidx == start:
            break
        nospcidx += 1
        idx += 1

    char_start = idx

    
    while nospcidx < end:
        nospcidx += 1
        idx += 1
        while idx < len(text) and text[idx].isspace():
            idx += 1
        
    char_end = idx+1

    
    
    if (text[char_start:char_end] == '/translation upstream factor' and
        ttext                     == 'translation upstream factor'):
        print >> sys.stderr, "NOTE: applying special-case fix ..."
        char_start += 1

    
    ref_text = text[char_start:char_end]
    assert ref_text == ttext, "Mismatch: '%s' vs '%s' [%d:%d] (%s %d-%d)" % (ttext, ref_text, char_start, char_end, text, start, end)

    return char_start, char_end

def main(argv):
    if len(argv) != 4:
        print >> sys.stderr, "Usage:", argv[0], "BC2TEXT BC2TAGS OUTPUT-DIR"
        return 1

    textfn, tagfn, outdir = argv[1:]

    
    tags = {}
    with open(tagfn, 'rU') as tagf:
        for l in tagf:
            l = l.rstrip('\n')
            m = re.match(r'^([^\|]+)\|(\d+) (\d+)\|(.*)$', l)
            assert m, "Format error in %s: %s" % (tagfn, l)
            sid, start, end, text = m.groups()
            start, end = int(start), int(end)

            if sid not in tags:
                tags[sid] = []
            tags[sid].append((start, end, text))

    
    texts = {}
    with open(textfn, 'rU') as textf:
        for l in textf:
            l = l.rstrip('\n')
            m = re.match(r'(\S+) (.*)$', l)
            assert m, "Format error in %s: %s" % (textfn, l)
            sid, text = m.groups()

            assert sid not in texts, "Error: duplicate ID %s" % sid
            texts[sid] = text

    
    
    offsets = {}
    for sid in texts:
        offsets[sid] = []
        for start, end, ttext in tags.get(sid,[]):
            soff, eoff = char_offsets(texts[sid], start, end, ttext)
            offsets[sid].append((soff, eoff))

    
    for sid in texts:
        with open(os.path.join(outdir, sid+".txt"), 'w') as txtf:
            print >> txtf, texts[sid]
        with open(os.path.join(outdir, sid+".ann"), 'w') as annf:
            tidx = 1
            for soff, eoff in offsets[sid]:
                print >> annf, "T%d\tGENE %d %d\t%s" % (tidx, soff, eoff, texts[sid][soff:eoff])
                tidx += 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
