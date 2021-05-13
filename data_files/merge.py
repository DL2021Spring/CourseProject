



from __future__ import with_statement



from collections import defaultdict
from os.path import join as join_path
from os.path import split as split_path
from shlex import split as shlex_split
from sys import stderr, stdin
from subprocess import Popen, PIPE

try:
    from argparse import ArgumentParser
except ImportError:
    from os.path import basename
    from sys import path as sys_path
    
    sys_path.append(join_path(basename(__file__), '../server/lib'))
    from argparse import ArgumentParser



UNMERGED_SUFFIXES=['a1', 'a2', 'co', 'rel']

MERGED_SUFFIX='ann'
ARGPARSER = ArgumentParser(description=("Merge BioNLP'11 ST annotations "
    'into a single file, reads paths from stdin'))
ARGPARSER.add_argument('-w', '--no-warn', action='store_true',
        help='suppress warnings')




def keynat(string):
    
    it = type(1)
    r = []
    for c in string:
        if c.isdigit():
            d = int(c)
            if r and type( r[-1] ) == it:
                r[-1] = r[-1] * 10 + d
            else: 
                r.append(d)
        else:
            r.append(c.lower())
    return r

def main(args):
    argp = ARGPARSER.parse_args(args[1:])
    
    id_to_ann_files = defaultdict(list)
    
    for file_path in (l.strip() for l in stdin):
        if not any((file_path.endswith(suff) for suff in UNMERGED_SUFFIXES)):
            if not argp.no_warn:
                import sys
                print >> sys.stderr, (
                        'WARNING: invalid file suffix for %s, ignoring'
                        ) % (file_path, )
            continue
        
        dirname, basename = split_path(file_path)
        id = join_path(dirname, basename.split('.')[0])
        id_to_ann_files[id].append(file_path)

    for id, ann_files in id_to_ann_files.iteritems():
        
        lines = []
        for ann_file_path in ann_files:
            with open(ann_file_path, 'r') as ann_file:
                for line in ann_file:
                    lines.append(line)

        with open(id + '.' + MERGED_SUFFIX, 'w') as merged_ann_file:
            for line in lines:
                merged_ann_file.write(line)

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
