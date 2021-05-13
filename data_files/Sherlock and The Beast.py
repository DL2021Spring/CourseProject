
__author__ = 'Danyang'


class Solution(object):
    def solve(self, N):
        
        for i in xrange(N / 3 * 3, -1, -3):
            if (N - i) % 5 == 0:
                return "5" * i + "3" * (N - i)

        return "-1"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = int(f.readline().strip())

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
