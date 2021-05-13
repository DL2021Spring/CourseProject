
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        length, lst = cipher

        return reduce(lambda x, y: x | y, lst) * 2 ** (length - 1) % (10 ** 9 + 7)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        length = int(f.readline().strip())
        lst = map(lambda x: int(x), f.readline().strip().split(" "))
        cipher = [length, lst]
        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
