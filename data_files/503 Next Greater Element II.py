

from bisect import bisect


class Solution:
    def nextGreaterElements(self, nums):
        
        
        stk = []
        for n in nums[::-1]:
            while stk and stk[-1] <= n:
                stk.pop()
            stk.append(n)

        ret = []
        for n in nums[::-1]:
            while stk and stk[-1] <= n:
                stk.pop()
            ret.append(stk[-1] if stk else -1)
            stk.append(n)

        return ret[::-1]

    def nextGreaterElements_error(self, nums):
        
        A = nums + nums
        print(A)
        ret = []
        for e in nums:
            t = bisect(A, e)
            if t == len(A):
                ret.append(-1)
            else:
                ret.append(A[t])

        print(ret)
        return ret


if __name__ == "__main__":
    assert Solution().nextGreaterElements([1,2,1]) == [2, -1, 2]
