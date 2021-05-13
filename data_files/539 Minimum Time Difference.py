

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        ret = float("inf")
        A = list(sorted(map(self.minutes, timePoints)))
        n = len(A)
        for i in range(n - 1):
            ret = min(ret, self.diff(A[i+1], A[i]))

        ret = min(ret, self.diff(A[n-1], A[0]))
        return ret

    def diff(self, b, a):
        ret = b - a
        if ret > 12 * 60:
            ret = 24 * 60 - ret

        return ret

    def minutes(self, a):
        h, m = a.split(":")
        minutes = 60 * int(h) + int(m)
        return minutes


if __name__ == "__main__":
    assert Solution().findMinDifference(["23:59","00:00"]) == 1
