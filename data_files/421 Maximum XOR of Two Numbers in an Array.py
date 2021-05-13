



class Solution:
    def findMaximumXOR(self, nums):
        
        ret = 0
        for i in reversed(range(32)):
            prefixes = set(num >> i for num in nums)
            ret <<= 1
            
            cur = ret + 1
            for p in prefixes:
                
                if cur ^ p in prefixes:
                    ret = cur
                    break  

        return ret


if __name__ == "__main__":
    assert Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28
