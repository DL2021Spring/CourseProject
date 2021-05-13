
__author__ = 'Daniel'


class PriorityQueue(object):
    def __init__(self):
        self.lst = []

    def bisect(self, t):
        
        l = 0
        h = len(self.lst)
        while l < h:
            m = (l+h)/2
            if self.lst[m] < t:
                l = m+1
            else:
                h = m

        return l

    def insert(self, t):
        pos = self.bisect(t)
        self.lst.insert(pos, t)  

    def remove(self, t):
        pos = self.bisect(t)
        if self.lst[pos] != t:
            raise ValueError("%s not found in the queue"%str(t))
        del self.lst[pos]

    def __getitem__(self, item):
        return self.lst[item]


import heapq
from collections import defaultdict


class Heap(object):
    def __init__(self):
        self.h = []
        self.existing = defaultdict(int)
        self.len = 0

    def push(self, t):
        heapq.heappush(self.h, t)
        self.existing[t] += 1
        self.len += 1

    def pop(self):
        
        while True:
            a = heapq.heappop(self.h)
            if self.existing[a] == 0:
                continue
            else:
                self.remove(a)
                return a

    def remove(self, t):
        
        if self.existing[t] < 1:
            raise ValueError("%s does not exist in the heap"%str(t))

        self.existing[t] -= 1
        self.len -= 1

    def __len__(self):
        return self.len

    def peek(self):
        a = self.h[0]
        if self.existing[a] > 0:
            return a

        a = self.pop()
        self.push(a)
        return a

    def __repr__(self):
        return repr(self.existing)


class DualHeap(object):
    def __init__(self):
        self.min_h = Heap()  
        self.max_h = Heap()  

    def _rebalance(self):
        r = len(self.min_h)
        l = len(self.max_h)
        if abs(l-r) <= 1:
            return

        if r > l:
            self.max_h.push(-self.min_h.pop())
        else:
            self.min_h.push(-self.max_h.pop())

        self._rebalance()

    def add(self, t):
        if len(self.min_h) > 0 and t > self.min_h.peek():
            self.min_h.push(t)
        else:
            self.max_h.push(-t)

        self._rebalance()

    def remove(self, t):
        if len(self.min_h) > 0 and t >= self.min_h.peek():
            self.min_h.remove(t)
        else:
            self.max_h.remove(-t)

        self._rebalance()

    def median(self):
        r = len(self.min_h)
        l = len(self.max_h)
        if r > l:
            return self.min_h.peek()
        else:
            return -self.max_h.peek()

    def __repr__(self):
        return repr(self.max_h)+repr(self.min_h)


class Solution:
    def medianSlidingWindow(self, nums, k):
        
        if len(nums) < 1:
            return []

        ret = []
        dh = DualHeap()
        for i in xrange(k):
            dh.add(nums[i])
        ret.append(dh.median())

        for i in xrange(k, len(nums)):
            dh.remove(nums[i-k])
            dh.add(nums[i])
            ret.append(dh.median())

        return ret

    def medianSlidingWindow_TLE(self, nums, k):
        
        if len(nums) < 1:
            return []

        pq = PriorityQueue()
        for i in xrange(k):
            pq.insert(nums[i])

        ret = []
        mid = k/2
        if k%2 == 0:
            mid -= 1

        ret.append(pq[mid])
        for i in xrange(k, len(nums)):
            pq.remove(nums[i-k])
            pq.insert(nums[i])
            ret.append(pq[mid])

        return ret


if __name__ == "__main__":
    assert Solution().medianSlidingWindow([1, 2, 7, 8, 5], 3) == [2, 7, 7]