

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        
        ret = -float("inf")
        prev_max = A[0]
        for a in A[1:]:
            ret = max(ret, prev_max - 1 + a)
            prev_max = max(prev_max - 1, a)

        return ret

    def maxScoreSightseeingPair_error(self, A: List[int]) -> int:
        
        n = len(A)
        B = []
        for i in range(n):
            B.append(A[i] - i)

        
        m1, m2 = None, None
        for i in range(n):
            if m1 is None:
                m1 = i
            elif m2 is None:
                m2 = i
            elif B[i] + (i - m1) > B[m1]:
                m1 = i
            elif B[i] + (i - m2) > B[m2]:
                m2 = i
        return A[m2] + A[m1] - abs(m2 - m1)


if __name__ == "__main__":
    assert Solution().maxScoreSightseeingPair([8,1,5,2,6]) == 11
