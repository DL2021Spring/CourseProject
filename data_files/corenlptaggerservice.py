



from argparse import ArgumentParser
from cgi import FieldStorage
from os.path import dirname, join as path_join

from corenlp import CoreNLPTagger

try:
    from json import dumps
except ImportError:
    
    from sys import path as sys_path
    sys_path.append(path_join(dirname(__file__), '../../server/lib/ujson'))
    from ujson import dumps

from sys import stderr
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


ARGPARSER = ArgumentParser(description='XXX')
ARGPARSER.add_argument('-p', '--port', type=int, default=47111,
        help='port to run the HTTP service on (default: 47111)')
TAGGER = None

CORENLP_PATH = path_join(dirname(__file__), 'stanford-corenlp-2012-04-09')



class CoreNLPTaggerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print >> stderr, 'Received request'
        field_storage = FieldStorage(
                headers=self.headers,
                environ={
                    'REQUEST_METHOD':'POST',
                    'CONTENT_TYPE':self.headers['Content-Type'],
                    },
                fp=self.rfile)

        global TAGGER
        json_dic = TAGGER.tag(field_storage.value)

        
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()

        self.wfile.write(dumps(json_dic))
        print >> stderr, ('Generated %d annotations' % len(json_dic))

    def log_message(self, format, *args):
        return 

def main(args):
    argp = ARGPARSER.parse_args(args[1:])

    print >> stderr, "WARNING: Don't use this in a production environment!"

    print >> stderr, 'Starting CoreNLP process (this takes a while)...',
    global TAGGER
    TAGGER = CoreNLPTagger(CORENLP_PATH)
    print >> stderr, 'Done!'

    server_class = HTTPServer
    httpd = server_class(('localhost', argp.port), CoreNLPTaggerHandler)
    print >> stderr, 'CoreNLP tagger service started'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print >> stderr, 'CoreNLP tagger service stopped'

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
