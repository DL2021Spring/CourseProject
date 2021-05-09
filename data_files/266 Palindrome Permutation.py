
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def canPermutePalindrome(self, s):
        
        m = defaultdict(int)
        for c in s:
            m[c] += 1

        once = False
        for v in m.values():
            if v % 2 == 1:
                if once:
                    return False
                once = True

        return True