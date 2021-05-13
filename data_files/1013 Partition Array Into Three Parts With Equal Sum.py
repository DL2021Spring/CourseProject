

from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False

        target = s // 3
        count = 0
        cur_sum = 0
        for a in A:
            cur_sum += a
            if cur_sum == target:
                count += 1
                cur_sum = 0
            
            
            

        return count == 3 and cur_sum == 0


if __name__ == "__main__":
    assert Solution().canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]) == True
