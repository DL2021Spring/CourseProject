

__author__ = 'Danyang'
MOD = 1234567


class Solution(object):
    def solve(self, cipher):
        
        return reduce(lambda x, y: x * y % MOD, cipher)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N = int(f.readline().strip())
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
