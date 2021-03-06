
__author__ = 'Daniel'
from collections import namedtuple

Sum = namedtuple("Sum", "sum i j")  


class Solution:
    def continuousSubarraySumII(self, A):
        
        if len(A) < 1:
            return [-1, -1]
        linear = self.linear_max_sum(A)
        circular = self.circular_max_sum(A)
        if linear.sum > circular.sum:
            return [linear.i, linear.j]

        return [circular.i, circular.j]

    def circular_max_sum(self, A):
        
        n = len(A)
        left = [None for _ in A]
        right = [None for _ in A]

        cur, max_sum, idx = 0, A[0], 0
        for i in xrange(n):
            cur += A[i]
            if cur > max_sum:
                idx = i
                max_sum = cur
            left[i] = (max_sum, idx)

        cur, max_sum, idx = 0, A[n-1], n-1
        for i in xrange(n-1, -1, -1):
            cur += A[i]
            if cur > max_sum:
                idx = i
                max_sum = cur
            right[i] = (max_sum, idx)

        ret = Sum(A[0], 0, 0)
        for i in xrange(1, n):
            r = right[i]
            l = left[i-1]
            if ret.sum < r[0]+l[0]:
                ret = Sum(r[0]+l[0], r[1], l[1])

        return ret

    def linear_max_sum(self, A):
        
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

        return ret

if __name__ == "__main__":
    assert Solution().continuousSubarraySumII([3, 1, -100, -3, 4]) == [4, 1]
    assert Solution().continuousSubarraySumII([-5, 10, 5, -3, 1, 1, 1, -2, 3, -4]) == [1, 8]