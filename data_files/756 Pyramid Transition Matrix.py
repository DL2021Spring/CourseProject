

import itertools
from typing import List
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        T = defaultdict(set)  
        for a, b, c in allowed:
            T[a, b].add(c)

        return self.dfs(T, bottom)

    def dfs(self, T, level) -> bool:
        if len(level) == 1:
            return True

        
        for nxt_level in itertools.product(
            *[T[a, b] for a, b in zip(level, level[1:])]
        ):
            if self.dfs(T, nxt_level):
                return True

        return False

    def gen_nxt_level(self, T, level, lo):
        
        if lo + 1 >= len(level):
            yield ""
            return

        for head in T[level[lo], level[lo + 1]]:
            for tail in self.gen_nxt_level(T, level, lo + 1):
                yield head + tail


    def dfs_deep(self, T, level, lo, nxt_level) -> bool:
        if lo + 1 == len(level):
            return True

        for nxt in T[level[lo], level[lo + 1]]:
            nxt_level.append(nxt)
            if self.dfs(T, level, lo + 1, nxt_level):
                
                if self.dfs(T, nxt_level, 0, []):
                    return True
            nxt_level.pop()

        return False


if __name__ == "__main__":
    assert Solution().pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF"]) == True
    assert Solution().pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]) == False
