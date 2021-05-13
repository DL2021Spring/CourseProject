





import logging

from ._collections import RecentlyUsedContainer
from .connectionpool import HTTPConnectionPool, HTTPSConnectionPool
from .connectionpool import connection_from_url, port_by_scheme
from .request import RequestMethods
from .util import parse_url


__all__ = ['PoolManager', 'ProxyManager', 'proxy_from_url']


pool_classes_by_scheme = {
    'http': HTTPConnectionPool,
    'https': HTTPSConnectionPool,
}

log = logging.getLogger(__name__)


class PoolManager(RequestMethods):
    

    def __init__(self, num_pools=10, headers=None, **connection_pool_kw):
        RequestMethods.__init__(self, headers)
        self.connection_pool_kw = connection_pool_kw
        self.pools = RecentlyUsedContainer(num_pools,
                                           dispose_func=lambda p: p.close())

    def clear(self):
        
        self.pools.clear()

    def connection_from_host(self, host, port=None, scheme='http'):
        
        port = port or port_by_scheme.get(scheme, 80)

        pool_key = (scheme, host, port)

        
        
        pool = self.pools.get(pool_key)
        if pool:
            return pool

        
        pool_cls = pool_classes_by_scheme[scheme]
        pool = pool_cls(host, port, **self.connection_pool_kw)

        self.pools[pool_key] = pool

        return pool

    def connection_from_url(self, url):
        
        u = parse_url(url)
        return self.connection_from_host(u.host, port=u.port, scheme=u.scheme)

    def urlopen(self, method, url, redirect=True, **kw):
        
        u = parse_url(url)
        conn = self.connection_from_host(u.host, port=u.port, scheme=u.scheme)

        kw['assert_same_host'] = False
        kw['redirect'] = False
        if 'headers' not in kw:
            kw['headers'] = self.headers

        response = conn.urlopen(method, u.request_uri, **kw)

        redirect_location = redirect and response.get_redirect_location()
        if not redirect_location:
            return response

        if response.status == 303:
            method = 'GET'

        log.info("Redirecting %s -> %s" % (url, redirect_location))
        kw['retries'] = kw.get('retries', 3) - 1  
        return self.urlopen(method, redirect_location, **kw)


class ProxyManager(RequestMethods):
    

    def __init__(self, proxy_pool):
        self.proxy_pool = proxy_pool

    def _set_proxy_headers(self, headers=None):
        headers_ = {'Accept': '*/*'}
        if headers:
            headers_.update(headers)

        return headers_

    def urlopen(self, method, url, **kw):
        "Same as HTTP(S)ConnectionPool.urlopen, ``url`` must be absolute."
        kw['assert_same_host'] = False
        kw['headers'] = self._set_proxy_headers(kw.get('headers'))
        return self.proxy_pool.urlopen(method, url, **kw)


def proxy_from_url(url, **pool_kw):
    proxy_pool = connection_from_url(url, **pool_kw)
    return ProxyManager(proxy_pool)
