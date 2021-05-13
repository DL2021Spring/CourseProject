
__author__ = 'Daniel'


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    @staticmethod
    def cmp(a, b):
        
        if a.start != b.start:
            return a.start-b.start
        else:
            return a.end-b.end

    def countOfAirplanes(self, airplanes):
        
        return self.count_heap(airplanes)

    def count_heap(self, intervals):
        
        import heapq

        intervals.sort(cmp=Solution.cmp)
        heap = []
        cnt = 0
        for intv in intervals:
            
            heapq.heappush(heap, intv.end)
            
            while heap[0] <= intv.start:
                heapq.heappop(heap)

            cnt = max(cnt, len(heap))

        return cnt


if __name__ == "__main__":
    assert Solution().countOfAirplanes([Interval(i[0], i[1]) for i in [[1, 10], [2, 3], [5, 8], [4, 7]]]) == 3