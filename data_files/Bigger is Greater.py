

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = list(cipher)
        A = map(ord, A)
        n = len(A)

        a = -1
        for i in xrange(n - 1, 0, -1):
            if A[i - 1] < A[i]:
                a = i - 1
                break
        else:
            return "no answer"

        b = -1
        for i in xrange(n - 1, a, -1):
            if A[i] > A[a]:
                b = i
                break
        else:
            return "no answer"

        A[a], A[b] = A[b], A[a]  
        A = A[:a + 1] + A[n - 1:a:-1]  
        return "".join(map(chr, A))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip()

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
