

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @classmethod
    def new(cls, lst):
        return [
            cls(s, e)
            for s, e in lst
        ]

from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals):
        
        indexes = {
            itv.start: idx
            for idx, itv in enumerate(intervals)
        }
        starts = list(sorted(indexes.keys()))
        ret = []
        for itv in intervals:
            idx = bisect_left(starts, itv.end)
            if idx >= len(starts):
                ret.append(-1)
            else:
                ret.append(
                    indexes[starts[idx]]
                )

        return ret


if __name__ == "__main__":
    assert Solution().findRightInterval(Interval.new([ [3,4], [2,3], [1,2] ])) == [-1, 0, 1]
    assert Solution().findRightInterval(Interval.new([ [1,2] ])) == [-1]
    assert Solution().findRightInterval(Interval.new([ [1,4], [2,3], [3,4] ])) == [-1, 2, -1]
