
__author__ = 'Daniel'


class Solution(object):
    def findMissing(self, nums):
        
        nth = -1
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == n:
                nth = nums[i]
                i += 1
            elif nums[i] != i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]  
                
            else:
                i += 1

        if nth == -1:
            return n
        else:
            return nums.index(nth)


if __name__ == "__main__":
    print Solution().findMissing([9,8,7,6,2,0,1,5,4])




