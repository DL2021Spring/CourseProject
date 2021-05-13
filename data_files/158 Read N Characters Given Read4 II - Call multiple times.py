
__author__ = 'Daniel'


def read4(buf):
    
    return 0


class Solution(object):
    def __init__(self):
        self.prev = []

    def read(self, buf, n):
        
        l = min(len(self.prev), n)
        buf[:l] = self.prev[:l]
        self.prev = self.prev[l:]  

        idx = l  
        while idx < n:
            buf4 = ["" for _ in xrange(4)]
            r = read4(buf4)
            if idx+r < n:
                buf[idx:idx+r] = buf4[:r]
                idx += r
                if r < 4: return idx
            else:
                buf[idx:n] = buf4[:n-idx]
                self.prev = buf4[n-idx:r]  
                idx = n

        return idx