
__author__ = 'Danyang'
fib = lambda n: reduce(lambda x, n: [x[1], x[0] + x[1]], xrange(n), [0, 1])[0]


class Solution(object):
    def solve(self, cipher):
        
        num = int(cipher)
        n = 0
        while fib(n) < num:
            n += 1
        if fib(n) == num:
            return "IsFibo"
        else:
            return "IsNotFibo"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip()

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
