
__author__ = 'Daniel'


class Solution:
    def largestNumber(self, nums):
        
        nums = map(str, nums)
        nums.sort(cmp=self.cmp, reverse=True)
        nums = "".join(nums)
        nums = nums.lstrip("0")
        if not nums:
            nums = "0"
        return nums

    def cmp(self, a, b):
        
        order = 1
        if len(a) > len(b):
            order = -1
            a, b = b, a

        for i in xrange(len(a)):
            if int(a[i]) != int(b[i]):
                return order*(int(a[i])-int(b[i]))

        if len(a) == len(b):
            return 0

        return order*self.cmp(a, b[len(a):])


if __name__ == "__main__":
    assert Solution().largestNumber([0, 0]) == "0"
    assert Solution().largestNumber([1, 20, 23, 4, 8]) == "8423201