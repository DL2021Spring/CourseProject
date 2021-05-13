

from collections import defaultdict


class Solution:
    def findTargetSumWays(self, A, S):
        
        if not A:
            return
        F = defaultdict(lambda: defaultdict(int))
        F[0][0] = 1
        for i in range(len(A)):
            for k in F[i].keys():  
                F[i+1][k-A[i]] += F[i][k]
                F[i+1][k+A[i]] += F[i][k]

        return F[len(A)][S]


if __name__ == "__main__":
    assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
