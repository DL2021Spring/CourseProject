
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        ret = 0
        for i, val in enumerate(A):
            if (i + 1) * (N - i) % 2 == 1:
                ret ^= val
        return ret


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
