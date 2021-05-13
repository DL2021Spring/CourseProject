
__author__ = 'Danyang'
class Solution:
    def minimumTotal(self, triangle):
        
        dp = []
        length = len(triangle)

        
        dp.insert(0, [num for num in triangle[length-1]])
        
        for row in xrange(length-1-1, -1, -1):
            dp.insert(0, [])
            for col in xrange(len(triangle[row])):
                dp[0].append(triangle[row][col]+min(dp[1][col], dp[1][col+1]))  

        assert len(dp[0])==1

        return dp[0][0]


if __name__=="__main__":
    Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])