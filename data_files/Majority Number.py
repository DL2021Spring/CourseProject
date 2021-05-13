
__author__ = 'Danyang'


class Solution:
    def majorityNumber(self, nums):
        
        cnt = 0
        maj = 0
        for ind, num in enumerate(nums):
            if num == nums[maj]:
                cnt += 1
            else:
                cnt -= 1  

            if cnt < 0:
                maj = ind
                cnt = 1

        
        return nums[maj]


if __name__ == "__main__":
    assert Solution().majorityNumber([1, 1, 1, 2, 2, 2, 2, 1, 1]) == 1



