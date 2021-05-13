
__author__ = 'Danyang'


class Solution:
    def findMedianSortedArrays(self, A, B):
        
        m = len(A)
        n = len(B)
        if ((m+n)&1 == 0):
            return (self.find_kth(A, B, (m+n)/2)+self.find_kth(A, B, (m+n)/2-1))/2.0
        else:
            return self.find_kth(A, B, (m+n)/2)

    def find_kth(self, A, B, k):
        
        if not A:  return B[k]
        if not B:  return A[k]
        if k == 0: return min(A[0], B[0])

        m, n = len(A), len(B)
        
        if A[m/2] >= B[n/2]:
            if k > m/2+n/2:
                return self.find_kth(A, B[n/2+1:], k-n/2-1)  
            else:
                return self.find_kth(A[:m/2], B, k)  
        else:
            return self.find_kth(B, A, k)


if __name__ == "__main__":
    assert Solution().findMedianSortedArrays([1, 2], [1, 2, 3]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [3]) == 2
    assert Solution().findMedianSortedArrays([1], [2, 3]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [1, 2]) == 1.5
