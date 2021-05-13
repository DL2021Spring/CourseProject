
__author__ = 'Daniel'
import heapq
from collections import defaultdict


class Building(object):
    def __init__(self, h):
        self.h = h
        self.deleted = False

    def __cmp__(self, other):
        
        return other.h - self.h


class Event(object):
    def __init__(self):
        
        self.starts = []
        self.ends = []


class Solution:
    def buildingOutline(self, buildings):
        
        events = defaultdict(Event)
        for start, end, height in buildings:
            building = Building(height)
            events[start].starts.append(building)
            events[end].ends.append(building)

        ret = []
        cur_heap = []
        cur_max_hi = 0
        begin = None
        for x, event in sorted(events.items()):
            for building in event.starts:  
                heapq.heappush(cur_heap, building)
            for building in event.ends:  
                building.deleted = True

            while cur_heap and cur_heap[0].deleted:
                heapq.heappop(cur_heap)

            new_hi = cur_heap[0].h if cur_heap else 0
            if cur_max_hi != new_hi:
                if cur_max_hi != 0:
                    ret.append([begin, x, cur_max_hi])
                begin = x

                cur_max_hi = new_hi

        return ret

if __name__ == "__main__":
    assert Solution().buildingOutline([
        [1, 3, 3],
        [2, 4, 4],
        [5, 6, 1]
    ]) == [[1, 2, 3], [2, 4, 4], [5, 6, 1]]