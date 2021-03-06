













from __future__ import with_statement

import sys
import re
try:
    import annotation
except ImportError:
    import os.path
    from sys import path as sys_path
    
    sys_path.append(os.path.join(os.path.dirname(__file__), '../server/src'))
    import annotation


sys_path.append(os.path.join(os.path.dirname(__file__), '..'))
    
options = None

def ent2event(anntype, fn):
    global options

    mapped = 0

    try:
        
        nosuff_fn = fn.replace(".ann","")

        with annotation.TextAnnotations(nosuff_fn) as ann_obj:

            for ann in ann_obj.get_entities():
                if ann.type != anntype:
                    
                    continue

                

                
                
                new_id = ann_obj.get_new_id('E')
                eann = annotation.EventAnnotation(ann.id, [], new_id, ann.type, '')            

                
                
                
                for e in ann_obj.get_events():
                    for i in range(0, len(e.args)):
                        role, argid = e.args[i]
                        if argid == ann.id:
                            
                            argid = new_id
                            e.args[i] = role, argid
                for c in ann_obj.get_oneline_comments():
                    if c.target == ann.id:
                        
                        c.target = new_id

                
                ann_obj.add_annotation(eann)

                mapped += 1

            if options.verbose:
                print >> sys.stderr, mapped, 'mapped in', fn

    except annotation.AnnotationFileNotFoundError:
        print >> sys.stderr, "%s:\tFailed: file not found" % fn
    except annotation.AnnotationNotFoundError, e:
        print >> sys.stderr, "%s:\tFailed: %s" % (fn, e)

def argparser():
    import argparse

    ap=argparse.ArgumentParser(description="Rewrite entity annotations of a given type as events.")
    ap.add_argument("-v", "--verbose", default=False, action="store_true", help="Verbose output.")
    ap.add_argument("type", metavar="TYPE", help="Type to rewrite.")
    ap.add_argument("files", metavar="FILE", nargs="+", help="File to process.")
    return ap

def main(argv=None):
    global options

    if argv is None:
        argv = sys.argv
    arg = argparser().parse_args(argv[1:])

    options = arg

    for fn in arg.files:
        ent2event(arg.type, fn)

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
