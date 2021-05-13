

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = cipher
        B = []
        B.append(A[0])
        for i in xrange(1, len(A)):
            B.append(A[i] * A[i - 1] / self.gcd(A[i], A[i - 1]))
        B.append(A[-1])

        return " ".join(map(str, B))

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N = int(f.readline().strip())
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
