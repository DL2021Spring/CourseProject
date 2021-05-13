
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K, A, B = cipher
        A.sort()
        B.sort(reverse=True)  
        for i in xrange(N):
            if not A[i] + B[i] >= K:
                return "NO"
        return "YES"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N, K = map(int, f.readline().strip().split(" "))
        A = map(int, f.readline().strip().split(' '))
        B = map(int, f.readline().strip().split(' '))
        cipher = N, K, A, B
        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
