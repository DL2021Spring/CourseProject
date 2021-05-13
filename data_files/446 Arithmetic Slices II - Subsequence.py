

from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A):
        
        ret = 0
        D = defaultdict(lambda: defaultdict(int))
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                D[i][d] += 1 + D[j][d]
                if D[j][d] > 0:
                    
                    ret += D[j][d]  

        return ret

    def numberOfArithmeticSlices_error(self, A):
        
        ret = 0
        D = defaultdict(lambda: defaultdict(int))
        for i in range(len(A)):
            for j in range(i):
                delta = A[i] - A[j]
                D[i][delta] += 1 + D[j][delta]

            for j in range(i):
                delta = A[i] - A[j]
                if D[j][delta] > 0:
                    ret += D[i][delta]  

        return ret


if __name__ == "__main__":
    assert Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]) == 7
