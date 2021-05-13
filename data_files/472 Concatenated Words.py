

from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        TrieNode = lambda: defaultdict(TrieNode)  
        self.root = TrieNode()  

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        words.sort(key=len)
        ret = []
        for w in words:
            if self.can_concat(w, 0):
                ret.append(w)

            cur = self.root
            for c in w:
                cur = cur[c]
            cur["end"] = True

        return ret

    def can_concat(self, word, lo):
        if not word:
            return False

        k = len(word)
        if lo >= k:
            return True

        cur = self.root
        for i in range(lo, k):
            cur = cur[word[i]]
            if cur.get("end", False) and self.can_concat(word, i + 1):
                return True

        return False


class SolutionTLE:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        ret = []
        
        visited = set(words)
        for w in words:
            if self.can_concat(w, visited):
                ret.append(w)

        return ret

    def can_concat(self, w, visited):
        if not w:
            return False

        k = len(w)
        F = [False for _ in range(k + 1)]
        F[0] = True
        for i in range(1, k + 1):
            for j in range(i):
                if j == 0 and i == k:
                    continue  
                if F[j] and w[j:i] in visited:
                    F[i] = True

        return F[k]


if __name__ == "__main__":
    assert Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) == ["catsdogcats","dogcatsdog","ratcatdogcat"]
