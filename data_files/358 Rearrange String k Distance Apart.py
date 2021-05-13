
from collections import defaultdict
import heapq

__author__ = 'Daniel'


class Val(object):
    def __init__(self, cnt, val):
        self.cnt = cnt
        self.val = val

    def __cmp__(self, other):
        if self.cnt == other.cnt:
            return cmp(self.val, other.val)

        return -cmp(self.cnt, other.cnt)


class Solution(object):
    def rearrangeString(self, s, k):
        
        if not s or k == 0: return s

        d = defaultdict(int)
        for c in s:
            d[c] += 1

        h = []
        for char, cnt in d.items():
            heapq.heappush(h, Val(cnt, char))

        ret = []
        while h:
            cur = []
            for _ in xrange(k):
                if not h:
                    return "".join(ret) if len(ret) == len(s) else ""

                e = heapq.heappop(h)
                ret.append(e.val)
                e.cnt -= 1
                if e.cnt > 0:
                    cur.append(e)

            for e in cur:
                heapq.heappush(h, e)

        return "".join(ret)


if __name__ == "__main__":
    assert Solution().rearrangeString("aabbccdd", 4) == "abcdabcd"
