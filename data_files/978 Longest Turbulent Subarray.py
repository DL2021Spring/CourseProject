

from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        
        flag = None  
        ret = 1
        cur = 1
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                flag = None
                cur = 1
            elif A[i] > A[i+1]:
                if flag is None or flag == 1:
                    cur += 1
                    ret = max(ret, cur)
                else:
                    cur = 2
                flag = 0
            else:  
                if flag is None or flag == 0:
                    cur += 1
                    ret = max(ret, cur)
                else:
                    cur = 2
                flag = 1

        return ret


if __name__ == "__main__":
    assert Solution().maxTurbulenceSize([9,4,2,10,7,8,8,1,9]) == 5
