
__author__ = 'Daniel'


class Solution:
    def maximalSquare(self, matrix):
        
        m = len(matrix)
        if m < 1: return 0
        n = len(matrix[0])
        if n < 1: return 0
        for i in xrange(m):
            matrix[i] = map(int, matrix[i])

        maxa = 0
        to_top = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        to_left = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        square_width = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if matrix[i-1][j-1] == 0:
                    continue

                to_top[i][j] += to_top[i-1][j] + matrix[i-1][j-1]
                to_left[i][j] += to_left[i][j-1] + matrix[i-1][j-1]
                square_width[i][j] = min(
                    square_width[i-1][j-1]+1,
                    to_left[i][j],
                    to_top[i][j],
                )
                maxa = max(maxa, square_width[i][j])

        return maxa*maxa

