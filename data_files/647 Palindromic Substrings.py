

from collections import defaultdict


class Solution:
    def countSubstrings(self, s):
        
        F = defaultdict(lambda: defaultdict(bool))
        n = len(s)
        for i in range(n):
            F[i][i] = True
            F[i][i+1] = True

        for i in range(n-1, -1, -1):
            for j in range(i+2, n+1):
                if s[i] == s[j-1]:
                    F[i][j] = F[i+1][j-1]
                else:
                    F[i][j] = False

        return sum(
            1
            for i in range(n)
            for j in range(i+1, n+1)
            if F[i][j]
        )


if __name__ == "__main__":
    assert Solution().countSubstrings("aaa") == 6
