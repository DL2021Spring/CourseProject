

import sys

__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        self.dirs = [(0, 1, 'L'), (0, -1, 'R'), (-1, 0, 'D'), (1, 0, 'U')]

    def solve(self, cipher):
        
        M, N, K, mat = cipher
        i_dest = -1
        j_dest = -1
        for i in xrange(M):
            for j in xrange(N):
                if mat[i][j] == "*":
                    i_dest = i
                    j_dest = j
                    break

        f = [[[sys.maxint for _ in xrange(N)] for _ in xrange(M)] for _ in xrange(K + 1)]
        for k in xrange(K + 1):  
            f[k][0][0] = 0

        for k in xrange(1, K + 1):  
            for i in xrange(0, M):
                for j in xrange(0, N):
                    for dir in self.dirs:
                        i_pre = i + dir[0]
                        j_pre = j + dir[1]
                        if 0 <= i_pre < M and 0 <= j_pre < N:
                            if mat[i_pre][j_pre] == dir[2]:
                                f[k][i][j] = min(f[k][i][j], f[k - 1][i_pre][j_pre])
                            else:
                                f[k][i][j] = min(f[k][i][j], f[k - 1][i_pre][j_pre] + 1)

        mini = sys.maxint
        for k in xrange(K + 1):
            mini = min(mini, f[k][i_dest][j_dest])
        return mini if mini != sys.maxint else -1


if __name__ == "__main__":
    f = open("0.in", "r")
    
    solution = Solution()
    M, N, K = map(int, f.readline().strip().split(' '))
    mat = []
    for i in xrange(M):
        mat.append(list(f.readline().strip()))

    cipher = M, N, K, mat
    
    s = "%s\n" % (solution.solve(cipher))
    print s,
