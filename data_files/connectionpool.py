





import logging
import socket
import errno

from socket import error as SocketError, timeout as SocketTimeout

try: 
    from http.client import HTTPConnection, HTTPException
    from http.client import HTTP_PORT, HTTPS_PORT
except ImportError:
    from httplib import HTTPConnection, HTTPException
    from httplib import HTTP_PORT, HTTPS_PORT

try: 
    from queue import LifoQueue, Empty, Full
except ImportError:
    from Queue import LifoQueue, Empty, Full


try: 
    HTTPSConnection = object
    BaseSSLError = None
    ssl = None

    try: 
        from http.client import HTTPSConnection
    except ImportError:
        from httplib import HTTPSConnection

    import ssl
    BaseSSLError = ssl.SSLError

except (ImportError, AttributeError): 
    pass


from .request import RequestMethods
from .response import HTTPResponse
from .util import get_host, is_connection_dropped, ssl_wrap_socket
from .exceptions import (
    ClosedPoolError,
    EmptyPoolError,
    HostChangedError,
    MaxRetryError,
    SSLError,
    TimeoutError,
)

from .packages.ssl_match_hostname import match_hostname, CertificateError
from .packages import six


xrange = six.moves.xrange

log = logging.getLogger(__name__)

_Default = object()

port_by_scheme = {
    'http': HTTP_PORT,
    'https': HTTPS_PORT,
}




class VerifiedHTTPSConnection(HTTPSConnection):
    
    cert_reqs = None
    ca_certs = None
    ssl_version = None

    def set_cert(self, key_file=None, cert_file=None,
                 cert_reqs='CERT_NONE', ca_certs=None):
        ssl_req_scheme = {
            'CERT_NONE': ssl.CERT_NONE,
            'CERT_OPTIONAL': ssl.CERT_OPTIONAL,
            'CERT_REQUIRED': ssl.CERT_REQUIRED
        }

        self.key_file = key_file
        self.cert_file = cert_file
        self.cert_reqs = ssl_req_scheme.get(cert_reqs) or ssl.CERT_NONE
        self.ca_certs = ca_certs

    def connect(self):
        
        sock = socket.create_connection((self.host, self.port), self.timeout)

        
        
        self.sock = ssl_wrap_socket(sock, self.key_file, self.cert_file,
                                    cert_reqs=self.cert_reqs,
                                    ca_certs=self.ca_certs,
                                    server_hostname=self.host,
                                    ssl_version=self.ssl_version)

        if self.ca_certs:
            match_hostname(self.sock.getpeercert(), self.host)




class ConnectionPool(object):
    

    scheme = None
    QueueCls = LifoQueue

    def __init__(self, host, port=None):
        self.host = host
        self.port = port

    def __str__(self):
        return '%s(host=%r, port=%r)' % (type(self).__name__,
                                         self.host, self.port)


