
import bisect

__author__ = 'Daniel'


class Solution(object):
    def maxEnvelopes(self, A):
        
        if not A: return 0

        A.sort(key=lambda (w, h): (w, -h))
        F = [-1 for _ in xrange(len(A)+1)]

        F[1] = A[0][1]  
        k = 1
        for _, h in A[1:]:
            idx = bisect.bisect_left(F, h, 1, k+1)
            F[idx] = h
            k += 1 if idx == k+1 else 0

        return k

    def maxEnvelopesTLE(self, A):
        
        if not A: return 0

        predicate = lambda a, b: b[0] > a[0] and b[1] > a[1]
        A.sort()
        n = len(A)
        F = [1 for _ in xrange(n)]
        for i in xrange(1, n):
            for j in xrange(i):
                if predicate(A[j], A[i]):
                    F[i] = max(F[i], 1 + F[j])

        return max(F)


if __name__ == "__main__":
    assert Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    assert Solution().maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]) == 5
