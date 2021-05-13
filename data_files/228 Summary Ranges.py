
__author__ = 'Daniel'


class Solution:
    def summaryRanges(self, nums):
        
        ret = []
        n = len(nums)
        if n < 1:
            return ret

        bgn = nums[0]
        pre = nums[0]
        for i in xrange(1, n):
            if nums[i] != pre+1:
                if pre != bgn:
                    ret.append("%d->%d"%(bgn, pre))
                else:
                    ret.append("%d"%bgn)
                bgn = nums[i]

            pre = nums[i]

        
        if pre != bgn:
            ret.append("%d->%d"%(bgn, pre))
        else:
            ret.append("%d"%bgn)

        return ret


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ['0->2', '4->5', '7']