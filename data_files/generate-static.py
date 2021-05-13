






import sys
import os

try:
    import argparse
except ImportError:
    from os.path import basename
    from sys import path as sys_path
    
    sys_path.append(join_path(basename(__file__), '../server/lib'))
    import argparse



known_filename_extensions = [".txt", ".a1", ".a2"]


def argparser():
    ap=argparse.ArgumentParser(description="Generate web page linking to visualizations of BioNLP ST documents.")
    ap.add_argument("-v", "--visualizer", default="visualizer.xhtml", metavar="URL", help="Visualization script")
    ap.add_argument("-s", "--staticdir", default="static", metavar="DIR", help="Directory containing static visualizations")
    ap.add_argument("-d", "--dataset", default=None, metavar="NAME", help="Dataset name (derived from directory by default.)")
    ap.add_argument("directory", help="Directory containing ST documents.")
    ap.add_argument("prefix", metavar="URL", help="URL prefix to prepend to links")
    return ap


def files_to_process(dir):

    try:
        toprocess = []
        for fn in os.listdir(dir):
            fp = os.path.join(dir, fn)
            if os.path.isdir(fp):
                print >> sys.stderr, "Skipping directory %s" % fn
            elif os.path.splitext(fn)[1] not in known_filename_extensions:
                print >> sys.stderr, "Skipping %s: unrecognized suffix" % fn
            else:
                toprocess.append(fp)
    except OSError, e:
        print >> sys.stderr, "Error processing %s: %s" % (dir, e)

    return toprocess

def print_links(files, arg, out=sys.stdout):
    
    grouped = {}
    for fn in files:
        root, ext = os.path.splitext(fn)
        if root not in grouped:
            grouped[root] = []
        grouped[root].append(ext)

    
    sorted = grouped.keys()
    sorted.sort()

    print >> out, "<table>"

    for root in sorted:
        path, fn = os.path.split(root)

        print >> out, "<tr>"
        print >> out, "  <td>%s</td>" % fn

        
        print >> out, "  <td><a href=\"%s\">dynamic</a></td>" % (arg.prefix+arg.visualizer+"#"+arg.dataset+"/"+fn)

        
        print >> out, "  <td><a href=\"%s\">svg</a></td>" % (arg.prefix+arg.staticdir+"/svg/"+arg.dataset+"/"+fn+".svg")
        print >> out, "  <td><a href=\"%s\">png</a></td>" % (arg.prefix+arg.staticdir+"/png/"+arg.dataset+"/"+fn+".png")

        
        for ext in known_filename_extensions:
            if ext in grouped[root]:
                print >> out, "  <td><a href=\"%s\">%s</a></td>" % (arg.prefix+root+ext, ext[1:])
            else:
                
                print >> out, "  <td>-</td>"

        print >> out, "</tr>"

    print >> out, "</table>"

def main(argv=None):
    if argv is None:
        argv = sys.argv
    arg = argparser().parse_args(argv[1:])

    
    if arg.dataset is None:
        dir = arg.directory
        
        while dir[-1] == os.sep:
            dir = dir[:-1]
        arg.dataset = os.path.split(dir)[1]
        print >> sys.stderr, "Assuming dataset name '%s', visualizations in %s" % (arg.dataset, os.path.join(arg.staticdir,arg.dataset))

    try:
        files = files_to_process(arg.directory)
        if files is None or len(files) == 0:
            print >> sys.stderr, "No files found"
            return 1
        print_header()
        print_links(files, arg)
        print_footer()
    except:
        print >> sys.stderr, "Error processing %s" % arg.directory
        raise
    return 0

def print_header(out=sys.stdout):
    print >> out, 

def print_footer(out=sys.stdout):
    print >> out, 

if __name__ == "__main__":
    sys.exit(main())
