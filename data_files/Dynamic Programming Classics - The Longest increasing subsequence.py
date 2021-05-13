
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        maxa = 1
        f = [1 for _ in xrange(N)]
        for i in xrange(1, N):
            for j in xrange(i):
                if A[i] > A[j]:
                    f[i] = max(f[i], f[j] + 1)
            maxa = max(maxa, f[i])
        return maxa


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    N = int(f.readline().strip())

    A = []
    for _ in xrange(N):
        A.append(int(f.readline().strip()))
    cipher = N, A
    
    s = "%s\n" % (solution.solve(cipher))
    print s,
