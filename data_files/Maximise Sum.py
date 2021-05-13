

import bisect

__author__ = 'Daniel'


class Solution(object):
    def solve(self, cipher):
        
        N, M, A = cipher

        F = []
        s = 0
        maxa = 0
        for a in A:
            s += a
            s %= M
            idx = bisect.bisect_left(F, s)
            F.insert(idx, s)  

            
            idx = min(bisect.bisect_right(F, (s+1)%M), len(F)-1)
            maxa = max(maxa, (s-F[idx])%M, (s-F[idx-1])%M, s%M)

        return maxa

    def solve_brute(self, cipher):
        
        N, M, A = cipher
        F = [0]
        s = 0
        for a in A:
            s = (s+a) % M
            F.append(s)

        maxa = 0
        for i in xrange(1, len(A)+1):
            for j in xrange(i):
                maxa = max(maxa, F[i], (F[i]-F[j])%M)

        return maxa

if __name__ == "__main__":
    import sys
    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N, M = map(int, f.readline().strip().split(' '))
        A = map(int, f.readline().strip().split(' '))
        cipher = N, M, A
        
        s = "%s\n" % (solution.solve(cipher))
        print s,