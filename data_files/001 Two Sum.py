
__author__ = 'Danyang'


class Solution:
    def twoSum_TLE(self, num, target):
        
        nums = num
        for ind1, val in enumerate(nums):
            try:
                ind2 = nums.index(target - val)
                return ind1+1, ind2+1
            except ValueError:
                continue

    def twoSum_TLE_2(self, num, target):
        nums = num
        for ind1, val in enumerate(nums):
            if target-val in nums:
                return ind1+1, nums.index(target-val)+1

    def twoSum(self, num, target):
        
        hash_map = {}
        for ind, val in enumerate(num):
            hash_map[val] = ind

        for ind1, val in enumerate(num):
            if target-val in hash_map:
                ind2 = hash_map[target-val]
                if ind1!=ind2:
                    return ind1+1, ind2+1


if __name__=="__main__":
    print Solution().twoSum([3, 2, 4], 6)