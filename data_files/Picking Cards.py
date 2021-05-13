
__author__ = 'Danyang'
MOD = 1000000007


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        cnts = [0 for _ in xrange(N + 1)]
        for num in A:
            cnts[num] += 1

        if 0 not in cnts:
            return 0

        
        result = 1
        paths = cnts[0]
        for i in xrange(1, N):
            if paths <= 0:
                return 0
            result *= paths  
            result %= MOD
            paths += cnts[i]
            paths -= 1  

        return result


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N = int(f.readline().strip())
        A = map(int, f.readline().strip().split(' '))
        cipher = N, A
        
        s = "%s\n" % (solution.solve(cipher))
        print s,
