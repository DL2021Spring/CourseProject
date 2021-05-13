

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        s = cipher
        r = s[::-1]
        s = map(ord, list(s))
        r = map(ord, list(r))
        for i in xrange(1, len(s)):
            if abs(s[i] - s[i - 1]) != abs(r[i] - r[i - 1]):
                return "Not Funny"
        return "Funny"


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip()

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
