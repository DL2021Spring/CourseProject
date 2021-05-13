
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N = cipher

        x = 1
        while True:  
            binary = bin(x)[2:]
            nine_ary = str(binary).replace("1", "9")
            dec = int(nine_ary)
            if dec % N == 0:
                return dec
            x += 1


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = int(f.readline().strip())

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
