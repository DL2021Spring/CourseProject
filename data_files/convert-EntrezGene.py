






























from __future__ import with_statement

import sys
import re
import codecs

INPUT_ENCODING = "UTF-8"


TAX_ID_LABEL = 'Organism'
GENE_ID_LABEL = 'Gene ID'
SYMBOL_LABEL = 'Symbol'
LOCUS_LABEL = 'Locus'
SYNONYM_LABEL = 'Also known as'
CHROMOSOME_LABEL = 'Chromosome'
DESCRIPTION_LABEL = 'Description'
GENE_TYPE_LABEL = 'Gene type'
SYMBOL_AUTHORITY_LABEL = 'Official symbol'
FULL_NAME_AUTHORITY_LABEL = 'Official full name'
OTHER_DESIGNATION_LABEL = 'Name'


OUTPUT_LABEL_ORDER = [
    SYMBOL_AUTHORITY_LABEL,
    SYMBOL_LABEL,
    FULL_NAME_AUTHORITY_LABEL,
    GENE_TYPE_LABEL,
    TAX_ID_LABEL,
    SYNONYM_LABEL,
    OTHER_DESIGNATION_LABEL,
    LOCUS_LABEL,
    CHROMOSOME_LABEL,
    DESCRIPTION_LABEL,
]


FILTER_LIST = [

]

def process_tax_id(val, record):
    assert re.match(r'^[0-9]+$', val)
    record.append(('info', TAX_ID_LABEL, val))

def process_gene_id(val, record):
    assert re.match(r'^[0-9]+$', val)
    record.append(('key', GENE_ID_LABEL, val))

def process_symbol(val, record):
    assert val != '-'
    for v in val.split('|'):
        assert re.match(r'^\S(?:.*\S)?$', v)
        record.append(('name', SYMBOL_LABEL, v))

def process_locus(val, record):
    if val != '-':
        assert re.match(r'^[^\s|]+$', val)
        record.append(('name', LOCUS_LABEL, val))

def process_synonyms(val, record):
    if val != '-':
        for v in val.split('|'):
            assert re.match(r'^\S(?:.*\S)?$', v)
            record.append(('name', SYNONYM_LABEL, v))

def process_chromosome(val, record):
    if val != '-':
        assert re.match(r'^\S(?:.*\S)?$', val)
        record.append(('info', CHROMOSOME_LABEL, val))

def process_description(val, record):
    if val != '-':
        record.append(('info', DESCRIPTION_LABEL, val))        

def process_gene_type(val, record):
    if val != '-':
        record.append(('info', GENE_TYPE_LABEL, val))        

def process_symbol_authority(val, record):
    if val != '-':
        record.append(('name', SYMBOL_AUTHORITY_LABEL, val))

def process_full_name_authority(val, record):
    if val != '-':
        record.append(('name', FULL_NAME_AUTHORITY_LABEL, val))

def process_other_designations(val, record):
    if val != '-':
        for v in val.split('|'):
            assert re.match(r'^\S(?:.*\S)?$', v)
            record.append(('name', OTHER_DESIGNATION_LABEL, v))

field_processor = [
    process_tax_id,
    process_gene_id,
    process_symbol,
    process_locus,
    process_synonyms,
    None, 
    process_chromosome,
    None, 
    process_description,
    process_gene_type,
    process_symbol_authority,
    process_full_name_authority,
    None, 
    process_other_designations,
    None, 
]

output_priority = {}
for i, l in enumerate(OUTPUT_LABEL_ORDER):
    output_priority[l] = output_priority.get(l, i)

filter = set(FILTER_LIST)

def process_line(l):
    fields = l.split('\t')
    assert len(fields) == 15

    record = []
    for i, f in enumerate(fields):
        if field_processor[i] is not None:
            try:
                field_processor[i](f, record)
            except:
                print >> sys.stderr, "Error processing field %d: '%s'" % (i+1,f)
                raise

    
    keys = [r for r in record if r[0] == 'key']
    assert len(keys) == 1
    key = keys[0]
    record = [r for r in record if r[0] != 'key']

    record.sort(lambda a, b: cmp(output_priority[a[1]],
                                 output_priority[b[1]]))

    filtered = []
    for r in record:
        if r not in filter:
            filtered.append(r)
    record = filtered

    seen = set()
    uniqued = []
    for r in record:
        if (r[0],r[2]) not in seen:
            seen.add((r[0],r[2]))
            uniqued.append(r)
    record = uniqued

    print '\t'.join([key[2]]+[':'.join(r) for r in record])

def process(fn):
    with codecs.open(fn, encoding=INPUT_ENCODING) as f:
        for ln, l in enumerate(f):
            l = l.rstrip('\r\n')

            
            if l and l[0] == '#':
                continue

            try:
                process_line(l)
            except Exception, e:
                print >> sys.stderr, "Error processing line %d: %s" % (ln, l)
                raise
            
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, "Usage:", argv[0], "GENE-INFO-FILE"
        return 1

    fn = argv[1]
    process(fn)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
