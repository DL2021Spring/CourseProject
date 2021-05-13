
__author__ = 'Danyang'
import math


class Solution(object):
    def solve(self, cipher):
        
        N = cipher

        if N % 2 == 1:
            return 0

        cnt = 0
        i = 1
        sq = math.sqrt(N)
        while i <= sq:
            if N % i == 0:
                if i % 2 == 0:
                    cnt += 1
                other = N / i
                if other != i and other % 2 == 0:
                    cnt += 1
            i += 1
        return cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = int(f.readline().strip())

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
