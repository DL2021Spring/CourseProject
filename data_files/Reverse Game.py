

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K = cipher
        if K < N / 2:
            return 2 * K + 1
        else:
            return 2 * (N - 1 - K)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
