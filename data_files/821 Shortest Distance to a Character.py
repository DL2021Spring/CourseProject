

from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
        idx = [
            i
            for i in range(len(S))
            if S[i] == C
        ]
        idx = [-float("inf")] + idx + [float("inf")]
        ret = []
        i = 0
        for j in range(len(S)):
            while not idx[i] <= j < idx[i+1]:
                i += 1

            ret.append(min(j - idx[i], idx[i+1] - j))

        return ret
