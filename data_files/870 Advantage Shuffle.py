

from typing import List
from collections import defaultdict


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        
        idxes = defaultdict(list)
        for i, b in enumerate(B):
            idxes[b].append(i)

        n = len(A)
        A.sort()
        B.sort()
        ret = [None for _ in range(n)]
        not_used = []
        j = 0
        for a in A:
            if a > B[j]:
                i = idxes[B[j]].pop()
                ret[i] = a
                j += 1
            else:
                not_used.append(a)

        for i in range(n):
            if ret[i] is None:
                ret[i] = not_used.pop()

        return ret


if __name__ == "__main__":
    assert Solution().advantageCount([2,7,11,15], [1,10,4,11]) == [2,11,7,15]
