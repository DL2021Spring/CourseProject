
import sys

__author__ = 'Danyang'


class Solution(object):
    def findMin(self, A):
        
        lo = 0
        hi = len(A)
        mini = sys.maxint
        while lo < hi:
            mid = (lo+hi)/2
            mini = min(mini, A[mid])
            if A[lo] <= A[mid] <= A[hi-1]:
                return min(mini, A[lo])
            elif A[lo] > A[mid] < A[hi-1]:
                hi = mid
            else:
                lo = mid+1

        return mini


if __name__ == "__main__":
    num = [7, 1, 2, 3, 4, 5, 6]
    assert Solution().findMin(num) == 1
