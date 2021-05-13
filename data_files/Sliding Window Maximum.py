
__author__ = 'Daniel'


class Solution:
    def maxSlidingWindow(self, nums, k):
        
        if not nums or k == 0:
            return []

        q = []
        ret = []
        for i in xrange(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ret.append(nums[q[0]])  

        for i in xrange(k, len(nums)):  
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            while q and q[0] < i-k+1:  
                q.pop(0)
            q.append(i)
            ret.append(nums[q[0]])

        return ret


if __name__ == "__main__":
    print Solution().maxSlidingWindow([1, 2, 7, 7, 8], 3)