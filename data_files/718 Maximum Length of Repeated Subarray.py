

from typing import List
from collections import defaultdict


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        
        m, n = len(A), len(B)
        F = defaultdict(lambda: defaultdict(int))
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    F[i][j] = F[i-1][j-1] + 1

        return max(
            F[i][j]
            for i in range(1, m+1)
            for j in range(1, n+1)
        )


if __name__ == "__main__":
    assert Solution().findLength([1,2,3,2,1], [3,2,1,4,7]) == 3
