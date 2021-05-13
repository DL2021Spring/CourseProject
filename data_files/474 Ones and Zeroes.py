

from collections import Counter


class Solution:
    def findMaxForm(self, strs, m, n):
        
        if not strs:
            return 0

        F = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        z, o = self.count(strs[0])
        for i in range(m+1):
            for j in range(n+1):
                if i + z<= m and j + o <= n:
                    F[i][j] = 1

        for e in range(1, len(strs)):
            z, o = self.count(strs[e])
            for i in range(m+1):
                for j in range(n+1):
                    if i + z <= m and j + o <= n:
                        F[i][j] = max(
                            F[i][j],
                            F[i + z][j + o] + 1
                        )

        ret = max(
            F[i][j]
            for i in range(m + 1)
            for j in range(n + 1)
        )
        return ret

    def count(self, s):
        z, o = 0, 0
        for e in s:
            if e == "0":
                z += 1
            else:
                o += 1

        return z, o

    def findMaxForm_TLE(self, strs, m, n):
        
        if not strs:
            return 0

        F = [[[0 for _ in range(len(strs))] for _ in range(n + 1)] for _ in range(m + 1)]
        count = Counter(strs[0])
        for i in range(m+1):
            for j in range(n+1):
                if i + count["0"] <= m and j + count["1"] <= n:
                    F[i][j][0] = 1

        for e in range(1, len(strs)):
            count = Counter(strs[e])
            for i in range(m+1):
                for j in range(n+1):
                    if i + count["0"] <= m and j + count["1"] <= n:
                        F[i][j][e] = F[i + count["0"]][j + count["1"]][e-1] + 1
                    F[i][j][e] = max(F[i][j][e], F[i][j][e-1])

        ret = max(
            F[i][j][-1]
            for i in range(m + 1)
            for j in range(n + 1)
        )
        return ret

    def findMaxForm_error(self, strs, m, n):
        
        if not strs:
            return 0

        F = [[[0 for _ in range(len(strs))] for _ in range(n + 1)] for _ in range(m + 1)]
        count = Counter(strs[0])
        if count["0"] <= m and count["1"] <= n:
            F[m - count["0"]][n - count["1"]][0] += 1

        for e in range(1, len(strs)):
            count = Counter(strs[e])
            for i in range(m+1):
                for j in range(n+1):
                    if count["0"] <= i and count["1"] <= j:
                        F[i - count["0"]][j - count["1"]][e] = F[i][j][e-1] + 1
                    else:
                        F[i][j][e] = F[i][j][e-1]

        ret = max(
            F[i][j][-1]
            for i in range(m + 1)
            for j in range(n + 1)
        )
        return ret

    def findMaxForm_error(self, strs, m, n):
        
        strs.sort(key=len)
        ret = 0
        for a in strs:
            count = Counter(a)
            if count["0"] <= m and count["1"] <= n:
                ret += 1
                m -= count["0"]
                n -= count["1"]

        return ret


if __name__ == "__main__":
    assert Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4
    assert Solution().findMaxForm(["10", "0", "1"], 1, 1) == 2
    assert Solution().findMaxForm(["111", "1000", "1000", "1000"], 9, 3) == 3
