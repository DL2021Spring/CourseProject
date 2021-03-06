





from __future__ import with_statement

import sys
import re
import os
import codecs

INPUT_ENCODING = "ASCII"
OUTPUT_ENCODING = "UTF-8"

output_directory = None

def unescape_PTB(s):
    
    
    return s.replace("-LRB-", "(").replace("-RRB-", ")").replace("-LSB-", "[").replace("-RSB-", "]").replace("-LCB-", "{").replace("-RCB-", "}").replace('``', '"'). replace("''", '"').replace('\\/', '/')

def quote(s):
    return s in ('"', )

def space(t1, t2, quote_count = None):
    
    
    

    if re.match(r'^[\($]$', t1):
        return False
    if re.match(r'^[.,;%\)\?\!]$', t2):
        return False
    if quote(t1) and quote_count is not None and quote_count % 2 == 1:
        return False
    if quote(t2) and quote_count is not None and quote_count % 2 == 1:
        return False
    return True

def tagstr(start, end, ttype, idnum, text):
    
    assert '\n' not in text, "ERROR: newline in entity '%s'" % (text)
    assert text == text.strip(), "ERROR: tagged span contains extra whitespace: '%s'" % (text)
    return "T%d\t%s %d %d\t%s" % (idnum, ttype, start, end, text)

def output(infn, docnum, sentences):
    global output_directory

    if output_directory is None:
        txtout = sys.stdout
        soout = sys.stdout
    else:
        outfn = os.path.join(output_directory, os.path.basename(infn)+'-doc-'+str(docnum))
        txtout = codecs.open(outfn+'.txt', 'wt', encoding=OUTPUT_ENCODING)
        soout = codecs.open(outfn+'.ann', 'wt', encoding=OUTPUT_ENCODING)

    offset, idnum = 0, 1

    doctext = ""

    for si, sentence in enumerate(sentences):

        prev_token = None
        prev_tag = "O"
        curr_start, curr_type = None, None
        quote_count = 0

        for token, ttag, ttype in sentence:

            if curr_type is not None and (ttag != "I" or ttype != curr_type):
                
                
                print >> soout, tagstr(curr_start, offset, curr_type, idnum, doctext[curr_start:offset])
                idnum += 1
                curr_start, curr_type = None, None

            if prev_token is not None and space(prev_token, token, quote_count):
                doctext = doctext + ' '
                offset += 1

            if curr_type is None and ttag != "O":
                
                curr_start, curr_type = offset, ttype

            doctext = doctext + token
            offset += len(token)

            if quote(token):
                quote_count += 1

            prev_token = token
            prev_tag = ttag
        
        
        if curr_type is not None:
            print >> soout, tagstr(curr_start, offset, curr_type, idnum, doctext[curr_start:offset])
            idnum += 1

        if si+1 != len(sentences):
            doctext = doctext + '\n'        
            offset += 1
            
    print >> txtout, doctext

def process(fn):
    docnum = 1
    sentences = []

    with codecs.open(fn, encoding=INPUT_ENCODING) as f:

        
        current = []

        lines = f.readlines()

        for ln, l in enumerate(lines):
            l = l.strip()

            if re.match(r'^\s*$', l):
                
                if len(current) > 0:
                    sentences.append(current)
                current = []

                
                if len(sentences) >= 10:
                    output(fn, docnum, sentences)
                    sentences = []
                    docnum += 1

                continue

            
            
            
            m = re.match(r'^(\S+)\s(\S+)$', l)
            if not m:
                m = re.match(r'^(\S+)\s\S+\s(\S+)$', l)
            assert m, "Error parsing line %d: %s" % (ln+1, l)
            token, tag = m.groups()

            
            m = re.match(r'^([BIO])((?:-[A-Za-z_]+)?)$', tag)
            assert m, "ERROR: failed to parse tag '%s' in %s" % (tag, fn)
            ttag, ttype = m.groups()
            if len(ttype) > 0 and ttype[0] == "-":
                ttype = ttype[1:]

            token = unescape_PTB(token)

            current.append((token, ttag, ttype))

        
        if len(current) > 0:
            sentences.append(current)
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
            print >> sys.stderr, "Error processing %s: %s" % (fn, e)
            fail_count += 1

    if fail_count > 0:
        print >> sys.stderr,  % (fail_count, len(filenames))

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
