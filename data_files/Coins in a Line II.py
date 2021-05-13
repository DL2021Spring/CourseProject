
__author__ = 'Daniel'


class Solution:
    def firstWillWin_MLE(self, values):
        
        n = len(values)
        if n <= 2:
            return True

        F = [[0 for _ in xrange(n)] for _ in xrange(2)]
        s = [0 for _ in xrange(n)]
        s[n-1] = values[n-1]
        for i in xrange(n-2, -1, -1):
            s[i] = values[i] + s[i+1]

        F[0][n-1] = F[1][n-1] = s[n-1]
        F[0][n-2] = F[1][n-2] = s[n-2]
        for i in xrange(n-3, -1, -1):
            for p in xrange(2):
                F[p][i] = max(
                    values[i]+s[i+1]-F[1^p][i+1],
                    values[i]+values[i+1]+s[i+2]-F[1^p][i+2]
                )
        if F[0][0]>F[1][1] or F[0][0]>F[1][2]:
            return True
        return False

    def firstWillWin(self, values):
        
        n = len(values)
        if n <= 2:
            return True

        F = [[0 for _ in xrange(4)] for _ in xrange(2)]

        s = values[n-1]
        F[0][(n-1)%4] = F[1][(n-1)%4] = s

        s += values[n-2]
        F[0][(n-2)%4] = F[1][(n-2)%4] = s

        for i in xrange(n-3, -1, -1):
            for p in xrange(2):
                t = i%4
                F[p][t] = max(
                    values[i]+s-F[1^p][(t+1)%4],
                    values[i]+s-F[1^p][(t+2)%4]
                )
                if i == 0:
                    break

            s += values[i]

        t = 0
        if F[0][t] > F[1][(t+1)%4] or F[0][t] > F[1][(t+2)%4]:
            return True

        return False

if __name__ == "__main__":
    values = [16,27,25,23,25,16,12,9,1,2,7,20,19,23,16,0,6,22,16,11,8,27,9,2,20,2,13,7,25,29,12,12,18,29,27,13,16,1,22,
              9,3,21,29,14,7,8,14,5,0,23,16,1,20]
    assert Solution().firstWillWin(values)==True

