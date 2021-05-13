

import collections

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        d = collections.defaultdict(int)
        for c in cipher:
            d[c] += 1

        cnt = 0
        for v in d.values():
            if v & 1 == 1:
                cnt += 1
            if cnt > 1:
                return "NO"
        return "YES"


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    cipher = f.readline().strip()

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
