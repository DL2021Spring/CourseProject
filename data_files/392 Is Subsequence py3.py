

from bisect import bisect_left
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        char_pos = defaultdict(list)
        for p, c in enumerate(t):
            char_pos[c].append(p)
            

        lo_po = -1
        for c in s:
            if c not in char_pos:
                return False
            pos = char_pos[c]
            i = bisect_left(pos, lo_po)
            if i == len(pos):
                return False
            lo_po = pos[i] + 1  

        return True


if __name__ == "__main__":
    assert Solution().isSubsequence("abc", "ahbgdc") == True
    assert Solution().isSubsequence("acb", "ahbgdc") == False
