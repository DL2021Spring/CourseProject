
__author__ = 'Daniel'
from collections import namedtuple
Sum = namedtuple("Sum", "sum i j")  


class Solution:
    def continuousSubarraySum(self, A):
        
        if len(A) < 1:
            return [-1, -1]

        ret = Sum(A[0], 0, 0)
        cur = 0  
        s = 0
        for e, v in enumerate(A):
            cur += v
            if ret.sum < cur:
                ret = Sum(cur, s, e)

            if cur < 0:
                s = e+1
                cur = 0

        return [ret.i, ret.j]


if __name__ == "__main__":
    assert Solution().continuousSubarraySum(
        [-101, -33, -44, -55, -67, -78, -101, -33, -44, -55, -67, -78, -100, -200, -1000, -22, -100, -200, -1000, -22]
    ) == [15, 15]
