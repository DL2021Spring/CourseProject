

from typing import List
from collections import defaultdict


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        m, n = len(A), len(A[0])
        F = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for j in range(n):
            F[m-1][j] = A[m-1][j]

        for i in range(m-2, -1, -1):
            for j in range(n):
                F[i][j] = min(F[i+1][j-1], F[i+1][j], F[i+1][j+1]) + A[i][j]

        return min(
            F[0][j]
            for j in range(n)
        )

    def minFallingPathSum_std(self, A: List[List[int]]) -> int:
        
        m, n = len(A), len(A[0])
        F = [[float('inf') for _ in range(n)] for _ in range(m)]
        for j in range(n):
            F[m-1][j] = A[m-1][j]

        for i in range(m-2, -1, -1):
            for j in range(n):
                F[i][j] = min(F[i][j], F[i+1][j] + A[i][j])
                if j - 1 >= 0:
                    F[i][j] = min(F[i][j], F[i+1][j-1] + A[i][j])
                if j + 1 < n:
                    F[i][j] = min(F[i][j], F[i+1][j+1] + A[i][j])

        return min(F[0])


if __name__ == "__main__":
    assert Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 12
