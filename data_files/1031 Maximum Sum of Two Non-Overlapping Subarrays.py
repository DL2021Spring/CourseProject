

from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        n = len(A)
        F = [0 for _ in range(n + 1)]
        for i, a in enumerate(A):
            F[i+1] = F[i] + a

        ret = -float("inf")
        for l, m in ((L, M), (M, L)):
            for i in range(n + 1 - l):
                for j in range(i + l, n + 1 - m):  
                    cur = F[i + l] - F[i] + F[j + m] - F[j]
                    ret = max(ret, cur)

        return ret


if __name__ == "__main__":
    assert Solution().maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2) == 20
