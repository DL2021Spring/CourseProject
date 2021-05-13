

from collections import defaultdict


class Solution:
    def fourSumCount(self, A, B, C, D):
        
        N = len(A)
        AB = defaultdict(int)
        CD = defaultdict(int)
        for i in range(N):
            for j in range(N):
                AB[A[i] + B[j]] += 1
                CD[C[i] + D[j]] += 1

        ret = 0
        
        for gross, count in AB.items():
            target = 0 - gross
            ret += count * CD[target]

        return ret


if __name__ == "__main__":
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    assert Solution().fourSumCount(A, B, C, D) == 2
