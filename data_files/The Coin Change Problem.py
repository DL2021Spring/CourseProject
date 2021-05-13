

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        total, n, lst = cipher
        f = [[0 for _ in xrange(n)] for _ in xrange(total + 1)]

        for i in xrange(n):
            if lst[i] < total + 1:
                f[lst[i]][i] = 1  

        for k in xrange(1, total + 1):
            for i in reversed(xrange(n)):
                if k - lst[i] >= 0:
                    f[k][i] += f[k - lst[i]][i]  
                if i + 1 < n:
                    f[k][i] += f[k][i + 1]  

        return f[total][0]


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    N, M = map(int, f.readline().strip().split(' '))
    lst = map(int, f.readline().strip().split(' '))

    cipher = N, M, lst
    
    s = "%s\n" % (solution.solve(cipher))
    print s,
