



from argparse import ArgumentParser

from os.path import join as path_join
from os.path import dirname

try:
    from json import dumps
except ImportError:
    
    from sys import path as sys_path
    sys_path.append(path_join(dirname(__file__), '../server/lib/ujson'))
    from ujson import dumps

from subprocess import PIPE, Popen

from random import choice, randint
from sys import stderr
from urlparse import urlparse
try:
    from urlparse import parse_qs
except ImportError:
    
    from cgi import parse_qs
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import re


from sentencesplit import sentencebreaks_to_newlines


from BIOtoStandoff import BIO_lines_to_standoff


DOCUMENT_BOUNDARY = 'END-DOCUMENT'
NERSUITE_SCRIPT   = path_join(dirname(__file__), './nersuite_tag.sh')
NERSUITE_COMMAND  = [NERSUITE_SCRIPT, '-multidoc', DOCUMENT_BOUNDARY]

ARGPARSER = ArgumentParser(description='An example HTTP tagging service using NERsuite')
ARGPARSER.add_argument('-p', '--port', type=int, default=47111,
        help='port to run the HTTP service on (default: 47111)')



tagger_process = None

def run_tagger(cmd):
    
    global tagger_process
    try:
        tagger_process = Popen(cmd, stdin=PIPE, stdout=PIPE, bufsize=1)
    except Exception, e:
        print >> stderr, "Error running '%s':" % cmd, e
        raise

def _apply_tagger(text):
    global tagger_process, tagger_queue

    
    try:
        splittext = sentencebreaks_to_newlines(text)
    except:
        
        
        print >> stderr, "Warning: sentence splitting failed for input:\n'%s'" % text
        splittext = text

    print >> tagger_process.stdin, splittext
    print >> tagger_process.stdin, DOCUMENT_BOUNDARY
    tagger_process.stdin.flush()

    response_lines = []
    while True:
        l = tagger_process.stdout.readline()
        l = l.rstrip('\n')
        
        if l == DOCUMENT_BOUNDARY:
            break

        response_lines.append(l)
        
    try:
        tagged_entities = BIO_lines_to_standoff(response_lines, text)
    except:
        
        print >> stderr, "Warning: BIO-to-standoff conversion failed for BIO:\n'%s'" % '\n'.join(response_lines)
        return {}

    anns = {}

    for t in tagged_entities:
        anns["T%d" % t.idNum] = {
            'type': t.eType,
            'offsets': ((t.startOff, t.endOff), ),
            'texts': (t.eText, ),
            }

    return anns

class NERsuiteTaggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        query = parse_qs(urlparse(self.path).query)

        try:
            json_dic = _apply_tagger(query['text'][0])
        except KeyError:
            
            json_dic = {}

        
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()

        self.wfile.write(dumps(json_dic))
        print >> stderr, ('Generated %d annotations' % len(json_dic))

    def log_message(self, format, *args):
        return 

def main(args):
    argp = ARGPARSER.parse_args(args[1:])

    print >> stderr, 'Starting NERsuite ...'
    run_tagger(NERSUITE_COMMAND)

    server_class = HTTPServer
    httpd = server_class(('localhost', argp.port), NERsuiteTaggerHandler)

    print >> stderr, 'NERsuite tagger service started'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print >> stderr, 'NERsuite tagger service stopped'

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
