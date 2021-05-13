

__author__ = 'Daniel'


class Solution(object):
    def maxCoins(self, A):
        
        n = len(A)

        def get(i):
            if i < 0 or i >= n: return 1
            return A[i]

        F = [[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
        for i in xrange(n+1, -1, -1):
            for j in xrange(i+1, n+1):
                F[i][j] = max(
                    F[i][k]+get(i-1)*get(k)*get(j)+F[k+1][j]
                    for k in xrange(i, j)
                )

        return max(map(max, F))


if __name__ == "__main__":
    assert Solution().maxCoins([3, 1, 5, 8]) == 167

