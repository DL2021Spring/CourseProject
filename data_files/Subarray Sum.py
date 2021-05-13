
__author__ = 'Daniel'
from collections import defaultdict


class Solution:
    def subarraySum(self, nums):
        
        n = len(nums)
        f = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            f[i] = f[i-1]+nums[i-1]

        d = defaultdict(list)
        for i in xrange(1, n+1):
            d[f[i]].append(i)

        for k, v in d.items():
            if k == 0:
                return [0, v[0]-1]
            if len(v) > 1:
                return [v[0], v[1]-1]

        return [-1, -1]


if __name__ == "__main__":
    print Solution().subarraySum([-5, 10, 5, -3, 1, 1, 1, -2, 3, -4])