
__author__ = 'Daniel'


class Solution:
    def submatrixSum(self, matrix):
        
        m = len(matrix)
        n = len(matrix[0])
        to_top = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]  
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                to_top[i][j] = to_top[i-1][j] + matrix[i-1][j-1]

        for up in xrange(m):
            for down in xrange(up, m):
                h = {}  
                s = 0
                h[s] = -1  
                for j in xrange(n):
                    s += to_top[down+1][j+1] - to_top[up][j+1]
                    if s in h:
                        return [[up, h[s]+1], [down, j]]
                    h[s] = j

        return [[-1, -1], [-1, -1]]

if __name__ == "__main__":
    assert Solution().submatrixSum([
        [1, 5, 7],
        [3, 7, -8],
        [4, -8, 9],
    ]) == [[1, 1], [2, 2]]



