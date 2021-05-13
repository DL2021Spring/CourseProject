

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        l = len(cipher)
        if l == 1:
            if int(cipher) % 8 == 0:
                return "YES"
            else:
                return "NO"
        elif l == 2:
            if int(cipher) % 8 == 0 or int(cipher[::-1]) % 8 == 0:
                return "YES"
            else:
                return "NO"

        
        hm = [0 for _ in xrange(10)]
        for char in cipher:
            hm[int(char)] += 1

        for i in xrange(0, 1000, 8):
            copy = list(hm)
            s = "00" + str(i)
            j = -1
            while j >= -3:  
                d = int(s[j])
                if copy[d] <= 0: break
                copy[d] -= 1
                j -= 1
            if j == -4:
                return "YES"
        return "NO"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip()

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
