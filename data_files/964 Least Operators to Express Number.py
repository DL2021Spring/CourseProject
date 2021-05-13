

from functools import lru_cache


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        
        return self.dfs(target, x, 0) - 1

    @lru_cache(maxsize=None)
    def dfs(self, target, x, power):
        
        if target == 0:
            return 0

        if target == 1:
            return self.ops(power)

        d, r = target // x, target % x
        ret = r * self.ops(power) + self.dfs(d, x, power + 1)
        
        if r != 0:
            ret2 = (x - r) * self.ops(power) + self.dfs(d + 1, x, power + 1)
            ret = min(ret, ret2)

        return ret

    def ops(self, power):
        
        if power == 0:
            return 2
        else:
            return power


if __name__ == "__main__":
    assert Solution().leastOpsExpressTarget(3, 19) == 5
    assert Solution().leastOpsExpressTarget(5, 501) == 8
    assert Solution().leastOpsExpressTarget(2, 125046) == 50
