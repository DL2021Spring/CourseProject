
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, lst = cipher
        for i in xrange(N):
            for j in xrange(i + 1, N):
                if self.gcd(lst[i], lst[j]) == 1:
                    return "YES"
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
        
        N = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(' '))
        cipher = (N, lst)
        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
