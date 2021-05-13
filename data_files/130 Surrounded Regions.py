
__author__ = 'Danyang'
CONNECTED = 'C'
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def solve(self, board):
        
        if not board or not board[0]:
            return
        q = []
        
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            if board[i][0]=='O': q.append((i, 0))
            if board[i][n-1]=='O': q.append((i, n-1))
        for j in xrange(1, n-1):
            if board[0][j]=='O': q.append((0, j))
            if board[m-1][j]=='O': q.append((m-1, j))


        while q: 
            cor = q.pop()
            board[cor[0]][cor[1]]=CONNECTED  
            for direction in directions:
                row = cor[0]+direction[0]
                col = cor[1]+direction[1]
                if 0<=row<m and 0<=col<n and board[row][col]=='O':
                    q.append((row, col))


        for i in xrange(m):
            for j in xrange(n):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                elif board[i][j]==CONNECTED:
                    board[i][j] = 'O'


if __name__=="__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    expected_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    Solution().solve(board)
    assert board==expected_board




