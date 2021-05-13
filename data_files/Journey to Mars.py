
import math
from decimal import *

__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        getcontext().prec = 28

    def solve(self, cipher):
        
        N, K = cipher
        LSB = pow(2, N - 1, 10 ** K)

        
        MSB = int(str(self.get_MSB(2, N - 1) * 10 ** K)[:K])

        return MSB + LSB

    def get_MSB(self, b, n):
        
        p = Decimal(n) * Decimal(b).log10()
        f = Decimal(p) - Decimal(math.floor(p))
        return Decimal(10) ** f


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
