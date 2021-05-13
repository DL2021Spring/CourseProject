

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)

        ret = 0
        cur_end = -float("inf")
        for i in range(n):
            if pairs[i][0] <= cur_end:
                continue

            cur_end = pairs[i][1]
            ret += 1

        return ret

    def findLongestChain2(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)

        ret = 0
        i = 0
        while i < n:
            ret += 1
            cur_end = pairs[i][1]

            i += 1
            while i < n and pairs[i][0] <= cur_end:
                i += 1

        return ret


class Solution2:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: tuple(x))
        n = len(pairs)
        F = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    F[i] = max(F[i], F[j] + 1)

        return max(F)


if __name__ == "__main__":
    assert Solution().findLongestChain([[1,2], [2,3], [3,4]]) == 2
