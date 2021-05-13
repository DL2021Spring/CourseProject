



class Solution:
    def checkSubarraySum(self, nums, k):
        
        h = {0: 0}  
        s = 0
        for l in range(1, len(nums) + 1):
            s += nums[l-1]
            if k != 0:  
                s %= k
            if s in h:
                if l - h[s] >= 2:  
                    return True
            else:
                
                h[s] = l

        return False


if __name__ == "__main__":
    assert Solution().checkSubarraySum([23,2,4,6,7], 6) == True
