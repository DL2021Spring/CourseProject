



import socket

from .models import Response
from .packages.urllib3.poolmanager import PoolManager, proxy_from_url
from .hooks import dispatch_hook
from .compat import urlparse
from .utils import DEFAULT_CA_BUNDLE_PATH, get_encoding_from_headers
from .structures import CaseInsensitiveDict
from .packages.urllib3.exceptions import MaxRetryError
from .packages.urllib3.exceptions import TimeoutError
from .packages.urllib3.exceptions import SSLError as _SSLError
from .packages.urllib3.exceptions import HTTPError as _HTTPError
from .cookies import extract_cookies_to_jar
from .exceptions import ConnectionError, Timeout, SSLError

DEFAULT_POOLSIZE = 10
DEFAULT_RETRIES = 0


class BaseAdapter(object):
    

    def __init__(self):
        super(BaseAdapter, self).__init__()

    def send(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class HTTPAdapter(BaseAdapter):
    
    def __init__(self, pool_connections=DEFAULT_POOLSIZE, pool_maxsize=DEFAULT_POOLSIZE):
        self.max_retries = DEFAULT_RETRIES
        self.config = {}

        super(HTTPAdapter, self).__init__()

        self.init_poolmanager(pool_connections, pool_maxsize)

    def init_poolmanager(self, connections, maxsize):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize)

    def cert_verify(self, conn, url, verify, cert):
        if url.startswith('https') and verify:

            cert_loc = None

            
            if verify is not True:
                cert_loc = verify

            if not cert_loc:
                cert_loc = DEFAULT_CA_BUNDLE_PATH

            if not cert_loc:
                raise Exception("Could not find a suitable SSL CA certificate bundle.")

            conn.cert_reqs = 'CERT_REQUIRED'
            conn.ca_certs = cert_loc
        else:
            conn.cert_reqs = 'CERT_NONE'
            conn.ca_certs = None

        if cert:
            if len(cert) == 2:
                conn.cert_file = cert[0]
                conn.key_file = cert[1]
            else:
                conn.cert_file = cert

    def build_response(self, req, resp):
        response = Response()

        
        response.status_code = getattr(resp, 'status', None)

        
        response.headers = CaseInsensitiveDict(getattr(resp, 'headers', {}))

        
        response.encoding = get_encoding_from_headers(response.headers)
        response.raw = resp

        if isinstance(req.url, bytes):
            response.url = req.url.decode('utf-8')
        else:
            response.url = req.url

        
        extract_cookies_to_jar(response.cookies, req, resp)

        
        response.request = req
        response.connection = self

        
        response = dispatch_hook('response', req.hooks, response)
        return response

    def get_connection(self, url, proxies=None):
        
        proxies = proxies or {}
        proxy = proxies.get(urlparse(url).scheme)

        if proxy:
            conn = proxy_from_url(proxy)
        else:
            conn = self.poolmanager.connection_from_url(url)

        return conn

    def close(self):
        
        self.poolmanager.clear()

    def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        

        conn = self.get_connection(request.url, proxies)

        self.cert_verify(conn, request.url, verify, cert)

        try:
            
            resp = conn.urlopen(
                method=request.method,
                url=request.path_url,
                body=request.body,
                headers=request.headers,
                redirect=False,
                assert_same_host=False,
                preload_content=False,
                decode_content=False,
                retries=self.max_retries,
                timeout=timeout,
            )

        except socket.error as sockerr:
            raise ConnectionError(sockerr)

        except MaxRetryError as e:
            raise ConnectionError(e)

        except (_SSLError, _HTTPError) as e:
            if isinstance(e, _SSLError):
                raise SSLError(e)
            elif isinstance(e, TimeoutError):
                raise Timeout(e)
            else:
                raise Timeout('Request timed out.')

        r = self.build_response(request, resp)

        if not stream:
            r.content

        return r
