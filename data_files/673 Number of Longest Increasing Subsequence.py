

from typing import List


class LenCnt:
    def __init__(self, l, c):
        self.l = l
        self.c = c

    def __repr__(self):
        return repr((self.l, self.c))


class Solution:
    def findNumberOfLIS(self, A: List[int]) -> int:
        
        if not A:
            return 0

        n = len(A)
        F = [LenCnt(l=1, c=1) for _ in A]
        mx = LenCnt(l=1, c=1)
        for i in range(1, n):
            for j in range(i):
                if A[i] > A[j]:
                    if F[i].l < F[j].l + 1:
                        F[i].l = F[j].l + 1
                        F[i].c = F[j].c
                    elif F[i].l == F[j].l + 1:
                        F[i].c += F[j].c

            if F[i].l > mx.l:
                
                mx.l = F[i].l
                mx.c = F[i].c
            elif F[i].l == mx.l:
                mx.c += F[i].c

        return mx.c


if __name__ == "__main__":
    assert Solution().findNumberOfLIS([1,1,1,2,2,2,3,3,3]) == 27
    assert Solution().findNumberOfLIS([1, 3, 5, 4, 7]) == 2
    assert Solution().findNumberOfLIS([2, 2, 2, 2, 2]) == 5
