

from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        
        ret = []
        for i in range(1, 10):
            ret.extend(self.dfs(i, N, K))

        if N == 1:
            ret.append([0])  

        return list(
            map(lambda x: int("".join(map(str, x))), ret)
        )

    def dfs(self, start: int, N: int, K: int) -> List[List[int]]:
        if (start, N, K) not in self.cache:
            ret = []
            if N == 1:
                ret = [[start]]
            elif N > 1:
                if start + K <= 9:
                    for e in self.dfs(start + K, N - 1, K):
                        ret.append([start] + e)
                if start - K >= 0 and K != 0:  
                    for e in self.dfs(start - K, N - 1, K):
                        ret.append([start] + e)

            self.cache[start, N, K] = ret

        return self.cache[start, N, K]


if __name__ == "__main__":
    Solution().numsSameConsecDiff(3, 7) == [181,292,707,818,929]
