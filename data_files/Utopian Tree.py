
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N = int(cipher[0])
        
        height = 1  
        for cycle in xrange(N):
            if cycle & 1 == 0:
                height *= 2
            else:
                height += 1

        return height


if __name__ == "__main__":
    import sys
    
    f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip().split(' ')

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
