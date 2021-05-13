
__author__ = 'Danyang'


class Solution:
    def minSubArray(self, nums):
        

        mini = min(nums)
        current = 0
        for a in nums:
            current += a
            mini = min(mini, current)
            if current > 0:
                current = 0

        return mini


if __name__ == "__main__":
    assert Solution().minSubArray([1, -1, -2, 1]) == -3


