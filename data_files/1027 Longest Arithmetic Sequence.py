

from typing import List
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        F = defaultdict(lambda: defaultdict(lambda: 1))
        for i in range(len(A)):
            for j in range(i):
                delta = A[i] - A[j]
                F[i][delta] = F[j][delta] + 1

        ret = 0
        for d in F.values():
            for v in d.values():
                ret = max(ret, v)

        return ret


if __name__ == "__main__":
    assert Solution().longestArithSeqLength([20,1,15,3,10,5,8]) == 4
