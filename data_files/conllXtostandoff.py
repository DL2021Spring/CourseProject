





from __future__ import with_statement

import sys
import re
import os
import codecs



MAX_DOC_SENTENCES = 10


OUTPUT_ROOT = True

ROOT_STR = 'ROOT'

INPUT_ENCODING = "UTF-8"
OUTPUT_ENCODING = "UTF-8"

output_directory = None



charmap = {
    '<' : '_lt_',
    '>' : '_gt_',
    '+' : '_plus_',
    '?' : '_question_',
    '&' : '_amp_',
    ':' : '_colon_',
    '.' : '_period_',
    '!' : '_exclamation_',
}

def maptype(s):
    return "".join([charmap.get(c,c) for c in s])

def tokstr(start, end, ttype, idnum, text):
    
    assert '\n' not in text, "ERROR: newline in entity '%s'" % (text)
    assert text == text.strip(), "ERROR: tagged span contains extra whitespace: '%s'" % (text)
    return "T%d\t%s %d %d\t%s" % (idnum, maptype(ttype), start, end, text)

def depstr(depid, headid, rel, idnum):
    return "R%d\t%s Arg1:T%d Arg2:T%d" % (idnum, maptype(rel), headid, depid)

def output(infn, docnum, sentences):
    global output_directory

    if output_directory is None:
        txtout = sys.stdout
        soout = sys.stdout
    else:
        
        
        if MAX_DOC_SENTENCES:
            outfnbase = os.path.basename(infn)+'-doc-'+str(docnum)
        else:
            outfnbase = os.path.basename(infn)
        outfn = os.path.join(output_directory, outfnbase)
        txtout = codecs.open(outfn+'.txt', 'wt', encoding=OUTPUT_ENCODING)
        soout = codecs.open(outfn+'.ann', 'wt', encoding=OUTPUT_ENCODING)

    offset, idnum, ridnum = 0, 1, 1

    doctext = ""

    for si, sentence in enumerate(sentences):
        tokens, deps = sentence

        
        
        idmap = {}

        
        prev_form = None

        if OUTPUT_ROOT:
            
            tokens = [('0', ROOT_STR, ROOT_STR)] + tokens

        for ID, form, POS in tokens:

            if prev_form is not None:
                doctext = doctext + ' '
                offset += 1

            
            print >> soout, tokstr(offset, offset+len(form), POS, idnum, form)
            assert ID not in idmap, "Error in data: dup ID"
            idmap[ID] = idnum
            idnum += 1

            doctext = doctext + form
            offset += len(form)
            
            prev_form = form

        
        for dep, head, rel in deps:

            
            if not OUTPUT_ROOT and head == '0':
                continue

            print >> soout, depstr(idmap[dep], idmap[head], rel, ridnum)
            ridnum += 1
        
        if si+1 != len(sentences):
            doctext = doctext + '\n'        
            offset += 1
            
    print >> txtout, doctext

def process(fn):
    docnum = 1
    sentences = []

    with codecs.open(fn, encoding=INPUT_ENCODING) as f:

        tokens, deps = [], []

        lines = f.readlines()

        for ln, l in enumerate(lines):
            l = l.strip()

            
            if len(l) > 0 and l[0] == "#":
                continue

            if re.match(r'^\s*$', l):
                
                if len(tokens) > 0:
                    sentences.append((tokens, deps))
                tokens, deps = [], []

                
                if MAX_DOC_SENTENCES and len(sentences) >= MAX_DOC_SENTENCES:
                    output(fn, docnum, sentences)
                    sentences = []
                    docnum += 1

                continue

            
            
            
            
            
            
            
            
            fields = l.split('\t')

            assert len(fields) == 10, "Format error on line %d in %s: expected 10 fields, got %d: %s" % (ln, fn, len(fields), l)

            ID, form, POS = fields[0], fields[1], fields[4]
            head, rel = fields[6], fields[7]

            tokens.append((ID, form, POS))
            
            if head != "_":
                deps.append((ID, head, rel))

        
        if len(tokens) > 0:
            sentences.append((tokens, deps))
        if len(sentences) > 0:
            output(fn, docnum, sentences)

def main(argv):
    global output_directory

    
    output_directory = None
    filenames = argv[1:]
    if len(argv) > 2 and argv[1] == "-o":
        output_directory = argv[2]
        print >> sys.stderr, "Writing output to %s" % output_directory
        filenames = argv[3:]

    fail_count = 0
    for fn in filenames:
        try:
            process(fn)
        except Exception, e:
            m = unicode(e).encode(OUTPUT_ENCODING)
            print >> sys.stderr, "Error processing %s: %s" % (fn, m)
            fail_count += 1

    if fail_count > 0:
        print >> sys.stderr,  % (fail_count, len(filenames))

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
