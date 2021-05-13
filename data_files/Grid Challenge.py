

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        m = len(cipher)
        n = len(cipher[0])
        cipher = map(lambda x: sorted(x), cipher)
        
        for j in xrange(n):
            for i in xrange(m - 1):
                if cipher[i][j] > cipher[i + 1][j]:
                    return "NO"
        return "YES"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        n = int(f.readline().strip())
        cipher = []
        for i in xrange(n):
            cipher.append(list(f.readline().strip()))

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
