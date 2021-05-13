
__author__ = 'Danyang'


class Solution(object):
    def solve_error(self, cipher):
        
        a, b = cipher
        m = len(a)
        n = len(b)
        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])  
        return dp[-1][-1]

    def solve(self, cipher):
        
        a, b = cipher
        m = len(a)
        n = len(b)
        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])  
        return dp[-1][-1]


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    cipher = []
    cipher.append(f.readline().strip())
    cipher.append(f.readline().strip())

    s = "%s\n" % (Solution().solve(cipher))
    print s,
