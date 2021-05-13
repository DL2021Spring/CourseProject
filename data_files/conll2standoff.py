





import sys
import re
import os
import codecs

try:
    import psyco
    psyco.full()
except:
    pass





SEQUENCE_ERROR_RECOVER, SEQUENCE_ERROR_DISCARD, SEQUENCE_ERROR_FAIL = range(3)

SEQUENCE_ERROR_PROCESSING = SEQUENCE_ERROR_RECOVER




out = sys.stdout
reference_directory = None
output_directory = None

def reference_text_filename(fn):
    
    

    fnbase = os.path.basename(fn)
    reffn = os.path.join(reference_directory, fnbase)

    
    
    if not os.path.exists(reffn):
        reffn = re.sub(r'(.*)\..*', r'\1.txt', reffn)

    return reffn

def output_filename(fn):
    if output_directory is None:
        return None

    reffn = reference_text_filename(fn)
    return os.path.join(output_directory, os.path.basename(reffn).replace(".txt",".a1"))

def process(fn):
    global out

    reffn = reference_text_filename(fn)

    try:
        
        reffile = codecs.open(reffn, "rt", "UTF-8")
    except:
        print >> sys.stderr, "ERROR: failed to open reference file %s" % reffn
        raise
    reftext = reffile.read()
    reffile.close()

    
    try:
        
        tagfile = codecs.open(fn, "rt", "UTF-8")
    except:
        print >> sys.stderr, "ERROR: failed to open file %s" % fn
        raise
    tagtext = tagfile.read()
    tagfile.close()

    
    
    if output_directory is not None:
        outfn = output_filename(fn)
        
        out = open(outfn, "wt")

    
    
    
    
    
    
    
    
    
    

    taggedTokens = []
    for ln, l in enumerate(tagtext.split('\n')):
        if l.strip() == '':
            
            continue

        fields = l.split('\t')
        assert len(fields) == 7, "Error: expected 7 tab-separated fields on line %d in %s, found %d: %s" % (ln+1, fn, len(fields), l.encode("UTF-8"))

        start, end, ttext = fields[0:3]
        tag = fields[6]
        start, end = int(start), int(end)

        
        m = re.match(r'^([BIO])((?:-[A-Za-z_]+)?)$', tag)
        assert m, "ERROR: failed to parse tag '%s' in %s" % (tag, fn)
        ttag, ttype = m.groups()

        
        if len(ttype) > 0 and ttype[0] == "-":
            ttype = ttype[1:]

        
        assert ((ttype == "" and ttag == "O") or
                (ttype != "" and ttag in ("B","I"))), "Error: tag format '%s' in %s" % (tag, fn)

        
        assert reftext[start:end] == ttext, "ERROR: text mismatch for %s on line %d: reference '%s' tagged '%s': %s" % (fn, ln+1, reftext[start:end].encode("UTF-8"), ttext.encode("UTF-8"), l.encode("UTF-8"))

        
        taggedTokens.append((start, end, ttag, ttype))

    
    
    
    

    

    
    
    def entityStr(startOff, endOff, eType, idNum, fullText):
        
        
        eText = fullText[startOff:endOff]
        assert "\n" not in eText, "ERROR: newline in entity in %s: '%s'" % (fn, eText)
        assert eText == eText.strip(), "ERROR: entity contains extra whitespace in %s: '%s'" % (fn, eText)
        return "T%d\t%s %d %d\t%s" % (idNum, eType, startOff, endOff, eText)

    idIdx = 1
    prevTag, prevEnd = "O", 0
    currType, currStart = None, None
    for startoff, endoff, ttag, ttype in taggedTokens:

        
        
        
        
        if prevTag != "O" and ttag == "I" and currType != ttype:
            if SEQUENCE_ERROR_PROCESSING == SEQUENCE_ERROR_RECOVER:
                
                ttag = "B"
            elif SEQUENCE_ERROR_PROCESSING == SEQUENCE_ERROR_DISCARD:
                ttag = "O"
            else:
                assert SEQUENCE_ERROR_PROCESSING == SEQUENCE_ERROR_FAIL
                pass 

        
        if prevTag == "O" and ttag == "I":
            if SEQUENCE_ERROR_PROCESSING == SEQUENCE_ERROR_RECOVER:
                ttag = "B"            
            elif SEQUENCE_ERROR_PROCESSING == SEQUENCE_ERROR_DISCARD:
                ttag = "O"
            else:
                assert SEQUENCE_ERROR_PROCESSING == SEQUENCE_ERROR_FAIL
                pass 

        if prevTag != "O" and ttag != "I":
            
            assert currType is not None and currStart is not None, "ERROR at %s (%d-%d) in %s" % (reftext[startoff:endoff], startoff, endoff, fn)
            
            print >> out, entityStr(currStart, prevEnd, currType, idIdx, reftext).encode("UTF-8")

            idIdx += 1

            
            currType, currStart = None, None

        elif prevTag != "O":
            
            assert ttag == "I", "ERROR in %s" % fn
            assert currType == ttype, "ERROR: entity of type '%s' continues as type '%s' in %s" % (currType, ttype, fn)
            
        if ttag == "B":
            
            currType, currStart = ttype, startoff
            
        prevTag, prevEnd = ttag, endoff

    
    
    if prevTag != "O":
        print >> out, entityStr(currStart, prevEnd, currType, idIdx, reftext).encode("UTF-8")

    if output_directory is not None:
        
        out.close()

def main(argv):
    global reference_directory, output_directory


    

    
    

    if len(argv) < 3 or argv[1] != "-d":
        print >> sys.stderr, "USAGE:", argv[0], "-d REF-DIR [-o OUT-DIR] (FILES|DIR)"
        return 1

    reference_directory = argv[2]

    

    output_directory = None
    filenames = argv[3:]
    if len(argv) > 4 and argv[3] == "-o":
        output_directory = argv[4]
        print >> sys.stderr, "Writing output to %s" % output_directory
        filenames = argv[5:]


    
    
    input_directory = None
    if len(filenames) == 1 and os.path.isdir(filenames[0]):
        input_directory = filenames[0]
        filenames = [os.path.join(input_directory, fn) for fn in os.listdir(input_directory)]
        print >> sys.stderr, "Processing %d files in %s ..." % (len(filenames), input_directory)

    fail_count = 0
    for fn in filenames:
        try:
            process(fn)
        except Exception, e:
            print >> sys.stderr, "Error processing %s: %s" % (fn, e)
            fail_count += 1

            
            
            ofn = output_filename(fn)
            try:
                os.remove(ofn)
            except:
                
                pass

    if fail_count > 0:
        print >> sys.stderr,  % (fail_count, len(filenames))

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
