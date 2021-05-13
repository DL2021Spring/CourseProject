

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = cipher
        L = [-1 for _ in A]
        for i in xrange(1, len(A)):
            idx = i - 1
            while idx != -1:
                if A[idx] > A[i]:
                    L[i] = idx
                    break
                idx = L[idx]

        R = [-1 for _ in A]
        for i in xrange(len(A) - 2, -1, -1):
            idx = i + 1
            while idx != -1:
                if A[idx] > A[i]:
                    R[i] = idx
                    break
                idx = R[idx]

        maxa = -1
        for i in xrange(len(A)):
            left = L[i] + 1
            right = R[i] + 1
            maxa = max(maxa, left * right)

        return maxa


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    N = int(f.readline().strip())

    cipher = map(int, f.readline().strip().split(' '))

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
