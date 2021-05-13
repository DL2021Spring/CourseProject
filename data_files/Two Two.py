
__author__ = 'Danyang'


class Solution(object):
    def solve_TLE(self, cipher):
        
        
        a = cipher[0]
        counter = 0
        for i in xrange(len(a)):
            if a[i] == "0":
                continue
            for j in xrange(i, len(a)):
                
                strength = a[i:j + 1]
                strength = int(strength)
                if strength & (strength - 1) == 0:
                    counter += 1
        return counter

    def solve(self, cipher):
        

    def strength(self, a, i, j):
        
        if a[i] == 0:
            return 0
        value = 0
        for k in xrange(i, j + 1):
            value = value * 10 + a[k]
        return value


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip().split(' ')

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
