



from argparse import ArgumentParser
from cgi import FieldStorage

try:
	from json import dumps
except ImportError:
	
	from sys import path as sys_path
	from os.path import join as path_join
	from os.path import dirname
	sys_path.append(path_join(dirname(__file__), '../server/lib/ujson'))
	from ujson import dumps

from random import choice, randint
from sys import stderr
from urlparse import urlparse
try:
	from urlparse import parse_qs
except ImportError:
	
	from cgi import parse_qs
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

import json
import urllib
import urllib2
import base64




ARGPARSER = ArgumentParser(description='An example HTTP tagging service, '
				'tagging Confuse-a-Cat **AND** Dead-parrot mentions!')
ARGPARSER.add_argument('-p', '--port', type=int, default=56789,
				help='port to run the HTTP service on (default: 56789)')









def build_headers(email="", password=""):
	headers = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Authorization': b'Basic ' + base64.b64encode(email + b':' + password),
	}
	return headers

def build_data(text):
	return json.dumps({'text': text}).encode('utf-8')

def convert_for_brat(pubdic_result, text):
	anns = {}
	for idx, entity in enumerate(pubdic_result):
		ann_id = 'T%d' % idx
		anns[ann_id] = {
			'type': entity['obj'],     
			'offsets': ((entity['begin'], entity['end']), ),
			'texts': (text[entity['begin']:entity['end']], ),
			
			
		}
	return anns


class RandomTaggerHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		field_storage = FieldStorage(
			headers=self.headers,
			environ={
					'REQUEST_METHOD':'POST',
					'CONTENT_TYPE':self.headers['Content-type'],
					},
			fp=self.rfile)

			
		try:
			
			headers = build_headers("", "")     
			text    = field_storage.value.decode('utf-8')     
			data    = build_data(text)
			
			
			annotator_url = "http://pubdictionaries.dbcls.jp:80/dictionaries/EntrezGene%20-%20Homo%20Sapiens/text_annotation?matching_method=approximate&max_tokens=6&min_tokens=1&threshold=0.8&top_n=0"
			request = urllib2.Request(annotator_url, data=data, headers=headers)
			
			f   = urllib2.urlopen(request)
			res = f.read()
			f.close()

			
			json_dic = convert_for_brat(json.loads(res), text)

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

		server_class = HTTPServer
		httpd = server_class(('localhost', argp.port), RandomTaggerHandler)

		print >> stderr, 'PubDictionary NER tagger service started on port %s' % (argp.port)
		try:
				httpd.serve_forever()
		except KeyboardInterrupt:
				pass
		httpd.server_close()
		print >> stderr, 'PubDictionary tagger service stopped'


if __name__ == '__main__':
		from sys import argv
		exit(main(argv))



