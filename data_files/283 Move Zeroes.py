

__author__ = 'Daniel'


class Solution(object):
    def moveZeroes(self, nums):
        
        left = -1
        for i in xrange(len(nums)):
            if nums[i] != 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]


class SolutionCount(object):
    def moveZeroes(self, nums):
        
        cnt = 0
        for elt in nums:
            if elt != 0:
                nums[cnt] = elt
                cnt += 1

        for j in xrange(cnt, len(nums)):
            nums[j] = 0


if __name__ == "__main__":
    lst = [0, 1, 0, 3, 12]
    Solution().moveZeroes(lst)
    assert lst == [1, 3, 12, 0, 0]
