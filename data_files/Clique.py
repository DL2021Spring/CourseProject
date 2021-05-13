
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, M = cipher
        
        
        
        
        
        
        
        


        
        
        
        low = 0
        high = N
        while low + 1 < high:
            mid = (low + high) / 2
            r = self.Turan(N, mid)

            if r < M:
                low = mid
            else:
                high = mid
        return high

    def Turan(self, n, r):
        
        return 0.5 * (n ** 2 - (n % r) * (n / r + 1) ** 2 - (r - (n % r)) * (n / r) ** 2)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
