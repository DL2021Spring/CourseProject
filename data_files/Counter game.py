
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N = cipher
        turn = 0
        while N > 1:
            turn += 1
            if N & (N - 1) == 0:
                N /= 2
            else:
                num = 1
                while num < N:
                    num <<= 1
                num >>= 1
                N -= num

        if turn & 1 == 0:
            return "Richard"
        else:
            return "Louise"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = int(f.readline().strip())

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
