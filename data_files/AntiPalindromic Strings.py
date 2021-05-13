

__author__ = 'Danyang'

MOD = 10 ** 9 + 7


class Solution(object):
    def solve(self, cipher):
        
        N, M = cipher
        s = M
        if N > 1:
            s *= (M - 1)
        if N > 2:
            s *= pow(M - 2, N - 2, MOD)  
            s %= MOD
        return s % MOD

    def _exp(self, a, b):
        
        ret = 1
        b %= MOD
        while b > 0:
            if b & 1 == 0:
                b /= 2
                a *= a
                a %= MOD
            else:
                ret *= a
                ret %= MOD
                b -= 1
        return ret


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
