




import sys
import re
import os
import codecs


FIELDED_OUTPUT_RE = re.compile(r'^\d+\|')

class taggedEntity:
    def __init__(self, startOff, endOff, eType, idNum):
        self.startOff = startOff
        self.endOff   = endOff  
        self.eType    = eType   
        self.idNum    = idNum   

    def __str__(self):
        return "T%d\t%s %d %d" % (self.idNum, self.eType, self.startOff, self.endOff)

def MetaMap_lines_to_standoff(metamap_lines, reftext=None):
    tagged = []
    idseq = 1
    for l in metamap_lines:
        l = l.rstrip('\n')

        
        if not FIELDED_OUTPUT_RE.match(l):
            continue
        
        
        
        
        
        
        
        fields = l.split('|')

        if len(fields) < 9:
            print >> sys.stderr, "Note: skipping unparseable MetaMap output line: %s" % l
            continue

        ctext, CUI, semtype, offset = fields[3], fields[4], fields[5], fields[8]

        
        semtype = semtype.replace('[','').replace(']','')

        
        
        
        m = re.match(r'^(?:\d+:\d+,)*(\d+):(\d+)$', offset)
        start, length = m.groups()
        start, length = int(start), int(length)

        tagged.append(taggedEntity(start, start+length, semtype, idseq))
        idseq += 1


    print >> sys.stderr, "MetaMaptoStandoff: returning %s tagged spans" % len(tagged)

    return tagged

if __name__ == "__main__":
    lines = [l for l in sys.stdin]
    standoff = MetaMap_lines_to_standoff(lines)
    for s in standoff:
        print s

