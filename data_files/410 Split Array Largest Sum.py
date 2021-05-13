

from typing import List
from functools import lru_cache


class SolutionDP:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        n = len(nums)
        sums = [0]
        for e in nums:
            sums.append(sums[-1] + e)

        F = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
        for l in range(1, n + 1):
            F[l][1] = sums[l] - sums[0]
        

        for l in range(1, n + 1):
            for k in range(1, m + 1):
                for j in range(l):
                    F[l][k] = min(
                        F[l][k], max(F[j][k-1], sums[l] - sums[j])
                    )

        return F[n][m]


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        lo = max(nums)
        hi = sum(nums) + 1
        ret = hi
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = 1  
            cur_sum = 0
            for e in nums:
                if cur_sum + e > mid:
                    cnt += 1
                    cur_sum = e
                else:
                    cur_sum += e

            if cnt <= m:
                ret = min(ret, mid)  
                hi = mid
            else:
                lo = mid + 1

        return ret


class SolutionTLE2:
    def __init__(self):
        self.sums = [0]

    def splitArray(self, nums: List[int], m: int) -> int:
        
        for n in nums:
            self.sums.append(self.sums[-1] + n)

        ret = self.dfs(len(nums), m)
        return ret

    @lru_cache(maxsize=None)
    def dfs(self, hi, m):
        
        if m == 1:
            return self.sums[hi] - self.sums[0]

        mini = float("inf")
        for j in range(hi):
            right = self.sums[hi] - self.sums[j]
            left = self.dfs(j, m - 1)
            
            mini = min(mini, max(left, right))

        return mini


class SolutionTLE:
    def __init__(self):
        self.sums = [0]

    def splitArray(self, nums: List[int], m: int) -> int:
        
        for n in nums:
            self.sums.append(self.sums[-1] + n)
        ret = self.dfs(tuple(nums), 0, len(nums), m)
        return ret

    @lru_cache(maxsize=None)
    def dfs(self, nums, lo, hi, m):
        
        if m == 1:
            return self.sums[hi] - self.sums[lo]

        mini = float("inf")
        for j in range(lo, hi):
            left = self.sums[j] - self.sums[lo]
            right = self.dfs(nums, j, hi, m - 1)
            
            mini = min(mini, max(left, right))

        return mini


if __name__ == "__main__":
    assert Solution().splitArray([1, 4, 4], 3) == 4
    assert Solution().splitArray([7,2,5,10,8], 2) == 18
