



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
        

class Solution:
    def eraseOverlapIntervals(self, intervals):
        
        ret = 0
        if not intervals:
            return ret

        intervals.sort(key=lambda x: x.start)
        cur = intervals[0]
        for itv in intervals[1:]:
            if cur.end <= itv.start:
                cur = itv
            else:
                ret += 1
                cur = cur if cur.end < itv.end else itv

        return ret


if __name__ == "__main__":
    assert Solution().eraseOverlapIntervals(Interval.new([ [1,2], [2,3], [3,4], [1,3] ])) == 1
    assert Solution().eraseOverlapIntervals(Interval.new([ [1,2], [1,2], [1,2] ])) == 2
    assert Solution().eraseOverlapIntervals(Interval.new([ [1,2], [2,3] ])) == 0
