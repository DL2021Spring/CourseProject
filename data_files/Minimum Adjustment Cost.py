
__author__ = 'Danyang'


class Solution:
    def MinAdjustmentCost(self, A, target):
        
        S = 100
        n = len(A)
        f = [[1<<31 for _ in xrange(S+1)] for _ in xrange(n+1)]

        for j in xrange(S+1):
            f[0][j] = 0

        for i in xrange(1, n+1):
            for j in xrange(1, S+1):
                for k in xrange(max(1, j-target), min(S, j+target)+1):
                    f[i][j] = min(f[i][j], f[i-1][k]+abs(A[i-1]-j))

        mini = 1<<31
        for j in xrange(1, S+1):
            mini = min(mini, f[n][j])

        return mini


if __name__ == "__main__":
    assert Solution().MinAdjustmentCost([12, 3, 7, 4, 5, 13, 2, 8, 4, 7, 6, 5, 7], 2) == 19

