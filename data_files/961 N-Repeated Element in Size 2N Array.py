

from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        n = len(A)
        for i in range(n - 1):
            for j in range(3):
                if A[i] == A[min(n - 1, i + 1 + j)]:
                    return A[i]

        raise


if __name__ == "__main__":
    assert Solution().repeatedNTimes([1,2,3,3]) == 3
