
__author__ = 'Danyang'
class Solution:
    def minPathSum(self, grid):
        
        if not grid:
            return 0

        row_cnt = len(grid)
        col_cnt = len(grid[0])


        dp = [[1<<31 for _ in xrange(col_cnt)] for _ in xrange(row_cnt)]

        
        for i in xrange(row_cnt):
            for j in xrange(col_cnt):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i==0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j==0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]  

        return dp[row_cnt-1][col_cnt-1]