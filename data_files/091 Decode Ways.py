
__author__ = 'Danyang'


class Solution(object):
    def numDecodings(self, s):
        
        if s.startswith("0"):
            return 0

        n = len(s)
        if not s:
            return 0
        F = [0 for _ in xrange(n+1)]
        F[0] = 1
        F[1] = 1

        for i in xrange(2, n+1):
            if s[i-1] != "0":
                F[i] = F[i-1]
                if 10 <= int(s[i-2]+s[i-1]) < 27:
                    F[i] += F[i-2]
            else:  
                if s[i-2] in ("1", "2"):
                    F[i] = F[i-2]
                else:
                    return 0

        return F[-1]


if __name__ == "__main__":
    assert Solution().numDecodings("10") == 1
    assert Solution().numDecodings("27") == 1
    assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("0") == 0