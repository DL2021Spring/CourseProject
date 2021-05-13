

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        l = N + 1

        E = 0
        for cur in A:
            k = 0
            for a in A:
                if a >= cur:
                    k += 1  
            E += float(l) / (k + 1)
        return "%.2f" % E


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N = int(f.readline().strip())
        A = map(int, f.readline().strip().split(' '))
        cipher = N, A

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
