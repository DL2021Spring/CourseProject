
__author__ = 'Daniel'


class Solution(object):
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i < n:
            v = A[i]
            if v <= 0 or v > n:
                i += 1
            elif A[v-1] != v:
                A[v-1], A[i] = v, A[v-1]
            else:
                i += 1

        for i in xrange(n):
            if A[i] != i+1:
                return i+1

        return n+1


if __name__ == "__main__":
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2