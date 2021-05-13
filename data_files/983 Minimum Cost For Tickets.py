

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        F = [float("inf") for _ in range(366 + 30)]
        for i in range(366, 366 + 30):
            F[i] = 0

        days_set = set(days)
        for i in range(365, 0, -1):
            if i not in days_set:
                F[i] = F[i+1]
            else:
                F[i] = min(
                    c + F[i+d]
                    for d, c in zip([1, 7, 30], costs)
                )

        return F[1]

    def mincostTickets_error(self, days: List[int], costs: List[int]) -> int:
        
        n = len(days)
        F = [float("inf") for _ in range(n)]
        F[-1] = costs[0]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                delta = days[j] - days[i]
                if delta <= 1:
                    F[i] = min(F[i], costs[0] + F[j])
                if delta <= 7:
                    F[i] = min(F[i], costs[1] + F[j])
                if delta <= 30:
                    F[i] = min(F[i], costs[2] + F[j])
                else:
                    break
        return F[0]

    def mincostTickets_error(self, days: List[int], costs: List[int]) -> int:
        
        F = [float("inf") for _ in range(365 + 1)]
        F[0] = 0
        days_set = set(days)
        for i in range(1, 366):
            if i not in days_set:
                F[i] = F[i-1]
            else:
                
                F[i] = min(F[i], F[i-1] + costs[0])


if __name__ == "__main__":
    assert Solution().mincostTickets([1,4,6,7,8,20], [2,7,15]) == 11
