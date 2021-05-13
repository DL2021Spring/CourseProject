
__author__ = 'Danyang'


class Solution:
    def maxTwoSubArrays(self, nums):
        
        n = len(nums)

        f = [[-1<<31 for _ in xrange(n+1)] for _ in xrange(2)]

        cur = 0
        for i in xrange(1, n+1):
            cur += nums[i-1]
            f[0][i] = max(nums[i-1], f[0][i-1], cur)
            if cur < 0:
                cur = 0

        cur = 0
        for i in xrange(n-1, -1, -1):
            cur += nums[i]
            f[1][i] = max(nums[i], f[1][i+1], cur)
            if cur < 0:
                cur = 0

        maxa = -1<<31
        for i in xrange(1, n):
            maxa = max(maxa, f[0][i]+f[1][i])
        return maxa


if __name__ == "__main__":
    print Solution().maxTwoSubArrays([1, 3, -1, 2, -1, 2])





