

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        a, b, x = cipher
        if a > 1:
            result = int((a ** b) / float(x) + 0.5) * x
        else:
            result = 1
        if result != int(result):
            if result > 0.5 and x == 1:
                return 1
            else:
                return 0
        return result


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
