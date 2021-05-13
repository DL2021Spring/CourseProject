

from typing import List
from functools import lru_cache


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        
        N = len(stones)
        sums = [0]
        for s in stones:
            sums.append(sums[-1] + s)

        @lru_cache(None)
        def F(i, j, m):
            if i >= j or m < 1:
                return float("inf")

            n = j - i
            if (n - m) % (K - 1) != 0:
                return float("inf")

            if j == i + 1:
                if m == 1:
                    return 0
                return float("inf")

            if m == 1:
                return F(i, j, K) + sums[j] - sums[i]

            ret = min(
                F(i, mid, 1) + F(mid, j, m - 1)
                for mid in range(i + 1, j, K - 1)
            )
            return ret

        ret = F(0, N, 1)
        return ret if ret != float("inf") else -1


if __name__ == "__main__":
    assert Solution().mergeStones([3,5,1,2,6], 3) == 25
