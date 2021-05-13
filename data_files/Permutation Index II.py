
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def permutationIndexII(self, A):
        
        idx = 0
        factor = 1
        cnt = defaultdict(int)

        cnt[A[-1]] += 1
        n = len(A)
        for i in xrange(n-2, -1, -1):
            cnt[A[i]] += 1  
            for k, v in cnt.items():
                if k < A[i]:
                    idx += v * factor / cnt[A[i]]

            factor = factor * (n-i) / cnt[A[i]]

        return idx+1

if __name__ == "__main__":
    print Solution().permutationIndexII([1, 4, 2, 2])
