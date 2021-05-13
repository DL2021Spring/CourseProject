



from httplib import HTTPConnection, HTTPSConnection
from httplib import FORBIDDEN, MOVED_PERMANENTLY, NOT_FOUND, OK, TEMPORARY_REDIRECT
from sys import stderr
from urlparse import urlparse


CONNECTION_BY_SCHEME = {
        'http': HTTPConnection,
        'https': HTTPSConnection,
        }



def _request_wrap(conn, method, url, body=None,
        headers=None):
    depth = 0
    curr_conn = conn
    curr_url = url
    while depth < 100: 
        curr_conn.request(method, curr_url, body,
                headers=headers if headers is not None else {})
        res = curr_conn.getresponse()
        if res.status not in (MOVED_PERMANENTLY, TEMPORARY_REDIRECT, ):
            return res
        res.read() 
        res_headers = dict(res.getheaders())
        url_soup = urlparse(res_headers['location'])
        
        
        try:
            curr_conn = CONNECTION_BY_SCHEME[url_soup.scheme](url_soup.netloc)
        except KeyError:
            assert False, 'redirected to unknown scheme, dying'
        curr_url = url_soup.path
        depth += 1
    assert False, 'redirects and moves lead us astray, dying'

def main(args):
    
    if len(args) != 2:
        print >> stderr, 'Usage: %s url_to_brat_installation' % (args[0], )
        return -1
    brat_url = args[1]
    url_soup = urlparse(brat_url)

    if url_soup.scheme:
        try:
            Connection = CONNECTION_BY_SCHEME[url_soup.scheme.split(':')[0]]
        except KeyError:
            print >> stderr, ('ERROR: Unknown url scheme %s, try http or '
                    'https') % url_soup.scheme
            return -1
    else:
        
        path_soup = url_soup.path.split('/')
        assumed_netloc = path_soup[0]
        assumed_path = '/' + '/'.join(path_soup[1:])
        print >> stderr, ('WARNING: No url scheme given, assuming scheme: '
                '"http", netloc: "%s" and path: "%s"'
                ) % (assumed_netloc, assumed_path, )
        url_soup = url_soup._replace(scheme='http', netloc=assumed_netloc,
                path=assumed_path)
        Connection = HTTPConnection

    
    conn = Connection(url_soup.netloc)
    res = _request_wrap(conn, 'HEAD', url_soup.path)
    if res.status != OK:
        print >> stderr, ('Unable to load "%s", please check the url.'
                ) % (brat_url, )
        print >> stderr, ('Does the url you provdide point to your brat '
                'installation?')
        return -1
    res.read() 

    
    ajax_cgi_path = url_soup.path + '/ajax.cgi'
    ajax_cgi_url = url_soup._replace(path=ajax_cgi_path).geturl()
    res = _request_wrap(conn, 'HEAD', ajax_cgi_path)
    if res.status == FORBIDDEN:
        print >> stderr, ('Received forbidden (403) when trying to access '
                '"%s"') % (ajax_cgi_url, )
        print ('Have you perhaps forgotten to enable execution of CGI in '
                ' your web server configuration?')
        return -1
    elif res.status != OK:
        print >> stderr, ('Unable to load "%s", please check your url. Does '
                'it point to your brat installation?') % (ajax_cgi_url, )
        return -1
    
    res_headers = dict(res.getheaders())
    try:
        content_type = res_headers['content-type']
    except KeyError:
        content_type = None

    if content_type != 'application/json':
        print >> stderr, ('Didn\'t receive json data when accessing "%s"%s.'
                ) % (ajax_cgi_url,
                        ', instead we received %s' % content_type
                            if content_type is not None else '')
        print >> stderr, ('Have you perhaps forgotten to add a handler for '
                'CGI in your web server configuration?')
        return -1

    
    print 'Congratulations! Your brat server appears to be ready to run.'
    print ('However, there is the possibility that there are further errors, '
            'but at least the server should be capable of communicating '
            'these errors to the client.')
    return 0

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
