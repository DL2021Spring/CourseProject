
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        num = int(cipher)
        cnt = 0
        for char in cipher:
            digit = int(char)
            if digit == 0: continue
            if num % digit == 0:
                cnt += 1

        return cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip()

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
