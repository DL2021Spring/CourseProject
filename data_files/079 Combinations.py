
__author__ = 'Danyang'
class Solution:
    def combine(self, n, k):
        
        result = []
        nums = [i+1 for i in xrange(n)]  
        self.get_combination(k, nums, [], result)
        return result

    def get_combination(self, k, nums, current, result):
        if len(current)==k:
            result.append(current)
            return  
        elif len(current)+len(nums)<k:
            return  

        for ind, val in enumerate(nums):
            
            self.get_combination(k, nums[ind+1:], current+[val], result)  
            
            
            


if __name__=="__main__":
    print Solution().combine(4, 2)