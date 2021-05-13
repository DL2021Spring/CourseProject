

import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        L, S1, S2, qs = cipher
        v = abs(S1 - S2) / math.sqrt(2)
        rets = []
        for q in qs:
            t = (L - math.sqrt(q)) / v
            rets.append(t)
        return "\n".join(map(lambda x: "%f" % x, rets))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    L, S1, S2 = map(int, f.readline().strip().split(' '))
    q = int(f.readline().strip())
    qs = []
    for t in xrange(q):
        qs.append(int(f.readline().strip()))

    
    cipher = L, S1, S2, qs
    
    s = "%s\n" % (solution.solve(cipher))
    print s,
