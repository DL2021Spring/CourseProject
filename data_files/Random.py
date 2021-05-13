

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    n, a, b = map(int, f.readline().strip().split(' '))
    D = map(int, f.readline().strip().split(' '))
    cipher = n, a, b, D

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
