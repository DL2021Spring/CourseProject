
__author__ = 'Danyang'


class Solution:
    def findPeak(self, A):
        
        n = len(A)
        l = 0
        h = n
        while l < h:
            m = (l+h)/2
            if A[m-1] < A[m] > A[m+1]:
                return m
            elif A[m+1] > A[m]:
                l = m+1
            else:
                h = m

        raise Exception  


if __name__ == "__main__":
    assert Solution().findPeak([1, 2, 1, 3, 4, 5, 7, 6]) in (1, 6)

