
__author__ = 'Daniel'
import heapq


class DualHeap(object):
    def __init__(self):
        
        self.min_h = []
        self.max_h = []

    def insert(self, num):
        if not self.min_h or num > self.min_h[0]:
            heapq.heappush(self.min_h, num)
        else:
            heapq.heappush(self.max_h, -num)
        self.balance()

    def balance(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        if l1 - l2 > 1:
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
            self.balance()
        elif l2 - l1 > 1:
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
            self.balance()
        return

    def get_median(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        m = (l1 + l2 - 1) / 2
        if (l1 + l2) % 2 == 1:
            if m == l2 - 1:
                return -self.max_h[0]
            elif m == l2:
                return self.min_h[0]
            raise Exception("not balanced")
        else:
            return (-self.max_h[0] + self.min_h[0]) / 2.0


class Solution:
    def __init__(self):
        self.dh = DualHeap()

    def solve(self, cipher):
        
        self.dh.insert(cipher)
        return self.dh.get_median()


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = int(f.readline().strip())
        s = "%.1f\n" % (solution.solve(cipher))
        print s,
