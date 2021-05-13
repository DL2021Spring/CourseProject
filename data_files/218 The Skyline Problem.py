

__author__ = 'Daniel'
from collections import defaultdict, namedtuple
import heapq


class Building(object):
    def __init__(self, h):
        self.h = h
        self.deleted = False  

    def __cmp__(self, other):
        
        assert isinstance(other, Building)
        return other.h - self.h



Event = namedtuple('Event', 'starts ends')


class Solution:
    def getSkyline(self, buildings):
        
        
        events = defaultdict(lambda: Event(starts=[], ends=[]))
        for left, right, height in buildings:
            building = Building(height)
            events[left].starts.append(building)  
            events[right].ends.append(building)

        heap_h = []  
        cur_h = 0  
        ret = []
        
        for x, event in sorted(events.items()):  
            for building in event.starts:
                heapq.heappush(heap_h, building)
            for building in event.ends:
                building.deleted = True

            
            
            while heap_h and heap_h[0].deleted:
                heapq.heappop(heap_h)

            
            
            new_h = heap_h[0].h if heap_h else 0

            if new_h != cur_h:
                cur_h = new_h
                ret.append([x, cur_h])

        return ret


if __name__ == "__main__":
    assert Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]) == \
           [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]