
MOD = 10 ** 9
__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        
        self.C = [[1 for _ in xrange(2000)] for _ in xrange(2000)]
        for n in xrange(1, 2000):
            for k in xrange(1, n):  
                self.C[n][k] = self.C[n - 1][k - 1] + self.C[n - 1][k]

    def solve(self, cipher):
        
        N, K = cipher
        return self.C[N + K - 1][K] % MOD


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())
    solution = Solution()
    for t in xrange(testcases):
        
        N = int(f.readline().strip())
        K = int(f.readline().strip())
        cipher = N, K
        
        s = "%s\n" % (solution.solve(cipher))
        print s,
