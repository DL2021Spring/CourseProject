

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        f = [0 for _ in xrange(N + 1)]
        for i in xrange(1, N + 1):
            f[i] = f[i - 1] + A[i - 1]

        for i in xrange(N):
            if f[i] == f[N] - f[i + 1]:
                return "YES"
        return "NO"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N = int(f.readline().strip())
        A = map(int, f.readline().strip().split(' '))

        cipher = N, A
        
        s = "%s\n" % (solution.solve(cipher))
        print s,
