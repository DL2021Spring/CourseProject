

__author__ = 'Danyang'
import heapq


class Solution:
    def thirdMax(self, nums):
        
        if not nums:
            return None

        h = []
        for e in set(nums):
            if len(h) < 3:
                heapq.heappush(h, e)
            elif len(h) == 3 and e > h[0]:
                heapq.heappushpop(h, e)

        assert len(h) <= 3
        if len(h) == 3:
            ret = min(h)
        else:
            ret = max(h)
        return ret


if __name__ == "__main__":
    assert Solution().thirdMax([1, 2, 3, 4]) == 2
    assert Solution().thirdMax([4, 3, 2, 1]) == 2
    assert Solution().thirdMax([2, 2, 3, 1]) == 1
    assert Solution().thirdMax([4, 3]) == 4
