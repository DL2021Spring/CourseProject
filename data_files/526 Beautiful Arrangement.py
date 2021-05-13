



class Solution:
    def countArrangement(self, N: int) -> int:
        
        candidates = set(range(1, N+1))
        ret = self.dfs(candidates, 1, N)
        return ret

    def dfs(self, candidates, i, N):
        if i > N:
            return 1

        ret = 0
        for c in candidates:
            if c % i == 0 or i % c == 0:
                candidates.remove(c)
                ret += self.dfs(candidates, i+1, N)
                candidates.add(c)
        return ret


if __name__ == "__main__":
    assert Solution().countArrangement(2) == 2
