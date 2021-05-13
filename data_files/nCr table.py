
MOD = 10 ** 9
__author__ = 'Danyang'


class Solution(object):
    def solve(self, n):
        
        result = []

        comb = 1  
        result.append(comb)
        for i in xrange(1, n + 1):
            comb = comb * (n + 1 - i) / i
            result.append(comb % MOD)

        return " ".join(map(str, result))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = int(f.readline().strip())

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