class HTTPConnectionPool(ConnectionPool, RequestMethods):
    

    scheme = 'http'

    def __init__(self, host, port=None, strict=False, timeout=None, maxsize=1,
                 block=False, headers=None):
        ConnectionPool.__init__(self, host, port)
        RequestMethods.__init__(self, headers)

        self.strict = strict
        self.timeout = timeout
        self.pool = self.QueueCls(maxsize)
        self.block = block

        
        for _ in xrange(maxsize):
            self.pool.put(None)

        
        self.num_connections = 0
        self.num_requests = 0

    def _new_conn(self):
        
        self.num_connections += 1
        log.info("Starting new HTTP connection (%d): %s" %
                 (self.num_connections, self.host))
        return HTTPConnection(host=self.host,
                              port=self.port,
                              strict=self.strict)

    def _get_conn(self, timeout=None):
        
        conn = None
        try:
            conn = self.pool.get(block=self.block, timeout=timeout)

        except AttributeError: 
            raise ClosedPoolError(self, "Pool is closed.")

        except Empty:
            if self.block:
                raise EmptyPoolError(self,
                                     "Pool reached maximum size and no more "
                                     "connections are allowed.")
            pass  

        
        if conn and is_connection_dropped(conn):
            log.info("Resetting dropped connection: %s" % self.host)
            conn.close()

        return conn or self._new_conn()

    def _put_conn(self, conn):
        
        try:
            self.pool.put(conn, block=False)
            return 
        except AttributeError:
            
            pass
        except Full:
            
            log.warning("HttpConnectionPool is full, discarding connection: %s"
                        % self.host)

        
        conn.close()

    def _make_request(self, conn, method, url, timeout=_Default,
                      **httplib_request_kw):
        
        self.num_requests += 1

        if timeout is _Default:
            timeout = self.timeout

        conn.timeout = timeout 
        conn.request(method, url, **httplib_request_kw)

        
        sock = getattr(conn, 'sock', False) 
        if sock:
            sock.settimeout(timeout)

        try: 
            httplib_response = conn.getresponse(buffering=True)
        except TypeError: 
            httplib_response = conn.getresponse()

        
        http_version = getattr(conn, '_http_vsn_str', 'HTTP/?')
        log.debug("\"%s %s %s\" %s %s" % (method, url, http_version,
                                          httplib_response.status,
                                          httplib_response.length))
        return httplib_response

    def close(self):
        
        
        old_pool, self.pool = self.pool, None

        try:
            while True:
                conn = old_pool.get(block=False)
                if conn:
                    conn.close()

        except Empty:
            pass 

    def is_same_host(self, url):
        
        if url.startswith('/'):
            return True

        
        scheme, host, port = get_host(url)

        if self.port and not port:
            
            port = port_by_scheme.get(scheme)

        return (scheme, host, port) == (self.scheme, self.host, self.port)

    def urlopen(self, method, url, body=None, headers=None, retries=3,
                redirect=True, assert_same_host=True, timeout=_Default,
                pool_timeout=None, release_conn=None, **response_kw):
        
        if headers is None:
            headers = self.headers

        if retries < 0:
            raise MaxRetryError(self, url)

        if timeout is _Default:
            timeout = self.timeout

        if release_conn is None:
            release_conn = response_kw.get('preload_content', True)

        
        if assert_same_host and not self.is_same_host(url):
            host = "%s://%s" % (self.scheme, self.host)
            if self.port:
                host = "%s:%d" % (host, self.port)

            raise HostChangedError(self, url, retries - 1)

        conn = None

        try:
            
            conn = self._get_conn(timeout=pool_timeout)

            
            httplib_response = self._make_request(conn, method, url,
                                                  timeout=timeout,
                                                  body=body, headers=headers)

            
            
            
            
            response_conn = not release_conn and conn

            
            response = HTTPResponse.from_httplib(httplib_response,
                                                 pool=self,
                                                 connection=response_conn,
                                                 **response_kw)

            
            
            
            

        except Empty as e:
            
            raise TimeoutError(self, "Request timed out. (pool_timeout=%s)" %
                               pool_timeout)

        except SocketTimeout as e:
            
            raise TimeoutError(self, "Request timed out. (timeout=%s)" %
                               timeout)

        except BaseSSLError as e:
            
            raise SSLError(e)

        except CertificateError as e:
            
            raise SSLError(e)

        except (HTTPException, SocketError) as e:
            
            conn = None
            
            err = e

            if retries == 0:
                raise MaxRetryError(self, url, e)

        finally:
            if release_conn:
                
                
                
                self._put_conn(conn)

        if not conn:
            
            log.warn("Retrying (%d attempts remain) after connection "
                     "broken by '%r': %s" % (retries, err, url))
            return self.urlopen(method, url, body, headers, retries - 1,
                                redirect, assert_same_host,
                                timeout=timeout, pool_timeout=pool_timeout,
                                release_conn=release_conn, **response_kw)

        
        redirect_location = redirect and response.get_redirect_location()
        if redirect_location:
            if response.status == 303:
                method = 'GET'
            log.info("Redirecting %s -> %s" % (url, redirect_location))
            return self.urlopen(method, redirect_location, body, headers,
                                retries - 1, redirect, assert_same_host,
                                timeout=timeout, pool_timeout=pool_timeout,
                                release_conn=release_conn, **response_kw)

        return response


class HTTPSConnectionPool(HTTPConnectionPool):
    

    scheme = 'https'

    def __init__(self, host, port=None,
                 strict=False, timeout=None, maxsize=1,
                 block=False, headers=None,
                 key_file=None, cert_file=None,
                 cert_reqs='CERT_NONE', ca_certs=None, ssl_version=None):

        HTTPConnectionPool.__init__(self, host, port,
                                    strict, timeout, maxsize,
                                    block, headers)
        self.key_file = key_file
        self.cert_file = cert_file
        self.cert_reqs = cert_reqs
        self.ca_certs = ca_certs
        self.ssl_version = ssl_version

    def _new_conn(self):
        
        self.num_connections += 1
        log.info("Starting new HTTPS connection (%d): %s"
                 % (self.num_connections, self.host))

        if not ssl: 
            if not HTTPSConnection or HTTPSConnection is object:
                raise SSLError("Can't connect to HTTPS URL because the SSL "
                               "module is not available.")

            return HTTPSConnection(host=self.host,
                                   port=self.port,
                                   strict=self.strict)

        connection = VerifiedHTTPSConnection(host=self.host,
                                             port=self.port,
                                             strict=self.strict)
        connection.set_cert(key_file=self.key_file, cert_file=self.cert_file,
                            cert_reqs=self.cert_reqs, ca_certs=self.ca_certs)

        if self.ssl_version is None:
            connection.ssl_version = ssl.PROTOCOL_SSLv23
        else:
            connection.ssl_version = self.ssl_version

        return connection


def connection_from_url(url, **kw):
    
    scheme, host, port = get_host(url)
    if scheme == 'https':
        return HTTPSConnectionPool(host, port=port, **kw)
    else:
        return HTTPConnectionPool(host, port=port, **kw)
