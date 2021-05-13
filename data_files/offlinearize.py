



import sys
from urlparse import urlparse, urljoin
from os.path import dirname, join as joinpath
from os import makedirs
from urllib import urlopen
from simplejson import loads

try:
    base_url = sys.argv[1]
    url = urlparse(base_url)
except:
    print sys.argv[1]
    print "Syntax: %s <url>" % sys.argv[0]
    sys.exit(1)

this_dir = dirname(sys.argv[0])
datadir = joinpath(this_dir, '../offline_data')

coll_and_doc = url.fragment
coll = dirname(coll_and_doc)[1:]

def convert_coll(coll):
    if coll == '':
        ajax_coll = '/'
    else:
        ajax_coll = '/%s/' % coll

    coll_query_url = urljoin(base_url, 'ajax.cgi?action=getCollectionInformation&collection=%s' % ajax_coll)
    coll_dir = joinpath(datadir, coll)
    try:
        makedirs(coll_dir)
    except:
        pass 

    print ajax_coll
    conn = urlopen(coll_query_url)
    jsonp = conn.read()
    conn.close
    with open(joinpath(coll_dir, 'collection.js'), 'w') as f:
        f.write("jsonp=")
        f.write(jsonp)

    coll_data = loads(jsonp)
    for item in coll_data['items']:
        if item[0] == 'd':
            doc = item[2]
            print "  %s" % doc
            doc_query_url = urljoin(base_url, 'ajax.cgi?action=getDocument&collection=%s&document=%s' % (ajax_coll, doc))

            conn = urlopen(doc_query_url)
            jsonp = conn.read()
            conn.close
            with open(joinpath(coll_dir, '%s.data.js' % doc), 'w') as f:
                f.write("jsonp=")
                f.write(jsonp)
        elif item[0] == 'c' and item[2] != '..':
            convert_coll(item[2])

convert_coll(coll)
