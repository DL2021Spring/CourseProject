
__author__ = 'Daniel'


def read4(buf):
    
    return 0


class Solution(object):
    def read(self, buf, n):
        
        idx = 0
        while idx < n:
            buf4 = ["" for _ in xrange(4)]
            r = read4(buf4)
            if idx+r < n:
                buf[idx:idx+r] = buf4[:r]
                idx += r
                if r < 4: break
            else:
                buf[idx:n] = buf4[:n-idx]
                idx = n

        return idx
