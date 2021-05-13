

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        l = 1
        h = cipher
        while l <= h:
            mid = (l + h) / 2
            if self.sum_of_squares(mid) <= cipher:
                l = mid + 1
            else:
                h = mid - 1

        l -= 1
        return l

    def sum_of_squares(self, n):
        return n * (n + 1) * (2 * n + 1) / 6


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = int(f.readline().strip())

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
