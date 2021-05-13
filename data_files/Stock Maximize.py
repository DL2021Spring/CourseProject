

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        f = [0 for _ in A]
        f[N - 1] = A[N - 1]
        for i in xrange(N - 2, -1, -1):
            f[i] = max(A[i], f[i + 1])

        profit = 0
        for i in xrange(N - 1):
            profit += max(0, f[i + 1] - A[i])

        return profit


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N = int(f.readline().strip())
        A = map(int, f.readline().strip().split(' '))
        cipher = N, A
        
        s = "%s\n" % (solution.solve(cipher))
        print s,
