

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        F = [float('inf') for _ in range(n+1)]
        F[0] = 0
        F[1] = 0
        for i in range(2, n+1):
            F[i] = min(
                F[i-2] + cost[i-2],
                F[i-1] + cost[i-1]
            )

        return F[-1]


if __name__ == "__main__":
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15
