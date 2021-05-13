
__author__ = 'Daniel'


class Solution:
    def postOffice_TLE(self, A, K):
        
        A.sort()
        N = len(A)
        F = [[0 for _ in xrange(K+1)] for _ in xrange(N+1)]
        c = [[0 for _ in xrange(N+1)] for _ in xrange(N+1)]  

        for i in xrange(N):
            for j in xrange(i+1, N+1):
                m = (i+j)/2
                for l in xrange(i, j):
                    c[i][j] += abs(A[m]-A[l])

        for n in xrange(1, N+1):
            F[n][1] = c[0][n]

        for n in xrange(1, N+1):
            for k in xrange(2, K+1):
                F[n][k] = min(
                    F[l][k-1]+c[l][n] for l in xrange(n)
                )

        return F[N][K]

    def postOffice_TLE(self, A, K):
        
        


if __name__ == "__main__":
    assert Solution().postOffice([112,122,360,311,85,225,405,53,405,43,342,13,588,424,299,37,104,289,404,414], 3) == 673