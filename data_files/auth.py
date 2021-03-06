



import os
import time
import hashlib
import logging

from base64 import b64encode

from .compat import urlparse, str
from .utils import parse_dict_header


log = logging.getLogger(__name__)

CONTENT_TYPE_FORM_URLENCODED = 'application/x-www-form-urlencoded'
CONTENT_TYPE_MULTI_PART = 'multipart/form-data'


def _basic_auth_str(username, password):
    

    return 'Basic ' + b64encode(('%s:%s' % (username, password)).encode('latin1')).strip().decode('latin1')


class AuthBase(object):
    

    def __call__(self, r):
        raise NotImplementedError('Auth hooks must be callable.')

class HTTPBasicAuth(AuthBase):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self, r):
        r.headers['Authorization'] = _basic_auth_str(self.username, self.password)
        return r


class HTTPProxyAuth(HTTPBasicAuth):
    
    def __call__(self, r):
        r.headers['Proxy-Authorization'] = _basic_auth_str(self.username, self.password)
        return r


class HTTPDigestAuth(AuthBase):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.last_nonce = ''
        self.nonce_count = 0
        self.chal = {}

    def build_digest_header(self, method, url):

        realm = self.chal['realm']
        nonce = self.chal['nonce']
        qop = self.chal.get('qop')
        algorithm = self.chal.get('algorithm', 'MD5')
        opaque = self.chal.get('opaque', None)

        algorithm = algorithm.upper()
        
        if algorithm == 'MD5':
            def md5_utf8(x):
                if isinstance(x, str):
                    x = x.encode('utf-8')
                return hashlib.md5(x).hexdigest()
            hash_utf8 = md5_utf8
        elif algorithm == 'SHA':
            def sha_utf8(x):
                if isinstance(x, str):
                    x = x.encode('utf-8')
                return hashlib.sha1(x).hexdigest()
            hash_utf8 = sha_utf8
        
        KD = lambda s, d: hash_utf8("%s:%s" % (s, d))

        if hash_utf8 is None:
            return None

        
        entdig = None
        p_parsed = urlparse(url)
        path = p_parsed.path
        if p_parsed.query:
            path += '?' + p_parsed.query

        A1 = '%s:%s:%s' % (self.username, realm, self.password)
        A2 = '%s:%s' % (method, path)

        if qop == 'auth':
            if nonce == self.last_nonce:
                self.nonce_count += 1
            else:
                self.nonce_count = 1

            ncvalue = '%08x' % self.nonce_count
            s = str(self.nonce_count).encode('utf-8')
            s += nonce.encode('utf-8')
            s += time.ctime().encode('utf-8')
            s += os.urandom(8)

            cnonce = (hashlib.sha1(s).hexdigest()[:16])
            noncebit = "%s:%s:%s:%s:%s" % (nonce, ncvalue, cnonce, qop, hash_utf8(A2))
            respdig = KD(hash_utf8(A1), noncebit)
        elif qop is None:
            respdig = KD(hash_utf8(A1), "%s:%s" % (nonce, hash_utf8(A2)))
        else:
            
            return None

        self.last_nonce = nonce

        
        base = 'username="%s", realm="%s", nonce="%s", uri="%s", ' \
           'response="%s"' % (self.username, realm, nonce, path, respdig)
        if opaque:
            base += ', opaque="%s"' % opaque
        if entdig:
            base += ', digest="%s"' % entdig
            base += ', algorithm="%s"' % algorithm
        if qop:
            base += ', qop=auth, nc=%s, cnonce="%s"' % (ncvalue, cnonce)

        return 'Digest %s' % (base)

    def handle_401(self, r):
        

        num_401_calls = r.request.hooks['response'].count(self.handle_401)
        s_auth = r.headers.get('www-authenticate', '')

        if 'digest' in s_auth.lower() and num_401_calls < 2:

            self.chal = parse_dict_header(s_auth.replace('Digest ', ''))

            
            
            r.content
            r.raw.release_conn()

            r.request.headers['Authorization'] = self.build_digest_header(r.request.method, r.request.url)
            _r = r.connection.send(r.request)
            _r.history.append(r)

            return _r

        return r

    def __call__(self, r):
        
        if self.last_nonce:
            r.headers['Authorization'] = self.build_digest_header(r.method, r.url)
        r.register_hook('response', self.handle_401)
        return r
