

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi and nums[lo] <= nums[lo + 1]:
            lo += 1

        while lo < hi and nums[hi - 1] <= nums[hi]:
            hi -= 1

        if hi <= lo:
            return 0

        mini = float('inf')
        maxa = -float('inf')
        for i in range(lo, hi + 1):
            mini = min(mini, nums[i])
            maxa = max(maxa, nums[i])

        while lo - 1 >= 0 and nums[lo - 1] > mini:
            lo -= 1
        while hi + 1 < n and nums[hi + 1] < maxa:
            hi += 1

        return hi - lo + 1

    def findUnsortedSubarray_sort(self, nums: List[int]) -> int:
        
        expected = list(sorted(nums))
        i = 0
        while i < len(nums) and nums[i] == expected[i]:
            i += 1

        j = len(nums) - 1
        while j >= i and nums[j] == expected[j]:
            j -= 1

        return j - i + 1


if __name__ == "__main__":
    assert Solution().findUnsortedSubarray([2, 1]) == 2
    assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
