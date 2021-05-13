

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = cipher

        bit = 0
        for item in A:
            bit ^= item
        return bit


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    N = int(f.readline().strip())


    
    cipher = map(int, f.readline().strip().split(' '))

    
    s = "%s\n" % (Solution().solve(cipher))
    print s,
