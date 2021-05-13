

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K, A = cipher
        total = N * (N + 1) / 2
        total_only_s = 0
        i = 0
        while i < N:
            if A[i] > K:
                i += 1
            else:
                j = i + 1
                while j < N and A[j] <= K: j += 1
                l = j - i
                total_only_s += l * (l + 1) / 2

                i = j

        return total - total_only_s


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N, K = map(int, f.readline().strip().split(' '))
        A = map(int, f.readline().strip().split(' '))
        cipher = N, K, A
        
        s = "%s\n" % (solution.solve(cipher))
        print s,
