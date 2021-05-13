

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        a, b, x, y = cipher
        if self.gcd(a, b) == self.gcd(x, y):
            return "YES"
        else:
            return "NO"

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
