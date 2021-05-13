
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        r2, k = cipher

        required = 0
        r = r2 ** 0.5

        for x in xrange(0, int(r) + 1):
            
            low = 0
            high = int(r) + 1
            while low <= high:
                mid = (low + high) / 2
                if x * x + mid * mid == r2:
                    if mid == 0 or x == 0:
                        required += 2
                    else:
                        required += 4
                    if required > k: return "impossible"
                    break
                elif x * x + mid * mid < r2:
                    low = mid + 1
                else:
                    high = mid - 1

        if required > k: return "impossible"
        return "possible"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
