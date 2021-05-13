




from __future__ import with_statement

import sys
import re
import os
import codecs



MAX_DOC_SENTENCES = 10


OUTPUT_ROOT = True

ROOT_STR = 'ROOT'
ROOT_POS = 'ROOT'
ROOT_FEAT = ''

INPUT_ENCODING = "UTF-8"
OUTPUT_ENCODING = "UTF-8"





F_ID, F_FORM, F_LEMMA, F_POS, F_FEAT, F_HEAD, F_DEPREL, F_FILLPRED, F_PRED, F_APRED1 = range(10)

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

def featstr(lemma, feats, idnum):
    return "#%d\tData T%d\tLemma: %s, Feats: %s" % (idnum, idnum, lemma, feats)

def depstr(depid, headid, rel, idnum):
    return "R%d\t%s Arg1:T%d Arg2:T%d" % (idnum, maptype(rel), headid, depid)

def output(infn, docnum, sentences):
    global output_directory

    if output_directory is None:
        txtout = codecs.getwriter(OUTPUT_ENCODING)(sys.stdout)
        soout = codecs.getwriter(OUTPUT_ENCODING)(sys.stdout)
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
            
            tokens[0] = (ROOT_STR, ROOT_STR, ROOT_POS, ROOT_FEAT)

        for id_ in tokens:

            form, lemma, pos, feat = tokens[id_]

            if prev_form is not None:
                doctext = doctext + ' '
                offset += 1

            
            print >> soout, tokstr(offset, offset+len(form), pos, idnum, form)
            print >> soout, featstr(lemma, feat, idnum)
            assert id_ not in idmap, "Error in data: dup ID"
            idmap[id_] = idnum
            idnum += 1

            doctext = doctext + form
            offset += len(form)
            
            prev_form = form

        
        for head in deps:
            for dep in deps[head]:
                for rel in deps[head][dep]:
                    
                    if not OUTPUT_ROOT and head == 0:
                        continue
                    
                    print >> soout, depstr(idmap[dep], idmap[head], rel, ridnum)
                    ridnum += 1
        
        if si+1 != len(sentences):
            doctext = doctext + '\n'        
            offset += 1
            
    print >> txtout, doctext

def read_sentences(fn):
    
    
    sentences=[[]]
    with codecs.open(fn, 'rU', INPUT_ENCODING) as f:
        for line in f:
            line=line.rstrip()
            if not line:
                continue
            
            if line and line[0] == "#":
                continue
            cols=line.split(u'\t')
            
            
            if cols[0] == u'1' and sentences[-1]:
                sentences.append([])
            sentences[-1].append(cols)
    return sentences

def resolve_format(sentences, options):
    fields = {}

    

    
    
    fields[F_ID] = 0
    fields[F_FORM] = 1
    fields[F_LEMMA] = 2
    
    fields[F_POS] = 4
    
    fields[F_FEAT] = 6
    
    fields[F_HEAD] = 8
    
    fields[F_DEPREL] = 10
    
    fields[F_FILLPRED] = 12
    fields[F_PRED] = 13
    fields[F_APRED1] = 14

    return fields

def mark_dependencies(dependency, head, dependent, deprel):
    if head not in dependency:
        dependency[head] = {}
    if dependent not in dependency[head]:
        dependency[head][dependent] = []
    dependency[head][dependent].append(deprel)
    return dependency

def process_sentence(sentence, fieldmap):
    
    
    dependency = {}
    
    
    token = {}

    for fields in sentence:
        id_ = int(fields[fieldmap[F_ID]])
        form = fields[fieldmap[F_FORM]]
        lemma = fields[fieldmap[F_LEMMA]]
        pos = fields[fieldmap[F_POS]]
        feat = fields[fieldmap[F_FEAT]]
        try:
            head = int(fields[fieldmap[F_HEAD]])
        except ValueError:
            assert fields[fieldmap[F_HEAD]] == 'ROOT', \
                'error: unexpected head: %s' % fields[fieldmap[F_HEAD]]
            head = 0
        deprel = fields[fieldmap[F_DEPREL]]
        
        
        

        mark_dependencies(dependency, head, id_, deprel)
        assert id_ not in token
        token[id_] = (form, lemma, pos, feat)

    return token, dependency
        
def process(fn, options=None):
    docnum = 1
    sentences = read_sentences(fn)

    fieldmap = resolve_format(sentences, options)
    processed = []

    for i, sentence in enumerate(sentences):
        token, dependency = process_sentence(sentence, fieldmap)
        processed.append((token, dependency))

        
        if MAX_DOC_SENTENCES and len(processed) >= MAX_DOC_SENTENCES:
            output(fn, docnum, processed)
            processed = []
            docnum += 1

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
            raise
            
            

    if fail_count > 0:
        print >> sys.stderr,  % (fail_count, len(filenames))

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
