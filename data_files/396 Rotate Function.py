
import sys

__author__ = 'Daniel'


class Solution(object):
    def maxRotateFunction(self, A):
        
        if not A: return 0

        gmax = -sys.maxint
        n = len(A)
        s = sum(A)

        cur = sum(idx * val for idx, val in enumerate(A))
        for r in reversed(A):
            cur = cur + s - n * r
            gmax = max(gmax, cur)

        return gmax


if __name__ == "__main__":
    assert Solution().maxRotateFunction([4, 3, 2, 6]) == 26
