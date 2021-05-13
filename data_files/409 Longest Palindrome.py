
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def longestPalindrome(self, s):
        
        c = defaultdict(int)
        for elt in s:
            c[elt] += 1

        ret = 0
        for v in c.values():
            ret += (v/2) * 2

        if any(map(lambda x: x % 2 == 1, c.values())):
            ret += 1

        return ret


if __name__ == "__main__":
    assert Solution().longestPalindrome("abccccdd") == 7
