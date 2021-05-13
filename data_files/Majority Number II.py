
__author__ = 'Danyang'


class Solution:
    def majorityNumber(self, nums):
        
        n1, n2 = None, None
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num in (n1, n2):
                if num == n1:
                    cnt1 += 1
                else:
                    cnt2 += 1
            else:  
                if cnt1 == 0:
                    n1 = num
                    cnt1 += 1
                elif cnt2 == 0:
                    n2 = num
                    cnt2 += 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1

        
        if len(filter(lambda x: x == n1, nums)) > len(nums)/3:
            return n1
        else:
            return n2


if __name__ == "__main__":
    assert Solution().majorityNumber(
        [169, 43, 133, 93, 60, 29, 60, 104, 26, 60, 38, 52, 60, 118, 45, 183, 49, 42, 60, 0, 66, 67, 194, 127, 60, 60,
         60, 60, 60, 60]) == 60