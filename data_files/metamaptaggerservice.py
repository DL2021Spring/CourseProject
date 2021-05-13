



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


from MetaMaptoStandoff import MetaMap_lines_to_standoff


METAMAP_SCRIPT   = path_join(dirname(__file__), './metamap_tag.sh')
METAMAP_COMMAND  = [METAMAP_SCRIPT]

ARGPARSER = ArgumentParser(description='An example HTTP tagging service using MetaMap')
ARGPARSER.add_argument('-p', '--port', type=int, default=47111,
        help='port to run the HTTP service on (default: 47111)')


def run_tagger(cmd):
    
    try:
        tagger_process = Popen(cmd, stdin=PIPE, stdout=PIPE, bufsize=1)
        return tagger_process
    except Exception, e:
        print >> stderr, "Error running '%s':" % cmd, e
        raise    

def _apply_tagger_to_sentence(text):
    
    tagger_process = run_tagger(METAMAP_COMMAND)

    print >> tagger_process.stdin, text
    tagger_process.stdin.close()
    tagger_process.wait()

    response_lines = []

    for l in tagger_process.stdout:
        l = l.rstrip('\n')
        response_lines.append(l)
        
    try:
        tagged_entities = MetaMap_lines_to_standoff(response_lines, text)
    except:
        
        print >> stderr, "Warning: MetaMap-to-standoff conversion failed for output:\n'%s'" % '\n'.join(response_lines)
        raise
        

    
    for t in tagged_entities:
        t.eText = text[t.startOff:t.endOff]

    return tagged_entities

def _apply_tagger(text):
    
    

    try:
        splittext = sentencebreaks_to_newlines(text)
    except:
        
        
        print >> stderr, "Warning: sentence splitting failed for input:\n'%s'" % text
        splittext = text

    sentences = splittext.split('\n')
    all_tagged = []
    baseoffset = 0
    for s in sentences:
        tagged = _apply_tagger_to_sentence(s)

        
        for t in tagged:
            t.startOff += baseoffset
            t.endOff += baseoffset

        all_tagged.extend(tagged)
        baseoffset += len(s)+1

    anns = {}

    idseq = 1
    for t in all_tagged:
        anns["T%d" % idseq] = {
            'type': t.eType,
            'offsets': ((t.startOff, t.endOff), ),
            'texts': (t.eText, ),
            }
        idseq += 1

    return anns
        

class MetaMapTaggerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        
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

    print >> stderr, 'Starting MetaMap ...'

    server_class = HTTPServer
    httpd = server_class(('localhost', argp.port), MetaMapTaggerHandler)

    print >> stderr, 'MetaMap tagger service started'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print >> stderr, 'MetaMap tagger service stopped'

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
