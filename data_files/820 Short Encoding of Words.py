

from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        root = {}
        ends = []
        for word in set(words):
            cur = root
            for c in word[::-1]:
                nxt = cur.get(c, {})
                cur[c] = nxt
                cur = nxt

            ends.append((cur, len(word)))

        return sum(
            l + 1
            for node, l in ends
            if len(node) == 0  
        )


if __name__ == "__main__":
    assert Solution().minimumLengthEncoding(["time", "me", "bell"]) == 10
