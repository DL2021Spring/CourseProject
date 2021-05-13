
from collections import deque

__author__ = 'Daniel'


class Solution(object):
    def largestDivisibleSubset(self, A):
        
        if not A: return []

        F = {}
        pi = {}
        A.sort()
        for i in xrange(len(A)):
            F[i] = 1
            pi[i] = i
            for j in xrange(i):
                if A[i] % A[j] == 0:
                    if F[i] < 1 + F[j]:
                        F[i] = 1 + F[j]
                        pi[i] = j

        max_i, max_v = 0, 1
        for k, v in F.items():
            if v > max_v:
                max_i, max_v = k, v

        ret = deque()
        cur = max_i
        ret.appendleft(A[cur])
        while pi[cur] != cur:
            cur = pi[cur]
            ret.appendleft(A[cur])

        return list(ret)


if __name__ == "__main__":
    assert Solution().largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8]
