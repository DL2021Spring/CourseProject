
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        global_max = -1
        A, B = cipher
        for i in xrange(A, B + 1):
            for j in xrange(i + 1, B + 1):
                global_max = max(global_max, i ^ j)
        return global_max


if __name__ == "__main__":
    import sys
    
    f = sys.stdin
    A = int(f.readline().strip())
    B = int(f.readline().strip())
    cipher = (A, B)

    s = "%s\n" % (Solution().solve(cipher))
    print s,
