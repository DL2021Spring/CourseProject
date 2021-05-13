

from typing import List


class Solution:
    def checkPossibility(self, A: List[int]) -> bool:
        
        changed = False
        for i in range(len(A) - 1):
            if A[i] <= A[i + 1]:
                continue
            if not changed:
                if i - 1 < 0 or A[i-1] <= A[i+1]:
                    A[i] = A[i+1]
                else:
                    A[i+1] = A[i]
                changed = True
            else:
                return False

        return True

    def checkPossibility_error(self, A: List[int]) -> bool:
        
        changed = False
        for i in range(len(A) - 1):
            if A[i] <= A[i + 1]:
                continue
            if not changed:
                A[i] = A[i + 1]  
                if i - 1 < 0 or A[i - 1] <= A[i]:
                    changed = True
                else:
                    return False
            else:
                return False

        return True


if __name__ == "__main__":
    assert Solution().checkPossibility([4,2,3]) == True
    assert Solution().checkPossibility([3,4,2,3]) == False
    assert Solution().checkPossibility([2,3,3,2,4]) == True
