




from __future__ import with_statement

import sys
import re
import os
import codecs

class taggedEntity:
    def __init__(self, startOff, endOff, eType, idNum, fullText):
        self.startOff = startOff
        self.endOff   = endOff  
        self.eType    = eType   
        self.idNum    = idNum   
        self.fullText = fullText

        self.eText = fullText[startOff:endOff]

    def __str__(self):
        return "T%d\t%s %d %d\t%s" % (self.idNum, self.eType, self.startOff, 
                                      self.endOff, self.eText)

    def check(self):
        
        
        assert "\n" not in self.eText, \
            "ERROR: newline in entity: '%s'" % self.eText
        assert self.eText == self.eText.strip(), \
            "ERROR: entity contains extra whitespace: '%s'" % self.eText

def BIO_to_standoff(BIOtext, reftext, tokenidx=2, tagidx=-1):
    BIOlines = BIOtext.split('\n')
    return BIO_lines_to_standoff(BIOlines, reftext, tokenidx, tagidx)

next_free_id_idx = 1

def BIO_lines_to_standoff(BIOlines, reftext, tokenidx=2, tagidx=-1):
    global next_free_id_idx

    taggedTokens = []

    ri, bi = 0, 0
    while(ri < len(reftext)):
        if bi >= len(BIOlines):
            print >> sys.stderr, "Warning: received BIO didn't cover given text"
            break

        BIOline = BIOlines[bi]

        if re.match(r'^\s*$', BIOline):
            
            bi += 1
        else:
            
            fields = BIOline.split('\t')

            try:
                tokentext = fields[tokenidx]
            except:
                print >> sys.stderr, "Error: failed to get token text " \
                    "(field %d) on line: %s" % (tokenidx, BIOline)
                raise

            try:
                tag = fields[tagidx]
            except:
                print >> sys.stderr, "Error: failed to get token text " \
                    "(field %d) on line: %s" % (tagidx, BIOline)
                raise

            m = re.match(r'^([BIO])((?:-[A-Za-z0-9_-]+)?)$', tag)
            assert m, "ERROR: failed to parse tag '%s'" % tag
            ttag, ttype = m.groups()

            
            if len(ttype) > 0 and ttype[0] == "-":
                ttype = ttype[1:]

            
            assert ((ttype == "" and ttag == "O") or
                    (ttype != "" and ttag in ("B","I"))), \
                    "Error: tag/type mismatch %s" % tag

            
            while ri < len(reftext) and reftext[ri].isspace():
                ri += 1

            
            assert reftext[ri:ri+len(tokentext)] == tokentext, \
                "ERROR: text mismatch: reference '%s' tagged '%s'" % \
                (reftext[ri:ri+len(tokentext)].encode("UTF-8"), 
                 tokentext.encode("UTF-8"))

            
            taggedTokens.append((ri, ri+len(tokentext), ttag, ttype))
            
            
            ri += len(tokentext)
            bi += 1

            
            while ri < len(reftext) and reftext[ri].isspace():
                ri += 1
            
    
    
    if (len([c for c in reftext[ri:] if not c.isspace()]) != 0 or
        len([c for c in BIOlines[bi:] if not re.match(r'^\s*$', c)]) != 0):
        assert False, "ERROR: failed alignment: '%s' remains in reference, " \
            "'%s' in tagged" % (reftext[ri:], BIOlines[bi:])

    standoff_entities = []

    
    
    revisedTagged = []
    prevTag = None
    for startoff, endoff, ttag, ttype in taggedTokens:
        if prevTag == "O" and ttag == "I":
            print >> sys.stderr, "Note: rewriting \"I\" -> \"B\" after \"O\""
            ttag = "B"
        revisedTagged.append((startoff, endoff, ttag, ttype))
        prevTag = ttag
    taggedTokens = revisedTagged

    
    
    revisedTagged = []
    prevTag, prevType = None, None
    for startoff, endoff, ttag, ttype in taggedTokens:
        if prevTag in ("B", "I") and ttag == "I" and prevType != ttype:
            print >> sys.stderr, "Note: rewriting \"I\" -> \"B\" at type switch"
            ttag = "B"
        revisedTagged.append((startoff, endoff, ttag, ttype))
        prevTag, prevType = ttag, ttype
    taggedTokens = revisedTagged    

    prevTag, prevEnd = "O", 0
    currType, currStart = None, None
    for startoff, endoff, ttag, ttype in taggedTokens:

        if prevTag != "O" and ttag != "I":
            
            assert currType is not None and currStart is not None, \
                "ERROR in %s" % fn
            
            standoff_entities.append(taggedEntity(currStart, prevEnd, currType, 
                                                  next_free_id_idx, reftext))

            next_free_id_idx += 1

            
            currType, currStart = None, None

        elif prevTag != "O":
            
            assert ttag == "I", "ERROR in %s" % fn
            assert currType == ttype, "ERROR: entity of type '%s' continues " \
                "as type '%s'" % (currType, ttype)
            
        if ttag == "B":
            
            currType, currStart = ttype, startoff
            
        prevTag, prevEnd = ttag, endoff

    
    
    if prevTag != "O":
        standoff_entities.append(taggedEntity(currStart, prevEnd, currType,
                                              next_free_id_idx, reftext))
        next_free_id_idx += 1

    for e in standoff_entities:
        e.check()

    return standoff_entities


RANGE_RE = re.compile(r'^(-?\d+)-(-?\d+)$')

def parse_indices(idxstr):
    
    
    indices = []
    for i in idxstr.split(','):
        if not RANGE_RE.match(i):
            indices.append(int(i))
        else:
            start, end = RANGE_RE.match(i).groups()
            for j in range(int(start), int(end)):
                indices.append(j)
    return indices

def main(argv):
    if len(argv) < 3 or len(argv) > 5:
        print >> sys.stderr, "Usage:", argv[0], "TEXTFILE BIOFILE [TOKENIDX [BIOIDX]]"
        return 1
    textfn, biofn = argv[1], argv[2]

    tokenIdx = None
    if len(argv) >= 4:
        tokenIdx = int(argv[3])
    bioIdx = None
    if len(argv) >= 5:
        bioIdx = argv[4]

    with open(textfn, 'rU') as textf:
        text = textf.read()
    with open(biofn, 'rU') as biof:
        bio = biof.read()

    if tokenIdx is None:
        so = BIO_to_standoff(bio, text)
    elif bioIdx is None:
        so = BIO_to_standoff(bio, text, tokenIdx)
    else:
        try:
            indices = parse_indices(bioIdx)
        except:
            print >> sys.stderr, 'Error: failed to parse indices "%s"' % bioIdx
            return 1
        so = []
        for i in indices:
            so.extend(BIO_to_standoff(bio, text, tokenIdx, i))

    for s in so:
        print s

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
