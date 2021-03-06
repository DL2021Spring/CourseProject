

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        h = {}
        for i, c in enumerate(order):
            h[c] = i

        for i in range(1, len(words)):
            if self.cmp(words[i], words[i-1], h) == -1:
                return False

        return True

    def cmp(self, w1, w2, h):
        for c1, c2 in zip(w1, w2):
            if h[c1] < h[c2]:
                return -1
            elif h[c1] > h[c2]:
                return 1

        if len(w1) == len(w2):
            return 0
        elif len(w1) > len(w2):
            return 1
        else:
            return -1


if __name__ == "__main__":
    assert Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
