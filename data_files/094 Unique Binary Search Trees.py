
import math

__author__ = 'Danyang'


class Solution(object):
    def numTrees_math(self, n):
        
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n))-math.factorial(2*n)/(
            math.factorial(n+1)*math.factorial(n-1))

    def numTrees(self, n):
        
        if n < 2:
            return n

        dp = [0 for _ in xrange(n+1)]
        dp[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]


if __name__ == "__main__":
    assert Solution().numTrees(100) == Solution().numTrees_math(100)