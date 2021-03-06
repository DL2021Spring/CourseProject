



class Solution:
    def findMaxConsecutiveOnes(self, nums):
        
        s = 0
        e = 0
        ret = 0
        while s < len(nums):
            if nums[s] == 1:
                while e < len(nums) and nums[e] == 1:
                    e += 1
                ret = max(ret, e - s)
            else:
                e += 1

            s = e

        return ret


if __name__ == "__main__":
    assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
