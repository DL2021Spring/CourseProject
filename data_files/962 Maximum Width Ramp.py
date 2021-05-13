

from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        
        ret = -float("inf")
        V = [(a, i) for i, a in enumerate(A)]
        V.sort()
        min_idx = float("inf")
        for _, i in V:
            
            ret = max(ret, i - min_idx)
            min_idx = min(min_idx, i)

        return max(ret, 0)
