

__author__ = 'Danyang'

MOD = 1005060097


class Solution(object):
    def solve(self, cipher):
        
        N, K = cipher
        


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
