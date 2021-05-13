

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        a = map(set, cipher)
        ret = a[0].intersection(a[1])
        if len(ret) > 0:
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = []
        cipher.append(f.readline().strip())
        cipher.append(f.readline().strip())
        
        s = "%s\n" % (solution.solve(cipher))
        print s,
