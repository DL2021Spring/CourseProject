
MOD = 10 ** 9 + 7
import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, M = cipher
        return math.factorial(N + M - 1) / math.factorial(N) / math.factorial(M - 1) % MOD


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
