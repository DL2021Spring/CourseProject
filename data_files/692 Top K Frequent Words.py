

import heapq
from collections import defaultdict
from typing import List


class Word:
    def __init__(self, content, count):
        self.content = content
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.content > other.content

        return self.count < other.count


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        h = []
        counter = defaultdict(int)
        for w in words:
            counter[w] += 1

        for w, c in counter.items():
            heapq.heappush(h, Word(w, c))
            if len(h) > k:
                heapq.heappop(h)

        ret = []
        while h:
            w = heapq.heappop(h).content
            ret.append(w)

        return ret[::-1]


if __name__ == "__main__":
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
