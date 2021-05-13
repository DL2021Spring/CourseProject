

__author__ = 'Daniel'
import heapq


class Solution:
    def findKthLargest(self, nums, k):
        
        h = []
        n = len(nums)
        for i, v in enumerate(nums):
            if i < k:
                heapq.heappush(h, v)
            else:
                if v <= h[0]:
                    continue
                heapq.heappop(h)
                heapq.heappush(h, v)

        return heapq.heappop(h)


if __name__ == "__main__":
    print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)

