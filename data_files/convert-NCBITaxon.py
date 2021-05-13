






















from __future__ import with_statement

import sys
import re
import codecs

INPUT_ENCODING = "UTF-8"





DISCARD_NAME_CLASS = [
    "misspelling",
    "misnomer",
    "type material",
    "includes",
    "in-part",
    "authority",
    "teleomorph",
    "genbank anamorph",
    "anamorph",
    "blast name",
]




NAME_CLASS_MAP = {
    "genbank common name" : "common name",
    "genbank synonym" : "synonym",
    "equivalent name" : "synonym",
    "acronym" : "synonym",
    "genbank acronym" : "synonym",
    "genbank anamorph" : "anamorph",
}


NAME_ORDER_BY_CLASS = [
    "scientific name",
    "common name",
    "synonym",
] + DISCARD_NAME_CLASS

def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, "Usage:", argv[0], "names.dmp"
        return 1

    namesfn = argv[1]

    
    names_by_tax_id = {}
    with codecs.open(namesfn, encoding=INPUT_ENCODING) as f:
        for i, l in enumerate(f):
            l = l.strip('\n\r')
            
            fields = l.split('|')

            assert len(fields) >= 4, "Format error on line %d: %s" % (i+1, l)
            fields = [t.strip() for t in fields]
            tax_id, name_txt, name_class = fields[0], fields[1], fields[3]

            if tax_id not in names_by_tax_id:
                names_by_tax_id[tax_id] = []
            names_by_tax_id[tax_id].append((name_txt, name_class))

    
    for tax_id in names_by_tax_id:
        for dnc in DISCARD_NAME_CLASS:            
            filtered = [(t, c) for t, c in names_by_tax_id[tax_id] if c != dnc]
            if filtered:
                names_by_tax_id[tax_id] = filtered
            else:
                print "emptied", tax_id, names_by_tax_id[tax_id]

    
    for tax_id in names_by_tax_id:
        mapped = []
        for t, c in names_by_tax_id[tax_id]:
            mapped.append((t, NAME_CLASS_MAP.get(c,c)))
        names_by_tax_id[tax_id] = mapped

    
    nc_rank = dict((b,a) for a,b in enumerate(NAME_ORDER_BY_CLASS))
    for tax_id in names_by_tax_id:
        names_by_tax_id[tax_id].sort(lambda a, b: cmp(nc_rank[a[1]],
                                                      nc_rank[b[1]]))

    
    for tax_id in sorted(names_by_tax_id, lambda a, b: cmp(int(a),int(b))):
        sys.stdout.write(tax_id)
        for t, c in names_by_tax_id[tax_id]:
            c = c[0].upper()+c[1:]
            sys.stdout.write("\tname:%s:%s" % (c, t))
        sys.stdout.write("\n")

if __name__ == "__main__":
    sys.exit(main(sys.argv))
