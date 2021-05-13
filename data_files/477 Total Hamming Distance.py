



class Solution:
    def totalHammingDistance(self, nums):
        
        ret = 0
        while any(nums):  
            z, o = 0, 0
            for i in range(len(nums)):
                if nums[i] & 1 == 0:
                    o += 1
                else:
                    z += 1
                nums[i] >>= 1

            ret += z * o

        return ret


if __name__ == "__main__":
    assert Solution().totalHammingDistance([4, 14, 2]) == 6
